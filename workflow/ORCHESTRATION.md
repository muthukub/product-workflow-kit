# Coordinator runbook

## Intake and dispatch

Determine product slug, supplied sources, requested stage(s), and desired depth. Search existing artifacts before asking for information already present. Start at the requested stage; do not regenerate accepted upstream documents unnecessarily. If no product brief is supplied, request it before product-specific generation. Creating this reusable kit does not require a product brief.

Read the shared contract, the specialist profile, its template, and the relevant existing artifacts. Create/update the product index and reserve artifact IDs. Dispatch this payload to the named custom agent:

```text
Task: create or revise <artifact type>; scope <one bounded outcome>.
Product root: products/<slug>/
Assigned ID and exclusive output path: <id>, <path>
Input files and source sections: <paths and sections>
Required parent IDs / roadmap item: <ids>
Assigned risk IDs and route: <ids or explicit none>
Known decisions, constraints, terminology: <facts>
Missing inputs / permitted assumptions: <items>
Read workflow/CONTRACT.md and templates/<type>.md before writing.
Edit only the assigned output path. Return templates/handoff.md fields.
Do not spawn further agents. Report conflicting inputs to the coordinator.
```

The register task instead owns the one register path and may allocate new RISK IDs. Dispatch batches serially to that agent. IDs returned by it are reconciled into affected PRDs, roadmap, and destination artifacts through their owning specialists. The coordinator alone updates INDEX.md. Use the profile for the current client: `.codex/agents/*.toml` in Codex, `.claude/agents/*.md` in Claude Code, with role-name mapping in `CLAUDE.md`. If a client lacks custom-agent discovery, attach the complete specialist instructions (TOML `developer_instructions` or the Claude Markdown body) to a general subagent task; do not claim the custom profile was loaded. Use one active coordinator per product workspace, including across clients.

## Stages

1. **Lean Canvas:** capture the nine blocks and distinguish assumptions from evidence. Return assumptions for prioritization, not premature formal risk records.
2. **Roadmap:** derive outcome-oriented Now / Next / Later initiatives with stable item IDs, measurable outcomes, rationale, confidence, and promotion criteria. Do not invent dates or expand every Later item into a PRD.
3. **Lean PRD + risk registration:** draft one PRD per selected initiative/problem. PRD agent returns risk candidates in its risk table. Register agent deduplicates against existing entries and assigns IDs. PRD agent replaces candidate references with the returned risk links. Roadmap agent links the risks to the initiative. This completes the stage where the risk is born; downstream routing can remain pending until its artifact exists.
4. **Epics:** decompose the selected PRD into minimal outcome-oriented epics. Identify which epic owns each risk response. Preserve the PRD's outcomes, exclusions, and measures.
5. **Stories and enablers:** delegate independent items with separate files and reserved IDs. Business/user risks go directly into stories. Technical enablers provide spikes, infrastructure, migration, or operational work with verifiable deliverables. Keep architectural unknowns explicit.
6. **RFCs and ADRs:** technical risks get RFCs for evaluation or ADRs for decisions. Move this stage earlier if a decision blocks decomposition. A documented RFC conclusion can lead to a proposed ADR; mark accepted only when authorized. Record resulting enablers and dependencies through the enabler agent, then reconcile affected stories. No requirement to create both an RFC and ADR for every technical risk.
7. **Reconcile:** register agent adds destination links and updates exposure based on evidence; artifact agents add reciprocal links. Check the index, links, duplicate IDs, orphan items, scope, risk routing, and stale decisions. Return a compact status and unresolved blockers.

Run sequentially when one output changes another's requirements. Parallel work is permitted only for independent items with distinct paths, at most three subagents or the runtime's lower limit. A high-risk dependency can keep an item out of Now. Do not interpret the diagram as a one-way waterfall: new evidence can revise upstream drafts and produce new versions of decisions.

## Completion criteria

For the requested scope, every artifact follows its template; parent links resolve; all PRD risks are registered; every business/user risk has a story route and every technical risk an RFC/ADR route once routing is in scope. Every risk has an owner or explicit assignment blocker, a next action, and a closure criterion. Unknowns and unreviewed decisions remain visible. A partial-stage request can complete with explicitly pending future routes; an end-to-end request cannot claim routing is complete with those routes pending.

Never automatically promote documents to approved or decisions to accepted. Continue useful drafting without adding routine approval pauses. Explain precisely what evidence or user decision is required if readiness or an actual decision is blocked.
