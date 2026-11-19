"""Read-only structural and reference audit for adopted EARS PRD tables."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


HEADERS = ["Requirement ID", "Pattern", "EARS statement", "Source / rationale", "Verification", "Risks"]
REQ = r"PRD-\d{3,}-R\d{2,}"
LINK = re.compile(r"\[(" + REQ + r")\]\(([^)\n]+)\)")
SHAPES = {
    "ubiquitous": r"^The\s+.+?\s+shall\s+\S.+",
    "event-driven": r"^When\s+.+,\s+the\s+.+?\s+shall\s+\S.+",
    "state-driven": r"^While\s+.+,\s+the\s+.+?\s+shall\s+\S.+",
    "unwanted-behavior": r"^If\s+.+,\s+then\s+the\s+.+?\s+shall\s+\S.+",
    "optional-feature": r"^Where\s+.+,\s+the\s+.+?\s+shall\s+\S.+",
}


def prose(text):
    """Omit fenced examples so they do not become active requirements."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines)


def section(text, name):
    match = re.search(r"^## " + re.escape(name) + r"[ \t]*\n(.*?)(?=^## |\Z)",
                      text, re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def field(text, name):
    header = text.split("\n## ", 1)[0]
    match = re.search(r"^\|\s*" + re.escape(name) + r"\s*\|\s*([^|]+)\|", header, re.MULTILINE)
    return match.group(1).strip().strip("`") if match else ""


def cells(line):
    return [cell.strip().replace(r"\|", "|")
            for cell in re.split(r"(?<!\\)\|", line.strip()[1:-1])]


def tables(text):
    result, current = [], []
    for line in (text + "\n\n").splitlines():
        if line.strip().startswith("|") and line.strip().endswith("|"):
            current.append(cells(line))
        elif current:
            if len(current) >= 2:
                valid_separator = all(re.fullmatch(r":?-{3,}:?", item) for item in current[1])
                if valid_separator and len(current[0]) == len(current[1]):
                    result.append((current[0], current[2:]))
                else:
                    result.append((current[0] + ["INVALID TABLE DELIMITER"], current[1:]))
            current = []
    return result


def justified_none(text):
    match = re.search(r"^None[ \t]*-[ \t]*(\S[^\n]*)", text, re.MULTILINE | re.IGNORECASE)
    return bool(match and not re.search(r"<[^>]+>", match.group(1)))


def pattern_matches(pattern, statement):
    if pattern == "complex":
        clauses = re.findall(r"(?:^|,\s*)(where|while|when|if)\b", statement, re.IGNORECASE)
        return (len(clauses) >= 2
                and bool(re.search(r",\s*(?:then\s+)?the\s+.+?\s+shall\s+\S.+", statement, re.IGNORECASE)))
    return pattern in SHAPES and bool(re.fullmatch(SHAPES[pattern], statement, re.IGNORECASE))


def audit(product_root):
    root = Path(product_root).resolve()
    result = {"errors": [], "skipped": [], "adopted": 0, "requirements": 0, "references": 0}
    errors = result["errors"]
    if not root.is_dir():
        errors.append(f"Product directory does not exist: {root}")
        return result
    prd_rows, adopted_paths, documents = {}, set(), {}

    def load(path):
        if not path.resolve().is_relative_to(root):
            errors.append(f"File resolves outside product root: {path.name}")
            return None
        return prose(path.read_text(encoding="utf-8-sig"))

    for path in sorted((root / "prds").glob("*.md")):
        text = load(path)
        if text is None:
            continue
        documents[path.resolve()] = text
        if field(text, "Status") == "superseded":
            result["skipped"].append(f"{path.name}: superseded history")
            continue
        body = section(text, "Behavioral requirements")
        if body is None:
            result["skipped"].append(f"{path.name}: legacy PRD without EARS section")
            continue
        result["adopted"] += 1
        adopted_paths.add(path.resolve())
        prd_id = field(text, "ID")
        if not re.fullmatch(r"PRD-\d{3,}", prd_id):
            errors.append(f"{path.name}: missing or invalid parent PRD ID")
        matching = [rows for header, rows in tables(body) if header == HEADERS]
        if not matching:
            if not justified_none(body):
                errors.append(f"{path.name}: missing canonical table or justified None")
            continue
        if len(matching) != 1:
            errors.append(f"{path.name}: use exactly one canonical requirement table")
        rows = [row for group in matching for row in group]
        if not rows and not justified_none(body):
            errors.append(f"{path.name}: empty table needs a justified None")
        seen_statements = set()
        retired = set()
        for header, changes in tables(section(text, "Requirement changes") or ""):
            if header == ["Requirement ID", "Change / rationale", "Replacement ID"]:
                retired.update(row[0] for row in changes if row)
        for row in rows:
            if len(row) != len(HEADERS) or not all(row):
                errors.append(f"{path.name}: requirement row must have six nonempty fields")
                continue
            req_id, pattern, statement, source, verification, risks = row
            if not re.fullmatch(re.escape(prd_id) + r"-R\d{2,}", req_id):
                errors.append(f"{path.name}: invalid or wrong-parent requirement ID {req_id}")
                continue
            if req_id in prd_rows:
                errors.append(f"{path.name}: duplicate requirement ID {req_id}")
            if req_id in retired:
                errors.append(f"{path.name}: retired requirement ID reused: {req_id}")
            if not pattern_matches(pattern, statement):
                errors.append(f"{req_id}: statement does not match supported {pattern!r} shape")
            if re.search(r"<[^>]+>|\bTBD\b", " ".join(row)):
                errors.append(f"{req_id}: unresolved placeholder/TBD; keep it a visible draft blocker")
            normalized = " ".join(statement.casefold().split())
            if normalized in seen_statements:
                errors.append(f"{req_id}: exact duplicate statement in this PRD")
            seen_statements.add(normalized)
            prd_rows[req_id] = path.resolve()
            result["requirements"] += 1

    if not result["adopted"]:
        errors.append("No active PRD has adopted Behavioral requirements; no EARS requirements checked")

    def validate_links(path, text):
        matches = list(LINK.finditer(text))
        for match in matches:
            req_id, destination = match.groups()
            result["references"] += 1
            parts = urlsplit(destination)
            target = (path.parent / unquote(parts.path)).resolve()
            if parts.scheme or parts.netloc or parts.query or not target.is_relative_to(root):
                errors.append(f"{path.name}: {req_id} must link to a PRD inside the product root")
            elif req_id not in prd_rows or target != prd_rows[req_id]:
                errors.append(f"{path.name}: missing, retired or wrong-destination requirement {req_id}")
            elif parts.fragment != "behavioral-requirements":
                errors.append(f"{path.name}: {req_id} link must target #behavioral-requirements")
        return {match.group(1) for match in matches}

    for folder in ("epics", "stories", "enablers", "rfcs", "adrs", "risks"):
        for path in sorted((root / folder).glob("*.md")):
            text = load(path)
            if text is None or field(text, "Status") == "superseded":
                continue
            all_refs = validate_links(path, text)
            if folder == "risks":
                continue  # Requirement links support, but never replace, risk routing.
            body = section(text, "Requirement references")
            if body is None:
                parents = field(text, "Parents")
                has_adopted_parent = any(field(documents[p], "ID") in parents for p in adopted_paths)
                if all_refs or has_adopted_parent:
                    errors.append(f"{path.name}: adopted scope needs Requirement references")
                continue
            declared = {m.group(1) for m in LINK.finditer(body)}
            raw_ids = set(re.findall(REQ, body))
            if raw_ids - declared:
                errors.append(f"{path.name}: bare requirement IDs need canonical Markdown links")
            if not declared and not justified_none(body):
                errors.append(f"{path.name}: declare requirement links or a justified None")
            if all_refs - declared:
                errors.append(f"{path.name}: criterion/body links were not declared in Requirement references")
            for header, rows in tables(text):
                if "Requirement" not in header:
                    continue
                column = header.index("Requirement")
                for row in rows:
                    if len(row) != len(header):
                        errors.append(f"{path.name}: malformed criterion table row or delimiter")
                        continue
                    value = row[column] if len(row) > column else ""
                    ids = set(re.findall(REQ, value))
                    links = {m.group(1) for m in LINK.finditer(value)}
                    if not value or ids != links or (not links and not justified_none(value)):
                        errors.append(f"{path.name}: criterion Requirement needs links or a justified None")

    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product_root", type=Path, help="Product directory containing prds/ and related artifacts")
    args = parser.parse_args()
    try:
        result = audit(args.product_root)
    except (OSError, ValueError) as exc:
        print(f"FAILED: {exc}")
        return 1
    for skipped in result["skipped"]:
        print(f"SKIP: {skipped}")
    for error in result["errors"]:
        print(f"ERROR: {error}")
    label = "FAILED" if result["errors"] else "PASS"
    print(f"{label}: {result['adopted']} adopted PRDs, {result['requirements']} active requirements, "
          f"{result['references']} requirement links checked.")
    print("Static plausibility and reference checks only; no semantic proof, completeness review, "
          "readiness/approval decision, or product pilot is performed.")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
