# Coordinator runbook

## Intake and dispatch

Identify the repository's product, supplied sources, requested stage(s), and desired depth. Default artifacts to docs/ with docs/INDEX.md; do not request a product slug or add another product directory inside the repository. Search existing artifacts before asking for information already present. Start at the requested stage; do not regenerate accepted upstream documents unnecessarily. For Lean Canvas work, accept a short plain-language idea directly from the chat; a formal product brief is optional. If the idea itself is absent, request it in plain English. Do not require answers to canvas blocks or market research before dispatch. Other stages need their relevant upstream context. Creating this reusable kit does not require a product brief.

Read the shared contract, the specialist profile, its template, and the relevant existing artifacts. Create/update the product index and reserve artifact IDs. Dispatch this payload to the named custom agent:

```text
Task: create or revise <artifact type>; scope <one bounded outcome>.
Product root: docs/
Assigned ID and exclusive output path: <id>, <path>
Input files and source sections: <paths and sections>
Required parent IDs / roadmap item: <ids>
Canonical requirement IDs / adoption scope: <PRD row links, or justified none/legacy; selected pilot initiative if any>
Semantic review scope: <source revision, applicable counterexamples/boundaries, known inconsistencies and existing review findings>
Repository context: <existing scaffold/code paths, engineering instructions and observed manifests/commands, or no code yet; read-only context for this planning assignment>
Assigned risk IDs and route: <ids or explicit none>
Known decisions, constraints, terminology: <facts>
Missing inputs / permitted assumptions: <items>
Research mode / constraints: <live by default for Lean Canvas; user restrictions or known tool limits>
Read workflow/CONTRACT.md and templates/<type>.md before writing.
Edit only the assigned output path. Return templates/handoff.md fields.
Do not spawn further agents. Report conflicting inputs to the coordinator.
```

The register task instead owns the one register path and may allocate new RISK IDs. Dispatch batches serially to that agent. IDs returned by it are reconciled into affected PRDs, roadmap, and destination artifacts through their owning specialists. The coordinator alone updates INDEX.md. Use the profile for the current client: `.codex/agents/*.toml` in Codex, `.claude/agents/*.md` in Claude Code, with role-name mapping in `CLAUDE.md`. If a client lacks custom-agent discovery, attach the complete specialist instructions (TOML `developer_instructions` or the Claude Markdown body) to a general subagent task; do not claim the custom profile was loaded. Use one active coordinator per product workspace, including across clients.

## Stages

