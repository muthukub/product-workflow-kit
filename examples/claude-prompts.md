# Claude Code prompts

Start `claude` from the repository root. Use the hyphenated names in CLAUDE.md. These agents reuse the same templates, handoffs and risk rules as Codex. For a Lean Canvas, a plain-language idea is sufficient; brief/source paths and target geography are optional context.

## Check discovery without generating product artifacts

```text
Check whether the nine project agents from CLAUDE.md are available. Delegate a
read-only check to lean-canvas: read workflow/CONTRACT.md and its template, then
return its role, the nine canvas headings and the output ownership rule. Do not
create files. Wait for the response. Report whether the named custom agent
loaded or a general-purpose fallback was used.
```

## Create a canvas

```text
Use lean-canvas to research this idea and create a complete Lean Canvas:
<Describe what you want to build and who it may help.>
Use available web search and page-reading tools to investigate customer problems,
alternatives, current advertised prices, channels and costs. Recommend all nine
blocks in plain English with source links, dates and clearly labeled assumptions.
Follow CLAUDE.md, workflow/LEAN-CANVAS-RESEARCH.md and the shared template.
Save under products/<slug>/ and identify practical tests for the key hypotheses.
```

Research uses tools available to the session; if access is unavailable, the agent must say so and return a useful draft. A complete canvas is a starting business model, not proof of customer demand or willingness to pay.

## Create a roadmap

```text
Use product-roadmap to turn products/<slug>/canvas/LC-001.md into a focused
Now / Next / Later roadmap. Preserve scope and assign stable initiative IDs,
success measures and promotion criteria. Do not invent delivery dates.
```

## Draft a PRD and register risks

```text
Use lean-prd for <initiative ID> in products/<slug>/roadmap/RM-001.md. Then use
risk-register to deduplicate and register the PRD's risks. Have lean-prd
reconcile stable risk links and product-roadmap update its initiative links.
Run these tasks sequentially. Stop after this stage and mark future routes pending.
```

## Complete a selected initiative

```text
Coordinate the nine Claude Code agents in CLAUDE.md for <initiative ID>, using
products/<slug>/ and <brief/source paths>. Follow workflow/ORCHESTRATION.md.
Reuse existing artifacts and reserve IDs before dispatch. Delegate independent
items only with distinct output paths; run dependencies sequentially.
Business/user risks must go directly into user-story artifacts. Technical risks
must go into rfc or adr artifacts; enabler work may support those routes.
Reconcile reciprocal links and report missing evidence. Keep undecided ADRs proposed.
```
