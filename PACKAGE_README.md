# WPEssential Catalog Publish Guard — AI-Native Development Prompt Package

**This package is a development specification and useful starter templates, not the completed WooCommerce plugin.**

## How to use in GitHub / with your coding agent

1. Copy `WPEssential_Catalog_Publish_Guard_AI_Native_Master_Development_Prompt.md` and `WPEssential_Catalog_Publish_Guard_START_AGENT.md` into your repository root.
2. Copy `scripts/`, `playground/`, `docs/rules.json`, `docs/UI_SCREEN_INVENTORY.json` and the `.ai` templates into the repository. Convert `START_HERE_TEMPLATE.md` to `START_HERE.md` only if no real state already exists; never overwrite established progress.
3. Give the coding agent repo access and paste the contents of `START_AGENT.md` once. It must inspect existing files, recover memory and execute next unblocked task without routine questions **while the agent runtime is active**.
4. Keep all five consolidated phases and their requirements: P0 research/setup, P1 Free, P2 Pro, P3 tests/fixes, P4 market-ready packages.
5. Do not confuse a persistent prompt with a daemon. For genuinely unattended multi-session work, set up an owner-authorized persistent coding runner/CI that automatically invokes agent execution from `START_HERE.md` and monitors cost/limits, permissions, production safeguards and rate limits.

## What's inside
- Master Development Prompt (~15,000+ words) with 79 rules, 17 UI surfaces, 56 critical scenarios.
- START AGENT launcher and recovery START_HERE template.
- `.ai/state.template.json`, `.ai/tasks.template.json`, BACKLOG template and decision template.
- `docs/rules.json`, `docs/UI_SCREEN_INVENTORY.json` and reference notes.
- WordPress Playground base, Free and Pro Blueprints.
- `scripts/build_playground_bundles.py`: validates actual Free/Pro ZIPs and packages self-contained bundles. It intentionally refuses missing packages.
- `scripts/validate_blueprints.py`: syntactic and structural checks.
- `scripts/generate_readmes.py`: starter docs generator with release approval/evidence validation. Extend/test within P0/P4 as specified.
- Example release metadata marked NOT APPROVED and NOT VERIFIED.

## Quick test of the *templates* (not plugins)
```bash
python scripts/validate_blueprints.py
python scripts/generate_readmes.py --metadata templates/release/product-docs.example.json --out /tmp/wpcpg-test-docs
# Expected: release gate blocks generation because the example has NO verified release features.
```

## Important
Free and Pro Blueprint templates refer to bundled plugin ZIPs which don't exist yet. Only after coding/building both real plugins, use:
```bash
python scripts/build_playground_bundles.py --free dist/wpessential-catalog-publish-guard.zip --pro dist/wpessential-catalog-publish-guard-pro.zip --out dist/playground
```
Then launch the bundle with the official Playground CLI. **A structural script check is NOT a WordPress test.** For concurrent publishing, approvals, locking and Woo importer correctness, use MySQL/MariaDB in addition to Playground.
