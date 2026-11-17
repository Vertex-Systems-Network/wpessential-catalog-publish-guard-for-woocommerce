# Product validation boundary

`ProductSnapshot` receives a fully assembled WooCommerce CRUD object plus a named source (`classic`, `rest`, `import`, `scheduled`, or a documented extension adapter). It clones the object so rule evaluation cannot mutate the caller's product. Each adapter must pass the pending field values, not re-fetch stale persisted data before save. A future serialized revision needs a separately verified snapshot format; this class does not provide revision isolation or database locking.

`RuleEngine` returns stable rule IDs, severity, field path and explanation. The first two rules are an early slice. Warnings do not block; only `block` severity does. Current code has **no publication interception**. Status transition guards must be tested per source against actual WooCommerce save order and WordPress post status transitions, including classic variation AJAX saves, REST requests, CSV imports and scheduled posts. A late `save_post` action cannot prevent first publication; changing status after publication would create an exposure window.

Free and Pro use separate PSR-4 roots. Pro depends on an active Free interface/version, with independent packaging. Bootstraps are intentionally inert until adapters have tested behavior. Do not ship as a functioning guard yet.
