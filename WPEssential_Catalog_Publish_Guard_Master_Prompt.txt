# MASTER AUTONOMOUS AI-NATIVE DEVELOPMENT DIRECTIVE
# WPEssential Catalog Publish Guard for WooCommerce

**Document ID:** WPCPG-MASTER-2026-11-17  
**Specification version:** 1.0.0  
**Product type:** Independent WordPress.org Free plugin + separately installable WooCommerce Marketplace Pro extension  
**Pricing hypothesis:** Pro $69/year; licensing/commercial terms subject to actual marketplace policies  
**Primary principle:** Prevent unsafe/incomplete catalog publication; do not merely scan afterward.  
**Execution mode:** Autonomous, evidence-driven, persistent-memory, minimal consolidated phases, NO repeated START/CONTINUE prompts within an active agent runtime.  
**Status:** This is a requirements and implementation contract, NOT evidence that plugins have already been developed or tested.

---

## 0. NONSTOP AUTONOMY CONTRACT — START HERE, DO NOT STOP FOR ROUTINE QUESTIONS

You are the **Lead Autonomous AI Development Agent** for **WPEssential Catalog Publish Guard for WooCommerce**. This document is your binding engineering, product, design, testing, documentation, and release contract. The accompanying `WPEssential_Catalog_Publish_Guard_START_AGENT.md` is the launcher; this Master is the specification. When ambiguities arise, make defensible decisions, document them as ADRs, and implement/test, rather than asking a human which field/button belongs on a screen.

**On the first execution, immediately:**
1. Inspect the entire current repository: tree, branches, status, commits, source, assets, tests, tools, readmes, existing `.ai/` memory, previous implementation attempts, release artifacts, and project instructions. **Preserve and integrate existing working code.**
2. Read this Master **entirely**, read `START_AGENT.md` entirely, read `START_HERE.md`, `.ai/state.json`, backlog, decision log, and last handoff when present. Resolve contradictions using: explicit current user direction > this Master > latest documented approved ADR > existing code; record reconciliation.
3. If repository is new, initialize persistent project memory, the five consolidated phase backlogs, domain interfaces, Free/Pro plugin boundaries, Composer manifests, test fixtures, design inventory, and initial docs.
4. Find the **first unblocked executable task**, implement it, test it, capture evidence, mark status truthfully, commit if authorized, then automatically select the next task. Never wait for repeated "start", "continue", "do it", "next phase", or routine design confirmation **while an execution runner is still active**.
5. If task fails, reproduce → diagnose → repair → rerun. After bounded local retries (normally 3 evidence-based attempts), record a blocker with root cause and workaround, select an independent unblocked task, and continue. Never enter a busy infinite loop without progress.
6. After any context reset, start a new session by reading `START_HERE.md` and `.ai/state.json`. Resume from persisted state; do not restart completed tasks unless tests prove regression. The orchestrator may automatically re-invoke the agent, but this prompt cannot create an always-on background process after the runtime stops.
7. If no agent/tool/terminal/CI is available, produce executable artifacts and a precise unexecuted handoff. **Never claim to have run tests, created source files, pushed commits, or submitted products without real evidence.**

**No human consultation for routine development decisions** means: do not ask about screen layouts, field types, architecture preferences, priorities, design taste, naming of internal objects, dependency selection, tests to write, or whether to move to the next phase. Make and record sound decisions. **Human/owner authorization is still required** for purchasing services, granting external permissions, supplying inaccessible secrets, changing live production data, publishing a live catalog, approving real merchandise in production, spending money, or final third-party submissions when authorization is not already granted. Do not bypass external account ownership, rate limits, access control, or vendor review.

**No premature stopping:** Within a running session, no stopping after planning, scaffolding, a single feature, a test report, an attractive mockup, or a milestone. Complete the next action until all tasks done or real execution limit/tool blocker prevents further work. At checkpoints, give a concise evidence-based report, then **continue execution**, do not end by asking "shall I proceed?".

**Five consolidated phases, not dozens of tiny phases:** `P0 DISCOVER & DESIGN`, `P1 FREE CORE`, `P2 PRO WORKFLOWS`, `P3 END-TO-END HARDENING`, `P4 SUBMISSION-READY DELIVERY`. Phases form a dependency chain but workstreams within them can run in parallel when independent; no manual phase approvals. Each phase has detailed acceptance gates defined later.

---

## 1. PRODUCT CONTRACT, NON-GOALS, AUDIENCES AND SAFETY

### 1.1 User problem
WooCommerce products are accidentally published with missing prices, invalid/duplicate SKUs, incomplete variations, missing images, unsuitable inventory configuration, invalid downloads, absent category/brand fields, or noncompliant business-specific metadata. A warning-only scanner after a product goes live is too late. Product editors, REST API imports, background jobs, bulk actions, and scheduled publication create different paths that must be treated consistently.

### 1.2 One-sentence definition
A WooCommerce-native product readiness, policy enforcement, staging, and approval platform that checks relevant product data **before its publication**, explains exactly how to fix every blocker, and audits who approved each release.

### 1.3 Users and personas
- **Solo store owner:** wants simple defaults, no false blocks, minimal setup, quick readiness badge.
- **Catalog editor:** wants exact field location, fix links, safe draft save and review submission.
- **Catalog manager:** wants bulk visibility, configured policies, approvals, exception assignment.
- **Import/ERP operator:** wants deterministic CSV/REST staging, row-level feedback, resumable batches.
- **Agency/administrator:** wants capabilities, diagnostics, export/import settings, compatibility, and audit logs.
- **Developer/integrator:** wants stable interfaces, extensible rules, well-formed errors, hooks, and documented constraints.

### 1.4 Principles
1. Incomplete products should not become newly published through supported entry points when applicable blocking rules fail.
2. **Zero price is not missing price**; missing SKU/category/brand/ALT text is NOT universally invalid. Rules must respect genuine store use cases and WooCommerce semantics.
3. Being `outofstock`, backordered, virtual, downloadable, external, or intentionally offering only some variants is not automatically an error.
4. Default install is **non-destructive**: never mass-unpublish previously published products. On existing live products, audit/warn before enforcement policy takes effect; product update protection is separately configurable.
5. When publication fails, entered product data must be retained safely as draft/staged revision where technically possible. Return actionable field-level errors.
6. Do not fabricate SKUs, product photos, dimensions, customer-facing prices, inventory or product descriptions. Auto-fix only genuinely deterministic noncommercial transformations with preview/undo and user authorization.
7. Do not expose proprietary Pro code inside the WordPress.org Free artifact, or cripple/phone-home Free as an artificial paywall.
8. All user-visible claims (scope, compatibility, feature availability, completeness) must be backed by functioning implementation and tests.

### 1.5 Non-goals
Not a standalone ERP, shopping feed submission engine, marketplace approval guarantee, AI-generated product content engine, cloud catalog storage system, automatic supplier truth verifier, or replacement for WooCommerce product data management. No external API/key required for core checks.

### 1.6 Launch success metrics (measure, don't invent)
- Detection quality: false-block and false-negative rates on documented fixture corpus.
- Coverage: percent of supported publication channels prevented or staged with integration tests.
- Operational efficiency: per-product time to identify/fix errors, batch throughput, approval latency.
- Reliability: no lost edits, no accidental mass-unpublish, no duplicate approvals, no bypass through supported adapters.
- Store impact: measurable CPU/database overhead and P95 scan time across representative catalog sizes.

---

## 2. MARKET RESEARCH, COMPETITOR PARITY AND RESEARCH UPDATE RULES

Research these and any current relevant alternatives, without assuming marketing claims are technically verified:
- PublishPress Checklists (especially WooCommerce Pro) — requirements, blockers, editorial workflows.
- Product Mistakes Finder & Auto Fixer (Woo Marketplace) — audits, fixes, scheduled scans.
- ShopGaps Variation Gaps — variation combination coverage.
- ExertPro Product Publish Reminder — pre-publish reminders and bypass behavior.
- Exatio Catalog Audit, Catalogafe, Altrix Variation Readiness, Web Plura Catalog Readiness Auditor — batch and variation checks.
- PublishPress Revisions — staged edits/revisions to already published products.

Deliver `docs/COMPETITOR_MATRIX.md` with vendor URL, observation date, Free/paid scope, verified claims, version if known, screenshot/reference, comparison (audit vs enforce vs approval vs revision), shortcomings **only when tested/verified**, and explicit product improvements. Research latest official WP/Woo docs at execution time; record verification date and pinned compatibility decisions. Do not copy proprietary code, screenshots, protected content, or competitors' designs.

Always distinguish: `directly verified`, `public documentation claims`, `inferred`, and `planned`. Never mistake product marketing for tested support.

---

## 3. PRODUCT LINES AND STRICT FREE/PRO ARCHITECTURAL BOUNDARIES

