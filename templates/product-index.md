# <Product name> artifact index

Product: <product name or repository identity>
Updated: <YYYY-MM-DD>
Scope of current request: <stages and selected initiatives>

Artifact root: `docs/` by default; record the actual assigned root when continuing an existing product. All links below are relative to that root.

## Sources and terminology

| Source / term | Reference / definition | Evidence or assumption |
| --- | --- | --- |
| <item> | <link or definition> | <classification> |

## Artifacts and reservations

| ID | Type | Path | Status | Parent IDs | Assigned agent |
| --- | --- | --- | --- | --- | --- |
| <id> | <type> | <relative link; reserve before dispatch> | <reserved or current status> | <ids> | <agent> |

## Risk routing coverage

| Risk | Origin PRD | Category | Story or RFC/ADR destination | Route status | Blocker |
| --- | --- | --- | --- | --- | --- |
| <risk link> | <PRD link> | <business/user/technical> | <artifact link> | <pending/linked> | <reason or none> |

## Open questions and blockers

| Question | Affected IDs | Needed from | Next action |
| --- | --- | --- | --- |
| <question> | <ids> | <source/person> | <action> |

## EARS adoption and semantic review

Record each adopted initiative/PRD, source revision and selected behavior. New PRDs use selective EARS by default; for existing PRDs identify adopted and untouched legacy scope. Keep historical snapshots unchanged. Follow workflow/EARS.md and summarize actual PRD/downstream semantic review separately from static checking. Do not claim human review, executed verification or resolved findings without evidence. Re-review affected behavior and criteria after material changes.

| Scope / PRD revision | Reviewer / method | Findings and disposition | Readiness blockers / next review |
| --- | --- | --- | --- |
| <initiative, revision, adopted behavior and unmigrated scope> | <role, actual cases/method, PRD review-section link; Not reviewed if pending> | <counterexamples, clarification IDs and criterion coverage or reasoned no issue found; separate static-check result> | <material unreviewed areas, unresolved limits/decisions, missing criteria, responsible role and trigger> |

## EARS pilot

Optional comparative measurement; routine adoption and semantic review are recorded above.

If a pilot is selected, record its initiative/PRD IDs, source revision, actual baseline, observations and continue/adjust/stop recommendation using workflow/EARS.md. Otherwise state Not selected. Do not invent measurements or convert all existing artifacts automatically.

| Measure | Baseline / source | Pilot observation / source | Interpretation / next action |
| --- | --- | --- | --- |
| <clarification rounds, missing edge cases, review effort or requirement corrections> | <actual observation or unavailable> | <actual observation or not yet measured> | <finding or pending> |
