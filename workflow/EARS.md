# EARS requirements within the existing workflow

Use Easy Approach to Requirements Syntax (EARS) for selected behavioral requirements in Lean PRDs. Keep founder input in ordinary language; specialists write the structured requirements. The nine agents, artifact types, risk routes and lifecycle states remain the same.

## Adoption policy

Following the KaamSaathi document pilot and the user's instruction on 2026-11-19 to continue selective adoption with semantic review, use EARS by default for suitable observable behavior in new Lean PRDs. Selectivity concerns what is expressed: system behavior belongs in canonical rows; outcomes, hypotheses, experiments, spike questions and decision rationale retain their existing formats. A discovery-only PRD can use a justified None. No new pilot or routine permission question is required for each new PRD.

For an existing PRD, adopt EARS within the requested revision's scope when its behavior is materially changed. Record the initiative, source revision, affected behavior and any untouched legacy scope in the product index before dispatch. Preserve existing requirement IDs, user edits, accepted decision history and unrelated artifacts. An incidental link or typo correction does not require migration. Do not bulk-convert existing products or rewrite historical pilot snapshots.

Record adoption scope and actual semantic-review findings using the existing PRD, index and handoff templates. This introduces no new specialist, product artifact type, lifecycle state or approval step. The user's adoption instruction authorizes kit policy; it does not approve product requirements, architecture choices, field work or unresolved risks.

