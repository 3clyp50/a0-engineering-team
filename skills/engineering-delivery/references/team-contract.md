## Engineering team contract

Preserve the user's outcome and accepted constraints through replanning and delegation. Complete the authorized scope; do not substitute an easier behavior. Continue useful independent work when one path is blocked.

Before judging or changing a repository, read its applicable `AGENTS.md` chain and referenced deep DOX, including adjacent file contracts where present. Recheck callers, extension paths, persisted data, config, tests and runtime ownership. After a meaningful change, update the owning DOX and affected indexes as required. Keep private lessons out of tracked docs.

Use the `engineering-delivery` skill for coordinated engineering and `engineering-review` for independent review/proof. Apply relevant `frdel` criteria while planning; history is evidence, never permission or Jan's personal approval. Managers give workers pertinent case IDs, rationale, counterexamples and source references; reviewers check their relevance independently. Jan-authored Git evidence (J) and paraphrased maintainer-feedback lessons (L/D) are different sources. Runtime roles read deployed native skills. The versioned project agents/ and skills/ directories own the source; reinstall ordinary runtime copies after source changes. Host Codex copies and raw transcripts are unnecessary.

Prefer an existing owner and native lifecycle. Minimize the number of concepts a maintainer must hold, including hidden state and indirection, while preserving requested capability, extension seams, safety and upgrade behavior. Measure suspected bottlenecks; remove disproven speculative fixes.

Keep a minimal task record: outcome/acceptance, constraints/owners, decisions/evidence, status/remaining work, native context/job IDs. Workers own bounded writes. Reviewers and verifiers report directly to their manager without silently expanding or fixing scope. Managers adjudicate findings and own integration. Use roles proportionately.

Keep handoffs concise: save detailed outputs and full test matrices in task-owned evidence files. Return the verdict, actionable findings, exact artifact paths/revision or hashes, key observed checks, evidence references and material limits; do not paste the full history/report. The manager records current decisions, status, reusable IDs and evidence links rather than duplicating child reports. Retain rationale and source checks.

## Git delivery and instance boundaries

Every commit needs a meaningful subject and a description/body explaining the change and relevant validation. Separate them with a real blank line. Use a message file or structured argument, never literal backslash-n characters as line separators; inspect `git log -1 --format=%B` after committing. Commit/push authorization still comes from the user and repository contracts.

Use these staging branches for development: `agent-zero` → `ready`; `a0-launcher` → `development`; `a0-connector` → `development`. Their `main` branches are main/release branches, not development targets. Check the actual branch/worktree and dirty state before writes. Preserve unrelated work; select or create an isolated checkout on the required staging branch when needed. Do not replace this rule with a generic feature-branch default. This mapping does not prescribe a branch for other repositories.

The development/test target defaults to the hosting instance. Use an explicitly configured target exactly as defined; if it is invalid or unreachable, report the problem without silently falling back. Missing configuration does not block work. Record the hosting instance and selected write/test target: identity/URL, process or container, actual checkout and relevant binds, branch/revision and write scope. Verify the chosen runtime rather than assuming a branch/worktree selects an instance. For an explicitly different target, verify its actual backing paths and any shared writable mounts. Never select a neighboring instance merely because it exists.

Same-instance product writes/tests are permitted under normal task and repository authorization. When the selected target hosts active workers, account for reload/restart interruption. Checkpoint relevant task records and coordinate outstanding jobs through existing lifecycle mechanisms as needed; preserve enough evidence to resume. A task-owned pure helper process proves only its bounded behavior. Roles are guidance, not permissions or an OS sandbox.

Report observed behavior, assumptions and gaps separately. Passing unit tests, a responding URL or a tool receipt does not prove the changed user flow. Verify the intended checkout/container/payload and preserve data. A role does not grant new tool access or permission to install, commit, publish, change access or contact others.
