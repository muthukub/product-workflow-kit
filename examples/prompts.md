# Copy-ready prompts

Replace angle-bracket placeholders with your own product and file paths. These prompts create drafts; an agent cannot invent product approval or architecture authorization.

## Check agent discovery

```text
Check whether all nine project custom agent types are available. Spawn lean_canvas
for a read-only smoke check: read workflow/CONTRACT.md and its template, then return
its role, the nine canvas headings, and its output ownership rule. Do not create
product artifacts. Wait for it and report whether the named custom agent loaded
or a general-agent fallback was used.
```

## Start with a canvas

```text
Use lean_canvas to create a Lean Canvas for <product> using <brief path>.
Follow AGENTS.md and the shared contract. Save under products/<slug>/.
Keep unverified claims explicit and identify the most useful first validation.
```

## Build the roadmap

```text
Use product_roadmap to turn products/<slug>/canvas/LC-001.md into an
outcome-oriented Now / Next / Later roadmap. Preserve the canvas scope,
assign stable initiative IDs, and define success and promotion criteria.
Do not invent delivery dates or create PRDs for every Later item.
```

## Draft a PRD and register its risks

```text
Use lean_prd for initiative <RM-001-I01> in products/<slug>/roadmap/RM-001.md.
Use risk_register to register its business, user and technical risks. Run those
tasks sequentially, then have lean_prd reconcile the stable risk IDs and
product_roadmap link them. Stop after the PRD stage; mark downstream routes
pending rather than claiming risk routing or mitigation is complete.
```

## Complete the selected initiative

```text
Coordinate the specialist agents in AGENTS.md for <initiative ID> using
products/<slug>/ and <brief/source paths>. Produce or revise only the necessary
Canvas, roadmap, Lean PRD, risk register, epics, stories, enablers and RFCs/ADRs.
Reuse existing artifacts. Run dependent stages sequentially and independent
items in parallel with distinct paths and reserved IDs. Put business/user risks
directly into stories and technical risks into RFCs or ADRs. Reconcile reciprocal
links and report evidence gaps. Keep undecided architecture proposed.
```

## Route a newly discovered risk

```text
Use risk_register to add this risk to products/<slug>/risks/RR-001.md:
<cause -> uncertain event -> impact, source PRD and discovery stage>.
Classify it, deduplicate, and return its stable ID. Then delegate the response
to user_story for business/user risk, or rfc/adr for technical risk. Link the
source and destination, and leave the risk open or mitigating until evidence
meets its closure criterion.
```

## Record a decision

```text
Use adr to record one decision for <risk/PRD/RFC IDs>. Decision evidence is
<actual owner/date/authorization source, or say unavailable>. Keep it proposed
if authorization is unavailable. Link consequences, validation and follow-up
enablers. Preserve existing accepted ADRs and their history.
```

## Update from real evidence

```text
Use risk_register to review <risk ID> using <measurement/evidence path>.
Compare observations to its closure criterion; preserve residual uncertainty.
Then revise affected stories, RFCs/ADRs and roadmap through their specialists.
Report exactly which status changes the evidence supports.
```
