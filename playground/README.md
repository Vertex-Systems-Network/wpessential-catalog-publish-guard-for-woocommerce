# WordPress Playground Blueprints — WPEssential Catalog Publish Guard

This folder includes 3 Blueprint templates:

- `blueprints/base/blueprint.json`: WooCommerce-only, for baseline WordPress/WooCommerce install smoke tests.
- `blueprints/free/blueprint.json`: WooCommerce + packaged **actual Free plugin**.
- `blueprints/pro/blueprint.json`: WooCommerce + packaged **actual Free** + **actual Pro plugin**, in required installation order.

**Run preflight:**
```bash
python scripts/validate_blueprints.py
python scripts/build_playground_bundles.py --base-only --out dist/playground
```
The second command produces a bundle structure, NOT proof of an executed WordPress test.

**After real plugin builds exist:**
```bash
python scripts/build_playground_bundles.py \
  --free dist/wpessential-catalog-publish-guard.zip \
  --pro dist/wpessential-catalog-publish-guard-pro.zip \
  --out dist/playground

npx @wp-playground/cli server --blueprint=dist/playground/free-playground-bundle.zip
npx @wp-playground/cli server --blueprint=dist/playground/pro-playground-bundle.zip
```

For local directories containing bundled resources use `--blueprint-may-read-adjacent-files` when required by your CLI version. Follow https://developer.wordpress.org/playground/blueprints/bundles/ for authoritative current semantics.

The structural linter isn't a substitute for schema validation or real browser/WordPress tests. Free/Pro blueprints reference plugin ZIPs not provided in this **prompt-only** package; bundler must reject missing ZIPs. Playground usually uses SQLite; run separate MySQL/MariaDB tests for concurrency, locking, approval and job reliability.

Capture real execution logs and screenshots under `dist/review-evidence/`, never falsely mark tests green.
