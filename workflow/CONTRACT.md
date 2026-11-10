# Shared artifact contract

## Scope and evidence

Use the supplied product brief, existing artifacts, and explicit user decisions. Preserve product terminology and agreed scope. Never invent interviews, market facts, commitments, estimates, experiments, approvals, or architecture decisions. Distinguish observed evidence, user decisions, assumptions, and recommendations. Cite source files with a section or external sources with a URL and access date. Browse when current external facts need verification; otherwise mark the claim unverified.

Fill every template heading. Use `None - <reason>` for genuinely inapplicable content and `TBD - <missing input and consequence>` for unknowns. Do not silently remove sections. Replace angle-bracket placeholders in generated artifacts. Keep outputs lean: one coherent problem per PRD, one outcome per epic, one deliverable per story/enabler, one decision per ADR. Add rows as needed without changing column names.

Ask only questions that materially affect scope or correctness. Continue drafting independent sections while an answer is pending. A missing input may block readiness without blocking creation of a reviewable draft. Never treat elapsed time as an answer. No routine approval pause is required to create or revise drafts.

## Files and identifiers

Product output root: `products/<product-slug>/`. Before delegating, the coordinator creates `INDEX.md` using `templates/product-index.md`, reads existing IDs, and reserves unused IDs. IDs are unique within a product, stable across revisions, and never reused after removal. Record reservations in the index before parallel dispatch. The risk register agent allocates risk IDs serially and returns them for reconciliation.

| Type | ID | Path relative to the product root |
| --- | --- | --- |
| Canvas | LC-001 | `canvas/LC-001.md` |
| Roadmap | RM-001 | `roadmap/RM-001.md` |
| PRD | PRD-001 | `prds/PRD-001.md` |
| Risk register | RR-001 | `risks/RR-001.md` |
| Risk entry | RISK-001 | Heading inside `risks/RR-001.md` |
| Epic | EPIC-001 | `epics/EPIC-001.md` |
| Story | US-001 | `stories/US-001.md` |
| Enabler | EN-001 | `enablers/EN-001.md` |
| RFC | RFC-001 | `rfcs/RFC-001.md` |
| ADR | ADR-001 | `adrs/ADR-001.md` |

Numbers have at least three digits and may grow beyond 999. One register serves all PRDs in a product. Artifact metadata fields are mandatory: ID, Type, Status, Owner, Updated, Revision, Parents, Risks, Sources. Dates use ISO `YYYY-MM-DD`; owner can be `TBD - assignment needed`. Use relative Markdown links with IDs as labels for local parents, risks, and downstream artifacts. For a risk, link to `../risks/RR-001.md#risk-001` (adjust relative path as needed). Risk headings are exactly `### RISK-001` so anchors remain stable. External input files may be absolute links where required by the client.

## Lifecycle

General artifacts: `draft`, `ready`, `approved`, `superseded`. `ready` means the specialist's checklist passes, not that a stakeholder approved it. `approved` requires a cited explicit user/stakeholder decision. Record blockers in Open questions and return them in the handoff. A downstream draft may use a draft parent, but must say so and cannot claim readiness while material upstream blockers remain.

RFC states: `draft`, `in-review`, `accepted`, `rejected`, `superseded`. ADR states: `proposed`, `accepted`, `rejected`, `superseded`. Accepted RFCs and ADRs require evidence of an actual authorized decision; a recommendation alone does not qualify. Existing accepted decisions are preserved; changed decisions get a new ADR that supersedes the old record, with links both ways.

## Risk rules

The Lean PRD stage is the formal point of risk identification and registration. Canvas/roadmap assumptions are candidates until the PRD stage; roadmap links are updated once risk IDs exist. Risks discovered later are added immediately, with the discovery stage recorded; do not hide a late risk or backdate its origin.

Write each risk as cause -> uncertain event -> impact. Classify it as exactly `business`, `user`, or `technical`. Split mixed concerns into linked risks rather than assigning an ambiguous category.

* Business/user risk -> at least one user story with an observable behavior or a measurable learning outcome, hypothesis, method, threshold, and next decision. An experiment can be a story if its user/business benefit is explicit. Do not disguise it as a technical enabler.
* Technical risk -> at least one RFC or ADR. Use an RFC when alternatives, feasibility, or tradeoffs need evaluation. Use an ADR when documenting a specific decision; an undecided ADR stays `proposed`. A timeboxed spike or implementation enabler may accompany either route but never replaces the architecture link.
* Link the risk in both the register's Routed artifacts field and the target's Risks metadata. Include the originating PRD and relevant roadmap item. If an epic does not exist at discovery time, retain the route as pending and complete it after epic decomposition. Pending routes prevent the routing stage from passing.

Risk states: `open`, `mitigating`, `accepted`, `closed`. Creating a story/RFC/ADR moves a risk at most to `mitigating`; documentation alone does not resolve uncertainty. Closing requires measured evidence against a stated closure criterion. Acceptance requires an explicit risk owner decision, rationale, residual exposure, and review date. Never claim zero residual risk without evidence.

Use qualitative probability and impact scores 1-3; score = probability x impact. Probability: 1 unlikely, 2 plausible, 3 likely; impact: 1 local/recoverable, 2 material/rework, 3 outcome-threatening. Explain the score. Review scores 6-9 before commitment to Now; scores guide judgment rather than inventing statistical precision.

## Traceability and delivery

The normal parent chain is Canvas -> Roadmap -> PRD -> Epic -> Story/Enabler. A roadmap initiative uses a stable item ID such as `RM-001-I01`. PRDs name that item. RFCs/ADRs link the affected story/enabler when it exists and always their originating PRD/risk; early risk evaluation need not wait for delivery decomposition. Ordinary stories and necessary technical decisions may exist without a risk; use `None - not risk-driven` explicitly.

Before return, compare headings and metadata against the assigned template, check parent existence and link targets, verify IDs and terminology, check risk routing and measurable criteria, and identify assumptions that prevent readiness. Return the structure in `templates/handoff.md`. Do not implement code, open tickets, publish, or contact people unless the user explicitly includes that work.
