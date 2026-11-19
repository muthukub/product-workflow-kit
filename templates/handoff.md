# Specialist handoff

- Agent: <custom agent name>
- Artifact: <ID and path>
- Status: <document status; distinguish readiness from approval>
- Inputs used: <source IDs, sections, and revisions>
- Summary: <what was produced or changed>
- Validation: <template, links, scope, measurable criteria; actual checks only>
- Risk candidates or updates: <category, cause/event/impact, proposed route, or none>
- Risk routing coverage: <risk ID -> destination ID; pending explicitly>
- Requirement coverage / change requests: <canonical PRD requirement links, scenario/verification coverage, missing rules or justified non-applicability; follow workflow/EARS.md>
- Semantic review: <reviewed input/current revisions and scope, role/method, actual counterexamples/findings and disposition, or Not reviewed/justified None; separate planned verification from evidence and flag readiness blockers>
- Assumptions and blockers: <unknowns, consequence, needed evidence>
- Downstream tasks: <agent, requested action, dependencies>

Return this in the subagent response. It is not a separate product artifact unless requested.
