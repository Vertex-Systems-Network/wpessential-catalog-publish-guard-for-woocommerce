# Acceptance test matrix — NOT YET EXECUTED

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

Each row must be implemented as real tests with environment version, command, test fixture, stdout/stderr, pass/fail, file paths and Git commit.
