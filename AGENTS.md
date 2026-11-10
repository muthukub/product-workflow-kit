# SDLC artifact workspace

This repository contains reusable Codex and Claude Code subagents and shared standardized Markdown templates. When asked to produce product artifacts, act as the coordinator and delegate each artifact to the matching specialist below. Follow `workflow/CONTRACT.md` and `workflow/ORCHESTRATION.md` before delegation. The table uses Codex names; Claude Code uses the equivalent names mapped in `CLAUDE.md`.

| Work | Custom agent | Template |
| --- | --- | --- |
| Lean Canvas | `lean_canvas` | `templates/lean-canvas.md` |
| Now / Next / Later roadmap | `product_roadmap` | `templates/product-roadmap.md` |
| Lean PRD | `lean_prd` | `templates/lean-prd.md` |
| Risk register | `risk_register` | `templates/risk-register.md` |
| Epic | `epic` | `templates/epic.md` |
| User story | `user_story` | `templates/user-story.md` |
| Technical enabler | `enabler` | `templates/enabler.md` |
| Request for Comments | `rfc` | `templates/rfc.md` |
| Architecture Decision Record | `adr` | `templates/adr.md` |

Use the primary agent as coordinator; no additional coordinator subagent is needed. Run dependent stages sequentially. Parallelize only independent artifacts with separate output paths and reserved IDs. Each specialist owns only its assigned artifacts; the coordinator owns the product index and dispatches register changes to `risk_register` as the single writer.

For modifications to this kit, edit its files directly; do not launch the product workflow or generate a fictional product. Preserve existing user changes. Codex TOML profiles hold the canonical specialist instructions; after editing them, regenerate Claude profiles with `python scripts/sync-claude-agents.py`. Validate both clients with `python scripts/validate-kit.py`. If the runtime does not expose these custom agent types, report that limitation; use a general subagent with the exact specialist instructions only if subagents are available, and describe the fallback accurately.
