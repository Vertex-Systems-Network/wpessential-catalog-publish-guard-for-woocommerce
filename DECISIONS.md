# Decisions

## 2026-11-17 — Separate plugin roots

Free and Pro use distinct Composer PSR-4 namespaces and bootstraps. Pro checks Free at runtime; Free has no Pro dependency. The current host lacks PHP/Composer, so syntax and activation cannot be asserted until CI or a PHP environment runs them.