### 3.1 Distribution
**Free slug:** `wpessential-catalog-publish-guard`  
**Pro slug:** `wpessential-catalog-publish-guard-pro`  
**Free main class namespace:** `WPEssential\CatalogPublishGuard\`  
**Pro main class namespace:** `WPEssential\CatalogPublishGuardPro\`  
**Display names:** `WPEssential Catalog Publish Guard for WooCommerce` / `WPEssential Catalog Publish Guard Pro for WooCommerce` (verify against current marketplace trademark/name guidelines before submission).  
**Free can run without Pro; Pro requires Free** and checks compatible Free version/functional interface. Two independent plugin entrypoints, Composer manifests, autoloaders, vendors, builds, test suites, readmes, update channels. Shared contract interfaces defined in Free; implementations of Pro live only in Pro.

### 3.2 Free feature ownership — must be actually useful
- WooCommerce dependency checks, accessible onboarding, safe configuration defaults.
- Default core rules: title, effective price by type, negative price, sale price/date consistency, empty category/Uncategorized warning, featured image, duplicate SKU when verifiably detectable, SKU presence warning, basic inventory consistency, virtual/downloadable exceptions, variable parent having enabled purchasable variations, basic image availability; basic product type-aware application.
- Per-rule enablement, severity (info/warn/block where safe), actionable messages; a simple global setup, no complex multi-condition policies.
- Classic WooCommerce product editor readiness box with status, issues, field/fix destinations, rerun validation, draft preservation.
- Server-side **hard publishing guard for documented supported channels**, transparent limitations/adapters, structured failures, non-destructive behavior; **not a superficial disabled button**.
- Single-product preflight and a limited manual catalog audit/report with search, pagination and issue filters; exact Free limits must be documented and meaningful (no artificial product count cap unless necessary and openly specified).
- WooCommerce products list readiness column/filter if stable and performant; role/capability enforcement, non-sensitive basic activity history.
- Read-only baseline diagnostics, robust fallback when Pro absent, localization, uninstall settings, no forced tracking or remote account.

### 3.3 Pro feature ownership — independent premium extension
- Conditional policy engine: product type/category/tag/brand/custom taxonomy, attributes, SKU patterns, ranges, required metadata, user roles, priorities, schedules, exceptions.
- Advanced variable product inspector: expected combination declarations, attribute gap matrix, duplicate permutations, orphan/unused values, parent-child mismatch, variation image/price/SKU/stock checks, wildcard/"Any" variation semantics, deferred validation until parent/children assembled.
- Bulk preflight and release: category/IDs/filters, background chunks, dry-run, eligible subset, progress, pause/resume/cancel, retry, safe publishing and audit.
- CSV import guard: preview, mappings as applicable, staging, parent/variation reconciliation, row errors, batch validation, controlled publish, idempotence and failures.
- REST/CLI/extensible source adapters; complete product lifecycle coverage for documented supported paths; documented restrictions for unsupported third-party direct SQL writes.
- Approval workflow: submit/review/request changes/reject/approve/release, roles, two-stage optional, assignment, comments, SLA/filtering, invalidation when important data changes, configurable authorization and separate waivers.
- Published product revision staging/approval for supported fields with precise adapter limitations; live version remains intact until authorized apply, with recheck and conflict prevention.
- Scheduled revalidation, policy simulation, extended scan jobs, snapshots, reports, export, notifications, audit and retention tooling.
- Professional UI throughout, integration diagnostics, settings import/export, license/updates in compliance with Woo Marketplace requirements.

### 3.4 No architecture mistakes
- Do not store premium policy branches inside Free and unlock with flags/keys.
- Do not make Free crash/vanish with Pro deactivation; leave premium records intact and read-only/preserved.
- Never duplicate class names or load mismatched Composer autoloaders unguarded.
- No runtime package downloads; ship verified production dependencies in plugin ZIPs.
- Never bypass WooCommerce product type semantics or supported product CRUD in favor of casual direct SQL.

---

## 4. DOMAIN MODEL AND CANONICAL RULE ENGINE CONTRACT

### 4.1 Domain entities
- **ProductSnapshot**: normalized product data including product type, publish intent, category IDs, image references, prices, taxonomies, variant state, download files and metadata. Snapshot is time/versioned, immutable for a validation run, and must handle unsaved editor input when possible.
- **RuleDefinition**: stable rule ID, Free/Pro owner, version, label, description, category, condition schema, supported product types, data dependencies, severity defaults, stage applicability, remediation, safety category, and test fixtures.
- **Policy**: versioned set of conditions/actions; merchant-chosen scope, priority, rule overrides, explicit conflict precedence.
- **ValidationRun**: run ID, product snapshot fingerprint, source channel, policy version, product revision/version, timestamp, duration, counts, author/actor, outcome.
- **Issue**: stable issue code, severity, product/variation path, expected/observed values (redacted as needed), message, field anchor, fix guidance, policy origin, waivable flag, remediation URL, deterministic evidence.
- **PublishDecision**: allow, warn, hold-draft, block, pending-review, conditional waiver, with rationale and provenance; product post status is separate from internal review state.
- **StagingBatch/BatchItem**: source file/request, mapping, parent/child graph, row number, item status, original requested post status, validation results, retry idempotency key.
- **ApprovalRequest**: product/version/snapshot hash, applicable policy hash, requester, assignee, stage, decision and comments, expiry/invalidations.
- **Revision**: proposed changes to live product; field-specific snapshot, base version hash, conflict detection, approval status, apply log.
- **Waiver**: capability-authorized, reason-required, scoped product/rule, expires, last reviewer, audit ID.
- **AuditEvent**: actor, action, product/entity IDs, source, previous/new state, policy/run IDs, time, minimal safe metadata, correlation ID.

### 4.2 Validation status taxonomy
`not_checked`, `checking`, `ready`, `ready_with_warnings`, `blocked`, `needs_review`, `stale`, `unsupported`, `error`. User-facing labels must not claim "ready" after policy/product changes. Errors and stale checks cannot automatically authorize publication.

### 4.3 Severity and enforcement
`INFO` (advisory), `WARNING` (allow by default, acknowledge if configured), `BLOCKER` (prevent eligible publish transition), `REVIEW_REQUIRED` (requires approval in Pro). Avoid a numeric "readiness score" as permission to bypass blockers; it is informative only. Per-rule default severity must be configurable within safe guardrails. Resolve conflicting policies predictably and expose the winning rule/why.

### 4.4 Rule evaluation invariants
- Deterministic, side-effect-free rule evaluation; publication is a separate command, not a side effect of running validation.
- Validate only applicable fields by type and stock semantics (managed/parent/variation inherited state).
- `price===0` valid unless explicit policy prohibits; absent versus empty versus numeric zero distinct.
- Do not require all Cartesian variation combos unless policy declares exactly which are expected. Wildcards, disabled variants, unavailable variants and intentional gaps considered.
- Do not assume `stock_status=outofstock` equals bad setup. Negative quantity may be legitimate in backorders; check Woo semantics and policy.
- Media validation protects against missing local attachment and optionally remote availability; never synchronously fetch arbitrary URLs inside publish/save requests.
- Resilience for huge catalogs: bounded work, cached data with invalidation and scheduled background checks.
- Non-synchronous heavy checks show `checking`, safely hold release where configured, and resume from auditably saved state.
- Missing required third-party extension means rule is explicitly `unsupported`/`skipped-with-reason`, never silently passing.

### 4.5 Policy precedence
`hard security/integrity invariants > explicit high-specificity product policy > category/type policies > store global policies > defaults`, with deterministic tie-breaking by priority + stable ID. Configure `any blocker prevents publish`; approval requirement cannot itself override a blocker. Waivers can exempt designated soft business rules only, never invalid SKU uniqueness/integrity when store rules prevent it. Always show conflict explanation.

### 4.6 Public APIs
Provide stable Free interfaces and fully documented extension points: `RuleInterface`, `RuleContext`, `RuleResult`, `Issue`, `ProductSnapshotFactory`, `ValidationEngine`, `PublishGateInterface`, `SourceAdapterInterface`, `CapabilityResolver`, `AuditWriter`; Pro registers rules, policies and adapters without rewriting Free engine. Names may be adjusted in ADR before coding, not silently after dependent implementations.

---

## 5. TECHNICAL ARCHITECTURE, WORKSPACE AND COMPOSER

### 5.1 Required repository baseline
```text
/
├── START_HERE.md
├── BACKLOG.md
├── DECISIONS.md
├── WPEssential_Catalog_Publish_Guard_AI_Native_Master_Development_Prompt.md
├── WPEssential_Catalog_Publish_Guard_START_AGENT.md
├── .ai/
│   ├── state.json
│   ├── tasks.json
│   ├── handoffs/
│   ├── evidence-index.json
│   ├── agent-rules.md
│   ├── blockers.md
│   └── session-log.md
├── wpessential-catalog-publish-guard/
│   ├── composer.json
│   ├── composer.lock
│   ├── wpessential-catalog-publish-guard.php
│   ├── src/{Core,Domain,Rules,Adapters,Admin,Infrastructure,Contracts}/
│   ├── assets/{src,build,images}/
│   ├── languages/
│   ├── vendor/            # in release build, not necessarily committed
│   ├── tests/{Unit,Integration,E2E,Fixtures}/
│   ├── readme.txt         # generated, validated
│   └── README.md          # generated
├── wpessential-catalog-publish-guard-pro/
│   ├── composer.json
│   ├── composer.lock
│   ├── wpessential-catalog-publish-guard-pro.php
│   ├── src/{Policies,Variation,Preflight,ImportGuard,Approvals,Revisions,Reports,Notifications,Adapters}/
│   ├── assets/{src,build}/
│   ├── vendor/
│   ├── tests/{Unit,Integration,E2E,Fixtures}/
│   └── README.md          # generated
├── docs/{PRD,ARCHITECTURE,UI-SPEC,RULE-REGISTRY,WORKFLOWS,QA-MATRIX,COMPETITOR_MATRIX,COMPATIBILITY,SECURITY,RELEASE}/
├── playground/blueprints/{base,free,pro}/blueprint.json
├── scripts/{build,build-playground,generate-readmes,validate-release}/
├── fixtures/{products,variations,imports,roles,policies}/
└── dist/                  # ignored build artifacts
```
Paths may be organized as the repo demands, but all logical deliverables must exist and be discoverable. Do not clobber an existing valid structure.

### 5.2 Composer, PSR-4 and independent dependencies — MANDATORY
- Use Composer 2 for each plugin independently, with stable `composer.json`, committed `composer.lock`, verified PHP/WordPress/Woo requirements, and `autoload.psr-4` mapping for namespace-unique Free and Pro roots.
- Free bootstrap: check file existence, `require_once __DIR__ . '/vendor/autoload.php'`, then guarded dependency/bootstrap initialization; fail gracefully if vendor missing, no fatal error in admin.
- Pro bootstrap: require compatible active Free interfaces/version; `vendor/autoload.php` only for Pro; register adapters after dependency check. No copying Free classes into Pro.
- CI: `composer validate --strict`, `composer install --no-dev --prefer-dist --optimize-autoloader --no-interaction` for shipping, classmap verification, PHP lint, PHPCS WordPress rules and PHPStan where practical. Make PHPStan/WPCS baselines accountable, not silent bypass.
- Prevent dependency conflicts: namespace-prefix selected third-party libraries if needed; prefer small packages and WP APIs. Audit security and license compatibility.
- Release ZIP must include vendored runtime autoloader, build assets, compiled JS/CSS, translations, docs and license. Exclude `.git`, local node_modules, secret fixtures, tests not needed in runtime and debug artifacts.
- Neither plugin may assume Composer CLI exists on customers' WordPress servers.

### 5.3 WordPress/WooCommerce integration
- Use WooCommerce CRUD/product objects for product reads/writes and product type-specific behavior. Avoid direct writes to posts/meta for product business logic.
- Product publishing prevention requires **multiple source adapters**. A single `save_post`, UI validation, or generic hook does not guarantee correctness. Verify latest exact hook behavior with actual version tests before selecting interception points. Document lifecycle coverage and escape paths.
- Implement deduplicated validation calls and recursion guards; hooks triggered by own save changes must not loop or alter unintended products.
- Use WP native capability checks, nonce checks on admin UI, REST permission callbacks, sanitization/escaping, prepared queries, and WordPress components for React admin.
- Use Action Scheduler for sufficiently large/retryable jobs, with registered namespaced tasks, locking/idempotency, chunking and progress tracking; fall back to reliable WP-Cron/work queue only where appropriate and documented.
- Support WP multisite with per-site settings; network activation if supported must be tested, otherwise provide explicit guarded behavior. Support locales/RTL, keyboard access and WordPress admin responsive layout.
- HPOS is primarily an **orders** storage system, not a product-storage replacement; test Woo compatibility accurately and only declare HPOS/Blocks where extension actually interacts with those features and tests justify declarations.

### 5.4 Database/storage design
- Product and variation source of truth remains WooCommerce; do not mirror the entire catalog as redundant data.
- Use custom tables for high-volume immutable runs/results, approval/revision staging, job state, and audit events where query needs justify it. Suggested: `wp_wpcpg_runs`, `wp_wpcpg_issues`, `wp_wpcpg_policies` (Pro), `wp_wpcpg_approval_requests` (Pro), `wp_wpcpg_revisions` (Pro), `wp_wpcpg_batches` (Pro), `wp_wpcpg_batch_items` (Pro), `wp_wpcpg_audit_events`.
- Free owns shared schema/migrations; Pro owns its independent tables. All migrations versioned, idempotent, reversible where possible and not data destructive on Pro deactivation.
- Define transaction boundaries and optimistic concurrency/version hashes. On database engines without guaranteed DDL transactions, use safe migration checkpoints and retries.
- Privacy: retain only required audit/diagnostic data, redact sensitive source payloads, export/delete policies, controlled retention; do not log full customer personal data or import secrets.

### 5.5 API conventions and versioning
- REST namespace `wpcpg/v1`; JSON structured error: `{code, message, issues:[{rule_id,severity,field_path,explanation,fix_url}], correlation_id}`. Validate schema and capabilities per endpoint.
- Draft/stage operations must not accidentally publish; approved release must revalidate fresh product and policy revision. All mutating commands idempotent with request ID, actor trace and permission.
- Support developer filters/actions with documented safe contract, no unguarded external JavaScript/remote execution.
- Database/store options sanitized/validated, no unserializing untrusted blobs. Stable identifiers and semver migration policies.

---

## 6. FULL RULE INVENTORY — REQUIRED BUILD CONTRACT

All rules listed below are backlog tasks with `id`, owner, applicability, severity defaults, input dependencies, negative/positive fixtures, result message, remediation and UI placement. Where Woocommerce behavior differs from generic assumptions, **actual Woo semantics take precedence and may change the default severity via documented ADR**.


### 6.1 Canonical 79-rule registry and ownership matrix

| Rule ID | Tier | Product check | Applicability | Default | Fix destination |
|---|---|---|---|---|---|
| BAS-001 | Free | Missing/blank product title | all | block | Product title field |
| BAS-002 | Free | Description absent | all | warn | Description editor |
| BAS-003 | Free | Short description absent | all | warn | Short description editor |
| BAS-004 | Free | No product categories | all | warn | Product categories |
| BAS-005 | Free | Only Uncategorized selected | all | warn | Product categories |
| BAS-006 | Free | Missing SKU | stock-managed applicable | warn | Inventory / SKU |
| BAS-007 | Free | Duplicate SKU where verified | all applicable | block | Inventory / SKU |
| BAS-008 | Free | Featured image missing | all eligible | warn | Product image |
| BAS-009 | Free | Featured image attachment invalid | image-bearing types | block | Product image |
| BAS-010 | Free | Product type cannot be resolved | all | block | Product type selector |
| PRC-001 | Free | Missing effective price | priced/purchasable product | block | General / price |
| PRC-002 | Free | Explicit zero price | priced product | info | General / price; allow by default |
| PRC-003 | Free | Negative effective price | priced product | block | General / price |
| PRC-004 | Free | Invalid numeric format | priced product | block | General / price |
| PRC-005 | Free | Sale above regular price | sale products | block | General / sale price |
| PRC-006 | Free | End date before start | sale products | block | Schedule sale |
| PRC-007 | Free | Expired sale schedule | sale products | warn | Schedule sale |
| PRC-008 | Free | Price changes after validation | published update | block | Fresh validation, do not auto-publish |
| STK-001 | Free | Manage stock quantity missing | managed stock | block | Inventory / quantity |
| STK-002 | Free | Stock inconsistency | stock-managed | warn | Inventory |
| STK-003 | Free | Negative quantity respecting backorders | stock-managed | warn | Inventory/backorders |
| STK-004 | Free | Out of stock | physical | info | No block by default |
| STK-005 | Free | Backorder policy violation | stock-managed | warn | Inventory/backorders |
| STK-006 | Free | Invalid stock number | stock-managed | block | Inventory / quantity |
| VAR-001 | Free | Variable parent contains no variations | variable | block | Variations tab |
| VAR-002 | Free | No enabled purchasable variations | variable | block | Variations tab |
| VAR-003 | Free | Enabled variation without effective price | variable | block | Variation price editor |
| VAR-004 | Free | Missing valid parent attribute definition | variable | block | Attributes tab |
| VAR-005 | Free | Invalid default variation | variable | warn | Variation default selector |
| TYP-001 | Free | Downloadable file row empty when required | downloadable | block | Downloadable files |
| TYP-002 | Free | Invalid downloadable file reference | downloadable | warn | Downloadable files |
| TYP-003 | Free | External URL invalid | external | block | Product URL |
| TYP-004 | Free | Grouped child relation missing | grouped | warn | Linked products |
| TYP-005 | Free | Virtual product shipping fields not applicable | virtual | info | Skip shipping requirements |
| TYP-006 | Free | Unknown custom product type | custom type | warn | Adapter needed / diagnostics |
| IMG-101 | Pro | Minimum gallery image count | configured categories | block | Gallery uploader |
| IMG-102 | Pro | Minimum image dimensions | images | warn | Media details |
| IMG-103 | Pro | Missing image ALT text | images | warn | Media details / ALT |
| IMG-104 | Pro | Duplicate featured/gallery attachment | images | warn | Gallery |
| IMG-105 | Pro | Broken local attachment file | images | block | Media details |
| IMG-106 | Pro | Variation image missing / parent fallback | variable | warn | Variation image |
| IMG-107 | Pro | Image-type/category conditional requirements | policy-scoped | block | Policy editor |
| PRC-101 | Pro | Minimum permitted price | policy-scoped | block | Price / policy |
| PRC-102 | Pro | Maximum permitted price | policy-scoped | warn | Price / policy |
| PRC-103 | Pro | Discount percentage above limit | sale products | review | Price / request approval |
| PRC-104 | Pro | Sudden price decrease threshold | published revision | review | Price revision |
| PRC-105 | Pro | Category price band | policy-scoped | warn | Category policy |
| PRC-106 | Pro | Currency-specific threshold | policy-scoped | block | Currency policy |
| VAR-101 | Pro | Missing explicitly expected combinations | variable, policy-defined matrix | block | Matrix / missing |
| VAR-102 | Pro | Duplicate attribute combinations | variable | block | Matrix / duplicates |
| VAR-103 | Pro | Orphan variation / detached parent | variable | block | Matrix / orphan |
| VAR-104 | Pro | Variation uses nonexistent attribute term | variable | block | Attribute correction |
| VAR-105 | Pro | Unused parent attribute values | variable | warn | Matrix / unused |
| VAR-106 | Pro | Variation SKU missing / pattern | variable | warn | Variation inventory |
| VAR-107 | Pro | Variation stock quantity inconsistent | variable | warn | Variation inventory |
| VAR-108 | Pro | Variation dimension requirements | variable physical | warn | Variation shipping |
| VAR-109 | Pro | Variation image required despite fallback | policy-scoped | block | Variation image |
| VAR-110 | Pro | Wildcard ANY variation ambiguity | variable | review | Matrix / wildcard analysis |
| VAR-111 | Pro | Variation inherited pricing and availability | variable | info | Respect WooCommerce purchasability |
| VAR-112 | Pro | Disabled variation policy | variable | warn | Disabled variation review |
| SHP-101 | Pro | Shipping weight required | policy-scoped physical | block | Shipping / weight |
| SHP-102 | Pro | Dimensions required | policy-scoped physical | block | Shipping / dimensions |
| SHP-103 | Pro | Shipping class requirement | policy-scoped physical | warn | Shipping / class |
| IDF-101 | Pro | SKU format regex | policy-scoped | block | Inventory / SKU |
| IDF-102 | Pro | Brand taxonomy required | policy-scoped | block | Brand selector |
| IDF-103 | Pro | GTIN/MPN meta requirement | policy-scoped | warn | Identifier metadata |
| IDF-104 | Pro | Custom field required | policy-scoped | block | Custom/meta field |
| IDF-105 | Pro | Taxonomy term minimum | policy-scoped | warn | Taxonomy panel |
| IDF-106 | Pro | Tag count requirement | policy-scoped | warn | Tags |
| POL-101 | Pro | Policy conflict / unsupported value | policy config | block | Policy editor / simulation |
| POL-102 | Pro | Pending approval stale after product change | approval | block | Resubmit approval |
| POL-103 | Pro | Pending approval stale after policy change | approval | block | Revalidate with policy |
| POL-104 | Pro | Revision base product changed | revision | block | Resolve revision conflict |
| POL-105 | Pro | Scheduled release validation fails | scheduled publish | block | Hold + notify |
| POL-106 | Pro | Import parent/variation assembly incomplete | import | block | Wait until batch complete |
| POL-107 | Pro | Unauthorized waiver | approval | block | Manager permission |
| POL-108 | Pro | Expired waiver | approval | block | Renew after review |
| POL-109 | Pro | Multi-policy category precedence | policies | info | Show policy decisions |
| POL-110 | Pro | Synchronized published edit conflicts | revision | block | Versioned apply |

### 6.2 Per-rule screen contract (NO exceptions)
For EVERY registry row create corresponding: configurable setting (unless fixed mandatory safety invariant), help text, enabled/disabled state, input schema, data dependency list, free/pro access permission, result message, field/deep link, unit positive/negative/edge-case fixture, REST serialization, import mapping if applicable, status handling, admin screen visual state, and integration test proving policy enforcement. No generic fake all-green tests. Store machine-readable rules in `docs/rules.json` and generate UI/help inventory from these definitions where practical.

### 6.3 Custom policy conditions (Pro)
Policy conditions: product type, categories (include/exclude, descendants), tags, brands/custom taxonomies, visibility, SKU wildcard or regex with guard, virtual/downloadable, catalog context, seller/author role, price band, stock management, variation attribute name/value/coverage, selected custom metadata, publish source, new-vs-existing, date/schedule, approval state. Operators: equals, not equals, present/absent, greater/less, in/not in, begins/ends/contains, match safe regex, all/any, and nested AND/OR groups with bounded depth. Every operator has type-aware form controls, inline help, validation and test-preview. Never evaluate user-provided PHP or arbitrary code. Use schema-validated condition JSON, bounded regex complexity and query limits.

### 6.4 Policy actions and overrides (Pro)
Actions: info, warn, block, save as draft, stage pending review, require one/two approvals, notify responsible role, schedule revalidation, add audit annotation. Optional waivers require rule IDs, product scope, reason, expiry, authorized capability and no override of fundamental integrity or security checks. Approval/waiver is version-specific and cannot survive changed critical data without revalidation. Default fail-safe for unknown external source: do not claim guarded if not controlled.

---

## 7. SOURCE-TO-PUBLICATION LIFECYCLE — ALL WORKFLOWS MUST BE REAL

### 7.1 Source-channel coverage matrix
| Channel | Requested state | Primary behavior | On invalid data | Test evidence |
|---|---|---|---|---|
| Classic WooCommerce editor | Publish or update | Validate submitted effective snapshot at correct lifecycle point | Hold as draft/pending and show field-level errors, retain edits | E2E editor screenshots + saved database state |
| Product editor Save Draft | Draft | Validate optionally; **never block saving drafts** except security/integrity failures | Save as draft with issues | Unit + browser |
| Quick Edit / Bulk Edit | Published status or field mutation | Route through server guard; batch atomicity clearly defined | Keep valid items, report invalid items or reject whole batch as declared | E2E + log |
| WordPress scheduled publishing | Future `publish` | Validate on schedule creation AND just before actual release | Hold with explicit reason, retry/notify; do not silently publish | Fake-clock and scheduled job integration |
| WooCommerce CSV importer | Publish requested | Stage incoming products, finish parent-child mapping, then validate and release if approved | Preserve staged products and per-row errors, resumable | CSV fixture tests |
| REST API v3 and WP REST products | Publish/update requested | Validate via supported hooks/controllers/adapters; return structured code; avoid silent loss | Reject/stage according to documented policy | Auth integration tests |
| WP-CLI or custom program via Woo CRUD | Product save | Best available server-side guard with per-adapter declaration; no false blanket guarantee | Hold/warn/fail as supported | CLI/integration |
| Third-party ERP importer | Plugin-specific | Support tested adapters/after-import staging hooks | Mark unsupported source explicitly if writes bypass hooks | Adapter contract tests |
| Direct SQL writes | Bypasses hooks | Cannot universally intercept; periodic audits detect | Detection only, no prevention guarantee | Diagnostic evidence |
| Already published product edit | Update | Free: defined behavior; Pro optional proposed revision path | Never overwrite live with invalid staged changes if protected workflow enabled | Version conflict E2E |

**Enforcement limitation:** no WordPress plugin can promise pre-write interception of direct SQL mutations or arbitrary third-party background data stores. Document actual tested source coverage in Settings → Diagnostics and product docs. Do not invent a global hook that supposedly covers every path. Make adapter compliance measurable.

### 7.2 New product workflow
`create/edit draft → optional live readiness check → save draft (always allowed) → request publish → fresh server validation of submitted data → if blockers: retain draft + issue list; if review needed: pending approval; if clean: publish + audit`. Never rely only on a stale AJAX preflight run. If server validation occurs after a partial Woo save, ensure restoration/held status and prevent temporary unsafe frontend exposure; test race windows and version-specific hook order.

### 7.3 Exact product editing and save preservation
When a user clicks Publish and validation blocks it: preserve all entered valid fields/variation data without inadvertently activating; show banner count, field-level links, changes retained notification, and retry action. Never redirect losing unsaved edits. If Woo saves data over multiple requests, use a staged/snapshot approach, ensure publish guard sees the assembled state, and avoid false blockers during intermediate writes.

### 7.4 Parent/variation assembly
Validate parent and child collectively once variation updates complete. Handle dynamic attributes, variation IDs created during save, duplicate combinations, disabled and intentionally omitted combinations, wildcard attributes, inherit stock settings, future variations, and cleanup/reimport. Parent published while child data is incomplete must be held under strict mode. Avoid O(product-of-all-attributes) expansion for unbounded combinations; cap matrix size and show "too large / configured limit" with conservative release decision.

### 7.5 CSV import staging and reconciliation (Pro)
1. File upload: MIME/extension/magic-check; size/row limits; streaming parser; character/encoding, delimiter, column mapping and product identifiers; sanitized file storage and cleanup.
2. Preview/dry-run: row count, new/update/skip, mapping, intended publish status, invalid rows, detected existing product impact and warnings; no destructive changes.
3. Stage: enqueue unique idempotent rows, preserve original requested status, import via Woo APIs, avoid exposing intermediate products. Match variable parents/children after assembly.
4. Preflight full batch: run rule engine on final assembled snapshots, retain original row numbers and product identifiers, show blockers and fix URLs.
5. Release selection: eligible only / manual selected / rerun changed; capability-confirmed publish with fresh validation, audit each item, suppress double release.
6. Recover: pause/resume/cancel/retry, error codes, import file expiry, persistent job checkpoints, no duplicate product creation after restart.
7. Compare to Woo native CSV mapping and supported import hooks; do not claim universal interception of third-party importers. Build an explicit workflow without hijacking all imports unexpectedly.

### 7.6 REST/API/CLI integration
On invalid request for publication, return stable error code and issue list (HTTP 4xx when correctly applicable), or stage as declared. Do not silently convert a published request into a draft without a documented response field. Preserve auth context, webhooks, source IDs and trace IDs. Test product creation, update, variation create/update, price and stock changes, private/draft/scheduled status and bulk API requests.

### 7.7 Multi-stage approval (Pro)
Request states: `not_submitted → pending_preflight → needs_fixes | ready_for_review → in_review → changes_requested | rejected | approved → release_pending → published` plus `invalidated`, `cancelled`, `expired`. Requester submits only validated snapshot; approver capability checked server-side; requester cannot self-approve when segregation option enabled; optional second approval; decision requires notes where configured. Every approval signs logical product fingerprint + policy version. If product/policy changes, invalidate and re-review. An `approved` state is not permission to skip fresh release validation.

### 7.8 Published product revisions (Pro)
On protected, already-published product: store proposed changes (including selected variation metadata) in a versioned, approval-bound revision; leave live product unchanged. Show side-by-side old/new values and preview. Detect conflicts if live product changes since revision base, and force rebase/resolve rather than blindly applying. Apply as one controlled operation where possible; capture compensating rollback if multi-write process fails. Scope exclusions clearly documented (external ERP stock synchronization, third-party custom data, unsupported product types).

### 7.9 Scheduled release and revalidation
Scheduled queue stores target date/timezone, policy fingerprint, product fingerprint, target channels. Re-evaluate at execution time: if allowed publish and log; if stale/block/review necessary hold, notify, preserve schedule attempt. Timezone conversion and DST correctly handled. Avoid race with an editor, import job or approval update.

### 7.10 Bulk preflight engine (Pro)
Selection filters: product IDs, title/SKU, product type, categories, taxonomy, status, readiness, stock status, date, vendor if supported, saved filter. Dry-run shows estimated count and effective policy. Jobs chunk, persist progress, apply backpressure, pause/resume/cancel, issue counts with pagination, export; releasing only eligible product IDs after latest full validation; concurrent jobs lock per product or serialize conflicting changes. Long jobs must not block PHP admin HTTP requests.

### 7.11 Exceptions and waivers (Pro)
Form includes: affected product(s), selected rule, scoped policy, reason (required, minimum length), requested by, requested expiration with max limits, supporting note, approver (role-based), preview impact. Cannot waive security-sensitive invariants, cannot be silent/default-permanent. Record creation, review, usage, expiration and revocation in audit history. Do not equate warning acknowledgment with authorized waiver.

### 7.12 Uninstallation and failures
Plugin disabled does not delete product data; Pro disabled retains existing Pro policy/approval records and Free operates normally. Data removal is separate deliberate uninstall preference with safety guard; document behavior for disabling Free while Pro remains, migrations, recovery snapshots, backups and rollback. If policy engine crashes, fail safely for protected publication paths, keep draft saving available and display actionable diagnostics (no site-wide fatal).

---

## 8. ADMIN UI/UX DESIGN CONTRACT — EXACT OPTIONS, LAYOUT, ACTIONS

### 8.1 Design system and obligations for EACH screen
Use the **real WordPress admin design system**, not a fantasy dashboard or colorful consumer SaaS. Primary UI: `@wordpress/components`, WP notices/tables/forms, existing WooCommerce product editor patterns; build only bespoke components that need domain-specific complexity. Text left-aligned in LTR, mirrored in RTL. Clear headings, accessible contrast, WC/WordPress standard spacing, white/neutral surfaces, minimal unnecessary cards; no arbitrary neon gradients or flashy glassmorphism. Responsive desktop first and functional narrow admin layout; clear keyboard navigation, meaningful labels and focus, no inaccessible icon-only actions.

Every screen and each control **MUST** have a written definition: unique UI ID, Free/Pro owner, exact URL/menu, user roles, loading/empty/permission-denied/error/partial-success/success states, fields (type, label, default, format, validation, placeholder, tooltip, persistence key), table columns, filters, sorting, bulk actions, button trigger, data effect, error/confirmation response, API/handler name, capability, and test ID. Do not mark UX done from static Figma mockups or HTML-only pages. Build an interaction test linking every button to a handler, including save/cancel/clear/search/sort/export/filter and keyboard-only access.

### 8.2 Navigation architecture
**WooCommerce → Catalog Publish Guard** submenu group:
1. Overview (Free)
2. Product Preflight (Free)
3. Rules (Free basics, Pro advanced policies)
4. Catalog Audit (Free basic, Pro bulk)
5. Variation Inspector (Pro)
6. Bulk Preflight (Pro)
7. Import Guard (Pro)
8. Approvals (Pro)
9. Pending Revisions (Pro)
10. Exceptions & Waivers (Pro)
11. Reports (Free summary, Pro advanced)
12. Activity Log (Free basic, Pro detailed)
13. Settings (Free/Pro tabs conditional)
14. Tools & Diagnostics (Free/Pro)
15. Inline Classic Product Editor readiness panel (Free/Pro)
16. WooCommerce Products list column + filter (Free)
17. Import/REST error displays (Pro plus core structured error)

No non-functional Pro menu screens masquerading as features in Free. An optional tasteful feature comparison link is allowed if WordPress.org directory/upsell policies are respected; the Free plugin itself must remain useful.

### 8.3 Shared list/table component specification
Toolbar: `Search` (product title/SKU/ID, debounced, enter-to-commit where appropriate), status multi-select, product type, category taxonomy selection, policy/severity, source channel, date range (inclusive, timezone aware), `Apply`, `Reset`, saved view when Pro. Columns choose/view: product ID, thumbnail, name linked to edit, SKU, type, product status, readiness state, blocker count, warnings, last checked time, author/assignee if relevant, actions. Pagination 20/50/100, total/filtered count, sortable permitted fields, bulk selection and confirmation, explicit selected-all-on-page vs selected-all-results. Exports must protect CSV formula injection and sensitive info. Loading skeleton/rows, empty state with next action, retryable transport error, no-permission screen, partial result and stale badge. Tables must not fetch thousands of products at once.

### 8.4 Shared validation result component
Show title `Ready / Ready with warnings / Blocked / Needs review / Stale / Not checked / Validation error`, counts, last validation time, source and policy version, concise reason, grouped sections, each issue severity + rule ID + summary + observed value safe redacted + field anchor + `Fix in editor`, `Learn why`, `Rerun` controls. Never show green ready while any blocker exists. `Publish` CTA disabled only as a UI aid; actual server policy enforces. Focus first blocker after action, announce error count to assistive technology. Tooltip explains legitimate `zero price`, `out of stock`, intentional missing variations.


### 8.5 — UI-001: Overview (Free with Pro enhancements)

**Location:** WooCommerce > Catalog Publish Guard > Overview  
**Purpose:** Actionable KPIs with actual linked queues and selected coverage scope.

**Exact fields, options and form behavior:**
- Date range: last 7/30/90 days/custom; default 30.
- Scope: all/new/changed/published/drafts.
- Category and product type filter.
- Readiness chart data count; no fabricated 0->100 stats.
- Recent blocked events, top rule failures, stale validation count.
- Pro: approval queues, batch jobs and policy health.

**Visible table/list columns (where applicable):** Latest activity time | Product linked edit | Source | Readiness | Top issue | Owner | Open detail.

**All clickable/interactive actions and expected handlers:**
- Run catalog audit: launch bounded background scan.
- Open blocked products: apply blocked filter.
- Review recent failures: open run.
- Dismiss notice only if dismissible.
- Refresh: refetch all widgets with settled timestamp.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** KPI aggregation + navigation E2E + role access + timezones. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.6 — UI-002: Product Preflight (Free)

**Location:** WooCommerce > Catalog Publish Guard > Product Preflight  
**Purpose:** Single-product diagnostic, never mutating merely by scanning.

**Exact fields, options and form behavior:**
- Product autocomplete by name/SKU/ID; required.
- Product type read-only.
- Publish intent: new publish / update / scheduled preview.
- Show selected policy and rule count.
- Allow non-publishing rerun on staged data.
- Pro: simulate policy profile and proposal diff.

**Visible table/list columns (where applicable):** Severity | Rule ID | Field path | Expected/actual safe values | Remediation | Fix link.

**All clickable/interactive actions and expected handlers:**
- Validate now (GET/read operation when possible).
- Open product edit.
- Show rule details.
- Print/export non-sensitive report.
- Pro: Submit for approval.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Single ID validation; missing product; no permissions; no mutation side effect. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.7 — UI-003: Basic Validation Rules (Free)

**Location:** WooCommerce > Catalog Publish Guard > Rules  
**Purpose:** Fast usable per-rule configuration for solo merchants.

**Exact fields, options and form behavior:**
- Category selector: basics/pricing/images/stock/variations/types.
- Rule enable switch default per registry.
- Severity: info/warn/block (bounded per rule).
- Rule-specific threshold inputs with units and validation.
- Application: new publishes and optionally updates/scheduled.
- Global preset: Recommended/Strict/Custom; reset with preview.
- Rule field help/links, unsaved changes warning.

**Visible table/list columns (where applicable):** Rule ID | Rule title | Applies to | Enabled | Severity | Last changed.

**All clickable/interactive actions and expected handlers:**
- Save rules; validation and capability checks.
- Reset to recommended (confirm).
- Run simulated sample (non-mutating).
- Expand rule details.
- Show linked affected products.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Persist/reload all controls; invalid threshold; same rule different product types. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.8 — UI-004: Policy Builder (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Policies  
**Purpose:** Conditional rules with AND/OR groups, priority and safe simulation.

**Exact fields, options and form behavior:**
- Policy name (required, <=120 chars), description.
- Status draft/active/paused/archived.
- Scope include/exclude: categories, descendants, types, tags, brands, roles, import source.
- Condition group builder AND/OR nested max depth 3.
- Condition field/operator typed value/regex validator.
- Requirements select registry rule; severity/action override.
- Priority integer and conflict preview.
- Applies on first publish/update/scheduled/import/bulk.
- Approval path optional 1/2 stages.
- Effective/expiry dates; timezone.
- Policy version read-only, active status badge.
- Import/export policies with schema validation.

**Visible table/list columns (where applicable):** Policy name | Status | Scope | Priority | Rules | Version | Last changed | Actions.

**All clickable/interactive actions and expected handlers:**
- Add policy, duplicate, activate, pause, archive, version history.
- Add/remove/reorder condition or requirement.
- Save draft and publish policy.
- Simulate on product IDs without mutation.
- Compare conflicts and effective rules.
- Export settings, import dry-run.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Policy AST fuzz tests + precedence + XSS + cache invalidation + role capability. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.9 — UI-005: Catalog Audit (Free baseline, Pro extended)

**Location:** WooCommerce > Catalog Publish Guard > Catalog Audit  
**Purpose:** Safe paged scan over Woo product data, actionable list and progress.

**Exact fields, options and form behavior:**
- Scope draft/pending/published/all; default published + drafts.
- Category/type filters; search SKU/title.
- Severity status filter.
- Last checked sort and limit.
- Free manual audit; Pro scheduled/advanced filters.

**Visible table/list columns (where applicable):** Product thumbnail | Name/SKU | Type | WP publish status | Readiness | Issues | Last checked | Actions.

**All clickable/interactive actions and expected handlers:**
- Scan selected products: bounded safe job.
- Rescan a product.
- Open product/issues.
- Filter/search/sort/paginate.
- Pro: export full report and start bulk preflight.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Large catalog stress; stable pagination; queue lock; no accidental publish. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.10 — UI-006: Variation Inspector (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Variation Inspector  
**Purpose:** Scalable parent/child variation diagnosis with explicit expected set controls.

**Exact fields, options and form behavior:**
- Variable parent product autocomplete.
- Attribute groups and available terms.
- Expected combinations policy: NONE / MANUAL / COMPLETE MATRIX with deliberate opt-in.
- Wildcard ANY variation treatment.
- Include/exclude disabled variations.
- Parent image fallback allowed switch.
- Thresholds for per-variation price/SKU/stock/images.
- Matrix cap and summary-only fallback.

**Visible table/list columns (where applicable):** Attribute combination | Variation ID | Enabled | SKU | Price | Stock | Image | Rule results | Fix.

**All clickable/interactive actions and expected handlers:**
- Inspect now.
- Toggle expected/ignored combination with confirmation.
- Preview missing/duplicate/orphan groups.
- Open exact variation editor.
- Export diagnostics CSV.
- Submit variant policy update for permissioned save.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Size-color combos, wildcards, intentional absent combos, huge matrix cap, 5000 variants. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.11 — UI-007: Bulk Preflight (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Bulk Preflight  
**Purpose:** Background dry-run/revalidate/release batches with progress and safe subset.

**Exact fields, options and form behavior:**
- Saved filter or explicit product IDs.
- Status/category/type/last-change/owner/issue filters.
- Batch label and dry-run default true.
- Chunk size configurable within bounded range.
- Include new vs update vs scheduled.
- Release plan: eligible-only / selected / staged review.
- Conflict behavior: revalidate, skip changed, manual review.

**Visible table/list columns (where applicable):** Batch ID | Created by | Total | Checked | Blocked | Ready | Pending | Progress % | Status | Actions.

**All clickable/interactive actions and expected handlers:**
- Create dry-run.
- Start/pause/resume/cancel job.
- Inspect row issues.
- Export results.
- Select ready rows.
- Preview impact.
- Release eligible products with capability and fresh revalidation.
- Retry failed rows idempotently.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** 10k catalog, concurrent jobs, job cancellation, stale rows, authorization, per-row outcome. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.12 — UI-008: CSV Import Guard (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Import Guard  
**Purpose:** Optional protected CSV import staging and deliberate release.

**Exact fields, options and form behavior:**
- CSV chooser, limits/encoding/delimiter.
- Column mapping: ID/SKU/name/type/status/parent/attributes/price/images and Woo supported fields.
- Update existing? yes/no; key identifier strategy.
- Target default: stage, preserve requested publish status.
- Preview count, created/updated/error/conflict.
- Variation assembly readiness and parent dependency.
- Import timeout/row error details with line numbers.

**Visible table/list columns (where applicable):** Row | Source identifier | Target product | Action create/update | Requested status | Stage status | Issues | Fix/retry.

**All clickable/interactive actions and expected handlers:**
- Upload/validate file.
- Save mapping profile.
- Preview dry-run (never mutate).
- Stage/import approved.
- Pause/resume/cancel.
- Review parent-child unresolved.
- Retry selected rows.
- Send eligible to bulk preflight.
- Remove uploaded statement according to retention.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Malformed CSV, UTF-8, duplicate SKUs, partial upload, parent-child order, idempotence. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.13 — UI-009: Approval Queue (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Approvals  
**Purpose:** Role-based product review, signed snapshot decisions and assignment.

**Exact fields, options and form behavior:**
- Tabs: Ready/Pending/In Review/Changes Requested/Approved/Expired.
- Filters status/assignee/submitter/category/stage/date.
- Approver selection, step 1/2 roles.
- Decision comment required on rejection/waiver; default editable.
- Approval mode: 1-stage/2-stage, self-approval forbidden default.
- Product diff and validation summary.
- Snapshot hash, policy version, last mutation.

**Visible table/list columns (where applicable):** Request ID | Product | Requester | Assignee | Validation result | Current stage | Age | Updated | Actions.

**All clickable/interactive actions and expected handlers:**
- Submit.
- Claim/assign.
- Approve (with fresh state check).
- Reject with reason.
- Request changes.
- Reassign.
- Cancel own request.
- View diff.
- Audit trail.
- Batch approve only homogeneous ready items with preview.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Approver capability, self-approval, concurrent approvals, changed snapshot, 2-stage order. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.14 — UI-010: Published Product Revisions (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Pending Revisions  
**Purpose:** Protect live listings while proposed changes await validation/approval.

**Exact fields, options and form behavior:**
- Product search, revision status and assignee.
- Fields changed select/filter.
- Compare live vs proposal, variation changes and images.
- Base version fingerprint, conflict indicator.
- Draft preview and per-field support notes.

**Visible table/list columns (where applicable):** Revision ID | Product | Original version | Changed fields | Author | Approval | Conflict | Submitted.

**All clickable/interactive actions and expected handlers:**
- Save proposal.
- Run validation.
- Submit for approval.
- Compare details.
- Approve or request changes.
- Resolve conflict/rebase.
- Apply revision (fresh version check).
- Reject/archive.
- Rollback assisted if supported.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Existing live remains unchanged, stale apply blocked, supported variation changes, rollback. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.15 — UI-011: Exceptions & Waivers (Pro)

**Location:** WooCommerce > Catalog Publish Guard > Waivers  
**Purpose:** Time-limited documented exception to selected non-critical business policies.

**Exact fields, options and form behavior:**
- Product IDs and rule/policy ID.
- Waiver reason required min 20 chars.
- Expiry date/time with bounded maximum.
- Reviewer/role and second approval optional.
- Scope one product/rule/limited batch.
- Evidence note optional, no public private file by default.
- Show non-waivable integrity/security errors.

**Visible table/list columns (where applicable):** Waiver ID | Product | Rule | Reason summary | Requester | Approver | Expiry | State.

**All clickable/interactive actions and expected handlers:**
- Request waiver.
- Approve/reject permissioned.
- Revoke.
- Expire job.
- Open audit history.
- Simulate new publish decision.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Expired waivers, unsupported rules, unauthorized request, edit after waiver. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.16 — UI-012: Reports (Free simple, Pro extended)

**Location:** WooCommerce > Catalog Publish Guard > Reports  
**Purpose:** Understand bottlenecks and track real policy outcomes.

**Exact fields, options and form behavior:**
- Preset 7/30/90 days or custom.
- Category/type/source/policy/rule/status/role filters.
- Report: issue frequency, blocked attempts, readiness trends, approvals, batch success.
- Grouping by day/week/month, timezone.
- Export format CSV/JSON Pro; limited summary Free.
- Anonymize mode and redaction toggle.

**Visible table/list columns (where applicable):** Period | Products checked | Blocked attempts | Most frequent rule | Resolved issues | Approvals | Average latency.

**All clickable/interactive actions and expected handlers:**
- Generate report.
- Filter.
- Export sanitized CSV/JSON.
- Save view (Pro).
- Open underlying event list.
- Clear filters.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** No fabricated metrics, permissions on private audit data, export injection, localization. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.17 — UI-013: Activity Log (Free basic, Pro extended)

**Location:** WooCommerce > Catalog Publish Guard > Activity  
**Purpose:** Trace decisions without leaking private business/customer data.

**Exact fields, options and form behavior:**
- Type: rule changed, validated, blocked, submitted, approved, rejected, released, waiver, import, revision.
- Product ID/SKU or actor filter.
- Date range and correlation ID.
- Pro diff/details, export, retention and purge controls.

**Visible table/list columns (where applicable):** Timestamp UTC/display local | Actor | Action | Entity ID | Channel | Decision | Correlation ID | Details.

**All clickable/interactive actions and expected handlers:**
- Filter/search/sort.
- View event detail.
- Export (Pro capability).
- Retention preview and confirm purge.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Immutable events, no secrets, pagination, actor redaction, no silent loss. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.18 — UI-014: Settings (Free base, Pro expanded)

**Location:** WooCommerce > Catalog Publish Guard > Settings  
**Purpose:** Explicit global enforcement, adoption safety, roles, notifications and integration settings.

**Exact fields, options and form behavior:**
- General: enable guard, mode audit/warn/enforce, first-install onboarding recommended; DO NOT silently unpublish existing.
- Apply to: first publish, updates, scheduled, quick/bulk, API, importer; display coverage limitations.
- Product exclusions: types/categories/IDs with explainable guards.
- Readiness defaults / preflight cache lifetime / staleness.
- Media checks sync/asynchronous caps and timeout.
- Inventory/zero-price defaults and intentional variant gaps.
- Notifications: email enabled, recipients by capabilities, event triggers; throttle.
- Pro policies: default precedence, waiver expiry max, role/capability mapping.
- Pro approvals: one/two stages, segregation of duties, approval expiration, revision mode.
- Pro jobs: chunk sizes, concurrency, memory/time limits, queue retries.
- Pro import: MIME/size/row cap, file retention, error behavior, staging default.
- Reporting: log retention, export privacy.
- Privacy: uninstall delete-or-preserve and opt-in telemetry (off by default).
- License: status, key masked, Woo Marketplace integration only if compliant.

**Visible table/list columns (where applicable):** Setting | Value | Owner Free/Pro | Last changed | Validation.

**All clickable/interactive actions and expected handlers:**
- Save each tab.
- Discard unsaved changes.
- Restore documented defaults (confirm).
- Export/import settings Pro with dry-run.
- Test notification (permissioned).
- Run rule simulation.
- View integration coverage matrix.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Cross-tab state persistence, invalid settings, role map escalation, settings upgrade migration. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.19 — UI-015: Tools & Diagnostics (Free base, Pro enhanced)

**Location:** WooCommerce > Catalog Publish Guard > Tools  
**Purpose:** Operational visibility and safe repair, no magic success messages.

**Exact fields, options and form behavior:**
- WordPress/PHP/Woo versions, active product editor.
- Composer autoload/class registry, DB schema/migration version.
- REST/status/quick edit/import adapter coverage tests.
- Cron/Action Scheduler queue status and stalled jobs.
- PHP error logs safe excerpts/redaction.
- Feature licensing status Pro.
- Debug log toggle with TTL.
- Data retention estimates and privacy preview.

**Visible table/list columns (where applicable):** Check name | Compatibility | Last checked | Status | Guidance | Action.

**All clickable/interactive actions and expected handlers:**
- Run health check.
- Self-test safe no product mutation.
- Copy sanitized diagnostics.
- Retry failed job.
- Run migration preview; execute only authorized.
- Export structured support package.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Missing Woo, PHP constraints, vendor absent, failed migration, jobs stuck, no secret leakage. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.20 — UI-016: Product Editor Readiness Box (Free, Pro extensions)

**Location:** Products > Edit Product > Publish panel / meta box  
**Purpose:** In-context actionable immediate feedback and preserved drafts.

**Exact fields, options and form behavior:**
- Auto check status, last checked timestamp and stale indicator.
- Counts blocker/warning/info.
- Issue accordion grouped by variation/field.
- Deep links to exact Woo product tab/variation.
- Pro policy origin and review request entrypoint.
- Reason for block, draft preserved confirmation.

**Visible table/list columns (where applicable):** Severity | Rule | Field | Observed | Fix link.

**All clickable/interactive actions and expected handlers:**
- Validate now.
- Fix issue (navigate field).
- Save draft.
- Request review (Pro).
- Submit again after correction.
- Show policy details.
- Dismiss informational notices only.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** Classic editor E2E, autosave, variation AJAX saves, REST publish bypass and no JS fallback. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.21 — UI-017: Products List Integration (Free)

**Location:** Products > All Products  
**Purpose:** At-a-glance readiness and filtered action results.

**Exact fields, options and form behavior:**
- Optional readiness column on/off.
- Filter Ready/Warnings/Blocked/Stale/Not checked.
- Show number of blockers.
- Last checked tooltip.
- Action: Validate selected under capability.

**Visible table/list columns (where applicable):** Thumbnail | Product | SKU | Stock | Price | Readiness | Last checked | Publish status.

**All clickable/interactive actions and expected handlers:**
- Filter by readiness.
- Sort by freshness if supported.
- Open preflight.
- Bulk scan selected.
- Refresh selected row status.

**States:** loading | not configured | empty | filtered empty | ready | validation failure | permission denied | network failure | partial success | retry.  
**Mandatory tests:** WP Products list responsive, paginate, translated labels, no N+1 per row. All actions additionally need role/capability, input validation, success/failure, keyboard and loading tests.

### 8.22 Screen design verification pipeline
For every one of UI-001 through UI-017: (1) domain contracts/API schema; (2) low-fidelity state map; (3) design tokens and clickable state spec; (4) actual WordPress/WooCommerce-integrated implementation; (5) Playwright browser interaction tests for every action; (6) captured real WordPress admin screenshots at wide/narrow widths + RTL; (7) accessibility audit and fixes; (8) screenshots linked to `.ai/evidence-index.json`; (9) review by QA agent. Figma is optional; UI code and validated UX are mandatory. Designs MUST show all form-field options, taxonomy selectors, product type controls, variation rows, statuses, review buttons, filters and error states; a card-grid concept is not a completed screen.

### 8.23 Permission requirements
Capabilities should be explicit namespaced capabilities, initialized/mapped predictably: `wpcpg_view`, `wpcpg_validate`, `wpcpg_manage_rules`, `wpcpg_manage_policies`, `wpcpg_run_bulk`, `wpcpg_import`, `wpcpg_submit_review`, `wpcpg_approve`, `wpcpg_manage_waivers`, `wpcpg_view_audit`, `wpcpg_manage_settings`. Avoid inheriting unrelated broad capabilities where least privilege works. Provide a documented role matrix (Admin, Shop Manager, Product Editor, Reviewer, custom role) and secure defaults. Check capabilities server-side for all REST/admin/action endpoints; JS hiding is not authorization.

---

## 9. AI-NATIVE MULTI-AGENT TEAM, RESPONSIBILITIES AND ALL-AGENT RULES

The Lead Agent may embody roles sequentially if only one agent is available. Parallel workers can be delegated where the runner supports it. Do not pretend independent agents exist unless tools actually launched them. Every role shares the same repo memory, contracts, test standards and task definitions; no conflicting code changes without integration ownership.

| Role | Ownership | Must deliver | Forbidden shortcuts |
|---|---|---|---|
| A01 **Orchestrator/Product Lead** | Task graph, scope, sequencing, blockers, persistent state, final integration | PRD, requirements traceability, checkpoints, continuous dispatch | Waiting for routine approval; fake "100% done" |
| A02 **Market/Standards Researcher** | competitor verified matrix, WP/Woo API docs, release rule updates | timestamped sources, compatibility ADRs | Copying competitors' code or asserting undocumented absence |
| A03 **Solution Architect** | Free/Pro isolation, domain contracts, data migration, source adapters | architecture diagram, interfaces, lifecycle coverage proof | Assuming one post hook protects all writes |
| A04 **Free PHP Engineer** | Free plugin foundation, 20+ basic rules, editor guard, basic screens | functioning installable Free ZIP, CRUD/REST integration and tests | Premium classes in Free, UI-only restrictions |
| A05 **Pro Policy/Variation Engineer** | rule conditions, precedence, variation matrix, waivers | reliable policy evaluator, matrix tests, conditional UI | Force all variation combinations without policy |
| A06 **Pro Workflow Engineer** | bulk preflight, CSV staging, approvals, revisions, schedules | lifecycle jobs, staging/approval data, idempotency tests | Publish unsafe partial import, approve stale revision |
| A07 **UI/UX Designer** | IA, wireframes, control inventory, states, accessibility | 17 native WP designs with all fields/actions and tests | Static cards with missing controls, fantasy WordPress UI |
| A08 **Frontend Engineer** | WP components / React implementation, state + API wiring | working controls, errors, sorting, keyboard, responsiveness | Dead buttons, placeholder toggles or fabricated data |
| A09 **Security/Privacy Engineer** | auth, source upload, CSRF/XSS/SQL, concurrency, retention | threat model, findings, remediations, evidence | Security signoff without tested cases |
| A10 **QA/Automation Engineer** | PHPUnit, Playwright, Playground, MySQL, import fixtures, regression | automated reproducible test evidence, fail/retry loop | Passing tests by skipping assertions |
| A11 **Documentation/Developer Relations** | readmes, user/admin/dev docs, version synchronization | generated readme files, migration/upgrade guides, changelog | Feature claims not tied to tests |
| A12 **Release/Marketplace Engineer** | build ZIPs, Plugin Check, Woo QIT, marketplace materials | reproducible packages, release evidence, reviewer kit | Claiming publication/review acceptance without vendor action |

### 9.1 Shared agent rules
- Every action references a unique task ID and phase, with input/output contracts and test evidence.
- One accountable owner per task; other roles can assist or review.
- Never discard existing source, partial work or tests merely to simplify implementation.
- Do not ask human for names/colors/button placement. Use WordPress admin convention, choose defaults, document ADR.
- Always build UI+backend together; no screen complete until a real database/API path handles actions.
- Never use placeholder content or demo data in production screens outside explicit empty/demo fixtures.
- Prevent silent data loss; on error preserve drafts, approvals, revisions and batch checkpoint.
- Never fake versions, successful scans, compatibility, acceptance, test metrics, screenshots or Git commits.
- Manage secrets safely: no private keys, production credentials, personally identifying datasets or paid plugin code committed.
- Only perform external side-effect operations (release submission, production catalog action, service purchase) when authorized.
- All output must be accessible/translated; no copy-pasted bespoke framework ignoring WP/Woo norms.
- Every role must run relevant targeted tests before handing off; orchestrator runs integration/regression.

### 9.2 Universal task contract
Each task MUST include:
```yaml
id: WPCPG-P1-UI016-001
phase: P1
owner: Free PHP Engineer
status: ready  # idea|ready|in_progress|testing|done|blocked|deferred
priority: critical
dependencies: [WPCPG-P1-CORE-001]
summary: Implement production product-editor readiness box and server guard
acceptance_criteria:
  - Display field-level blocker/warning links and current snapshot state
  - Draft save remains allowed with missing price
  - Invalid published transition blocked server-side
  - No lost data during classic variation AJAX save
