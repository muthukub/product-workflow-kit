# Use the agents inside an application repository

Keep the agents, product artifacts and implementation in the same Git repository. This kit is a source of reusable files; running the workflow does not require keeping its repository open, a second checkout, a submodule or an `sdlc-subagents/` directory inside the application.

## Repository layout

Use the existing root-relative kit paths for the first integration. They work alongside a Turborepo scaffold:

```text
my-product/
  AGENTS.md                    # engineering instructions plus planning routing
  CLAUDE.md                    # shared instructions and Claude role mapping
  .codex/
    config.toml
    agents/                    # nine planning profiles; other coding agents can coexist
  .claude/agents/              # generated planning profiles and any coding profiles
  apps/                       # applications from the scaffold
  packages/                   # shared code/tooling from the scaffold
  docs/
    INDEX.md                  # product planning index
    canvas/
    roadmap/
    prds/
    risks/
    epics/
    stories/
    enablers/
    rfcs/
    adrs/
  templates/                  # standardized planning templates
  workflow/                   # contract, orchestration, EARS and this guide
  scripts/                    # kit utilities alongside existing repo scripts
  tests/                      # kit utility tests alongside existing repo tests
  examples/                   # copy-ready planning prompts
  USER-MANUAL.md               # workflow manual; keep the application's own README
  package.json
  pnpm-workspace.yaml
  turbo.json
```

The app/package names and package manager above are illustrative; inspect the actual scaffold. The planning folders are ordinary versioned files, not runtime dependencies or workspace packages. Do not add a `package.json` to a planning folder just to make Turbo discover it. Keep the package manager's actual workspace configuration; Turborepo recommends `apps/*` and `packages/*` as a starting structure. [Official repository structure](https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository), accessed 2026-11-19.

The repository already identifies the product. Use `docs/INDEX.md` and one risk register under `docs/risks/` for all its apps/packages. No product slug or `products/<product-slug>/` wrapper is needed. Other engineering, operations or API documentation can coexist in separate subfolders of `docs/`. The root documentation folder is separate from any `apps/docs` application in the scaffold. Shared `workflow/` and `templates/` directories retain their root-relative locations.

For a different existing artifact location, pass its actual root explicitly and reuse its index. When relocation is requested, verify destination collisions first, move the artifact tree and check links, canonical references and historical snapshot hashes. The requirement checker accepts the artifact root as an argument: `python scripts/validate-requirements.py docs`. Preserve frozen records, including historical command strings. Existing ignore rules may match differently after relocation; review tracking separately without silently rewriting them.

## Install into a new or existing scaffold

