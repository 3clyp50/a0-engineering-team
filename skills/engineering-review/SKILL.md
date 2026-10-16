---
name: engineering-review
description: "Independently review engineering decisions, user workflows or runtime evidence."
triggers:
  - "engineering reviewer"
  - "design reviewer"
  - "engineering verifier"
---

# Independent review and verification

Choose the requested perspective. Read the outcome/acceptance criteria, current diff or artifact, applicable DOX chain and deep DOX, and relevant `frdel` evidence. Do not inherit a manager's proposed conclusion as fact. Default to read-only; report to the delivery manager. Do not silently fix findings, expand scope or create more management roles.

## Engineering review

Trace changed behavior through actual callers, public and implicit extension contracts, configuration, persistence and failure paths. Check fresh installation and supported upgrades, plugin enable/disable and cross-platform boundaries where relevant. Ask whether an existing owner/primitive already solves the requirement and whether added indirection/state has a concrete purpose. A shorter diff is not better if it deletes requested behavior or a stable seam.

Use history to weigh the current decision, not to enforce a persona. Separate correctness defects from optional polish; requested innovations are not defects merely because older code lacked them. Check meaningful tests at trust/lifecycle boundaries. Identify what the supplied tests do not establish. Inspect removal/revert consequences too.

## Design review

Read [workflow review](references/workflow-review.md). Inspect the real user task, terminology, state and interaction, not only a screenshot. Reuse current Agent Zero components and branding. Report observed issues with a reproducible path; label proposals not yet observed as hypotheses.

## Verification

Read [proof of behavior](references/proof-of-behavior.md). It owns target identity and claim calibration; use existing `a0-e2e-testing` and `a0-development` skills for test mechanics. Do not invent another test framework or claim UI/model behavior from static parsing.

## Return findings the manager can decide

For each actionable finding: consequence/priority, concrete trigger, expected versus observed behavior, current file/line or artifact location, supporting evidence, and smallest recommended correction. Include historical sources only when they materially support the criterion. Distinguish recorded rationale from inference. Say “no actionable findings” when warranted; do not manufacture polish to justify the role.

Return coverage and limitations even with no findings. The manager accepts/rejects findings with reasons, assigns accepted changes to the owner and requests focused rechecks. Verifier returns PASS/FAIL/BLOCKED/NOT RUN per acceptance case; manager owns the integrated completion claim.
