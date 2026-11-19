# User manual: from an idea to a delivery plan

You can start with an idea in ordinary language. The main chat coordinates specialist agents, saves their work in standard templates, and connects the documents. You provide direction, correct assumptions, and supply real-world evidence as you learn.

The workflow helps you answer progressively smaller questions: Who might need this? What should we focus on? What should the product do? What work and decisions will make that possible?

## 1. Start in the project folder

Use this repository as your working project in Codex, or start Claude Code from this folder. If using a different repository, follow the copying and merging instructions in the [README](README.md#use-in-another-repository).

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

Choose a short folder name for your product, such as `my-product`. In the prompts, replace `<product-slug>` with that name. Replace other angle-bracket placeholders with your own details. The coordinator handles folder creation, unused IDs and index entries. Example IDs below describe an initial run; reuse the actual IDs in your index when continuing existing work.

## 2. Describe the idea and get a researched Lean Canvas

**Question answered:** Who could this help, why might they care, and how might the business work?

**You provide:** A few sentences describing the idea. If known, add who you want to help, the country or market, and constraints such as your available time or budget. A formal brief is optional.

```text
Use lean_canvas to research this idea and create a complete Lean Canvas:
<Describe what you want to build and what it helps someone do.>

Useful context: <optional customer, geography, founder constraints or existing evidence>.
Use available web research tools, cite the supporting pages, and recommend a
starting business model in plain English. Label assumptions and propose the
three most useful validation tests. Save under products/<product-slug>/.
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
products/<product-slug>/canvas/LC-001.md.
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

```text
Use lean_prd to define initiative <initiative ID> from
products/<product-slug>/roadmap/RM-001.md.
Then use risk_register to deduplicate and register its risks.
Run these tasks sequentially. Have lean_prd replace temporary risk references
with the registered IDs and product_roadmap link them to the initiative.
Keep the scope small and make exclusions and evidence gaps explicit.
Stop after this stage; downstream response links may remain pending.
```

**You receive:** A PRD such as `prds/PRD-001.md` and the product's shared risk register, `risks/RR-001.md`. The PRD is the formal point where initial risks are born. Earlier canvas assumptions can feed this assessment.

Each risk gets a stable ID such as `RISK-001`, an origin, category, owner or assignment gap, next action and closure criterion. It states a cause, an uncertain event and its potential impact.

| Risk category | Plain-language question | Required response |
| --- | --- | --- |
| Business | Will this create enough business value or support a viable model? | User story with a measurable delivery or learning outcome |
| User | Can the intended person understand, use or benefit from it? | User story with observable behavior or a measurable learning test |
| Technical | Can the system meet the needed behavior or constraints? | RFC to evaluate options or ADR to record a decision |

**What to review:** Is the PRD solving one clear problem? Are essential behaviors and exclusions understandable? Can success be observed? Does each risk describe a real uncertainty, with a practical response?

**When to continue:** The requirements are clear enough to break down, and risk ownership and next actions are visible. Response links can be pending at this stage if their documents have not yet been created. An early technical uncertainty may need an RFC before the next step.

## 5. Break the PRD into epics

**Question answered:** What larger, coherent outcomes make up this requirement?

An epic groups related work around a useful result. It is smaller than the PRD's overall scope and larger than an individual story. For example, enabling a user to complete a useful workflow is a clearer outcome than grouping work only by database, API and screen.

```text
Use epic to break products/<product-slug>/prds/PRD-001.md into the minimum
useful epics. Create separate epic files with reserved IDs, outcome-level
acceptance criteria, scope boundaries and candidate stories/enablers.
Map risk responses to the relevant epic. Preserve PRD exclusions and report
dependencies or technical decisions that block further decomposition.
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
Use user_story and enabler to turn <epic ID> in products/<product-slug>/
into small, testable items. Give business/user risks direct story responses
with hypotheses, methods, thresholds and next decisions. Technical enablers
must identify the outcome they support and any required RFC/ADR dependency.
Reserve IDs and separate paths before independent work. Explain the order.
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
Review the technical risks for <PRD or epic ID> in products/<product-slug>/.
Use rfc where alternatives or feasibility need evaluation, and adr where a
specific decision needs recording. Link the originating PRD and risk IDs.
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
Reconcile the planning artifacts for <initiative ID> in products/<product-slug>/.
Check parent links, scope, dependencies, measurable criteria and the index.
Use risk_register to check that business/user risks link to stories and technical
risks link to RFCs/ADRs, with reciprocal links. Report missing responses, owners,
evidence and decisions. Give me an ordered next-action list and explain which
items are ready, blocked or still proposed. Do not claim work was implemented.
```

**You receive:** An updated `INDEX.md`, reconciled documents and a concise handoff explaining changes, checks, blockers and next actions. The index is the starting point for finding your current documents and their status.

**What to review:** Can every work item be traced back to an outcome? Does every registered risk have the required response once full routing is in scope? Do the response documents link back to their risks? Are any implementation items depending on undecided architecture or unresolved requirements?

**When to continue:** Choose the next appropriate action: run a customer-learning test, investigate a technical question, make a decision, or explicitly request implementation of a ready item. This kit produces planning artifacts; it does not automatically build software, run experiments, contact customers, open tickets or publish anything. A written story is a specification of work, not evidence that the work is done.

These are suggested review points, not mandatory approval pauses between every draft. You can request several stages together. The agents can draft and reconcile that scope while keeping genuine decisions and missing evidence visible.

## 9. Feed real evidence back into the plan

The workflow continues when research, customer conversations, experiments or implementation reveal something new. Give the coordinator your actual observations or a source file; it should not invent results on your behalf.

```text
New evidence for products/<product-slug>/: <observations or source path>.
Use risk_register to compare it with <risk ID>'s closure criterion.
Revise affected artifacts through their specialists and update the index.
Explain what changed, what remains uncertain and whether priorities should change.
```

Creating a response document moves a risk at most into mitigation. Closing it requires evidence that meets its stated criterion. Accepting a risk requires an actual owner decision, rationale, remaining exposure and a review date. A new risk found later is registered with its real discovery stage.

If a requirement changes, update the affected draft and its dependent work. If an accepted architecture decision changes, create a new ADR that supersedes it and preserve the old decision's history. Keep stable IDs when revising existing artifacts.

## Understand the statuses

| General document status | Meaning |
| --- | --- |
| `draft` | Useful work exists, but required inputs, evidence or checks remain incomplete |
| `ready` | The relevant planning checklist passes; this does not mean the product was built or demand validated |
| `approved` | An actual user/stakeholder approval is recorded |
| `superseded` | A newer artifact replaces it; the history is retained |

RFCs use `draft`, `in-review`, `accepted`, `rejected` and `superseded`. ADRs use `proposed`, `accepted`, `rejected` and `superseded`. Accepted means an authorized resolution is recorded, not simply that the agent prefers an option.

| Risk status | Meaning |
| --- | --- |
| `open` | The uncertainty still needs a response |
| `mitigating` | Work to address it is identified or underway; uncertainty may remain |
| `accepted` | The accountable owner explicitly accepts the remaining exposure |
| `closed` | Evidence satisfies the closure criterion |

## Find your files

All paths in this table are relative to `products/<product-slug>/`. The numbers are examples; the coordinator reserves unused IDs and reuses the existing register.

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
Continue products/<product-slug>/. Read INDEX.md and the relevant artifacts.
Summarize the current outcome, open risks and blockers, then recommend the
next bounded action. Reuse existing work and do not restart the workflow.
```

**Correct an assumption:**

```text
For products/<product-slug>/, correct this assumption: <correction>.
Update the affected artifacts and index through their owning specialists.
Preserve unrelated scope and explain the downstream effect.
```

**Request several stages together:**

```text
For <initiative ID> in products/<product-slug>/, coordinate the relevant
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
