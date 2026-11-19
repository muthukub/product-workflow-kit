# <Title>

| Field | Value |
| --- | --- |
| ID | <EN-001> |
| Type | enabler |
| Status | draft |
| Owner | <accountable person or explicit TBD> |
| Updated | <YYYY-MM-DD> |
| Revision | <positive integer> |
| Parents | <ID links; include originating PRD where applicable> |
| Risks | <RISK-ID links or explicit none> |
| Sources | <file/section/revision or URL/date; distinguish assumptions> |

## Capability enabled

Technical capability, why it is necessary, and which user/business outcome it enables. Use a technical task format rather than a fictional end-user persona.

## Kind and scope

Kind: spike, infrastructure, architecture, migration, security, operations, or other justified technical work. Included/excluded work and affected components.

## Deliverables and acceptance criteria

| Deliverable | Requirement | Observable acceptance criterion | Verification / evidence |
| --- | --- | --- | --- |
| <deliverable> | <canonical requirement ID link or None - investigation/other reason> | <criterion> | <method> |

## Requirement references

Follow workflow/EARS.md. Link the canonical PRD behaviors this work supports, without inventing competing requirements or resolving architecture implicitly. Use None with a specific reason when investigation-only work or an explicitly unmigrated parent has no applicable rows. Preserve spike questions, methods, timeboxes and decision-oriented exits. Apply the semantic review protocol to applicable numeric/device limits, failure states, platform side effects and expected evidence; report actual findings, input revisions and blockers in the handoff.

## Technical risk and architecture route

Related technical risk links and their RFC/ADR links. State how this work supports the route. For non-risk-driven work, explain the necessity. An enabler alone never satisfies a technical risk's routing requirement.

## Investigation plan and timebox

For a spike: question, hypotheses/options, smallest experiment, timebox, exit criterion, evidence, and decision it informs. For implementation work, state inapplicable with reason.

## Dependencies and rollout

Blocking decisions and work items; compatibility, migration, observability, rollout and rollback as applicable. Do not implement an unresolved architectural option as though accepted.

When used in a source repository, identify affected app/package paths, engineering instructions and actual verification commands, or TBD/no code yet. Distinguish scaffold defaults from accepted decisions and plan the coding handoff under workflow/IN-REPOSITORY.md; this planning assignment does not edit application code.

## Verification and completion

Definition of Ready, Definition of Done, and concrete evidence expected for completion. Mark estimates as assumptions unless supplied.

After separately requested execution, retain actual code/PR paths, experiment outputs and executed checks here, including inconclusive or failed results. Do not infer completion from the enabler document or change document/risk states automatically.

## Open questions

Unknowns that prevent readiness and next action.

## Readiness checklist

- [ ] A real capability and downstream benefit are clear.
- [ ] Deliverables and acceptance criteria are verifiable.
- [ ] Canonical requirement references and technical decision dependencies are consistent, or non-applicability is explained.
- [ ] Technical risks retain RFC/ADR routes.
- [ ] Spikes have a timebox and a decision-oriented exit.
