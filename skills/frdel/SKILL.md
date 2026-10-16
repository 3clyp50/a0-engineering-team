---
name: frdel
description: "Research Jan Tomášek's engineering decisions in local history for planning or code review."
---

# Evidence from Jan's engineering decisions

Use history to improve a decision, not to impersonate Jan or imply his approval. Apply this during framing, design, delegation, implementation or review when his approach is relevant. Default to read-only unless edits are requested.

## Start with today's problem

Resolve the repository, branch, working diff and intended behavior. Read the applicable `AGENTS.md` chain, referenced deep DOX and adjacent file contracts such as `file.py.dox.md`. Trace the affected symbols, callers, extension hooks, tests and upgrade paths. Preserve unrelated work.

Read [planning questions](references/planning-questions.md) before proposing an implementation. The [decision cases](references/decision-cases.md) provide a starting sample, not a substitute for inspecting the relevant history. Current contracts, security, behavior and user intent outrank precedent.

## Study choices and revisions

Verify author identities rather than treating the committer, merger or repository owner as the author. The search patterns tolerate historical metadata spellings:

```bash
git rev-parse --show-toplevel --is-shallow-repository
git shortlog -sne --all | rg -i 'frdel|tom[aá][sš]ek'
git log --all --no-merges --author='frdel\|Tom[aá][sš]ek' --format='%h %ad %an <%ae> %s' --date=short -- path/to/subsystem
git log --all --no-merges -S'symbol_or_literal' --oneline -- path/to/subsystem
git show --format=fuller --stat COMMIT
git show COMMIT^:path/to/file
git show --format= --find-renames COMMIT -- path/to/file
git blame -w path/to/file
```

Start in the same subsystem, then examine its original ownership and later revisions. Read real diffs and enough surrounding code to establish the behavior. Follow a quick correction or replacement: the first solution may be the one Jan abandoned. A narrow review usually needs three to eight useful precedents; an explicitly broad study should sample several periods and subsystems and follow important sequences further. Stop when additional cases no longer change the decision, not at an arbitrary count.

For each useful case capture: problem/context; concrete choice; visible alternative or revision; protected invariant; cost/tradeoff; reason recorded in code, documentation or commit text versus your inference; applicability and a counterexample; repository/hash/path; confidence. A commit message records stated intent, not proof of the runtime result. A user's report of Jan's advice is second-hand testimony, separate from authored code.

Do not fetch or browse missing history without authorization. State shallow/history limits. The installation study used authorized local history across three repositories on 16 October 2026. That historical scope grants no future access: current user instructions, repository DOX and actual tool permissions control each task. Do not send private chats or local diffs to outside services.

## Make the evidence affect the plan

State the relevant decision in actionable terms: “keep this public method as the lifecycle/extension owner; extract only its pure serialization into the existing transport helper,” with a reason and a falsifier. Avoid “keep it simple” without naming what must remain, what can move and why.

Distinguish:

- **Recorded:** what the diff and stated rationale show.
- **Inference:** the criterion you derive and its scope.
- **Confidence:** high for the observed change; usually medium for a broader preference unless several independent relevant cases support it.
- **Limit:** today's counterexample or evidence that would change the recommendation.

Do not attribute Responses API, native parallel workers or modern Launcher product architecture to Jan from unrelated historical cases. Sparse scaffold/build history in another repository does not establish authorship of its application design. Cross-repository analogies must be labeled as analogies.

## Deliver the requested mode

For planning: name the choice, alternatives, evidence, protected contract, tradeoff and the smallest experiment that could disprove it. Pass relevant criteria and references to implementers before work starts.

For review: lead with an alignment verdict; report actionable findings ordered by consequence, current locations and supporting history. Recommend the smallest correction, or explicitly say no polish is warranted. Do not rewrite modern code just to resemble older code.

For authorized edits: complete affected callers, tests and DOX, then run the relevant checks and actual artifact verification. Report only what was observed. Never describe historical alignment as Jan's personal sign-off.