source_files: []
changes: []
test_commands: []
verified_evidence: []
blocker: null
next_action: Implement class + tests and run Playground E2E
```
Every `done` task references a real commit/hash/path plus passing test record or justified verified exception; task status must be **machine-readable**. Avoid "done" because a file exists without integration.

---

## 10. AUTONOMOUS NONSTOP EXECUTION LOOP — MANDATORY

### 10.1 Required actual agent behavior
Execute this algorithm within a persistent worker/orchestrator (or repeatedly until current interactive task session/tool budget ends). This is an instruction to the runner; a text prompt alone cannot cause asynchronous execution after process/session termination.

```text
BOOT:
  inspect_repository_and_git()
  read_full_master_and_start_agent()
  restore_or_create(START_HERE.md, .ai/state.json, BACKLOG.md, .ai/tasks.json)
  verify_state_against_actual_files_commits_and_tests()
  calculate_unblocked_tasks()

WHILE runner_is_active:
  if all_mandatory_tasks_verified_done:
      run_full_release_gates()
      if gates_pass: produce_final_release_handoff(); STOP
      else: generate_defect_tasks(); CONTINUE
  task = pick_highest_priority_unblocked_task(critical_path_first)
  if task absent:
      investigate_blockers_and_retry_non_destructively()
      if all tasks blocked by external_authorization_or_unavailable_tools:
          persist_handoff(); report_truthful_blockers(); STOP
      else: CONTINUE
  acquire_task_lock(task)
  mark_in_progress(task)
  inspect_relevant_code_and_contracts()
  implement_small_verified_increment(task)
  run_static_checks_and_targeted_tests(task)
  if failure:
      classify_failure(); diagnose(); fix(); rerun()
      if repeated_non_progress_attempts >= 3:
          record_reproduction_and_blocker()
          unblock_other_independent_tasks()
          CONTINUE
  run_related_regression_and_integration_smoke()
  if UI: run_real_browser_test_and_capture_real_screenshots()
  if Free/Pro: run_package_dependency_and_activation_smoke()
  if acceptance_criteria_not_met: reopen_task_with_evidence(); CONTINUE
  update_backlog_memory_and_documentation()
  commit_if_authorized_and_repository_clean_in_scope()
  append_decisions_and_evidence_index()
  set_NEXT_TASK_to_first_executable_step()
  emit_short_checkpoint_if_meaningful_without_pausing_execution()
  release_task_lock(task)
  CONTINUE
