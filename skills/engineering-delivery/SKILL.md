---
name: engineering-delivery
description: "Deliver engineering changes across repos with DOX, clear ownership and runtime evidence."
triggers:
  - "engineering team"
  - "delivery manager"
  - "chief of staff"
---

# Engineering delivery

Use for framing, coordinating or completing an engineering initiative. It supports one complete change across repositories, not one manager per repository or layer. Small work can stay in one conversation; independent implementation or review gets a bounded native subordinate when useful.

## Know the intent before delegating

Keep the user's outcome, acceptance criteria, constraints and priority changes visible. Read [team contract](references/team-contract.md) once per working context and the relevant [maintainer-feedback lessons](references/chat-lessons.md). Read selectively by case/lesson ID; reread when context is missing or guidance changes. Chief and manager consult `frdel` and its planning questions before choosing an approach; workers receive relevant criteria and source references. This is decision support, not veto power for historical style.

For every affected repository, discover its root, current branch/diff, applicable `AGENTS.md` chain and deep DOX. In Agent Zero, adjacent `*.py.dox.md` files describe helper/tool behavior. Follow actual indexes and referenced contracts in each repository; do not assume every repo uses the same file-level format. Read callers, extension hooks, config, tests and installation paths before deciding what can move. Current DOX is authoritative; do not freeze its detailed rules into this skill.

Record the choice and its cost: existing owner/primitive reused, alternative rejected and why, protected behavior, uncertainties and the check that can disprove the hypothesis. New structure needs a concrete obligation; simplicity never excuses omitted requested behavior or broken compatibility.

## Execution boundaries

This workflow runs through Agent Zero's native tools, contexts and jobs. Skills and profiles are ordinary installed files under `/a0/usr/`; no Codex app, host transcript, external symlink or hidden host operator is required. A connector may provide authorized host-repository access; a role itself grants no capability. Discover the actual accessible checkout and read/write mode before assigning host work. A blocked host probe does not block independent server work.

Follow the commit-message, staging-branch and separate-instance requirements in the shared team contract. Record the actual controller and a different development/test target instance, including their backing checkouts/binds, before product work. A branch/worktree alone is insufficient. If the target is **not configured**, product writes/tests/restarts are blocked. Task-owned packaging and pure helper fixtures remain bounded activities, not proof of full instance separation. No fleet service is required.

## Roles and handoffs

| Profile ID | Accountability |
| --- | --- |
| `chief-of-staff` | User intent, priority and outcomes across independent initiatives. |
| `delivery-manager` | One complete change, including cross-repository integration. |
| `engineering-worker` | Bounded implementation or investigation with named write ownership. |
| `engineering-reviewer` | Independent correctness, contracts and development decisions. |
| `design-reviewer` | Independent workflow, language, components, accessibility and truthful state. |
| `engineering-verifier` | Independent behavior proof in the intended artifact/runtime. |

Reviewers and verifier report to the delivery manager; they do not silently edit findings. The manager adjudicates, returns accepted findings to the responsible worker and requests a focused recheck. Chief receives integrated outcomes from managers. Do not add middle managers by default or create a fixed six-agent ceremony for tiny edits.

Read [native delegation](references/native-delegation.md) for the actual continuation and parallel APIs and a minimal task record. Give independent workers disjoint write scopes. Shared contracts, dependent edits, settings changes and integration are sequenced. Keep existing native context IDs and job handles; do not build a queue, registry, daemon or orchestration service.

## Finish the whole change

1. Establish a reproducible defect or observable target behavior. Test uncertain assumptions before a broad edit.
2. Implement within ownership boundaries, covering callers, config, migrations, tests and DOX affected by the change. When removing/reverting something, trace its indirect consumers and persisted data too.
3. Request independent review proportional to consequence. Use `engineering-review` for correctness/design/verification, and existing `a0-development`, plugin authoring and `a0-e2e-testing` skills for their native procedures.
4. Verify the exact changed runtime/artifact and actual user flow. Distinguish automated checks, UI observation and model-driven behavior; none silently stands in for another. Preserve user data and restore task-owned temporary settings.
5. Close with outcome, meaningful decisions, evidence, remaining work and risk. A blocked model call is blocked, not a pass. Continue authorized work autonomously; approval is needed only for an actual permission boundary, not routine reversible steps.

No permission to install, commit, push, publish, send external messages or change access is implied by a role. Read each repository's permissions and the user's existing authorization. Do not expose secrets or raw chat history in task records or tracked DOX.

## Using the team

Choose **Chief of Staff** for several initiatives, or **Delivery Manager** for one outcome. A manager may start multiple independent worker/reviewer conversations using the same reusable profiles. Selecting a profile in a fresh chat or subordinate spawn loads its role; existing unrelated chats/settings are not migrated. Non-default child scoped presets win over a parent chat override; only Default children may inherit it. Record the effective preset/provider/model for important children without changing user defaults. No model/provider is prescribed here.
