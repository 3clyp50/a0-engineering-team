# Lessons from engineering feedback

## Evidence limits

These are paraphrased lessons from maintainer feedback during engineering work. Private conversations, identifiers, excerpts and audit statistics are deliberately excluded. They are contextual observations, not independently reproducible public evidence or Jan-authored rationale. Both successes and mistakes inform them. Current instructions and DOX outrank precedent; rank by user consequence rather than repetition.

## L1: Preserve user state and behavioral ownership

A smaller refactor can still remove a public extension seam. Before extraction or removal, trace explicit callers, decorators, namespace identities, plugin disable paths and old persisted state. Keep the real lifecycle owner. Passing tests and fewer lines do not establish compatibility.

## L2: Make claims and attribution auditable

Check who authored a change, what the source proves and what remains inference. Scaffold or build commits do not establish application authorship. Distinguish direct code evidence from second-hand feedback and do not claim tests that were not run.

## L3: Exercise the intended artifact and flow

Compatibility checks can pass while create/edit or save/reopen behavior fails. Identify the actual checkout/runtime and perform the requested user action. Keep static, automated, UI-observed and model-driven evidence separate.

## L4: Support existing installations

A repository update cannot add a port to an old image or upgrade a durable executable by itself. Cover fresh installs and supported upgrades, preserve old data and report platform limits honestly.

## L5: Measure the suspected owner

Separate costs before adding flags, locks or retries. Remove disproven fixes. Verify stale-result ownership across overlapping operations and chat switches. A welcomed speed improvement can coexist with an untested regression; use comparable measurements before claiming a multiplier.

## L6: Reuse shared primitives and preserve domain policy

Existing model presets and modal primitives can avoid duplicate editors and inconsistent behavior. Keep domain-specific decisions with the actual feature owner. Useful generalization and requested innovation still deserve implementation when an existing primitive does not cover the requirement.

## L7: Recheck original behavior before a new mechanism

Before inventing repeatability declarations or dispatch policy, inspect the behavior that regressed. Public commentary and canonical tool calls may both belong in repeat comparison; private reasoning and unique response IDs do not. Name the tradeoff and falsifying check. Proportional effort does not excuse missing acceptance or safety obligations.

## L8: Complete the consequences of a change

A successful refactor may still need blank/empty states, runtime assets, callers, tests, prompts and ownership docs. Track the original obligations through review and removal. Store private research outside public product contracts.

## Design lessons

- **D1: Familiar workflow.** Reuse current components, official assets and vocabulary. Check actual controls, focus and recovery; visual likeness is only one part of a working flow.
- **D2: Honest state.** Selected, inherited, effective, installed, available and running values differ. Verify persistence through reload and context switches. Show measured progress or honest indeterminate state.
- **D3: Clear first use.** Setup should expose useful choices without requiring users to understand internal services. Preserve privilege, consent and instance ownership instead of adding a competing permission system.
- **D4: Real capability boundaries.** Avoid migration interruptions for unused features. Check terminal or runtime capability directly rather than inferring it from a shell or platform label. Preserve a normal no-feature path and do not substitute a rejected fallback.

## Inspiration boundary

Coordination questions also drew on a prior pstack review. No external skill text, command framework, Cursor API or orchestration engine was imported. Use native Agent Zero contexts, jobs and tools with proportionate roles.
