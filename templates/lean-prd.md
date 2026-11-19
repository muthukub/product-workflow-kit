# <Title>

| Field | Value |
| --- | --- |
| ID | <PRD-001> |
| Type | lean-prd |
| Status | draft |
| Owner | <accountable person or explicit TBD> |
| Updated | <YYYY-MM-DD> |
| Revision | <positive integer> |
| Parents | <ID links; include originating PRD where applicable> |
| Risks | <RISK-ID links or explicit none> |
| Sources | <file/section/revision or URL/date; distinguish assumptions> |

## Problem and opportunity

One bounded problem, affected user, current alternative, evidence, and cost of doing nothing.

## Roadmap alignment

Parent roadmap link and initiative ID; explain contribution to its outcome.

## Users and jobs

Primary user, buyer if different, job to be done, and relevant context.

## Outcome and success measures

| Outcome | Metric | Baseline | Target / threshold | Measurement / window |
| --- | --- | --- | --- | --- |
| <outcome> | <metric> | <known or explicit unknown> | <target or hypothesis> | <method and window> |

## Scope

In-scope capabilities, principal user journey, business rules, permissions, key failure states, and measurable nonfunctional constraints where relevant. Label solution hypotheses.

## Behavioral requirements

Follow workflow/EARS.md. Selective EARS is the default for suitable observable behavior in new PRDs; record the scope of any existing PRD migration. Keep this table as the canonical source for behavioral obligations; other artifacts reference its stable IDs. Keep business hypotheses and learning methods in their existing sections. Use a justified None statement with no placeholder row if no behavior applies.

| Requirement ID | Pattern | EARS statement | Source / rationale | Verification | Risks |
| --- | --- | --- | --- | --- | --- |
| <PRD-001-R01> | <pattern value> | <explicit conditions/trigger, named system and observable shall response> | <source/decision link; label proposed choices> | <method, fixtures, observable result and relevant limits> | <risk links or None - reason> |

## Requirement changes

Record retired/replaced row IDs, rationale and replacements; never reuse an ID. State None if no rows have been retired. Wording revisions retain their ID and appear in the artifact revision history/context.

| Requirement ID | Change / rationale | Replacement ID |
| --- | --- | --- |
| <retired ID> | <why retired/replaced and source revision> | <replacement ID or None - removed> |

## Semantic review

Follow the semantic review protocol in workflow/EARS.md. Record the reviewed PRD/input revisions, behavior scope, reviewer role and actual method; identify specialist self-review and coordinator challenge accurately. Summarize the relevant areas below, combining rows where useful. Use Not reviewed for work not performed or None with a reason for inapplicable areas. No issue found must name the concrete cases considered. Material unresolved findings block readiness; planned tests are not resolution evidence.

| Review area | Finding / counterexample | Requirement IDs / source | Disposition / next action |
| --- | --- | --- | --- |
| <intent/boundary; values/limits; state/failure; data/side effects; cross-artifact consistency; verification/evidence> | <actual case, result, conflict or Not reviewed> | <canonical IDs or source section/revision; justified None if applicable> | <clarification/evidence, accountable role or TBD, material blocker and next review trigger> |

## Non-goals

Explicit exclusions that downstream epics must preserve.

## Assumptions and evidence

| Assumption / claim | Evidence | Confidence | Validation needed |
| --- | --- | --- | --- |
| <claim> | <source or gap> | <level and reason> | <test> |

## Risks born in this PRD

Before registration use local candidate labels such as CAND-PRD-001-01. Replace them with stable risk links returned by the register agent during this stage.

| Risk / candidate | Category | Cause -> uncertain event -> impact | Evidence / uncertainty | Required route | Closure criterion |
| --- | --- | --- | --- | --- | --- |
| <RISK link or temporary candidate> | <business/user/technical> | <statement> | <evidence/gap> | <story or RFC/ADR> | <observable proof> |

## Validation and release approach

Smallest useful release or experiment, measurement plan, guardrails, rollout/rollback needs, and continue/change/stop criteria. Do not imply testing has already happened.

## Epic candidates and dependencies

| Candidate outcome | Scope boundary | Dependency | Related risks |
| --- | --- | --- | --- |
| <outcome> | <boundary> | <dependency> | <risk links> |

## Open questions

Decision/input needed, accountable person or TBD, and impact on readiness.

## Readiness checklist

- [ ] Problem, user, scope, non-goals, and measurable outcome are clear.
- [ ] Roadmap initiative is linked and assumptions are labeled.
- [ ] Every identified risk has been registered with a stable ID.
- [ ] Active requirement IDs are stable, obligations are verifiable and patterns/terms/conditions are appropriate.
- [ ] Sources, assumptions and verification methods are explicit; contradictions, missing cases and architectural blockers have been reviewed.
- [ ] Actual semantic review and coordinator challenge are recorded; material unreviewed areas and findings block readiness.
- [ ] Material unknowns are resolved or explicitly block readiness.