```

### 10.2 Why not a literal infinite busy loop
The goal is **nonstop productive progression**, not CPU burn or accidental repeated edit/retry. Include watchdog for repeated identical failures, maximum backoff, deadlock detection, memory write safety and rate-limited job retry. On environmental limitation, transparently record exact reason and exit instead of claiming unstoppable execution. When a supported agent runner is restarted, it reads checkpoint and continues. A chat answer is not a daemon and cannot guarantee running after the turn ends.

### 10.3 No-routine-questions decision matrix
| Situation | AI behavior |
|---|---|
| Screen layout unspecified | Choose WC-native pattern, design all controls, ADR, implement |
| Rule severity unclear | Research Woo semantics, choose conservative sensible defaults, test, ADR |
| Free/Pro ownership ambiguous | Preserve useful Free core, premium advanced workflows, ADR |
| Git merge conflict | Inspect, preserve both valid edits, resolve and test without wiping history |
| Missing test fixture | Build synthetic fixture; never invent result |
| Plugin marketplace policy uncertain | Recheck official docs, document variance, implement safe compliant default |
| One integration unavailable | Create guarded interface, honest unsupported notice, continue other tasks |
| External vendor login/credentials required | Block only external action, prepare submission-ready artifact and exact checklist |
| Cost, legal account, production release | Must have proper authorization; do not auto-submit or incur charges |
| User absent after kickoff | Continue within active runner until tasks done or actual execution limit |

### 10.4 Checkpoint reporting without stopping
Checkpoint every meaningful vertical slice or major gate, not every function. Report: `Phase/current task`, `completed with commit IDs`, `tests actual pass/fail`, `implemented screens with evidence`, `new decisions`, `open blockers`, `next task already in progress`. Never end message with a question asking the user to approve routine work.

---

## 11. PERSISTENT BACKLOG, MEMORY AND SESSION RESUME

### 11.1 Required files and source of truth
| File | Responsibility | Update frequency |
|---|---|---|
| `START_HERE.md` | human/AI-readable exact resume instructions, last good commit, NEXT TASK | every checkpoint/task |
| `.ai/state.json` | machine-readable overall phase, active task, task counts, last verified commit, runner status | on every transition |
| `BACKLOG.md` | prioritized high-level task board by consolidated phase | on completion/new defect |
| `.ai/tasks.json` | all granular task IDs, dependencies, acceptance + evidence | on every task |
| `DECISIONS.md` or `docs/adr/` | dated architecture, UI and domain decisions and reasons | every material change |
| `.ai/evidence-index.json` | logs, screenshots, CI links, tests keyed by task | upon evidence |
| `.ai/blockers.md` | reproducible blockers, attempted fixes, external dependencies | whenever blocked |
| `.ai/handoffs/YYYY-MM-DD-HHMM.md` | latest session handoff with exact next command | each interrupted session |
| `docs/FEATURE_TRACEABILITY.md` | requirement → rule/UI/API/test/Free-Pro/package mapping | on each accepted slice |
| `docs/COMPATIBILITY.md` | supported versions, adapters, claims vs tested facts | each release |

### 11.2 State JSON contract
```json
{
  "schema_version": 1,
  "product": "WPEssential Catalog Publish Guard for WooCommerce",
  "master_spec_version": "1.0.0",
  "current_phase": "P0",
  "active_task_id": null,
  "next_executable_task_id": "WPCPG-P0-REPO-AUDIT",
  "execution_mode": "ready_to_run",
  "runner_active": false,
  "last_verified_commit": null,
  "completed_tasks": [],
  "blocked_tasks": [],
  "last_tested_environment": null,
  "release_gate_status": "NOT_TESTED",
  "last_handoff_path": null,
  "last_updated_utc": null,
  "important_warning": "Template: not evidence of implemented code or test results"
}
```
Validate state against real filesystem, Git and logs each session. If memory claims task done but source/test missing, reopen it. Atomic writes are mandatory (write temp then rename) to avoid corrupt state. Preserve old state snapshot under `.ai/history/` on significant migrations.

### 11.3 Backlog state rules and automatic task selection
States: `idea`, `ready`, `in_progress`, `testing`, `done`, `blocked`, `deferred`. Only `done` after all acceptance checks with artifact/evidence. Dependencies checked from `.ai/tasks.json`; if Pro task depends on Free contract, work on Free first. Prioritize `safety > architectural prerequisites > user-visible vertical slices > advanced workflow > accessibility > release paperwork`, but do not omit less visible requirements. Blocked tasks are regularly revisited after relevant changes; no permanent silent skip.

### 11.4 Handoff format
```md
# WPCPG HANDOFF — UTC timestamp
- Repository/branch/HEAD and uncommitted changes:
- Master spec hash and version:
- Verified phase and exact active task:
- Completed tasks with commit links and test evidence:
- Tests actually run, versions, PASS/FAIL, logs:
- Screens completed and actual screenshot locations:
- Release ZIPs and build provenance if present:
- Blockers, reproduction, last 3 attempts, fallback:
- Decisions and risk notes:
- The NEXT executable task and FIRST command/file to open:
- Known unverified areas (do not claim completion):
```

### 11.5 Recovery without human "continue"
`START_HERE.md` must instruct every new coding agent: "Read Master + START_AGENT, inspect Git, recover state, execute next unblocked task, verify evidence, repeat while runner active. Do not request routine approval. Keep file current." Scheduled external re-invocation requires an actual configured runner/CI, not mere wording; configure one only with repository/runner permissions, safe budgets and owner-approved external behavior.

---

## 12. FIVE CONSOLIDATED DEVELOPMENT PHASES — ALL SUBTASKS REQUIRED

The phases are **five broad execution envelopes**, intentionally fewer than the previous 10+ phase method. Removing phase gates does NOT remove features, UI contracts or tests. Each phase contains many individual backlog tasks (tasks are granular for memory only). Automatically transition phase when its acceptance gates pass.

### PHASE P0 — DISCOVER, DECIDE, DESIGN, BOOTSTRAP
Required work:
1. Audit repo/branch/existing plugins, dependency versions, previous work, test quality and environment. Do not replace functioning code.
2. Verify competitor scope, current WordPress/Woo API architecture, product-edit lifecycle, CSV import, scheduled publication, Plugin Directory and Woo Marketplace rules; timestamp sources.
3. Write PRD, requirements traceability, domain models, rule registry, policy AST schema, source adapter coverage matrix, threat model and decision logs.
4. Create independent Free/Pro plugin stubs with PHP headers, Woo dependency guards, Composer 2 / PSR-4, unique namespace and activation test; no false readme claims.
5. Define UI design system, actual 17 screen inventories, permission matrix, links, state maps and browser test plan. Implement shared UI component contracts.
6. Create CI skeleton, PHP/JS linters, PHPUnit/Playwright runner scaffolds, stable fixture files, baseline Playground Blueprint; ensure P0 files actually load.
7. Initialize complete persistent `.ai/` backlog and START_HERE, task graph with all 79 rules and 17 screen IDs, automatic next-action selection.
**P0 gate:** repo audit complete, contracts documented, Free & Pro Composer metadata valid, isolated bootstraps load without fatal, master state recoverable, first Playground base boots, no false claims. Move directly to P1.

### PHASE P1 — COMPLETE FREE PRODUCT AND ACTUAL PUBLISH PREVENTION
Required work:
1. ProductSnapshotFactory and RuleEngine interfaces, Free rule implementations and unit fixtures for every Free rule.
2. Classic product editor widget, product list readiness column, single-product preflight, basic rules/settings, catalog audit, overview, basic report/activity/diagnostics with all controls.
3. Server-side lifecycle interception tested for classic editor, known WC CRUD paths, scheduled publishing and other documented Free-supported sources. Preserve drafts and data on invalid publish.
4. Versioned schema, history, capability and REST endpoints; caching/staleness, Woo-type-aware behavior, variable parent basics, stock/price/image checks.
5. Full Free onboarding, admin notices, translatable strings, keyboard/RTL/wide/narrow visual QA, WP Playground Free bundle and browser test suite.
6. Free-generated `readme.txt` and README.md based on verified Free capabilities; Plugin Check preliminary scan; Free independently installable and usable.
**P1 gate:** Free package installs/activates alone; all documented core publish guards and buttons tested in actual WP; no lost draft edits; exact first-publish blocker works server-side; Free no Pro dependency. Move directly to P2.

### PHASE P2 — COMPLETE PRO POLICY, IMPORT, APPROVAL AND REVISION WORKFLOWS
Required work:
1. Pro dependency/version guard, separate Composer/autoloader, upgrade and activation/deactivation fallback.
2. Policy builder with typed conditions, AND/OR groups, precedence, simulation, presets, custom taxonomy/meta support and tests.
3. Advanced Variation Inspector including declared expected set, duplicate/wildcards/orphans, parent/child assembly and large-data safeguards.
4. Background scanner and Bulk Preflight/Release with chunking, locks, idempotency, pause/resume/cancel, stale-checks and per-product audit.
5. CSV Import Guard upload/preview/row mapping/streaming staging/resume; validate after variable parent/child assembly; authorized release; no intermediate public products.
6. REST/API/CLI adapter coverage, errors, staging and integration contracts; document direct SQL exclusion.
7. Approval Queue, roles/assignment/one-two stage decisions/waivers, invalidation on changes, request comments, audit and emails.
8. Published Product Revision staging, diff, conflict detection, approval/apply under tested adapter scope; scheduled revalidation and notification.
9. All Pro UI screens and fields/actions validated against backend; Pro reporting, retention settings, policy import/export and diagnostics.
10. Pro Playground Blueprint bundle, real E2E fixtures, Free+Pro activation/upgrade/downgrade tests.
**P2 gate:** Complete Pro install, every user-facing Pro workflow exercised E2E and no core feature stubbed, Free works with Pro turned off. Move directly to P3.

### PHASE P3 — HARDEN END-TO-END, TEST ALL FAILURES, FIX EVERYTHING
Required work:
1. Exhaustive rule unit tests, property-based policy/variation tests and test matrix linked to 79 rules.
2. Integration tests for all supported publish sources and changed-product invalidation; high-load tests for 1k, 10k and feasible 50k products/variation configurations.
3. SQLite-based Playground tests for UI/install/demo/reproduction; separate **MySQL/MariaDB** tests for transactional behavior, concurrent approvals, SQL locking and real Woo imports. Playground does not substitute DB reliability tests.
4. Security: capabilities, CSRF/nonces, stored/reflected XSS, REST/auth, uploads and CSV parser, SSRF risks, regex DoS, unsafe deserialization, CSV injection, file storage/public leakage, concurrency and audit tampering.
5. Accessibility WCAG-informed keyboard/screen reader focus, ARIA notices, contrast, RTL, compact screens, translation and JS fallback; test real WordPress admin screenshots not mockups.
6. Compatibility matrix for supported PHP, WordPress, WooCommerce, simple/variable/virtual/downloadable/external/grouped products, imports, popular themes and selected plugins.
7. Activation/upgrade/downgrade/uninstall/data retention and migration regression; no accidental mass unpublish or changes to live products on activation.
8. Performance profiling; queue retries/locks; fail-safe states; plugin configuration import/export schema and docs drift tests.
9. Create defects for every failure and repeat automated fix/retest until green or truthful blocker with reproduction; do not request normal human approval.
**P3 gate:** acceptance matrix passed with archived logs, source adapters truthfully documented, zero critical unresolved safety vulnerabilities, no serious known data loss; then P4 automatically.

### PHASE P4 — COMPLETE MARKETPLACE-READY DOCS, BUILDS AND EVIDENCE
Required work:
1. Produce deterministic Free ZIP (`wpessential-catalog-publish-guard.zip`) and Pro ZIP (`wpessential-catalog-publish-guard-pro.zip`), install each in CLEAN WP instance, verify vendor/autoload and compiled assets.
2. Generate Free `readme.txt`, Free/Pro `README.md`, versioned changelog and release notes from a single verified canonical manifest; reject docs drift or unsupported claims.
3. Free WordPress.org submission readiness: complete plugin headers, directory slug/name/trademark check, proper GPL-compatible licensing, tags, FAQ, changelog, screenshots, banners/icons, Text Domain and language files, Plugin Check, readme validator, SVN-ready release instructions, admin privacy/security, no Pro-only premium executable code in Free.
4. Pro Woo Marketplace submission readiness: vendor expectations/business model, security, documented supported WP/Woo/PHP versions, extension compatibility, accessibility, QIT/test evidence where available, reviewer guide, example products, product page content, licensing/update integration, screenshots, demo video optional, support policy and support contact placeholders that must be supplied by owner.
5. Build self-contained Playground bundles using **actual generated plugin ZIP files**, verify bundle JSONs, launch base/Free/Pro Playgrounds, capture logs/screenshots and store output paths in evidence index.
6. Create source archive, release checksums, SBOM/license list, generated docs, QA report, open issues, known exclusions, compatibility chart, roadmap, exact owner-only release steps.
7. Run clean-release acceptance with frozen source commit, repeatable build and no fabricated marketplace status.
**P4 gate:** all deliverables tested; archive exact paths and artifacts, state `SUBMISSION_READY_NOT_SUBMITTED` unless authorized actual submission completed and verified externally. End loop only after all mandatory tasks/evidence done, or documented genuine external block remains.

---

## 13. REQUIRED TEST MATRIX AND PROOF-BASED DEFINITION OF DONE

### 13.1 Test layer obligations
- **Static:** Composer validate, PHP syntax, WordPress Coding Standards, PHPStan, JS ESLint/TypeScript, dependency audit, forbidden production dev files, code license scan.
- **Unit:** each Free/Pro rule, policy AST, severity, conflict precedence, utility parsers, money/price semantics, variation permutations, approval state transition, fingerprint invalidation, authorization policy.
- **Integration WP/Woo:** product CRUD create/save, product types, database migrations, Woo Importer, REST routes, schedule events, version-specific hooks, roles and plugin lifecycle.
- **Playwright E2E:** real WooCommerce admin: product editor and every UI-001..UI-017 control, table sorting/pagination, keyboard focus, and error messages. Screenshot evidence from actual environment.
- **WordPress Playground:** repeatable base, Free and Free+Pro Blueprints for new install, reproduction, smoke tests, sample products; report actual command/browser run.
- **MySQL/MariaDB:** separate transactional/locking/concurrent updates, bulk scan performance, background queues, large variations and import recovery.
- **Release smoke:** fresh install from **built ZIPs**, Free-only, Free+Pro, Pro disabled/reactivated, Woo missing, bad version graceful handling, multilingual/RTL, multisite settings if supported.

### 13.2 Mandatory tricky scenarios (not exhaustive)
| ID | Scenario | Required assertion |
|---|---|---|
| T01 | Simple missing title | Block eligible publish, preserve draft |
| T02 | Missing price vs numeric `0` | Missing blocked by rule; genuine zero allowed by default |
| T03 | Sale price > regular | Block with exact price field guidance |
| T04 | Out-of-stock | Not automatically blocked |
| T05 | Backorders with negative quantity | Respect supported Woo semantics and policy |
| T06 | Virtual without dimensions | Not blocked by irrelevant shipping requirement |
| T07 | Downloadable file missing | Block only where file requirement applies |
| T08 | External product invalid URL | Block with field anchor |
| T09 | Grouped product with no children | Policy-driven treatment, safe default |
| T10 | Variable parent with no enabled purchasable variation | Block new publish |
| T11 | Variation intentional missing combination | Do not demand full Cartesian matrix by default |
| T12 | Variation wildcard ANY | No naive false duplicate/gap |
| T13 | Duplicate attribute permutation | Deterministic issue and blocked when configured |
| T14 | Orphan variation | Identify correct parent and safe remediation |
| T15 | Variation inherits allowed parent image | Pass where policy allows |
| T16 | Variation explicitly requires own image | Block under targeted Pro policy |
| T17 | Huge attribute matrix | Bound memory/time, show policy/limit error |
| T18 | Attribute value deleted after approval | Mark stale, prevent release |
| T19 | Product category changes | Recompute effective policies |
| T20 | REST tries publish invalid product | Structured server-side error/hold |
| T21 | REST edits published protected price | Revision staging per supported Pro adapter |
| T22 | Woo CSV includes parent before children | Defer final validation until all assembled |
| T23 | Woo CSV includes children before parent | Safe staging and relation resolution |
| T24 | Duplicate CSV import | Idempotency; no double creation/release |
| T25 | CSV malformed/UTF-8 invalid | Accurate row error, no partial public products |
| T26 | Background job fails mid-chunk | Resume without replay side effects |
| T27 | Two bulk release jobs same product | Product lock/version prevents duplicate release |
| T28 | Scheduled product becomes invalid | Hold and audit; never silently publish |
| T29 | Daylight saving/timezone shift | Correct date normalization and revalidation |
| T30 | Requester tries self-approve under segregation | Forbidden server-side |
| T31 | Approval stage 2 before stage 1 | Forbidden |
| T32 | Product edited after approval | Approval invalidated, re-review |
| T33 | Policies edited after approval | Recompute/review according to policy version |
| T34 | One manager revokes waiver | Future releases cannot reuse waiver |
| T35 | Waiver expired before scheduled release | Release blocked or held |
| T36 | Unsupported direct SQL importer | Detection may work; do not claim prevention |
| T37 | Pro turned off | Free continues and Pro records preserved |
| T38 | Free turned off while Pro active | Pro gracefully deactivates functionality |
| T39 | Activating plugin on 50k existing live products | No mass unpublish; asynchronous audit limits |
| T40 | Draft save without image | Still saved as draft |
| T41 | Failed save after HTTP timeout | No accidentally published partial data |
| T42 | Missing Composer vendor directory | Graceful notice and no fatal |
| T43 | Malicious user accesses approve API | Permission denied, audit security event |
| T44 | CSV formula payload in SKU/name | Export not executable in spreadsheet |
| T45 | Malicious media or external URL | No SSRF via sync validation |
| T46 | Concurrent revision apply after live edit | Version conflict and safe rejection |
| T47 | REST/API UI nonces, XSS payload | Safe sanitization/escaping/auth |
| T48 | Multiple policies conflict | Deterministic precedence and explanation |
| T49 | RTL / keyboard only | All functionality accessible |
| T50 | WordPress.org Free ZIP | Real activation + Plugin Check + readme validator |
| T51 | Woo Marketplace Pro ZIP | Free dependency guard + real QIT/compatible alternative report |
| T52 | Documentation features outpace code | Generator refuses unverified claim |
| T53 | Old pending validation after product update | Stale result never used to publish |
| T54 | Uninstall with preserve preference | No unintended deletion |
| T55 | Uninstall with delete preference | Only owned data deleted when authorized |
| T56 | Stale/corrupted persistent AI state | Verify Git/tests and recover, never invent completion |

Every acceptance scenario has environment version, fixture, command, timestamp, actual result, screenshot/log where applicable, and owner. **A test matrix listed in Markdown alone is not proof that testing happened.**

### 13.3 Definition of Done per granular task
Code implemented; all listed UI controls behave; positive/negative/permission tests pass; no regression; translated labels; analytics/reporting truthful; docs up to date; security reviewed for affected surfaces; evidence archived; verified commit or artifact hash; `.ai` state updated. Mock-only demos, source files without installation, TODO stubs, hardcoded success badges and test skips do NOT count.

### 13.4 Release STOP conditions
Block final "submission-ready" claim if: accidental product publishing; lost draft/live changes; incomplete approval security; unprotected known source falsely advertised as supported; untested Free/Pro clean install; missing Composer build; failing Plugin Check critical warnings; leaked private data; missing Playground bundle despite available ZIPs; packaging contains Pro code in Free; docs assert unimplemented functionality.

---

## 14. DOCUMENTATION GENERATION — SINGLE VERIFIED MANIFEST

**Never manually maintain diverging feature lists across `readme.txt`, `README.md`, docs and marketplace copy.** Maintain one canonical, schema-validated `docs/release/product_manifest.json` (example companion manifest intentionally marked `release_approved=false`). It records:
- Free and Pro identifiers, names, slugs, tested version range, author, support URL, license, text domain, version, PHP minimum, WC minimum, WP minimum and test status.
- Per-feature: stable ID, tier, implemented boolean, tests evidence paths, human-friendly summary, documentation claim text, last tested commit.
- Per-screen: UI ID, shipped boolean, test ID and screenshot evidence.
- Changelog with version/date/source commit; dependency/license info; credits/3rd-party data disclosures; real support and FAQ text.

### 14.1 Generator requirements
Implement `scripts/generate_readmes.py` so that it:
1. Validates manifest schema and refuses release docs for missing/unverified release version, licensing, tested compatibility, unsatisfied claimed features or absent evidence when `--release`.
2. Generates Free `readme.txt` in WordPress.org format: plugin name, contributors (verified), tags, Requires at least, Tested up to, Requires PHP, Stable tag, License, License URI, Short Description, Description, Installation, FAQ, Screenshots (real numbers/assets), Changelog, Upgrade Notice if relevant.
3. Generates Free `README.md` and Pro `README.md` plus optionally Marketplace listing copy, architecture compatibility notes and release changelog; Free text must NOT claim Pro-only features.
4. Aligns plugin main file Version, readme stable tag, release artifact names and deployed package metadata; CI fails on mismatch.
5. Exposes `--check` to compare generated bytes without editing; CI rejects stale docs.
6. Keeps private credentials, unsupported claims, placeholder screenshots, non-existent test results out of public docs. Use user-friendly installation/removal instructions and exact Woo dependency behavior.

### 14.2 User and developer documentation
`docs/user/GETTING_STARTED.md`, `docs/user/FREE_RULES.md`, `docs/user/PRODUCT_PREFLIGHT.md`, `docs/user/VARIATIONS.md`, `docs/user/POLICIES.md`, `docs/user/BULK_PREFLIGHT.md`, `docs/user/IMPORT_GUARD.md`, `docs/user/APPROVALS.md`, `docs/user/REVISIONS.md`, `docs/user/FAQ_TROUBLESHOOTING.md`; `docs/developer/HOOKS_APIS.md`, `docs/developer/ENFORCEMENT_COVERAGE.md`, `docs/developer/MIGRATIONS.md`, `docs/developer/TESTING.md`, `docs/developer/EXTENSION_GUIDE.md`, `docs/developer/SECURITY_PRIVACY.md`, `docs/release/WORDPRESS_ORG_CHECKLIST.md`, `docs/release/WOO_MARKETPLACE_CHECKLIST.md`. Every UI option and API status documented.

---

## 15. WORDPRESS PLAYGROUND + BLUEPRINT ENGINE — REQUIRED

### 15.1 Blueprints and packaging contract
In `playground/blueprints/base/blueprint.json`, `free/blueprint.json`, `pro/blueprint.json` use official schema `https://playground.wordpress.net/blueprint-schema.json`, appropriate `preferredVersions`, `login`, `landingPage`, `installPlugin` steps, and `pluginData` resource (NOT deprecated `pluginZipFile`). Base installs WooCommerce from WordPress.org and activates it; Free bundle then installs the actual built Free ZIP; Pro bundle installs Free before the actual Pro ZIP. Bundled resource paths must match ZIP root contents.

