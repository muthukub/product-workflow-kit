# Pilot EARS on one real initiative

Use these prompts with an actual initiative/PRD. The coordinator follows [the EARS guide](../workflow/EARS.md) and preserves existing lifecycle and risk rules. Use the Claude equivalents `lean-prd`, `user-story` and `risk-register` when naming those specialists in Claude Code.

## Routine adoption and semantic review

New PRDs use selective EARS by default; a fresh comparative pilot is optional. For an existing PRD, adopt behavior within the requested material revision and preserve untouched legacy scope. The coordinator records that scope and the actual review in the index.

```text
For <initiative/PRD ID> in docs/, follow workflow/EARS.md.
Use selective EARS for suitable observable behavior in this new PRD, or only
within the requested material revision of an existing PRD. Record source
revisions and untouched scope. Keep learning hypotheses and spikes in their formats.
Have lean_prd record actual semantic review and the coordinator challenge it.
Check relevant numeric limits, state/failure cases, data/platform boundaries,
cross-artifact thresholds and representative expected results. Report actual
counterexamples, unresolved questions and dispositions; do not invent test results.
Return canonical changes to lean_prd and risk changes to risk_register, then
reconcile affected dependents. Summarize review and coverage in INDEX.md;
run static checks separately. Keep material blockers visible before readiness.
```

## Completed pilot observation

The KaamSaathi prospective document pilot, recorded on 2026-11-19, produced 18 canonical behavioral rows and 14 linked artifacts. Its frozen prose baseline had 10 specified and 2 partial topics in a predeclared twelve-topic review; the final review had 11 specified and 1 partial. Concrete numeric/device limits remained unresolved. Two actual clarification batches included an early RFC review that separated application-initiated disclosure from platform backup/transfer; cross-artifact exploratory thresholds also needed reconciliation. Final linkage maintenance did not change canonical behavior.

This was a sequential assisted authoring exercise with additional research, not a controlled EARS comparison. Human review effort, product performance and customer impact were not measured. The user subsequently authorized continuing selective adoption with semantic review. The full workspace record is under `docs/pilot/RESULTS.md`; it need not be copied into another repository to use this kit. Historical records remain unchanged.

Use the remaining prompts when deliberately running a further comparative pilot.

## Select and record the scope

```text
Pilot EARS only for <initiative ID> in docs/.
Read the current index, PRD and related artifacts. Record the selected scope
and source revisions in INDEX.md. Preserve unrelated work and approvals.
Use the four measures in workflow/EARS.md; record actual baseline observations
or baseline unavailable. Do not invent historic review effort or customer data.
```

If no PRD exists, provide the real initiative and its upstream evidence so the coordinator can prepare the appropriate artifacts. A request to maintain this kit does not itself authorize creating a fictional product pilot.

## Author the canonical rules

```text
Use lean_prd to revise <PRD ID> for the selected EARS pilot.
Create the canonical Behavioral requirements table with stable local IDs,
appropriate patterns, source/rationale, verification approaches and relevant
risk links. Preserve scope and distinguish proposed rules from user decisions.
Keep learning hypotheses and experiments in their current sections.
Report missing cases, contradictions and decision blockers in plain English.
```

## Connect downstream work

```text
Have the relevant epic, user_story, enabler, rfc and adr specialists reconcile
their assigned pilot artifacts with the canonical PRD requirement IDs.
Stories keep concrete Given/When/Then examples. Technical work retains its
verification and architectural dependencies. Use justified None where no
behavior applies. Return missing/changed rules to the PRD owner; do not keep
competing copies of the same obligation. Preserve normal risk routing.
```

## Review and compare

```text
Run the read-only requirements checker for docs/.
Separately review intended meaning, necessary/sufficient conditions, terminology,
failure/boundary cases, contradictions and requirement-to-verification coverage.
Record actual clarification rounds, missing edge cases, review effort and
requirement corrections after decomposition, with sources/units comparable to
the baseline. Explain what EARS helped uncover and any duplicate maintenance
or added overhead. Recommend continue, adjust or stop; do not claim measured
gains if observations or a comparable baseline are unavailable.
```

The default risk route remains business/user risk to a story and technical risk to an RFC or ADR. A canonical requirement link is supporting traceability, not a replacement response or evidence of risk closure. A successful static check does not automatically set ready, approved, accepted or closed status.
