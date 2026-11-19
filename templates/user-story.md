# <Title>

| Field | Value |
| --- | --- |
| ID | <US-001> |
| Type | user-story |
| Status | draft |
| Owner | <accountable person or explicit TBD> |
| Updated | <YYYY-MM-DD> |
| Revision | <positive integer> |
| Parents | <ID links; include originating PRD where applicable> |
| Risks | <RISK-ID links or explicit none> |
| Sources | <file/section/revision or URL/date; distinguish assumptions> |

## Story

As a <specific user or stakeholder>, I want <capability or learning>, so that <user/business outcome>.

## Context and scope

Parent epic and PRD, relevant journey, constraints, and explicit exclusions.

## Acceptance criteria

| Criterion | Requirement | Given | When | Then |
| --- | --- | --- | --- | --- |
| <AC-01> | <canonical requirement ID link or None - learning-only reason> | <concrete starting state/fixture> | <action> | <observable result> |

Include relevant failure, authorization, accessibility, and boundary behavior. Do not add irrelevant boilerplate criteria.

## Requirement references

Follow workflow/EARS.md. Declare each applicable canonical PRD requirement ID with a direct link to its Behavioral requirements section and explain scenario coverage. Keep Given/When/Then as concrete examples of the rule, not independent copies of its normative text. For a learning-only story or an explicitly unmigrated parent, use None with a specific reason; retain the existing hypothesis and validation method. Apply the semantic review protocol to concrete normal/boundary/failure cases and cross-artifact thresholds; report actual findings, input revisions and blockers in the handoff.

## Business or user risk validation

For each linked business/user risk: hypothesis, experiment/method, audience/sample rationale, metric, threshold, observation window, evidence to capture, and continue/change/stop decision. For an ordinary non-risk-driven story, state why this section is inapplicable. A technical risk's required RFC/ADR remains linked separately.

## Dependencies and decisions

Blocking stories/enablers, pending RFCs/ADRs, and assumptions. Preserve explicit decision blockers.

## Verification and completion

How each acceptance criterion will be verified; risk evidence expected; Definition of Ready and Definition of Done. Done requires evidence, not merely writing the story. Estimates are optional; label any unvalidated estimate.

## Open questions

Missing requirements and their readiness impact.

## Readiness checklist

- [ ] User/stakeholder benefit and a small scope are explicit.
- [ ] Acceptance criteria describe observable results.
- [ ] Requirement links resolve to active PRD rows and scenarios agree with their canonical rules, or non-applicability is explained.
- [ ] Every linked business/user risk has a measurable validation plan.
- [ ] Dependencies and technical decision blockers are visible.
