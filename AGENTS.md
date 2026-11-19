# SDLC artifact workspace

This repository contains reusable Codex and Claude Code subagents and shared standardized Markdown templates. When asked to produce product artifacts, act as the coordinator and delegate each artifact to the matching specialist below. Follow `workflow/CONTRACT.md` and `workflow/ORCHESTRATION.md` before delegation. The table uses Codex names; Claude Code uses the equivalent names mapped in `CLAUDE.md`.

These specialists can be embedded at the root of an application repository alongside its source code. Follow `workflow/IN-REPOSITORY.md` for installation, scaffold context and coding handoff; do not require a separate planning repository or nested copy of this entire kit.

Default product artifacts to `docs/`. Reuse the assigned product root and its existing index when continuing work elsewhere; migrate an existing tree only within the user's requested scope and preserve historical records.

Route by the user's requested work. Product planning uses these specialists and their assigned Markdown paths. Explicit scaffolding or implementation requests use the primary coding agent or applicable coding workers under the repository's engineering instructions; planning-specialist file restrictions do not prohibit separately authorized coding work. Existing fixes and maintenance do not require regenerating the entire product workflow. A planning request alone does not authorize application edits or dependency installation.

| Work | Custom agent | Template |
| --- | --- | --- |
| Research-first Lean Canvas from a plain-language idea | `lean_canvas` | `templates/lean-canvas.md` |
| Now / Next / Later roadmap | `product_roadmap` | `templates/product-roadmap.md` |
| Lean PRD | `lean_prd` | `templates/lean-prd.md` |
| Risk register | `risk_register` | `templates/risk-register.md` |
| Epic | `epic` | `templates/epic.md` |
| User story | `user_story` | `templates/user-story.md` |
| Technical enabler | `enabler` | `templates/enabler.md` |
| Request for Comments | `rfc` | `templates/rfc.md` |
| Architecture Decision Record | `adr` | `templates/adr.md` |

Use the primary agent as coordinator; no additional coordinator subagent is needed. Run dependent stages sequentially. Parallelize only independent artifacts with separate output paths and reserved IDs. Each specialist owns only its assigned artifacts; the coordinator owns the product index and dispatches register changes to `risk_register` as the single writer.

For Lean Canvas requests, accept a short idea without requiring business-school knowledge or a detailed brief. The specialist follows `workflow/LEAN-CANVAS-RESEARCH.md`, uses available research tools by default, and delivers all nine blocks with sources, recommendations and testable assumptions. Ask only essential scope questions. If live research is unavailable, disclose it and return a useful draft without claiming verified research.

For new PRDs, use selective EARS by default for suitable observable behavior under `workflow/EARS.md`; the PRD owns canonical rows with stable local IDs and downstream artifacts link them. For existing PRDs, adopt only behavior within the requested material revision and record untouched legacy scope. Keep story scenarios, learning hypotheses, spike investigations, risk routes and lifecycle authorization rules intact. Record actual semantic review in the PRD, handoff and product index, including counterexamples, numeric/platform boundaries, cross-artifact consistency and verification gaps. Static syntax/link checks are separate. No new pilot is required for each PRD; do not invent results, mass-migrate products or revise historical snapshots.

For modifications to this kit, edit its files directly; do not launch the product workflow or generate a fictional product. Preserve existing user changes. Codex TOML profiles hold the canonical specialist instructions; after editing them, regenerate Claude profiles with `python scripts/sync-claude-agents.py`. Validate both clients with `python scripts/validate-kit.py`. If the runtime does not expose these custom agent types, report that limitation; use a general subagent with the exact specialist instructions only if subagents are available, and describe the fallback accurately.
