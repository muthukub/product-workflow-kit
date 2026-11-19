"""Validate the reusable agent kit without calling a model or writing files."""

from pathlib import Path
import argparse
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
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--embedded", action="store_true",
                    help="Validate in an application repo; allow extra agents and its own README")
EMBEDDED = parser.parse_args().embedded
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
if EMBEDDED:
    limit = settings.get("max_concurrent_threads_per_session")
    check(type(limit) is int and limit > 0,
          "Embedded configuration needs a positive subagent concurrency limit")
else:
    check(settings.get("max_concurrent_threads_per_session") == 3,
          "Expected three concurrent subagent slots")

all_profiles = list((ROOT / ".codex/agents").glob("*.toml"))
profile_names = {p.stem for p in all_profiles}
check(set(ROLES) <= profile_names if EMBEDDED else profile_names == set(ROLES),
      "Expected all nine SDLC specialist profiles" if EMBEDDED else "Expected exactly nine specialist profiles")
profiles = [p for p in all_profiles if p.stem in ROLES]
agents_doc = read(ROOT / "AGENTS.md")
readme = "" if EMBEDDED else read(ROOT / "README.md")
claude_doc = read(ROOT / "CLAUDE.md")
check("@AGENTS.md" in claude_doc, "CLAUDE.md must import shared AGENTS.md")
all_claude_profiles = list((ROOT / ".claude/agents").glob("*.md"))
claude_names = {p.stem for p in all_claude_profiles}
kit_claude_names = {role.replace("_", "-") for role in ROLES}
check(kit_claude_names <= claude_names if EMBEDDED else claude_names == kit_claude_names,
      "Expected all nine Claude SDLC profiles" if EMBEDDED else "Expected exactly nine Claude Code specialist profiles")
claude_profiles = [p for p in all_claude_profiles if p.stem in kit_claude_names]
for role in ROLES:
    check(f"`{role.replace('_', '-')}`" in claude_doc,
          f"{role}: missing Claude name mapping")
sync_script = ROOT / "scripts/sync-claude-agents.py"
if sync_script.is_file():
    sync_result = subprocess.run(
        [sys.executable, str(sync_script), "--check"] + (["--kit-only"] if EMBEDDED else []),
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
    check("Default new product artifacts to docs/." in instructions,
          f"{role}: default documentation artifact root missing")
    for required in ("AGENTS.md", "workflow/CONTRACT.md",
                     f"templates/{template}.md", "templates/handoff.md"):
        check(required in instructions, f"{role}: instructions must reference {required}")
        check((ROOT / required).is_file(), f"{role}: referenced file missing: {required}")
    check("Do not spawn further agents" in instructions, f"{role}: nesting rule missing")
    if role in {"lean_prd", "epic", "user_story", "enabler", "rfc", "adr", "risk_register"}:
        check("workflow/EARS.md" in instructions, f"{role}: EARS ownership/reference guidance missing")
        check("Semantic review:" in instructions,
              f"{role}: explicit semantic review responsibilities missing")
    check(f"`{role}`" in agents_doc and (EMBEDDED or f"`{role}`" in readme),
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
    if role in {"epic", "user_story", "enabler", "rfc", "adr"}:
        check("Requirement references" in headings, f"{template}: canonical requirement references missing")
    for match in re.finditer(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL):
        check(bool(match.group(2).strip()), f"{template}: empty section {match.group(1)}")

prd_template = read(ROOT / "templates/lean-prd.md")
for section in ("Behavioral requirements", "Requirement changes", "Semantic review"):
    check(f"## {section}\n" in prd_template, f"PRD missing {section}")
check("| Requirement ID | Pattern | EARS statement | Source / rationale | Verification | Risks |" in prd_template,
      "PRD canonical requirements schema mismatch")
check("| Criterion | Requirement | Given | When | Then |" in read(ROOT / "templates/user-story.md"),
      "Story scenarios must retain Given/When/Then and map requirements")
check("| Deliverable | Requirement | Observable acceptance criterion | Verification / evidence |"
      in read(ROOT / "templates/enabler.md"), "Enabler criteria must reference canonical requirements")
check("| Review area | Finding / counterexample | Requirement IDs / source | Disposition / next action |"
      in prd_template, "PRD semantic review record schema mismatch")
index_template = read(ROOT / "templates/product-index.md")
check("## EARS adoption and semantic review\n" in index_template,
      "Product index must record adoption scope and semantic review")
check("| Scope / PRD revision | Reviewer / method | Findings and disposition | Readiness blockers / next review |"
      in index_template, "Product index semantic review summary schema mismatch")
check("- Semantic review:" in read(ROOT / "templates/handoff.md"),
      "Handoff must return actual semantic findings or explicit non-applicability")
ears_guide = read(ROOT / "workflow/EARS.md")
for section in ("Adoption policy", "Semantic review protocol", "Measurement and gradual adoption"):
    check(f"## {section}\n" in ears_guide, f"EARS guide missing {section}")

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
                   "examples/claude-prompts.md", "USER-MANUAL.md", "workflow/EARS.md",
                   "examples/ears-pilot.md", "scripts/validate-requirements.py",
                   "tests/test_requirements.py", "workflow/IN-REPOSITORY.md"):
    read(ROOT / supporting)

# Check ordinary local Markdown links in kit documentation. Product placeholders
# and backticked illustrative paths are intentionally not treated as live links.
document_paths = [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "USER-MANUAL.md"]
if not EMBEDDED:
    document_paths.append(ROOT / "README.md")
for folder in ("workflow", "templates", "examples"):
    document_paths.extend((ROOT / folder).glob("*.md"))
links_checked = 0
for path in document_paths:
    # Example links inside fenced/inline code describe future product paths.
    live_text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", read(path))
    live_text = re.sub(r"`[^`\n]+`", "", live_text)
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", live_text):
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