1. Create the application scaffold if desired. For example, the official pnpm starter command is `pnpm dlx create-turbo@latest`; it creates example applications and libraries. This is repository setup, not proof of product behavior. Inspect generated files and retain only defaults that fit the intended repository. [Official installation guide](https://turborepo.dev/docs/getting-started/installation), accessed 2026-11-19.
2. Bring the reusable files into that same repository root using the table below. Omit this kit's `.git`, product examples/outputs, virtual environments and local settings. Preserve the application's existing files.
3. Merge the root instructions and client configuration. Keep build/test commands and any nested app/package engineering instructions. Do not replace the application's README with the kit README.
4. Run embedded checks below, start the client against the application root, and perform the read-only discovery check from the examples. Static file validation does not establish that a client has loaded its agents.
5. Commit the shared profiles, templates, workflow and intended planning artifacts with the application. Review `.gitignore` patterns rather than copying this kit's file verbatim; ensure the artifacts you intend to version are not ignored. Preserve local credential/settings exclusions.

| Kit files | Application destination / merge action |
| --- | --- |
| Nine `.codex/agents/*.toml` profiles | Same paths; reserve their role names and report a conflicting existing profile instead of overwriting it |
| Nine `.claude/agents/*.md` profiles | Same paths; preserve unrelated coding agents; regenerate only the kit roles |
| `[agents]` settings in `.codex/config.toml` | Merge into the existing table; preserve models, permissions, providers and unrelated settings; resolve conflicting values explicitly |
| `AGENTS.md` | Merge the planning role table, routing, ownership and shared-file references into the application's root instructions; preserve engineering rules |
| `CLAUDE.md` | Merge `@AGENTS.md`, role-name mapping and coordinator rules into any existing file; preserve app-specific instructions |
| `templates/`, `workflow/`, `examples/`, `USER-MANUAL.md` | Copy the reusable files at the same root-relative paths; compare and reconcile any existing same-name file |
| `scripts/sync-claude-agents.py`, `scripts/validate-kit.py`, `scripts/validate-requirements.py` | Same paths; these resolve kit paths from their parent repository root |
| Kit Python utility tests under `tests/` | Same paths; keep existing application tests intact |

This is a merge procedure, not a destructive copy command or automatic installer. If a destination already contains different content, produce a concrete proposed merge; do not use force/overwrite for convenience. No changes to the target's `package.json`, Turbo tasks, lockfile or source files are needed merely to add planning agents.

You can have the coding agent perform that integration with this prompt:

```text
Integrate the SDLC agent kit from <absolute kit source path> into this application
repository root using workflow/IN-REPOSITORY.md from the kit.
Inspect existing instructions, agent names, config, scripts and scaffold first.
Merge the nine planning profiles, shared workflow/templates and utilities into
the root-relative paths; preserve unrelated coding agents, engineering rules,
README, package manifests, lockfiles, source files and local permission settings.
Show concrete conflicts instead of overwriting differing same-name files.
Do not copy sample products, .git or local settings. Do not generate product
artifacts or implement features merely because the kit is being integrated.
Run the embedded checks and report which client discovery checks actually ran.
```

The target path is the application repository you are working in; the source path is only needed while copying/updating the kit. Subsequent planning and coding use the application checkout alone.

## Let planning and coding coexist

Root `AGENTS.md` should express this routing alongside the nine-role table:

```text
For product planning, coordinate the matching specialists using the shared
contract, orchestration and templates. Planning specialists edit only their
assigned artifact files; the coordinator owns the product index.

For explicitly requested scaffold or code work, use the primary coding agent
or coding workers and follow this repository's engineering instructions.
Read relevant product artifacts and material blockers for feature work.
Ordinary fixes do not require restarting the entire planning workflow.
A planning request alone does not authorize application edits or dependency installs.
```

Project Codex profiles belong in `.codex/agents/`; project Claude profiles belong in `.claude/agents/`. These are supported project-level locations, so no global installation or separate planning session is required by this kit. [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude project subagents](https://code.claude.com/docs/en/sub-agents), accessed 2026-11-19. Client availability and discovery must still be checked in the actual environment.

## Start from the real scaffold

Scaffolding can happen before product planning. If the user requests it, a coding agent creates/adjusts the repository structure, verifies what it can, and records observed facts: current paths, manifests, package manager, available commands, starter/demo behavior and missing components. This context can live in the product's Sources or a brief/baseline note once a product exists; it does not need an invented PRD or risk entry just to bootstrap a workspace.

When planning begins, specialists read relevant existing files as context. They distinguish:

| Item | Meaning |
| --- | --- |
| An `apps/web` directory and its current manifest | Observed scaffold, if actually inspected |
| Starter demo pages, database/auth defaults or an example service | Existing implementation/defaults, not automatically accepted product requirements or architecture |
| A proposed framework/service change | Option to evaluate; use RFC/ADR when a technical risk or enduring decision warrants it |
| A passing scaffold build | Evidence about that scaffold/configuration only, not the planned product's acceptance criteria |
| A missing API or schema | Explicit absent implementation/TBD; do not describe it as already available |

An initial planning prompt can be:

```text
We are building <plain-language idea> in this repository.
Inspect the existing scaffold and instructions as context; do not modify code.
Coordinate the product planning workflow under docs/.
Use researched assumptions, selective EARS and semantic review. Keep the first
Now initiative small. Distinguish observed scaffold defaults from proposed choices.
Produce the necessary artifacts and identify the first unblocked implementation
story/enabler, its code boundaries, verification approach and remaining blockers.
Do not claim customer validation or accept architecture decisions on my behalf.
```

## Hand one bounded item to the coding agent

After planning, use the same repository to implement a selected story or enabler. Do not ask the PRD/story specialist to become a coding agent outside its assignment. Use the primary coding agent or applicable coding workers; no tenth planning specialist is required.

The coding handoff contains:

| Input | What to inspect |
| --- | --- |
| Selected story/enabler and revision | Scope, concrete criteria, dependencies and completion evidence |
| Canonical PRD rows | Applicable stable IDs and current behavioral meaning |
| Relevant RFCs/ADRs | Actual decision status, constraints and unresolved alternatives |
| Risk entries | Material blockers, required evidence and responsible owner gaps |
| Real repository context | Affected apps/packages, nested instructions, existing implementation and actual validation commands |

```text
Implement <US/EN ID> from docs/<actual artifact path>.
Read its PRD requirement references, relevant risks/decisions and engineering
instructions. Inspect the actual app/package boundaries and commands first.
Implement only this bounded scope and its necessary tests. Preserve unrelated work.
Report any material blocker before depending on an unresolved choice; continue
independently unblocked work. Return missing/conflicting product behavior to the
coordinator/PRD owner instead of silently changing the canonical rule.
Run applicable checks. Record actual changed paths, executed checks and remaining
failures in the selected item's Verification and completion section, or hand those
updates to its owner if concurrent artifact ownership applies. Do not mark risks
closed or decisions accepted merely because code was written.
```

Document readiness and implementation completion remain different. No blanket approval of every artifact is required to start independently unblocked, authorized work. An unresolved material prerequisite blocks the affected implementation. Reference the selected story and requirement IDs in the PR description/verification evidence where useful; avoid tagging every source line or creating tests that merely mirror code.

When a spike or implementation reveals a product ambiguity, revise the canonical PRD through its owner and reconcile scenarios, decisions and code as needed. Keep the artifact and implementation changes reviewable together. Existing document lifecycle states remain intact; implementation evidence is not a new `implemented` document status.

## Validate in an application repository

```powershell
python scripts/sync-claude-agents.py --kit-only
python scripts/validate-kit.py --embedded
python -m unittest discover -s tests -v
# After a product PRD adopts EARS:
python scripts/validate-requirements.py docs
```

`--kit-only` manages only the nine SDLC profiles and leaves unrelated coding profiles untouched. `--embedded` validates those roles and their shared templates/configuration without requiring the application's README to be the kit catalog; unrelated profiles are outside this audit. Existing higher/lower positive concurrency settings are permitted, while the coordinator still caps independent planning work at three or the runtime's lower limit. The default validator mode remains strict for maintaining this kit itself.

Keep these Python checks separate from application lint/typecheck/test/build commands until you deliberately integrate them into the repo's scripts/CI. They require a Python environment with TOML parsing support as documented in the kit; installing the JavaScript scaffold does not itself provide Python. Do not invent npm scripts or cache a mutable artifact audit as if it proved semantic correctness. Static checks cannot establish agent discovery, implementation correctness, semantic completeness, accepted architecture or customer value.