Required outputs after real plugin builds:
```text
artifacts/playground-base.zip     # blueprint.json installs WooCommerce
artifacts/playground-free.zip     # blueprint.json + wpessential-catalog-publish-guard.zip
artifacts/playground-pro.zip      # blueprint.json + Free ZIP + Pro ZIP
```
Templates are checked-in valid JSON but Free/Pro **are not runnable until the plugin ZIPs exist and the builder assembles the resource bundle**. A builder must fail loudly on missing ZIPs. Do not mark Playground tests as passed until a real CLI/browser run completes.

### 15.2 Real commands, adapted to verified CLI version
```bash
# Example using official Playground CLI, after dependencies and bundles exist:
npx @wp-playground/cli server --blueprint=./artifacts/playground-free.zip
npx @wp-playground/cli server --blueprint=./artifacts/playground-pro.zip
# Directory bundles with local "bundled" resources may require --blueprint-may-read-adjacent-files
```
Run smoke: login, activate Free, activate Pro (Pro only after Free), inspect WooCommerce menus, create fixtures, capture Product Editor readiness, test invalid publish, test draft save, run ready product, approval and import paths. Export screenshot filenames and logs to evidence index, note PHP/WordPress/Woo actual versions.

### 15.3 Database limitation
Playground commonly uses SQLite for convenient reproducible UI tests. Always run database/concurrency/revision-locking tests separately on real MySQL/MariaDB. Never imply Playground proves production MySQL behavior.

