# Project operations

The versioned `agents/` and `skills/` directories are the source of truth. Install ordinary copies into the selected Agent Zero `usr/` tree. All six profiles must read `engineering-delivery` → `references/team-contract.md`; managers also load `frdel` planning evidence before choosing an approach.

Every commit requires a meaningful subject/title and description/body separated by an actual blank line. Use a message file and verify `git log -1 --format=%B`; literal backslash-n characters are not separators.

Product staging branches: `agent-zero` → `ready`; `a0-launcher` → `development`; `a0-connector` → `development`. `main` is their main/release branch. Check the actual worktree/branch and preserve dirty work. Do not substitute a feature-branch default. No product branch is prescribed for this standalone repository.

Development/test target instance: **not configured** by default. Read the ignored root `runtime.local.md` for locally configured identities; if absent or incomplete, the target remains not configured. Record controller and a DIFFERENT actual development/test INSTANCE, both backing checkouts/binds and separation proof before product writes/tests/restarts. A branch/worktree/process alone is not sufficient; target changes/restarts must leave the controller and workers stable. Never reuse an unassigned neighboring instance. Product work is blocked until that boundary is verified; independent planning and task-owned packaging may continue.

Keep runtime records, credentials, model settings, raw chats and detailed evidence out of Git. No role grants tool access or publication permission. Report only observed checks and explicit limitations.
