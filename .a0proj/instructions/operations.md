# Project operations

The versioned `agents/` and `skills/` directories are the source of truth. Install ordinary copies into the selected Agent Zero `usr/` tree. All six profiles must read `engineering-delivery` → `references/team-contract.md`; managers also load `frdel` planning evidence before choosing an approach.

Every commit requires a meaningful subject/title and description/body separated by an actual blank line. Use a message file and verify `git log -1 --format=%B`; literal backslash-n characters are not separators.

Product staging branches: `agent-zero` → `ready`; `a0-launcher` → `development`; `a0-connector` → `development`. `main` is their main/release branch. Check the actual worktree/branch and preserve dirty work. Do not substitute a feature-branch default. No product branch is prescribed for this standalone repository.

The development/test target defaults to the hosting instance. Use an explicitly configured target exactly as defined; if it is invalid or unreachable, report the problem without silently falling back. Read the ignored root `runtime.local.md` when present. An absent explicit target means the current hosting instance is selected; an incomplete explicit target is a configuration problem to report. Record hosting and selected target identities, actual checkout/binds, branch/revision and allowed writes. Same-instance product writes/tests are permitted under normal task and repository authorization. If reload/restart would interrupt active workers on that target, checkpoint and coordinate work through existing lifecycle mechanisms as needed. Never repurpose an unassigned neighboring instance.

Keep runtime records, credentials, model settings, raw chats and detailed evidence out of Git. No role grants tool access or publication permission. Report only observed checks and explicit limitations.