### 15.4 Future self-tests
Consider deterministic fixtures and safe test hooks only in test build, not plugin production zip. Sample products, image placeholders explicitly labeled fixtures; don't use real merchant catalog/production site without authorization.

---

## 16. WORDPRESS.ORG FREE SUBMISSION-READY CONTRACT

Verify most recent WordPress.org Detailed Plugin Guidelines, plugin headers, readme spec, trademark/naming conventions, WordPress coding standards, plugin directory requirements and Plugin Check outputs at release time. Required:
- GPL-compatible license and third-party licensing inventory.
- Clean Free ZIP with same root plugin directory/slug and main file, validated `Requires Plugins` dependencies if appropriate and compatible WordPress version behavior.
- No hidden Pro code, forced tracking, undisclosed SaaS API calls, unsolicited admin nag spam, unauthorized links, security weaknesses, unsafe PHP output or unescaped translations.
- Correct plugin header `Version`, `Requires at least`, `Requires PHP`, `Requires Plugins` if supported, `Text Domain`, `Domain Path`, `License` and Woo-compatible initialization.
- Accurate `readme.txt` with actual tested compatibility and functional claims, verified with official readme validator; screenshots/icons/banners from genuine tested screens, appropriate dimensions.
- Clean activation/deactivation/uninstall, data retention disclosure, WP Cron/AS cleanup, direct-file access protection, secure permission checks.
- Automated Plugin Check and important manual checks; store run outputs. If credentials/SVN access unavailable, generate package/reviewer instructions; **do not claim accepted/published**.
- SVN-ready layout/tested tags/trunk assets and release support/FAQ; WordPress.org approval is external and never guaranteed.

