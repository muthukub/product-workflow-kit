# <Title>

| Field | Value |
| --- | --- |
| ID | <RFC-001> |
| Type | rfc |
| Status | draft |
| Owner | <accountable person or explicit TBD> |
| Updated | <YYYY-MM-DD> |
| Revision | <positive integer> |
| Parents | <ID links; include originating PRD where applicable> |
| Risks | <RISK-ID links or explicit none> |
| Sources | <file/section/revision or URL/date; distinguish assumptions> |

## Summary and question

Problem to evaluate, affected PRD/story/enabler, and specific question requiring feedback or evidence.

## Context and constraints

Existing architecture, current behavior, relevant technical risks, decision drivers, and source evidence. Mark unknown architecture explicitly.

## Goals and non-goals

Measurable goals, preserved product boundaries, and excluded redesigns.

## Requirement references

Follow workflow/EARS.md. Link canonical PRD requirement IDs as evaluation constraints and explain which options or experiments address them. Do not restate competing normative behavior or infer an accepted decision. Use None with a specific reason for investigation without applicable rows or an explicitly unmigrated parent. Apply the semantic review protocol to option feasibility, numeric/support limits and application/platform boundaries; return actual counterexamples, input revisions and blockers through the handoff.

## Options and tradeoffs

| Option | Benefits | Costs / drawbacks | Risk effect | Evidence / unknowns |
| --- | --- | --- | --- | --- |
| <option, including status quo where viable> | <benefits> | <costs> | <effect> | <evidence/gap> |

## Proposal

Recommended option with rationale and confidence. Relevant interfaces, data, failure behavior, security, operations, compatibility, rollout, and rollback; omit detail only with a reason.

## Evaluation plan

For each technical risk: hypothesis, experiment/spike, measurement, pass/fail threshold, required evidence, and resulting decision. Link enablers if allocated. Do not report proposed experiments as completed.

## Feedback and resolution

Reviewers/decision owner or TBD, open objections, review trigger, actual feedback with sources, conclusion and authorization evidence if accepted/rejected. A review date is a proposal unless agreed.

## Consequences and downstream work

Expected residual risks, story/enabler changes, and ADR needed if the outcome becomes an enduring architecture decision.

## Open questions

Unresolved tradeoffs, evidence gaps, and impact on implementation readiness.

## Readiness checklist

- [ ] The question, alternatives, drivers, and proposal are clear.
- [ ] Technical risk links and evaluation thresholds are present.
- [ ] Evidence is separated from predictions.
- [ ] RFC acceptance is backed by an actual authorized resolution.