1. **Lean Canvas:** delegate a research-first canvas using `workflow/LEAN-CANVAS-RESEARCH.md`. The specialist uses available web search and page-reading tools to investigate customer problems, alternatives, pricing, channels, costs and constraints, then populates all nine blocks with recommendations and dated source links. Pass supplied decisions and research restrictions. Ask only essential plain-language scope questions; otherwise use explicit working assumptions. Keep evidence and source coverage inside the canvas unless a separate research-note path is assigned. If tool access is unavailable, the coordinator may supply permitted research through the same tools or report the limitation; keep an unresearched result draft. Review key claims against their cited pages and distinguish a complete planning document from validated demand. Return prioritized hypotheses and practical tests, not premature formal risk records.
2. **Roadmap:** derive outcome-oriented Now / Next / Later initiatives with stable item IDs, measurable outcomes, rationale, confidence, and promotion criteria. Do not invent dates or expand every Later item into a PRD.
3. **Lean PRD + risk registration:** draft one PRD per selected initiative/problem. Use selective EARS by default for suitable observable behavior in new PRDs; adopt existing behavior only within the requested material revision. Record scope/source revision and any unmigrated behavior in the index. Follow `workflow/EARS.md`: the PRD specialist owns stable local requirement IDs, canonical rows with source/rationale and verification approaches, and the Semantic review record. The coordinator challenges the draft using the semantic review protocol before readiness; route actual findings back to its owner. Keep hypotheses separate; no requirement-level approval lifecycle or fresh comparative pilot is required. PRD agent returns risk candidates in its risk table. Register agent deduplicates against existing entries and assigns IDs. PRD agent replaces candidate references with the returned risk links. Roadmap agent links the risks to the initiative. This completes the stage where the risk is born; downstream routing can remain pending until its artifact exists.
4. **Epics:** decompose the selected PRD into minimal outcome-oriented epics. Identify which epic owns each risk response. Preserve the PRD's outcomes, exclusions, and measures.
5. **Stories and enablers:** delegate independent items with separate files and reserved IDs. Business/user risks go directly into stories. Technical enablers provide spikes, infrastructure, migration, or operational work with verifiable deliverables. Keep architectural unknowns explicit.
6. **RFCs and ADRs:** technical risks get RFCs for evaluation or ADRs for decisions. Move this stage earlier if a decision blocks decomposition. A documented RFC conclusion can lead to a proposed ADR; mark accepted only when authorized. Record resulting enablers and dependencies through the enabler agent, then reconcile affected stories. No requirement to create both an RFC and ADR for every technical risk.
7. **Reconcile:** register agent adds destination links and updates exposure based on evidence; artifact agents add reciprocal links. For adopted EARS scope, review canonical row IDs, representative scenario/technical criteria with expected results, numeric/platform boundaries and cross-artifact terminology/thresholds under the semantic review protocol, then run `python scripts/validate-requirements.py docs` separately. Request missing or conflicting behavior through the PRD owner; do not create local competing statements or silently resolve competing thresholds. Reconcile affected dependents and record reviewed revisions, actual findings, coverage gaps and blockers in the index. Re-review affected behavior after material changes; linkage maintenance alone is not a substantive behavioral correction. Static checks do not establish readiness or semantic correctness. Check links, duplicate IDs, orphan items, scope, risk routing and stale decisions. Return a compact status and unresolved blockers. For a selected measurement pilot, record actual baseline/review observations in INDEX.md and recommend continue/adjust/stop; report unavailable measurements honestly.

Run sequentially when one output changes another's requirements. Parallel work is permitted only for independent items with distinct paths, at most three subagents or the runtime's lower limit. A high-risk dependency can keep an item out of Now. Do not interpret the diagram as a one-way waterfall: new evidence can revise upstream drafts and produce new versions of decisions.

## Handoff to coding in the same repository

Follow `workflow/IN-REPOSITORY.md`. Once the user requests implementation, select the specific story or enabler and its applicable PRD rows, RFC/ADR constraints and unresolved blockers. Inspect the real app/package boundaries and commands, then use the primary coding agent or coding workers; do not ask a planning specialist to exceed its artifact ownership. Ordinary scoped fixes need not launch the product workflow. A scaffold-only request can precede product planning: preserve existing files and record the generated baseline without treating starter choices as accepted product decisions.

For feature work, identify affected paths, relevant criteria, actual verification commands and any material prerequisite that blocks that implementation. Work can proceed on independently unblocked scope; no blanket requirement to approve every document is introduced. If code or a spike exposes a missing rule, return it to the PRD owner and reconcile dependents instead of silently rewriting product intent. Record actual implementation/test evidence under the existing story/enabler Verification and completion section and link changed paths/PRs when available. Keep document lifecycle states intact: ready does not mean implemented or risk resolved.

## Completion criteria

For the requested scope, every artifact follows its template; parent links resolve; all PRD risks are registered; every business/user risk has a story route and every technical risk an RFC/ADR route once routing is in scope. Every risk has an owner or explicit assignment blocker, a next action, and a closure criterion. Unknowns and unreviewed decisions remain visible. A partial-stage request can complete with explicitly pending future routes; an end-to-end request cannot claim routing is complete with those routes pending.

Never automatically promote documents to approved or decisions to accepted. Continue useful drafting without adding routine approval pauses. Explain precisely what evidence or user decision is required if readiness or an actual decision is blocked.

Apply selective EARS and semantic review as described in `workflow/EARS.md` for new PRDs and scoped material revisions. Existing artifacts can remain explicitly unmigrated; do not rewrite them solely to populate new sections. Adopted downstream artifacts use requirement-reference sections, including justified None for learning-only work. The index records adoption and actual review separately from optional pilot measurements. If no real initiative is available, maintain the kit without inventing a product or claiming a pilot ran.
