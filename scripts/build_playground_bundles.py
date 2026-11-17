#!/usr/bin/env python3
"""Build self-contained WordPress Playground ZIP bundles from genuine plugin ZIPs.

This script deliberately refuses to fabricate plugin packages. No private merchant catalog data or
secrets should be included. Run only after building each plugin with Composer vendor.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED, BadZipFile

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINTS = ROOT / 'playground' / 'blueprints'


def verify_plugin_zip(path: Path, slug: str) -> None:
    if not path.is_file():
        raise ValueError(f'Missing plugin ZIP: {path}')
    try:
        with ZipFile(path) as source:
            names = set(source.namelist())
            expected = [f'{slug}/{slug}.php', f'{slug}/vendor/autoload.php']
            for entry in expected:
                if entry not in names:
                    raise ValueError(f'{path.name}: required installable file is missing: {entry}')
            for name in names:
                if name.startswith('/') or '..' in Path(name).parts or '\\' in name:
                    raise ValueError(f'{path.name}: unsafe ZIP entry: {name}')
            if any(name.endswith(('.php', '.json', '.js')) and not name.startswith(slug + '/') for name in names):
                raise ValueError(f'{path.name}: files outside expected plugin root {slug}/')
    except BadZipFile as error:
        raise ValueError(f'Invalid ZIP {path}: {error}') from error


def checksum(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            sha.update(block)
    return sha.hexdigest()


def build(label: str, free: Path, pro: Path | None, out: Path) -> dict:
    blueprint = BLUEPRINTS / label / 'blueprint.json'
    configuration = json.loads(blueprint.read_text(encoding='utf-8'))
    references = [step['pluginData']['path'] for step in configuration['steps']
                  if step.get('step') == 'installPlugin'
                  and step.get('pluginData', {}).get('resource') == 'bundled']
    binaries = {'/wpessential-catalog-publish-guard.zip': free}
    if pro is not None:
        binaries['/wpessential-catalog-publish-guard-pro.zip'] = pro
    if sorted(references) != sorted(binaries):
        raise ValueError(f'Blueprint resource mismatch in {label}: {references}')
    target = out / f'{label}-playground-bundle.zip'
    with ZipFile(target, 'w', compression=ZIP_DEFLATED) as bundle:
        bundle.writestr('blueprint.json', json.dumps(configuration, indent=2) + '\n')
        for path_in_bundle, path_on_disk in binaries.items():
            bundle.write(path_on_disk, arcname=path_in_bundle.lstrip('/'))
    return {'type': label, 'file': str(target), 'sha256': checksum(target),
            'plugins': {p.name: checksum(p) for p in binaries.values()}}


def build_base(out: Path) -> dict:
    configuration = json.loads((BLUEPRINTS / 'base' / 'blueprint.json').read_text(encoding='utf-8'))
    target = out / 'base-playground-bundle.zip'
    with ZipFile(target, 'w', compression=ZIP_DEFLATED) as bundle:
        bundle.writestr('blueprint.json', json.dumps(configuration, indent=2) + '\n')
    return {'type': 'base', 'file': str(target), 'sha256': checksum(target), 'plugins': {}}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--free', type=Path, help='Real built Free installable ZIP')
    parser.add_argument('--base-only', action='store_true', help='Create a baseline WooCommerce-only Playground bundle')
    parser.add_argument('--pro', type=Path, help='Real built Pro installable ZIP')
    parser.add_argument('--out', type=Path, default=Path('dist/playground'))
    args = parser.parse_args()
    try:
        if not args.base_only and args.free is None:
            raise ValueError('--free is required unless --base-only is used')
        if args.base_only and (args.free or args.pro):
            raise ValueError('--base-only does not accept --free or --pro')
        if args.free:
            verify_plugin_zip(args.free, 'wpessential-catalog-publish-guard')
        if args.pro:
            verify_plugin_zip(args.pro, 'wpessential-catalog-publish-guard-pro')
        args.out.mkdir(parents=True, exist_ok=True)
        report = [build_base(args.out)]
        if args.free:
            report.append(build('free', args.free, None, args.out))
        if args.pro:
            report.append(build('pro', args.free, args.pro, args.out))
        (args.out / 'bundle-manifest.json').write_text(json.dumps(report, indent=2) + '\n')
        for entry in report:
            print(entry['type'], entry['file'], entry['sha256'])
        print('Bundle ZIPs built and structurally validated. Playground runtime NOT YET RUN.')
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print('ERROR:', error, file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
