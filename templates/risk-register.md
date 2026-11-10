# <Title>

| Field | Value |
| --- | --- |
| ID | <RR-001> |
| Type | risk-register |
| Status | draft |
| Owner | <accountable person or explicit TBD> |
| Updated | <YYYY-MM-DD> |
| Revision | <positive integer> |
| Parents | <ID links; include originating PRD where applicable> |
| Risks | <RISK-ID links or explicit none> |
| Sources | <file/section/revision or URL/date; distinguish assumptions> |

## Register scope

Product scope, review owner/cadence, and links to contributing PRDs and roadmap. One register per product.

## Scoring and lifecycle

Apply workflow/CONTRACT.md: probability 1-3 x impact 1-3. Explain scores; review 6-9 before Now commitment. States: open, mitigating, accepted, closed. Do not close a risk just because an artifact was created.

## Risks

Repeat the following heading and table for each risk. Use a stable heading exactly like `### RISK-001`, with the title in the table. Replace the placeholder heading below with its assigned ID.

### <RISK-ID>

| Field | Value |
| --- | --- |
| Title | <short title> |
| Category | <business/user/technical> |
| Statement | <cause -> uncertain event -> impact> |
| Origin | <PRD link and discovery stage; initial risks originate during Lean PRD> |
| Roadmap item | <roadmap link and stable initiative ID> |
| Evidence | <observed facts or explicit assumption/gap> |
| Probability | <1/2/3 with rationale> |
| Impact | <1/2/3 with rationale> |
| Score | <probability x impact> |
| Owner | <person or explicit assignment blocker> |
| Status | open |
| Required route | <user-story for business/user; rfc-or-adr for technical> |
| Routed artifacts | <relative links to US or RFC/ADR; pending explicitly until allocated> |
| Supporting work | <EN links, related risks, or none> |
| Response and next action | <action, responsible party, trigger/date> |
| Closure criterion | <measurable observation or proof> |
| Residual exposure | <remaining exposure or unknown> |
| Review date / trigger | <date or observable trigger> |
| Resolution evidence | <measured closure evidence or acceptance authorization; pending while open> |

## Change log

| Date | Risk | Change | Evidence / rationale |
| --- | --- | --- | --- |
| <date> | <id> | <creation/update/route/score/resolution> | <source> |

## Open questions

Missing owners, unrouted risks, missing evidence, and required next actions. If there are no risks, state the assessment scope and evidence; do not invent one to fill the template.

## Readiness checklist

- [ ] Risks are deduplicated and mixed concerns are split.
- [ ] Each risk has origin, category, owner or blocker, score rationale, and closure criterion.
- [ ] Business/user risks link to stories when routing is in scope.
- [ ] Technical risks link to RFCs/ADRs when routing is in scope.
- [ ] Route links are reciprocal and resolutions have actual evidence.
