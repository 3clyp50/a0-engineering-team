# Native delegation and the task record

Verified against `/a0/tools/call_subordinate.py(.dox.md)`, `/a0/tools/parallel.py(.dox.md)` and `/a0/helpers/parallel_tools.py(.dox.md)` on 16 October 2026. Read the currently exposed tool schema before invoking; the runtime can evolve or policy can hide a tool. These examples do not grant tool access.

## Brief and record

For a small direct change, structured notes in the owning conversation suffice. As soon as a child may be continued, or work spans review cycles or multiple workers, create one task-owned file in the existing workdir or project temporary area and pass its exact path. Avoid an additional ledger/database system. One writer (normally manager) owns the shared record; children return evidence and proposed updates. Do not make parallel writers append to it.

```text
Outcome and observable acceptance:
Scope and repositories:
Controller/hosting instance identity, URL, process/container, backing checkout/binds:
Selected development/test target: explicit configured target, otherwise current hosting instance:
Selected target identity and actual backing checkout/binds; explicit-target validation:
Reload/restart consequences for active workers; checkpoint/coordination and resumption:
Write checkout/workdir, required staging branch, revision, dirty state, allowed paths:
Verification runtime/process and artifact revision/hash:
Commit authorization, subject/body and real-newline check when applicable:
Isolation rationale; cleanup/recovery owner:
Constraints, permissions, protected contracts, non-goals:
Owners and allowed write paths:
Current DOX/deep-DOX and relevant decision evidence:
Decision, alternative, tradeoff, falsifying check:
Status / remaining work / blocker:
Evidence (command or user action -> observed result -> location):
Child context IDs / outstanding parallel job IDs / actual scoped and effective models:
```

A worker brief adds a concrete responsibility, acceptance criteria, read/write boundaries and return format. A reviewer gets the user's outcome, exact changed paths and path-filtered diff/artifact revision or hash; give relevant references without telling them the finding they should produce. Keep independent judgment. A verifier gets reproducible acceptance checks and target identity, not a demanded PASS.

## Create and continue

`call_subordinate` accepts `message`, optional `profile`, `name`, `reset`, `context_id` and attachments. Exact profile directory IDs are used, not titles.

```json
{"tool_name":"call_subordinate","tool_args":{"profile":"engineering-worker","name":"Investigate selector persistence","reset":true,"message":"Read-only investigation. Goal: explain selector persistence in the named target. Read current DOX and the supplied task record. No code/settings/git mutations. Return the traced owner, evidence and remaining uncertainty."}}
```

Fresh calls create persisted child contexts at the next agent number: A0 → A1 → A2. The result's **context_id** is the reusable child identity. Save it. Continue that exact child with `reset:false` and `context_id`; do not accidentally continue whichever child happens to occupy the default slot. Use `reset:true` for a new independent task or different profile. Never continue a still-running child concurrently. A child belongs to its own parent; a reviewer cannot impersonate a sibling's parent to continue it.

```json
{"tool_name":"call_subordinate","tool_args":{"context_id":"RETURNED_CHILD_ID","reset":false,"message":"Recheck the accepted finding after the owner's change; report only the changed result and evidence."}}
```

Children inherit the project. Scoped non-default model presets retain their configuration; default children may inherit the caller's chat override. Do not hardcode a model or write model dictionaries into `agent.yaml`. Read current `tools/call_subordinate.py.dox.md` for lifecycle/stop details.

## Independent work

Use `parallel` only when the calls are independent and the exposed runtime supports it. Its `tool_calls` entries use ordinary `tool_name`/`tool_args`. `wait:false` starts background work; collect/await using returned **job_ids**. A job ID identifies an invocation, while its child context ID identifies the reusable agent. Keep both durably when needed. Disjoint paths still share imports and test inputs: finish dependent writes before integration checks, and isolate checkouts when parallel writers cannot avoid interference.

```json
{"tool_name":"parallel","tool_args":{"tool_calls":[{"tool_name":"call_subordinate","tool_args":{"profile":"engineering-reviewer","reset":true,"message":"Independently review the specified diff, outcome and contracts. Read-only. Return actionable findings with evidence or no findings."}},{"tool_name":"call_subordinate","tool_args":{"profile":"design-reviewer","reset":true,"message":"Independently inspect the specified workflow and artifact against acceptance criteria. Read-only. Return observed usability/state issues and limitations."}}],"wait":true}}
```

Use only the actual findings to decide follow-up. Do not wrap `response` in parallel, recursively wrap parallel calls, run shared-settings mutations together, or split a dependent chain into a batch. Numbered child agents can use their own native delegation where genuinely needed. Outstanding jobs must be collected or intentionally cancelled before claiming completion. Reviewers return directly to their caller (the manager), not through a worker.
