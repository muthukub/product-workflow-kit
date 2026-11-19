# User manual: from an idea to a delivery plan

You can start with an idea in ordinary language. The main chat coordinates specialist agents, saves their work in standard templates, and connects the documents. You provide direction, correct assumptions, and supply real-world evidence as you learn.

The workflow helps you answer progressively smaller questions: Who might need this? What should we focus on? What should the product do? What work and decisions will make that possible?

## Workflow at a glance, including lifecycle

After the project setup in section 1, follow the planning stages below. The status belongs to an individual document or risk, rather than to the chat as a whole. Different documents can be at different stages at the same time.

| Workflow stage | What happens | Lifecycle / status | What you review |
| --- | --- | --- | --- |
| 1. Lean Canvas | Research the idea and recommend a complete starting business model | `draft` → `ready` → optional `approved` | Do the customer, problem, evidence and proposed model make sense? Ready means usable for validation planning. |
| 2. Roadmap | Organize outcomes into Now, Next and Later | `draft` → `ready` → optional `approved` | Is the first outcome focused, measurable and realistically sequenced? Horizons are separate from document status. |
| 3. Lean PRD | Define scope; use selective EARS for suitable new behavior and record semantic review | `draft` → `ready` → optional `approved` | Are rules observable, justified and verifiable? Have the specialist and coordinator reviewed counterexamples, limits and conflicts, and registered initial risks? Syntax alone does not establish readiness. |
| 4. Risk register | Track uncertainties and their required responses | Register document: `draft` → `ready` → optional `approved`. Each risk: `open`, `mitigating`, `accepted` or `closed` | Are owners, routes, next actions and closure criteria clear? A ready register can contain open risks. |
| 5. Epics | Break the requirement into coherent outcomes | `draft` → `ready` → optional `approved` | Does each epic have clear boundaries, acceptance criteria and a useful breakdown? |
| 6. Stories and enablers | Specify small tasks and link applicable PRD requirement IDs to concrete criteria | `draft` → `ready` → optional `approved` | Do scenarios agree with the canonical rules? Are learning tests and dependencies clear? Ready does not mean implemented. |
| 7. RFCs and ADRs | Evaluate technical options and record decisions; move earlier when needed | RFC: `draft` → `in-review` → `accepted` or `rejected`. ADR: `proposed` → `accepted` or `rejected` | Are alternatives, evidence, consequences and the actual decision recorded? The agent cannot invent acceptance. |
| 8. Reconcile and learn | Review meaning and criterion coverage across the connected plan, run static checks separately, and revise as evidence arrives | No separate stage status. Record actual findings/blockers in the index; update affected documents and risk entries | Do criteria agree with canonical behavior and thresholds? What should you validate, decide, investigate or implement next? |

