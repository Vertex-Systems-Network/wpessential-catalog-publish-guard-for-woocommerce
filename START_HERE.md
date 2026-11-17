# Resume WPCPG

Read the full Master and START_AGENT files, inspect Git and `.ai/state.json` / `.ai/tasks.json`, verify evidence, then continue the next unblocked task without routine approval.

Current phase: P0. Current task: `WPCPG-P0-COMPOSER`. First action: inspect both plugin `composer.json` and entrypoints; run `composer validate --strict`, `composer install`, PHP lint and activation smoke in a PHP/Woo runtime. Then continue P0 sources/contracts and P1 Free engine. No real WP runtime or ZIP test has passed yet.

2026-11-17 checkpoint: PHP test matrix configured in `.github/workflows/bootstrap.yml`; await actual CI logs before marking P0-COMPOSER done. Next independent task: P0-CONTRACTS; codify product snapshot and source adapter contract, then write tests. No publication interception exists.
