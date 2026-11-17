#!/usr/bin/env python3
"""A small executable starter for canonical Woo/WordPress documentation generation.

Examples are intentionally incomplete. Release generation must fail unless version,
platform requirements, and verified features are supplied by actual product tests.
Extend the generator and checks as instructed in Section 16D of the Master Prompt.
"""
import argparse
import json
from pathlib import Path
import re
import sys


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def cleaned(text):
    return str(text).strip()


def make_docs(data):
    if data.get('release_approved') is not True:
        raise ValueError('Release documentation generation refused: release_approved must be true after verified gates')
    required = ['release_version', 'requires_wp', 'tested_wp', 'requires_php',
                'requires_woocommerce', 'tested_woocommerce', 'license_uri']
    missing = [field for field in required if not nonblank(data.get(field))]
    if missing:
        raise ValueError('Release metadata not verified: ' + ', '.join(missing))
    version = data['release_version']
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+(?:[-.][a-zA-Z0-9.-]+)?', version):
        raise ValueError('Release version must resemble a valid semantic version')
    features = data.get('features', [])
    if not data.get('evidence_archive'):
        raise ValueError('An evidence_archive location is required for release')
    for feature in features:
        if feature.get('status') == 'verified' and not nonblank(feature.get('verified_test_id')):
            raise ValueError('Feature missing test ID: ' + str(feature.get('id')))

    for f in features:
        if f.get('status') == 'verified' and not nonblank(f.get('verified_test_id')):
            raise ValueError(f"Feature {f.get('id')} lacks evidence test ID")
    if not nonblank(data.get('verified_commit')):
        raise ValueError('Release verified_commit is required')
    docs = {}
    for tier in ['free', 'pro']:
        product = data[tier]
        if not nonblank(product.get('slug')) or not nonblank(product.get('name')):
            raise ValueError(f'{tier} name/slug missing')
        if not nonblank(product.get('short_description')) or len(product['short_description']) > 150:
            raise ValueError(f'{tier} short description must be <= 150 chars')
        own_features = [f['name'] for f in features
                        if f.get('status') == 'verified' and f.get('tier') == tier]
        if not own_features:
            raise ValueError(f'No independently verified {tier} features; do not advertise empty release')
        both_features = [f['name'] for f in features
                         if f.get('status') == 'verified' and f.get('tier') in (['free', 'pro'] if tier=='pro' else ['free'])]
        lines = [f"# {product['name']}", '', product['short_description'], '',
                 f"Version: {version}", f"Requires WordPress: {data['requires_wp']}",
                 f"Tested WordPress: {data['tested_wp']}", f"Requires PHP: {data['requires_php']}",
                 f"Requires WooCommerce: {data['requires_woocommerce']}",
                 f"Tested WooCommerce: {data['tested_woocommerce']}", '',
                 '## Description', product['description'], '', '## Verified features',
                 *('- ' + x for x in both_features), '', '## Installation',
                 *(f'{index}. {line}' for index,line in enumerate(product['installation'],1)),
                 '', '## Frequently asked questions']
        for faq in product.get('faq', []):
            lines += ['', f"### {faq['question']}", faq['answer']]
        lines += ['', '## Changelog']
        for row in data.get('changelog', []):
            if row.get('version') == version and row.get('verified') is True:
                lines.append('- '+row['text'])
        lines += ['', '## License', data.get('license','GPLv2 or later'), data['license_uri'], '']
        docs[f'{tier}/README.md'] = '\n'.join(lines)
    free=data['free']
    summary=free['short_description']
    headers = [f"=== {free['name']} ==="]
    if data.get('wporg_contributors'):
        headers.append('Contributors: ' + ', '.join(data['wporg_contributors']))
    headers += [
        'Tags: ' + ', '.join(data.get('tags', [])),
        'Requires at least: ' + data['requires_wp'],
        'Tested up to: ' + data['tested_wp'],
        'Stable tag: ' + version,
        'Requires PHP: ' + data['requires_php'],
        'License: ' + data.get('license','GPLv2 or later'),
        'License URI: ' + data['license_uri'],
        '', summary, '', '== Description ==', '', free['description'], '',
        'Verified features:', '',
        *('* ' + f['name'] for f in features if f.get('status')=='verified' and f.get('tier')=='free'),
        '', '== Installation ==', '',
        *(f'{i}. {entry}' for i,entry in enumerate(free['installation'],1)),
        '', '== Frequently Asked Questions ==', ''
    ]
    for faq in free.get('faq',[]):
        headers += [f"= {faq['question']} =", '', faq['answer'], '']
    headers += ['== Changelog ==', '', f'= {version} =']
    changes=[row['text'] for row in data.get('changelog',[])
             if row.get('version')==version and row.get('verified') is True]
    if not changes:
        raise ValueError('Verified changelog entry required for release version')
    headers += ['* '+x for x in changes]
    headers.append('')
    docs['free/readme.txt']='\n'.join(headers)
    return docs


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--metadata',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--check',action='store_true',help='Verify rendered docs match existing files; never modify')
    args=ap.parse_args()
    try:
        docs=make_docs(json.loads(args.metadata.read_text(encoding='utf-8')))
        for relative,contents in docs.items():
            destination=args.out/relative
            if args.check:
                if not destination.is_file() or destination.read_text(encoding='utf-8')!=contents:
                    raise ValueError(f'Missing/stale generated document: {destination}')
            else:
                destination.parent.mkdir(parents=True,exist_ok=True)
                destination.write_text(contents,encoding='utf-8')
            print(('CHECKED' if args.check else 'GENERATED'),destination)
        print('Local generator complete. Official WP.org validation and actual feature tests remain mandatory.')
        return 0
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError) as error:
        print('DOC GENERATION BLOCKED:',error,file=sys.stderr)
        return 1


if __name__=='__main__':
    raise SystemExit(main())