These are typical paths, not a requirement to visit every status in order. Explicit approval is needed to label a general document approved, but approval is not an automatic pause before every downstream draft. General documents and RFCs/ADRs can become superseded when replaced. Risk acceptance and risk closure are different outcomes, not consecutive mandatory steps. See [the lifecycle rules](#understand-the-statuses-and-lifecycle) for transition conditions and who can authorize them.

## 1. Start in the project folder

For a real product, open its application repository as the working project in Codex or start Claude Code from that root. Embed this kit's project profiles and shared files there using the [in-repository integration guide](workflow/IN-REPOSITORY.md). The planning files live alongside the application source; this kit checkout is only the reusable source. You can also use this checkout to maintain or evaluate the kit itself.

A Turborepo scaffold can already exist before planning. The specialists inspect its relevant manifests and source as context, distinguish starter defaults from product decisions, and keep their assignments limited to planning artifacts. When you explicitly request implementation, the primary coding agent or coding workers consume a selected story/enabler and its canonical requirements in that same repository. Ordinary fixes do not restart the complete discovery workflow. The guide includes copy-ready integration, planning and implementation prompts plus embedded validation commands.

Keep one main chat as the coordinator for a product at a time. You do not need to open a separate chat for each specialist. The coordinator assigns tasks, manages document IDs, updates the index and brings the results back to you. Avoid running Codex and Claude against the same product files simultaneously.

The examples below use Codex names. In Claude, substitute the name in the right-hand column:

| Job | Codex agent | Claude Code agent |
| --- | --- | --- |
| Research the starting business model | `lean_canvas` | `lean-canvas` |
| Prioritize outcomes | `product_roadmap` | `product-roadmap` |
| Define a bounded product requirement | `lean_prd` | `lean-prd` |
| Track uncertainties and responses | `risk_register` | `risk-register` |
| Break an outcome into a larger work package | `epic` | `epic` |
| Specify user value or a learning task | `user_story` | `user-story` |
| Specify supporting technical work | `enabler` | `enabler` |
| Evaluate technical options | `rfc` | `rfc` |
| Record an architecture decision | `adr` | `adr` |

Before your first run, you can use the read-only discovery prompt in [Codex prompts](examples/prompts.md#check-agent-discovery) or [Claude prompts](examples/claude-prompts.md#check-discovery-without-generating-product-artifacts). It checks whether the named specialists are available. If a fallback is used, the coordinator should tell you.

The repository is already the product workspace. Planning artifacts go directly under `docs/`, with the index at `docs/INDEX.md`; no additional product folder or slug is required. Replace prompt placeholders with your own details. The coordinator handles artifact subfolders, unused IDs and index entries. Example IDs below describe an initial run; reuse the actual IDs in your index when continuing existing work.

## 2. Describe the idea and get a researched Lean Canvas

**Question answered:** Who could this help, why might they care, and how might the business work?

**You provide:** A few sentences describing the idea. If known, add who you want to help, the country or market, and constraints such as your available time or budget. A formal brief is optional.

```text
Use lean_canvas to research this idea and create a complete Lean Canvas:
<Describe what you want to build and what it helps someone do.>

Useful context: <optional customer, geography, founder constraints or existing evidence>.
Use available web research tools, cite the supporting pages, and recommend a
starting business model in plain English. Label assumptions and propose the
three most useful validation tests. Save under docs/.
```

**The agent does:** Researches customer problems, alternatives, advertised prices, acquisition channels, costs and relevant constraints. It fills all nine canvas blocks: problem, customer segments, value proposition, solution, channels, revenue, costs, metrics and unfair advantage. Sources and research coverage are included in the canvas.

**You receive:** A canvas such as `canvas/LC-001.md`, plus a summary of evidence limits and the most useful first test.

**What to review:** Does the suggested customer match your intention? Are the problems meaningful? Can you realistically reach these people? Do the proposed solution and costs fit your constraints? Tell the coordinator what it got wrong rather than rewriting the document yourself.

The agent distinguishes facts, inferences, hypotheses and unknowns. A competitor's published price is a fact about its offer. Your proposed price is a hypothesis until tested. If no unfair advantage is established, the canvas should say so and suggest how one might be built.

**When to continue:** The canvas gives you a coherent starting position and practical tests. You can move into roadmap planning with explicit hypotheses; you do not need to pretend demand is already proven. If research tools are unavailable, the agent returns a useful draft and explains the gap. Fundamental scope or evidence gaps should be addressed before treating the canvas as ready.

## 3. Turn the canvas into a Now / Next / Later roadmap

**Question answered:** Which outcomes deserve attention first?

**You provide:** The canvas, your priorities and any real constraints. For example, tell the coordinator if you want to learn before building or can support only a small first release.

```text
Use product_roadmap to create a Now / Next / Later roadmap from
docs/canvas/LC-001.md.
Keep Now focused on the smallest useful outcome. Preserve the canvas scope.
Give initiatives stable IDs, success measures, dependencies and criteria for
moving between horizons. Explain the recommended order. Do not invent dates.
```

| Horizon | Meaning | What to look for |
| --- | --- | --- |
| Now | The current focus | Clear outcome, dependencies, success measure and exit criterion |
| Next | A likely following priority | Evidence or conditions needed before moving into Now |
| Later | A possibility to revisit | Why it may matter and what would trigger another look |

**You receive:** A roadmap such as `roadmap/RM-001.md`, with initiative IDs such as `RM-001-I01`. An initiative describes an outcome or problem to solve, rather than a pile of features.

**What to review:** Is Now small enough? Does its outcome help the chosen customer? Is there a cheaper way to learn? What has deliberately been deferred?

**When to continue:** Choose the initiative to explore in detail. You do not need a PRD for every Next or Later idea. These horizons express priorities; they are not automatic calendar commitments.

## 4. Write a Lean PRD and register its risks

**Question answered:** For the selected initiative, what should the product achieve and what could prevent it?

A PRD is a Product Requirements Document. Here it stays lean: one bounded problem, intended users, success measures, included behavior, exclusions and important constraints.

New PRDs use selective EARS by default for suitable observable behavior in their Behavioral requirements table. EARS means Easy Approach to Requirements Syntax: a lightweight way of making system conditions and expected responses explicit. You describe your intent in ordinary language; the specialist writes the structured rules and explains them. Business hypotheses and learning plans keep their existing formats. For an existing PRD, adoption covers the requested material revision; unrelated legacy behavior and historical decisions remain intact. A new comparative pilot is optional.

```text
Use lean_prd to define initiative <initiative ID> from
docs/roadmap/RM-001.md.
Then use risk_register to deduplicate and register its risks.
Run these tasks sequentially. Have lean_prd replace temporary risk references
with the registered IDs and product_roadmap link them to the initiative.
Keep the scope small and make exclusions and evidence gaps explicit.
Use workflow/EARS.md: author suitable canonical behavioral
rows with stable IDs, source/rationale and a verification approach. Keep learning
hypotheses separate and do not invent approvals or test results.
Record actual semantic review in the PRD; have the coordinator challenge it and
summarize scope, findings and blockers in INDEX.md separately from static checks.
Stop after this stage; downstream response links may remain pending.
```

**You receive:** A PRD such as `prds/PRD-001.md` and the product's shared risk register, `risks/RR-001.md`. The PRD is the formal point where initial risks are born. Earlier canvas assumptions can feed this assessment.

Each risk gets a stable ID such as `RISK-001`, an origin, category, owner or assignment gap, next action and closure criterion. It states a cause, an uncertain event and its potential impact.

| Risk category | Plain-language question | Required response |
| --- | --- | --- |
| Business | Will this create enough business value or support a viable model? | User story with a measurable delivery or learning outcome |
| User | Can the intended person understand, use or benefit from it? | User story with observable behavior or a measurable learning test |
| Technical | Can the system meet the needed behavior or constraints? | RFC to evaluate options or ADR to record a decision |

**What to review:** Is the PRD solving one clear problem? Are essential behaviors and exclusions understandable? In adopted EARS scope, does each rule have clear conditions, an observable response, a justified source and a verification method? Are important failures, conflicting rules and unresolved decisions visible? Does each risk describe a real uncertainty, with a practical response?

**When to continue:** The requirements are clear enough to break down, and risk ownership and next actions are visible. Response links can be pending at this stage if their documents have not yet been created. An early technical uncertainty may need an RFC before the next step.

### How a requirement travels through the workflow

The PRD is the source of truth for each behavioral rule. A row might have ID `PRD-001-R01`. An illustrative EARS statement is: "While a report is being generated, when a user requests its export, the application shall reject the export request."

An epic groups the outcome and references that ID. A story references the same ID and gives concrete Given/When/Then examples, including important boundary and failure cases. An enabler explains the technical work that supports it. An RFC/ADR references it as a constraint on the evaluated or chosen approach. These documents do not independently maintain copies of the normative sentence.

If a story exposes a missing behavior, ask the coordinator to have the PRD specialist add or revise the canonical row, then reconcile affected scenarios and decisions. Existing IDs stay stable across wording corrections. Retired/replaced rows are recorded in Requirement changes, and new obligations receive new IDs. A pure learning story or spike can explain why no behavioral requirement applies and retain its investigation format.

There is no new agent, artifact type or lifecycle state. The [EARS guide](workflow/EARS.md) explains adoption, patterns, linking, review and checking limits. Use the [adoption and optional pilot prompts](examples/ears-pilot.md) for routine work or a further comparative measurement. Existing products are not automatically migrated.

### How semantic review works

Semantic review checks what a rule means and whether its examples agree. The PRD specialist records actual review in the PRD, then the coordinator challenges it before treating the document as ready. Downstream specialists review their applicable rules against concrete examples and return findings through their handoffs. This can be agent review; it does not imply a human or customer tested anything.

| Review focus | Example question |
| --- | --- |
| Intent and boundary | Does this preserve the requested scope, and which actor/system controls the result? |
| Values and limits | What happens for zero, fractions, invalid dates or amounts beyond the supported range? |
| State and failure | What happens if saving fails or an action is retried? Is a new similar entry different from replay? |
| Data and side effects | Is the preview still current? Can logs, platform backup or a device flow expose different data? |
| Cross-artifact consistency | Do the sample sizes, thresholds, terminology and expected totals agree everywhere? |
| Verification and evidence | What concrete input has what expected outcome? Is that a planned test or an actual result? |

Only relevant questions apply. A review records the source revision, cases considered, findings and next actions; inapplicable areas need a reason, and unperformed checks stay Not reviewed. A missing numeric limit or unresolved platform assumption can keep a document draft even when the requirement sentence and links pass static checks. A complete review does not mean every finding is resolved.

You can request this without learning EARS syntax:

```text
Review <PRD ID> and its related artifacts using the semantic review protocol
in workflow/EARS.md. Show concrete counterexamples and inconsistent thresholds.
Have the owning specialist revise canonical rules when needed, then reconcile
affected criteria. Record actual findings, reviewed revisions and blockers in
the PRD/handoffs/index. Run static checks separately; do not invent test results
or change approval, architecture-acceptance or risk states without evidence.
```

The coordinator sends behavioral changes to the PRD specialist and register changes to the register specialist. Re-review affected rules and criteria after material changes. Updating links alone is maintenance, rather than a new behavioral correction or evidence of improved productivity.

## 5. Break the PRD into epics

**Question answered:** What larger, coherent outcomes make up this requirement?

An epic groups related work around a useful result. It is smaller than the PRD's overall scope and larger than an individual story. For example, enabling a user to complete a useful workflow is a clearer outcome than grouping work only by database, API and screen.

```text
Use epic to break docs/prds/PRD-001.md into the minimum
useful epics. Create separate epic files with reserved IDs, outcome-level
acceptance criteria, scope boundaries and candidate stories/enablers.
Map risk responses to the relevant epic. Preserve PRD exclusions and report
dependencies or technical decisions that block further decomposition.
Link applicable canonical PRD requirement IDs without copying their rules.
```

The coordinator assigns bounded tasks to the epic specialist, keeping one outcome per epic file.

**You receive:** Files such as `epics/EPIC-001.md`, with acceptance criteria and a proposed breakdown of work.

**What to review:** Does each epic produce something meaningful? Are outcomes duplicated? Does the combined work stay inside the PRD? Can a smaller useful slice come first?

**When to continue:** Each epic has a clear outcome, boundary and proposed smaller items. Unresolved technical decisions remain explicit.

## 6. Specify stories and technical enablers

**Question answered:** What small pieces of work or learning should someone carry out?

| Item | Purpose | What makes it useful |
| --- | --- | --- |
| User story | Deliver a user/business benefit or learn something important about it | A clear benefit and observable acceptance criteria |
| Enabler | Provide a technical capability that supports an outcome | A concrete deliverable and verification method |
| Spike | A time-limited investigation, represented as an enabler | One uncertainty, a timebox, an experiment and a decision it will inform |

Acceptance criteria describe how someone can tell the work succeeded. A story may express them as Given a starting situation, When an action happens, Then an observable result follows.

```text
Use user_story and enabler to turn <epic ID> in docs/
into small, testable items. Give business/user risks direct story responses
with hypotheses, methods, thresholds and next decisions. Technical enablers
must identify the outcome they support and any required RFC/ADR dependency.
Reserve IDs and separate paths before independent work. Explain the order.
Declare canonical PRD requirement references and map concrete criteria to them.
Use justified None for learning-only work or an explicitly unmigrated parent.
```

**You receive:** Story files such as `stories/US-001.md` and, where needed, technical work in `enablers/EN-001.md`.

**What to review:** Could someone understand what to do and how to verify it? Are stories small enough? Does a learning story specify what evidence would change your decision? Does each enabler have a real reason to exist?

**When to continue:** The work has testable criteria and visible dependencies. A technical enabler can support risk mitigation, but it does not replace a technical risk's required RFC/ADR link. Ordinary stories or necessary enablers do not need an invented risk just to fit the process.

## 7. Resolve technical questions with RFCs and ADRs

**Question answered:** What technical approach should we take, and why?

An RFC, or Request for Comments, compares options and identifies evidence needed to choose. An ADR, or Architecture Decision Record, captures one proposed or authorized architecture decision, its rationale and its consequences.

| Situation | Use |
| --- | --- |
| We need to investigate feasibility or compare meaningful alternatives | RFC |
| A specific decision needs to be proposed or recorded | ADR |
| Evaluation leads to an enduring architecture decision | RFC, then an ADR if appropriate |

```text
Review the technical risks for <PRD or epic ID> in docs/.
Use rfc where alternatives or feasibility need evaluation, and adr where a
specific decision needs recording. Link the originating PRD and risk IDs.
Reference canonical PRD requirements that constrain the options or decision.
Keep undecided ADRs proposed. Specify any supporting spike or implementation
enabler through the enabler specialist and reconcile affected work items.
```

**You receive:** Relevant files in `rfcs/` or `adrs/`, with alternatives, rationale, evidence gaps and follow-up work.

**What to review:** What is recommended? What does it cost or make harder? What evidence supports the choice? What remains uncertain? If you need help interpreting it, ask for an explanation in plain English and the consequences of each option.

**When to continue:** Decision blockers are resolved enough for the dependent work. A recommended choice remains proposed until an authorized person actually decides. Both an RFC and an ADR are not required for every technical risk.

This step can happen immediately after the PRD if technical uncertainty blocks useful epic/story planning. The order is flexible where dependencies require it; there is no need to finish every story before asking a technical question.

## 8. Check the connected plan and choose the next action

**Question answered:** Do the documents fit together, and what is actually ready to happen?

```text
Reconcile the planning artifacts for <initiative ID> in docs/.
Check parent links, scope, dependencies, measurable criteria and the index.
Use risk_register to check that business/user risks link to stories and technical
risks link to RFCs/ADRs, with reciprocal links. Report missing responses, owners,
evidence and decisions. Give me an ordered next-action list and explain which
items are ready, blocked or still proposed. Do not claim work was implemented.
For adopted EARS scope, check canonical IDs and reference/scenario agreement;
run the structural requirements checker and report its limits separately from
the specialist review of semantics and verification coverage.
```

**You receive:** An updated `INDEX.md`, reconciled documents and a concise handoff explaining changes, checks, blockers and next actions. The index is the starting point for finding your current documents and their status.

**What to review:** Can every work item be traced back to an outcome? Does every registered risk have the required response once full routing is in scope? Do the response documents link back to their risks? Are any implementation items depending on undecided architecture or unresolved requirements?

**When to continue:** Choose the next appropriate action: run a customer-learning test, investigate a technical question, make a decision, or explicitly request implementation of a ready item. This kit produces planning artifacts; it does not automatically build software, run experiments, contact customers, open tickets or publish anything. A written story is a specification of work, not evidence that the work is done.

These are suggested review points, not mandatory approval pauses between every draft. You can request several stages together. The agents can draft and reconcile that scope while keeping genuine decisions and missing evidence visible.

## 9. Feed real evidence back into the plan

The workflow continues when research, customer conversations, experiments or implementation reveal something new. Give the coordinator your actual observations or a source file; it should not invent results on your behalf.

```text
New evidence for docs/: <observations or source path>.
Use risk_register to compare it with <risk ID>'s closure criterion.
Revise affected artifacts through their specialists and update the index.
Explain what changed, what remains uncertain and whether priorities should change.
```

Creating a response document moves a risk at most into mitigation. Closing it requires evidence that meets its stated criterion. Accepting a risk requires an actual owner decision, rationale, remaining exposure and a review date. A new risk found later is registered with its real discovery stage.

If a requirement changes, update the affected draft and its dependent work. If an accepted architecture decision changes, create a new ADR that supersedes it and preserve the old decision's history. Keep stable IDs when revising existing artifacts.

## Understand the statuses and lifecycle

There are four lifecycles: general planning documents, RFCs, ADRs and individual risks. Their status names have different meanings. In particular, an accepted architecture decision does not mean its linked risk is closed.

### General planning documents

This lifecycle applies to the Lean Canvas, roadmap, PRDs, epics, stories, enablers and the risk register document itself.

| Status | Meaning | What permits the change |
| --- | --- | --- |
| `draft` | The document is being developed or has material unresolved inputs, evidence gaps or failed checks | The specialist can create a useful draft and explicitly record blockers. Material revisions that invalidate readiness need renewed checks. |
| `ready` | The applicable checklist passes and material blockers are resolved for the intended planning use | The specialist checks the artifact and the coordinator reconciles its index entry. Neither stakeholder approval, completed implementation nor validated demand is implied. |
| `approved` | The relevant user/stakeholder explicitly approves this document or scope | An actual decision and its source must be recorded. The agent cannot infer approval from readiness, silence or a request to draft the document. |
| `superseded` | A replacement document takes over | Record the replacement link and retain the old document's history. A normal revision with the same ID does not automatically require a new document. |

The usual progression is draft, then ready, with approved used when explicit approval is given. Superseded describes replacement rather than completion. Keep the ID stable when revising an existing artifact, update its revision/date, and recheck affected downstream documents. Do not assume an earlier approval covers materially changed content.

For the Lean Canvas, ready means sufficient research and clarity to plan bounded validation. It can still contain labeled hypotheses about price or customer demand. For a story or enabler, ready describes the specification; the kit does not use this document lifecycle to track implementation as in-progress or done.

For the roadmap, Now, Next and Later describe an initiative's priority horizon. They are not replacements for draft, ready or approved. A ready roadmap may contain initiatives in all three horizons, and moving one initiative does not automatically change the document's approval status.

### RFCs: evaluating an approach

| Status | Meaning | What permits the change |
| --- | --- | --- |
| `draft` | The technical question, alternatives and evaluation plan are being prepared | The specialist assembles a reviewable proposal and labels missing evidence. |
| `in-review` | The proposal is under review and feedback or evaluation is being considered | Record the review context, decision owner and unresolved questions; do not invent feedback or completed experiments. |
| `accepted` | An authorized decision-maker accepts the proposal | Record the actual resolution and its authorization evidence. A confident recommendation alone is insufficient. |
| `rejected` | An authorized decision-maker rejects the proposal | Record the actual resolution, rationale and authorization evidence. |
| `superseded` | A newer RFC replaces the proposal | Link the replacement and preserve the earlier record. |

The usual path is draft, then in-review, then accepted or rejected. The agent may prepare the proposal and evaluation plan without waiting for approval at every edit. Acceptance/rejection requires a real resolution. An accepted RFC may lead to an ADR when an enduring architecture decision needs recording; the two documents are not always both necessary.

### ADRs: recording a decision

| Status | Meaning | What permits the change |
| --- | --- | --- |
| `proposed` | A specific architecture choice is suggested but not yet authorized | The specialist can record the proposal, alternatives, rationale, consequences and evidence needed. |
| `accepted` | The authorized owner makes the decision | Record the actual owner, decision date and authorization source. The coordinator records your decision; it does not make approval up. |
| `rejected` | The authorized owner rejects the proposed choice | Record the decision, rationale and authorization source. |
| `superseded` | A new ADR replaces an earlier decision | Create a new ADR, link the records both ways, and retain the accepted decision's history rather than rewriting it. |

An ADR starts proposed, then can become accepted or rejected. There is no ready or approved status for an ADR in this kit. If an accepted choice changes, the new decision has its own record and authorization; it does not inherit acceptance automatically.

### Individual risks: managing uncertainty

The risk register has a document status in its metadata, and every RISK entry has its own risk status. These are independent: the register may be ready while a risk remains open or mitigating.

| Risk status | Meaning | What permits the change |
| --- | --- | --- |
| `open` | The uncertainty remains unresolved | Record its origin, category, owner or assignment blocker, required route, next action and closure criterion. |
| `mitigating` | A response is identified or underway; uncertainty may remain | Link the relevant story or RFC/ADR and supporting work. Creating these documents can move a risk at most to mitigating. |
| `accepted` | The accountable owner explicitly accepts the remaining exposure | Record the owner's decision, rationale, residual exposure and review date. This does not assert the risk was eliminated. |
| `closed` | Evidence satisfies the risk's stated closure criterion | Record the actual measurement or proof and compare it with the criterion. An artifact, recommendation or implementation claim alone is insufficient. |

A common path is open, then mitigating, followed by closed when evidence supports closure or accepted when the owner deliberately accepts the remaining exposure. Acceptance is not a prerequisite for closure. When a review date arrives or circumstances change, reassess the evidence and exposure rather than treating the old disposition as permanent.

For a business/user risk, the required response is a story with measurable behavior or a learning test. For a technical risk, it is an RFC or ADR; an enabler can support that response. Route completion and uncertainty resolution are separate: a correctly linked RFC may satisfy the routing requirement while its risk remains mitigating.

### Who updates status, and how to request it

Specialists update their assigned documents; the coordinator keeps INDEX.md consistent. Only the risk-register specialist edits the register and its risk entries. Real approvals, architecture resolutions and risk-acceptance decisions must come from an authorized person. Closure must be supported by actual evidence.

```text
Review the lifecycle status of <artifact or risk ID> in docs/.
Check it against the relevant checklist, decisions and evidence. Update only
the statuses supported by those checks, reconcile INDEX.md, and explain each
change. If a transition is blocked, state the exact missing input or evidence.
```

For approval or acceptance, provide what you actually decide and identify the document/revision or choice. For closure, provide the actual evidence or its file path. A request to review status by itself is not authorization to approve, accept or close everything. You may continue independent downstream drafting, but material unresolved upstream blockers still prevent the affected downstream artifact from claiming readiness.

## Find your files

All paths in this table are relative to `docs/`. The numbers are examples; the coordinator reserves unused IDs and reuses the existing register.

| File | What you use it for |
| --- | --- |
| `INDEX.md` | Current artifact list, parent IDs, risk coverage and blockers |
| `canvas/LC-001.md` | Starting business model, research and validation hypotheses |
| `roadmap/RM-001.md` | Current priorities and initiative IDs |
| `prds/PRD-001.md` | Bounded product requirements |
| `risks/RR-001.md` | Product-wide risks, required responses and evidence |
| `epics/EPIC-001.md` | Larger outcome and breakdown of work |
| `stories/US-001.md` | User/business behavior or learning work |
| `enablers/EN-001.md` | Supporting technical work or investigation |
| `rfcs/RFC-001.md` | Evaluation of a technical question |
| `adrs/ADR-001.md` | One architecture decision and its history |

## Useful everyday requests

**Resume in a new chat:**

```text
Continue docs/. Read INDEX.md and the relevant artifacts.
Summarize the current outcome, open risks and blockers, then recommend the
next bounded action. Reuse existing work and do not restart the workflow.
```

**Correct an assumption:**

```text
For docs/, correct this assumption: <correction>.
Update the affected artifacts and index through their owning specialists.
Preserve unrelated scope and explain the downstream effect.
```

**Request several stages together:**

```text
For <initiative ID> in docs/, coordinate the relevant
specialists to prepare the remaining planning documents through the delivery
handoff. Reuse existing artifacts, follow dependencies, and preserve scope.
Keep proposed decisions and evidence gaps explicit. Report what I need to
decide or validate and the next practical action. Do not implement code.
```

In Claude, use the mapped agent names if you name a specialist explicitly. Requests to the coordinator can describe the desired outcome in ordinary language.

## Common problems

| Situation | What to do |
| --- | --- |
| You only have a rough idea | Start with the canvas prompt; business terminology and a polished brief are unnecessary |
| The agent asks you to fill every canvas block | Ask it to follow the research playbook and propose answers; answer only essential scope questions |
| A specialist cannot browse | Have the coordinator check permitted research access or provide sources; keep unresearched content labeled and draft |
| A market claim lacks support | Ask for a source actually read, or for the claim to be labeled as an inference/hypothesis/unknown |
| The roadmap keeps growing | Select one initiative and state what is out of scope |
| A stage remains draft | Ask for the exact blocker, why it matters and the smallest way to resolve it |
| A technical question blocks stories | Move its RFC or proposed ADR earlier, then reconcile the dependent items |
| A risk is marked closed because an RFC exists | Ask for the measured evidence against its closure criterion; document creation alone does not close it |
| The named agent is unavailable | Use the discovery prompt and ask the coordinator to report any fallback accurately |

## Optional checks for the kit itself

You normally use the chat prompts rather than editing agent configuration. If you change the canonical specialist instructions, the repository's maintenance commands are:

```powershell
python scripts/sync-claude-agents.py
python scripts/validate-kit.py
```

These synchronize Claude profiles and check the reusable kit's configuration, templates and document links. They do not validate your business, prove live agent behavior, run product acceptance tests or audit generated product documents. The coordinator's stage reviews check the actual planning artifacts.

For the underlying rules, see the [shared contract](workflow/CONTRACT.md), [coordinator runbook](workflow/ORCHESTRATION.md) and [Lean Canvas research playbook](workflow/LEAN-CANVAS-RESEARCH.md).

For structural checking of adopted PRD requirements and their downstream references, use:

```powershell
python scripts/validate-requirements.py docs
```

This read-only check catches malformed tables, certain syntax problems, invalid/duplicate IDs and broken canonical references. It skips legacy PRDs without EARS sections and reports when none were checked. It cannot prove completeness, semantic correctness, test coverage or readiness, and never changes statuses. Record adoption scope and actual semantic review in the PRD/handoffs/index, separately from script output. Keep optional pilot measurements in the index; script tests are not evidence of product-pilot gains.