WordPress.org references: https://developer.wordpress.org/plugins/wordpress-org/ ; https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/ ; https://wordpress.org/plugins/developers/

---

## 17. WOO MARKETPLACE PRO SUBMISSION-READY CONTRACT

Check current Woo Marketplace vendor onboarding, product naming, revenue-share/pricing, WooCommerce branding, support, code requirements, PHP/WP/Woo version support, security and quality tests before submission. A paid plugin is not automatically accepted by Woo Marketplace because code is excellent. Required:
- Pro source ZIP with separate activation and version checks; Free dependency documented and functional.
- Vendor business review material, real differentiators/competitor context, $69/year suggested plan or current owner-approved price; no inaccurate freemium integration claims or off-marketplace upsell routing where prohibited.
- QIT test output where vendor tooling is available; automated alternatives and manual evidence where account-dependent QIT access is blocked. E2E install, activation, fatal detection, REST, accessibility, WP admin flows, PHP compatibility.
- Reproducible reviewer demo/setup: Free ZIP first, Pro ZIP second, 6 real test products (simple zero price, missing image, variable partial, bulk import, approval, protected revision), test policy JSON, click paths, expected result and screenshots/video if available.
- Woo HPOS and Cart/Checkout Blocks compatibility declarations only after applicable testing; avoid unrelated certifications. Verify actual product editor integrations and recent Woo versions.
- Public-facing Pro README, Marketplace summary, detailed description, actual screen assets, support policy/contact, privacy, license/updates integration, changelog, compatibility and limitations.
- Separate complete submission evidence pack: `dist/review-evidence/WOO/*`; status `SUBMISSION_READY` not `APPROVED` unless verified by external marketplace action.