The [pilot summary](../examples/ears-pilot.md#completed-pilot-observation) supports continuing the convention with these adjustments, not a claim of measured productivity or customer benefit. Human review effort was unavailable, the comparison was assisted, and additional research and review influenced the final requirements. Keep collecting actual observations on subsequent initiatives.

## Scope and ownership

The `lean_prd` specialist owns the canonical behavioral statements in its assigned PRD. Epics, stories, enablers, RFCs and ADRs reference those statements by ID. Do not maintain independent copies of the same normative sentence across artifacts. Concrete story scenarios may elaborate the rule with fixtures, boundary cases and expected results.

Keep Canvas research, roadmap outcomes, business/user hypotheses, experiment plans, spike questions and decision rationale in their existing formats. A proposition such as "buyers will pay this price" is a hypothesis requiring evidence, not a system requirement. Do not force investigation work into shall statements. Some measurable quality constraints fit EARS; others need a metric, operating conditions, observation window, threshold and verification method or a referenced decision table.

Do not introduce architecture choices to make a requirement precise. Specify externally observable behavior at the appropriate system boundary. If behavior depends on an unresolved choice, identify the dependency and keep affected readiness blocked.

## Pattern guide

EARS defines five basic patterns and combinations. The following syntax summary is for authoring; placeholders must be replaced in product artifacts.

| Pattern value | Shape | Use |
| --- | --- | --- |
| ubiquitous | The system shall respond. | An always-applicable obligation |
| event-driven | When an event occurs, the system shall respond. | A response to a triggering event |
| state-driven | While a state holds, the system shall respond. | Behavior active during a state |
| unwanted-behavior | If an unwanted situation occurs, then the system shall respond. | Failures, invalid inputs or other unwanted situations |
| optional-feature | Where a feature is included, the system shall respond. | A configured product feature, not an arbitrary event |
| complex | While a state holds, when an event occurs, the system shall respond. | Necessary combinations of feature, state, event or unwanted-condition clauses |

Use an explicit system/component name in place of "system" where helpful. Keep the subject consistent with the glossary. As a kit convention, favor one independently verifiable obligation per row; the EARS notation itself can contain multiple responses. Split unrelated obligations. Review whether the conditions are necessary and sufficient. Complex Boolean logic can reference a decision table rather than be hidden in a long sentence.

"When a request arrives, the application shall respond quickly" still needs a measurable response and time limit. A correct keyword does not resolve ambiguity, missing cases, contradictory obligations or unjustified thresholds.

## Canonical table and stable identifiers

Add `## Behavioral requirements` in the PRD and use these exact columns:

| Requirement ID | Pattern | EARS statement | Source / rationale | Verification | Risks |
| --- | --- | --- | --- | --- | --- |
| PRD-001-R01 | event-driven | When a user requests an export of a completed report, the application shall provide that report for download. | Illustrative proposed capability; actual rows cite their source and justify assumptions. | Inspect an export response for a completed-report fixture; compare its data with the source report. | None - illustrative behavior is not risk-driven |

This example is instructional, not a product decision or a completed test. Keep cells on one line; use `\|` for a literal pipe. Use plain requirement IDs in the first column. Pattern values are the six lowercase values above.

Use `<parent PRD ID>-R<sequence>` with at least two digits: `PRD-001-R01`, `PRD-001-R02`, and so on. These are PRD-local row identifiers, not new artifact types or separate documents. The PRD specialist allocates them serially within its exclusive file assignment after checking existing rows. Preserve IDs across wording corrections/revisions and never reuse a retired ID. The coordinator reserves PRD artifact IDs as before.

For references, link the exact requirement ID to the canonical PRD section, for example `[PRD-001-R01](../prds/PRD-001.md#behavioral-requirements)` from a story file. The visible ID identifies the row; the fragment points to the table. A PRD row's Source / rationale cites the originating input or decision and labels a proposed rule or threshold as such. Verification specifies how the obligation will be checked, not a claim that testing has passed. Risks links relevant registered IDs or explicitly states None with a reason; not every requirement needs an invented risk.

If no behavioral requirements apply, keep the section and write `None - <specific reason>` instead of retaining a placeholder row. For example, a pure discovery initiative may be represented by hypotheses and learning work. Preserve a decision-critical unknown as a blocker rather than inventing a shall statement to fill the table.

## References and change control

Every epic, story, enabler, RFC and ADR has a `## Requirement references` section. Link applicable requirement IDs and explain the coverage, constraint or decision relationship. If none apply, state `None - <specific reason>`, such as learning-only work or an explicitly unmigrated legacy PRD.

Story acceptance criteria retain Given / When / Then and add a Requirement column. Each scenario references the canonical ID it verifies. One requirement may need several scenarios; a scenario may cover more than one requirement when justified. Learning-only criteria can use None with a reason and retain the hypothesis/method/threshold/next-decision structure. Technical enabler criteria can similarly reference the behavior they support; investigations keep their timebox and evidence-producing exit criterion.

If a downstream specialist discovers a missing or conflicting rule, return a change request to the coordinator. The coordinator dispatches the update to `lean_prd`, then has dependent specialists revise affected references/scenarios. Do not introduce a conflicting local version of the rule. A genuinely new obligation gets a new ID. For retirement or replacement, retain the old ID, rationale, and replacement ID if any in a `## Requirement changes` table; remove it from the active table and reconcile dependents. The static checker rejects references to retired rows because only active rows are canonical.

The register may link requirement IDs as supporting work, but business/user risks still require stories and technical risks still require RFCs/ADRs. A requirement or passing syntax check alone never closes a risk. Ordinary PRD revisions keep their artifact ID; accepted ADR changes still require a new superseding decision record.

## Readiness review

Before a PRD is ready, review its active requirements for:

- Stable IDs, an explicit system boundary, suitable patterns and independently verifiable responses.
- Defined terminology and explicit triggers, states, configuration conditions and failure cases where relevant.
- Measurable limits with units and operating conditions when needed; unsupported numeric targets remain visibly proposed.
- Source/rationale and a verification approach, with evidence, assumptions and decisions distinguished.
- Missing cases, contradictions, duplicate obligations, hidden implementation choices and unresolved dependencies.
- Resolved or explicitly blocking material questions; syntax alone does not establish readiness.

Before downstream artifacts are ready, their references must resolve to active canonical rows and their criteria must agree with those rows. When full decomposition is in scope, reconcile requirement-to-scenario or technical-verification coverage; missing coverage must have an explicit next task or a material readiness blocker. The coordinator owns that review and index reconciliation. Do not require stories to exist before the PRD itself can become ready.

All current lifecycle rules still apply: draft is useful work in progress, ready means the applicable review passes, and approval or decision acceptance requires actual authorization. No per-requirement approval state or extra routine approval pause is introduced.

## Semantic review protocol

The PRD specialist first reviews its draft and records the reviewed revision, scope, reviewer role and method in `## Semantic review`. Before treating that PRD as ready, the coordinator challenges the rules against the source intent and checks relevant counterexamples. A coordinator may perform an agent review; describe it accurately rather than claiming human or independent validation. No additional reviewer subagent is required.

Use the following prompts where relevant. Mark an area not applicable with a reason when the scope genuinely excludes it; do not add unrelated constraints to fill a checklist.

| Review area | Questions and useful counterexamples |
| --- | --- |
| Intent and boundary | Does each rule preserve the requested outcome and exclusions? What input, actor, permission, state or external dependency is assumed? Are application-controlled behavior and platform/third-party behavior distinguished? |
| Values and limits | Are units, valid representations, ranges, zero/negative/empty values, rounding, dates and aggregate limits defined when needed? Can a concrete boundary case yield one expected answer? Unsupported limits remain proposed or TBD rather than being invented. |
| State and failure | What happens before/after commit, after interruption, on retry/replay, for a deliberately repeated action, after correction/removal, offline or when local state is unavailable? Review only applicable cases. |
| Data and side effects | What exact data and version are read, changed or disclosed? Consider stale previews, cancellation, failed handoff, logs/background tasks, platform backup/transfer and recipient behavior where relevant. Do not imply unobservable delivery or protection. |
| Cross-artifact consistency | Do terms, arithmetic, sample sizes, thresholds, observation windows, scope and expected results agree across the PRD, roadmap, stories, spikes and decisions? Report competing proposals to the coordinator; do not silently choose one or edit another owner's file. |
| Verification and evidence | Can representative normal, boundary and failure fixtures have explicit expected outcomes? Distinguish a planned verification method from an executed result and a document-review finding from product evidence. Keep technical feasibility and numeric/device contracts visibly unresolved until supported. |

Record actual findings, affected requirement IDs or source sections, and their disposition in the PRD's review table. For a reviewed area with no issue found, identify the cases considered and their reasoning; do not infer success from an unchecked box or a passing script. If an area has not been reviewed, say so. A review can be complete while a material product question still blocks readiness. Planned tests, a warning message and a well-formed shall statement do not resolve the underlying uncertainty.

Downstream specialists review the applicable canonical rows against their concrete scenarios, technical criteria and option constraints. Return a counterexample or conflict with the input revision, affected IDs, expected/ambiguous outcome, proposed clarification and readiness consequence. The coordinator sends behavioral changes to `lean_prd`, register changes to `risk_register`, then reconciles affected dependents. Keep stable IDs for clarifications and allocate a new ID for a new obligation. Capture new risks at their actual discovery stage.

The coordinator summarizes the actual review and requirement-to-verification coverage in the index, separate from the static-check result. Record missing criteria and material unreviewed areas as blockers or explicit next tasks. PRD readiness does not depend on future stories already existing; full decomposition requires actual downstream coverage review. Re-review affected behavior when canonical rows, boundary assumptions, thresholds or architecture constraints change, and refresh the index after dependent criteria are reconciled. Pure linkage maintenance is not a behavioral correction or an additional substantive clarification batch.

## Static checking

Run `python scripts/validate-requirements.py products/<product-slug>` after adopted PRDs and related references exist. The checker reads Markdown without modifying it. It checks active table structure, IDs, pattern shape, required fields, exact duplicate statements within a PRD and requirement-link destinations. It also checks that criterion-table references were declared in the artifact's Requirement references section.

Legacy PRDs without the new section are reported and skipped; they are not silently rewritten. A declared reference to a missing or inactive requirement is an error. If no PRD has adopted the section, the command reports that no EARS requirements were checked and exits unsuccessfully. A justified None section is supported for discovery-only work. Superseded artifacts are historical and excluded from the active reference audit.

This is a plausibility and traceability check, not a full EARS parser, consistency proof, assessment of actual source support, evidence of coverage completeness, readiness assessment or model evaluation. Human/specialist review handles semantics, requirement quality and missed behaviors. `scripts/validate-kit.py` continues to check the reusable kit itself.

## Measurement and gradual adoption

Keep adoption bounded to the new PRD or requested existing revision under the adoption policy above. Use the [pilot prompts](../examples/ears-pilot.md) when deliberately measuring the convention on another real initiative; a separate comparative pilot is optional for routine new work. New template sections can be filled normally; do not mass-convert old products or accepted decisions. The source of truth, semantic review and reference rules apply whenever an initiative adopts EARS.

1. Record a baseline from the existing version: clarification rounds, missing edge cases, review effort and requirement corrections after downstream decomposition. If no comparable earlier version exists, say baseline unavailable; do not invent improvement percentages.
2. Preserve the source revision. Have the PRD specialist author a small useful requirement set with labeled assumptions and verification approaches. Review whether it preserves the intended scope.
3. Have downstream specialists reference the rows and retain their concrete scenarios, learning methods and technical decision rationale. Reconcile the graph and run the static checker.
4. Record the same review measures using actual observations. Log duplicate maintenance, misinterpretations, useful gaps uncovered and overhead. Test fixtures used to check the script are not a product pilot.
5. Recommend continue, adjust or stop based on observed clarity and maintenance effort. Report the limits of a single initiative; no automatic broader migration or claim of validated gains follows.

The coordinator records pilot observations only when they actually exist. If no real initiative is supplied, prepare pilot guidance and report that the product pilot has not run.

## Sources

This kit's ownership, ID, traceability and pilot conventions are local design choices. EARS syntax is described in the [author's guide](https://alistairmavin.com/ears/). Pattern selection, review and limits are discussed in [Listens Learned: 8 Lessons Learned Applying EARS](https://www.researchgate.net/publication/308970788_Listens_Learned_8_Lessons_Learned_Applying_EARS). These sources were consulted for the preceding assessment; they do not establish measured benefits for this kit.
