"""Validate the reusable agent kit without calling a model or writing files."""

from pathlib import Path
import re
import subprocess
import sys

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        try:
            from pip._vendor import tomli as tomllib
        except ImportError:
            sys.exit("TOML parser missing: use Python 3.11+ or install tomli.")


ROOT = Path(__file__).resolve().parents[1]
ROLES = {
    "lean_canvas": "lean-canvas",
    "product_roadmap": "product-roadmap",
    "lean_prd": "lean-prd",
    "risk_register": "risk-register",
    "epic": "epic",
    "user_story": "user-story",
    "enabler": "enabler",
    "rfc": "rfc",
    "adr": "adr",
}
METADATA = {
    "ID", "Type", "Status", "Owner", "Updated", "Revision", "Parents", "Risks", "Sources"
}
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read(path):
    if not path.is_file():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def parse_toml(path):
    body = read(path)
    try:
        return tomllib.loads(body)
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"Invalid TOML {path.relative_to(ROOT)}: {exc}")
        return {}


config = parse_toml(ROOT / ".codex/config.toml")
settings = config.get("agents", {})
check(settings.get("enabled") is True, "Project agents must be enabled")
check(settings.get("max_concurrent_threads_per_session") == 3,
      "Expected three concurrent subagent slots")

profiles = list((ROOT / ".codex/agents").glob("*.toml"))
check({p.stem for p in profiles} == set(ROLES), "Expected exactly nine specialist profiles")
agents_doc = read(ROOT / "AGENTS.md")
readme = read(ROOT / "README.md")
claude_doc = read(ROOT / "CLAUDE.md")
check("@AGENTS.md" in claude_doc, "CLAUDE.md must import shared AGENTS.md")
claude_profiles = list((ROOT / ".claude/agents").glob("*.md"))
check({p.stem for p in claude_profiles} == {role.replace("_", "-") for role in ROLES},
      "Expected exactly nine Claude Code specialist profiles")
for role in ROLES:
    check(f"`{role.replace('_', '-')}`" in claude_doc,
          f"{role}: missing Claude name mapping")
sync_script = ROOT / "scripts/sync-claude-agents.py"
if sync_script.is_file():
    sync_result = subprocess.run(
        [sys.executable, str(sync_script), "--check"],
        capture_output=True, text=True, check=False,
    )
    check(sync_result.returncode == 0,
          "Claude profiles differ from canonical prompts: "
          + (sync_result.stdout + sync_result.stderr).strip())
else:
    check(False, "Missing scripts/sync-claude-agents.py")

for role, template in ROLES.items():
    profile = parse_toml(ROOT / f".codex/agents/{role}.toml")
    check(profile.get("name") == role, f"{role}: name must match filename")
    for field in ("name", "description", "developer_instructions"):
        check(isinstance(profile.get(field), str) and bool(profile[field].strip()),
              f"{role}: missing nonempty {field}")
    check(set(profile) <= {"name", "description", "developer_instructions"},
          f"{role}: unexpected fields; review supported schema before adding overrides")
    instructions = profile.get("developer_instructions", "")
    for required in ("AGENTS.md", "workflow/CONTRACT.md",
                     f"templates/{template}.md", "templates/handoff.md"):
        check(required in instructions, f"{role}: instructions must reference {required}")
        check((ROOT / required).is_file(), f"{role}: referenced file missing: {required}")
    check("Do not spawn further agents" in instructions, f"{role}: nesting rule missing")
    check(f"`{role}`" in agents_doc and f"`{role}`" in readme,
          f"{role}: missing from agent catalog")

    body = read(ROOT / f"templates/{template}.md")
    first_table = body.split("\n\n")[1] if "\n\n" in body else ""
    fields = re.findall(r"^\| ([^|]+?) \|", first_table, re.MULTILINE)
    check(set(fields) - {"Field", "---"} == METADATA,
          f"{template}: metadata does not match standard fields")
    check(f"| Type | {template} |" in body, f"{template}: incorrect Type value")
    headings = re.findall(r"^## (.+)$", body, re.MULTILINE)
    check(len(headings) == len(set(headings)), f"{template}: duplicate section headings")
    for required_heading in ("Open questions", "Readiness checklist"):
        check(required_heading in headings, f"{template}: missing {required_heading}")

canvas = read(ROOT / "templates/lean-canvas.md")
research_playbook = read(ROOT / "workflow/LEAN-CANVAS-RESEARCH.md")
canvas_profile = parse_toml(ROOT / ".codex/agents/lean_canvas.toml")
check("workflow/LEAN-CANVAS-RESEARCH.md" in canvas_profile.get("developer_instructions", ""),
      "Lean Canvas specialist must load the research playbook")
check("workflow/LEAN-CANVAS-RESEARCH.md" in agents_doc,
      "Coordinator instructions must route Lean Canvas work through the research playbook")
for section in ("Research brief", "Evidence and sources", "Research coverage"):
    check(f"## {section}\n" in canvas, f"Canvas missing research section: {section}")
for section in ("Start from the idea", "Use research tools by default",
                "Research the decisions that matter", "Turn evidence into a finished starting model",
                "Completion and readiness"):
    check(f"## {section}\n" in research_playbook,
          f"Lean Canvas research playbook missing section: {section}")
for block in ("Problem", "Customer segments", "Unique value proposition", "Solution",
              "Channels", "Revenue streams", "Cost structure", "Key metrics", "Unfair advantage"):
    check(f"## {block}\n" in canvas, f"Canvas missing standard block: {block}")
roadmap = read(ROOT / "templates/product-roadmap.md")
for horizon in ("Now", "Next", "Later"):
    check(f"## {horizon}\n" in roadmap, f"Roadmap missing horizon: {horizon}")
for supporting in ("workflow/CONTRACT.md", "workflow/ORCHESTRATION.md",
                   "templates/product-index.md", "templates/handoff.md",
                   "examples/prompts.md", "examples/risk-routing.md",
                   "examples/claude-prompts.md"):
    read(ROOT / supporting)

# Check ordinary local Markdown links in kit documentation. Product placeholders
# and backticked illustrative paths are intentionally not treated as live links.
document_paths = [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "README.md"]
for folder in ("workflow", "templates", "examples"):
    document_paths.extend((ROOT / folder).glob("*.md"))
links_checked = 0
for path in document_paths:
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", read(path)):
        if "://" in target or target.startswith("#") or "<" in target:
            continue
        local = target.split("#", 1)[0]
        check((path.parent / local).exists(), f"Broken link in {path.name}: {target}")
        links_checked += 1

if errors:
    print("FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"PASS: {len(profiles)} Codex TOML profiles, {len(claude_profiles)} synchronized "
      "Claude Code profiles, 9 artifact templates, "
      f"2 coordination templates, {links_checked} local links.")
print("Static kit checks only; custom-agent loading and generated artifact quality "
      "are not evaluated.")
