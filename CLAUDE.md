@AGENTS.md

# Claude Code adapter

Use the shared workflow and templates imported above. In Claude Code, delegate to the project agents in `.claude/agents/` using the names below. Translate Codex role names in the shared documents and prompts using this table; do not try to spawn an underscored name in Claude Code.

| Shared / Codex role | Claude Code agent |
| --- | --- |
| `lean_canvas` | `lean-canvas` |
| `product_roadmap` | `product-roadmap` |
| `lean_prd` | `lean-prd` |
| `risk_register` | `risk-register` |
| `epic` | `epic` |
| `user_story` | `user-story` |
| `enabler` | `enabler` |
| `rfc` | `rfc` |
| `adr` | `adr` |

The primary Claude conversation coordinates stages and owns INDEX.md. The risk-register agent alone writes the risk register. Pass the complete dispatch payload from workflow/ORCHESTRATION.md: each subagent needs explicit source paths, IDs, output path and constraints. Run dependent tasks sequentially. Limit independent work to three concurrent subagents or the runtime's lower limit; this is a coordinator instruction, not a Claude configuration setting. Do not start separate Codex and Claude coordinators against the same product files concurrently.

Use normal session tool permissions. Profiles request the parent model with `model: inherit`; environment or managed policy may affect the actual selection. Do not change permission modes or bypass approval to run this workflow. Specialists must report questions and downstream work to the primary conversation and must not spawn further agents.

For kit maintenance, `.codex/agents/*.toml` holds the canonical specialist instructions. After changing a profile, run `python scripts/sync-claude-agents.py`, then `python scripts/validate-kit.py`. The generated Claude profiles translate role identifiers and keep the same template, scope, evidence and risk rules. Do not edit generated profiles directly. See examples/claude-prompts.md for usage and a read-only discovery check.