Official reference: https://developer.woocommerce.com/docs/woo-marketplace/submitting-your-product ; https://developer.woocommerce.com/docs/best-practices/compatibility ; https://developer.woocommerce.com/docs/extensions/getting-started-extensions/

---

## 18. QA, SECURITY, PERFORMANCE AND RELEASE EVIDENCE REQUIREMENTS

### 18.1 Static and security checklist
Nonce, capability, REST authorization, HTML/JS escaping, sql prepared queries, upload paths and MIME, CSV formula prevention, regex ReDoS bounds, media validation SSRF, safe `unserialize` refusal, audit immutability, migration rollback, concurrent approvals, idempotent batch, revisions compare-and-swap, no PHP fatal on missing vendor/Woo, all data deletion deliberate. Audit actor and rule/policy versions; never log sensitive whole product/private claim payloads unnecessarily.

### 18.2 Performance
Never load all products/variation combinations in a synchronous admin request. Use pagination, background jobs, caches invalidated on product/policy/meta/category changes, bounded memory and queries, SQL indexes for repeated filters, batch retries and queue fairness. Benchmarks must identify environment and measured values; do not invent claims such as "10x faster".

### 18.3 Evidence structure
```text
dist/
├── wpessential-catalog-publish-guard.zip
├── wpessential-catalog-publish-guard-pro.zip
├── checksums.sha256
├── review-evidence/
│   ├── FREE/{plugin-check,readme-validator,zip-install,playground,screen-shots}/
│   ├── PRO/{qit-or-alternative,zip-install,playground,screen-shots,reviewer-guide}/
│   └── TESTS/{phpunit,playwright,mysql,security,performance,compatibility}/
└── release-manifest.json
```
All paths exist only when generated; until then, mark "planned". Track pass/fail/skipped status per test with explanation and actual log location. Any `SKIPPED` required check is either a release blocker or explicitly justified with real alternative evidence; it is not PASS.

### 18.4 Final release acceptance matrix
Free ZIP actual clean install ✅; Pro ZIP actual clean install ✅; Free-only works ✅; Free+Pro integration ✅; no fatal missing dependency ✅; 79 rules and applicability complete with tests ✅; 17 UI screens/surfaces functional with real controls ✅; core publish paths enforced as documented ✅; CSV/bulk/approval/revision flows tested ✅; Playground bundles execute ✅; MySQL/MariaDB concurrency ✅; Plugin Check/readme validator ✅; Woo vendor-ready review kit ✅; docs drift check ✅; security/RTL/accessibility ✅; state/backlog and handoff accurate ✅. Checkmarks here are **requirements to earn** and are NOT claims of completion.

---

## 19. FINAL EXECUTION DIRECTIVE

**Start immediately.** On an active coding-agent runner, inspect the repo, read the full specification, recover persistent memory, implement P0 then P1→P2→P3→P4 without waiting for routine human confirmation. Create/modify real source files, run verifiable tests, fix failures, maintain precise task state, and keep dispatching the next unblocked task. Do not end each session after providing a plan or ask "continue?". Resume from `START_HERE.md` when relaunched. Never claim the system can run after the runtime ceases without an actually configured runner, or submit externally without authorization.

**First executable instruction:** inspect `git status`, full repository and existing development files; reconcile `.ai/state.json` with actual Git/tests; choose `WPCPG-P0-REPO-AUDIT` if no verified prior work; otherwise execute the next unblocked task. **Report status truthfully; keep working.**
