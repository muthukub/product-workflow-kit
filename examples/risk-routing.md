# Illustrative routing example

This is fictional guidance, not product evidence or an accepted decision. IDs illustrate references that would be allocated in one product workspace.

## Business/user route

PRD-001 describes a self-service onboarding outcome. It identifies the uncertainty that new users may abandon the setup because the terminology is unfamiliar, preventing activation. The register assigns RISK-001, category user.

US-001 directly addresses the risk: as a new user, I want to complete setup with understandable guidance so I can reach my first useful result. Its criteria describe visible guidance and successful setup. Its validation section specifies the hypothesis, a proposed usability session with target users, a justified sample, a measurable completion threshold and time window, and the product decision if the threshold is missed. The threshold is a test hypothesis until measured.

RISK-001 links US-001; US-001 links RISK-001. The risk remains open/mitigating while evaluation is pending. Passing a software test for the guidance does not by itself establish that users understand it.

## Technical route

The same PRD identifies uncertainty about whether concurrent requests can create duplicate setup records. The register assigns RISK-002, category technical.

RFC-001 evaluates database uniqueness, idempotency keys, and other viable approaches against the actual constraints. EN-001 is a timeboxed spike with a defined concurrency experiment and observable exit criterion; it supports RFC-001. After an authorized choice, ADR-001 can record the decision and its consequences. Implementation work then follows the accepted decision.

RISK-002 links RFC-001 or ADR-001, and each destination links RISK-002. EN-001 alone would leave the required route incomplete. Choosing an approach does not prove duplicate creation has been prevented; the risk's closure evidence must show the chosen criterion is met under the relevant conditions.
