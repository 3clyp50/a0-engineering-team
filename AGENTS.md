# A0 Engineering Team DOX

## Purpose

Own the portable native Agent Zero team: six profiles, three skills, project metadata and installation checks.

## Ownership

- `agents/` and `skills/` are the versioned source. Deployed ordinary copies under an Agent Zero root's `usr/agents/` and `usr/skills/` are runtime artifacts; edit source, then reinstall and check.
- `.a0proj/project.json` and `.a0proj/instructions/operations.md` define the native project. Credentials, model overrides, runtime identities, chats and evidence stay local and ignored.
- `LICENSE` contains the MIT terms for this project.
- `scripts/install.py` copies only this team's files. `scripts/verify_native.py` checks native loading without model calls. `tests/` owns portable safety/format checks. `docs/verification.md` owns measured scope and limits.

## Local Contracts

Read the applicable AGENTS.md chain and referenced deep DOX before edits. Follow the shared contract in `skills/engineering-delivery/references/team-contract.md`; all profiles must retain native prompt inheritance and read that contract. Keep recorded Git evidence (J) separate from paraphrased feedback (L/D). Roles grant no new permissions or sandbox.

Every commit needs a meaningful title/subject AND description/body separated by actual newlines. Use a message file; inspect `git log -1 --format=%B`. Never use literal backslash-n characters as separators.

For product development, `agent-zero` uses `ready`; `a0-launcher` and `a0-connector` use `development`. Their `main` branches are main/release branches. Check branch/worktree and dirty state before writes; preserve unrelated work. This mapping does not impose a staging branch on this standalone repository.

The development/test target defaults to the hosting instance. Use an explicitly configured target exactly as defined; if it is invalid or unreachable, report the problem without silently falling back. Missing configuration is a usable same-instance default. Record the hosting instance, selected write/test target, actual checkout/binds, branch/revision and write scope. Same-instance product writes/tests follow normal task and repository authorization. When the selected target hosts active workers, account for reload/restart interruption: checkpoint and coordinate outstanding work using existing lifecycle mechanisms as needed. The ignored `runtime.local.md` holds local identities. Do not assign a neighboring instance by assumption.

Never publish personal paths, runtime/model settings, provider aliases, secrets, raw chats, private IDs or test receipts. No dependency installation, commit, push or publication permission is implied by a profile. The current owner's explicit authorization controls those actions.

## Work Guidance

Use one manager per complete outcome, even across repositories. Give workers bounded paths; independent reviewers/verifier report directly to the manager. Continue exact native context IDs for accepted corrections. No additional orchestration service, fixed role ceremony or model defaults.

Keep shared rules in the skill and concise role responsibilities in profiles. Update ownership docs and native project instructions when behavior changes. Installation must use ordinary files inside the selected Agent Zero `usr/` tree, never symlinks or a host-checkout dependency.

## Verification

Run `python3 -m unittest discover -s tests -v`. Install/check in a task-owned fixture before updating a live installation. Then use its framework runtime for `scripts/verify_native.py`; verify project discovery and instruction injection. Do not equate static loading with autonomous delivery. Audit the staged tree before publication, then verify the remote commit and its subject/body.

## Child DOX Index

No child DOX. The shared contract owns team behavior; `docs/verification.md` owns proof boundaries.
