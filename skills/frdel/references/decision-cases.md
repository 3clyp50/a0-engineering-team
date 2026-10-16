# Decision study, 16 October 2026

## Scope and evidence limits

All source inspection was local, with no fetch. The three clones report non-shallow history; that establishes local completeness relative to their fetched refs, not completeness of Jan's work everywhere. Author identity was checked through `git shortlog` and full commit metadata: `frdel` / `Jan Tomášek`, including his GitHub noreply and later personal-email identity. Email addresses are intentionally omitted here. Merge authorship does not establish authorship of the merged code.

The local non-merge author query returned 750 Agent Zero commits (June 2024–July 2026), 17 Launcher commits (November–December 2025), and one Connector initial commit. These counts describe the research boundary, not a quality score. The study inspected the actual diffs and relevant surrounding code of the cases below; it is a curated decision sample, not an audit of all 750 commits. “Recorded” refers to explicit commit text, code or docs; broader decision criteria are labeled inference. No historical runtime was executed.

Each reference is `repository @ commit : path`; use `git show COMMIT:path` even when the path has since moved. Agent Zero's clone is `/a0` in the live instance. Sibling repositories must be accessed through an authorized host connection or independently discovered checkout; their host paths are not assumed to exist in Docker.

## Observed evolution, within this sample

In 2024, context separation and prompt fallback turned shared assumptions into explicit per-chat ownership and layered specialization (J8/J2). In 2025, the subordinate fix moved from copying configuration to using its initialization owner (J3). March 2026 examples refine plugin namespaces, shared loader ownership, optional dependency readiness and the image/repository boundary (J1/J5/J6/J9). July's startup work adds substantial delivery machinery, then narrows its discovery around actual entry points (J7). This supports adapting structure to a demonstrated lifetime, consumer or delivery obligation—not a claim that Jan steadily prefers more abstraction or always deletes it. The queue removal and new bundler are deliberate counterexamples to either universal story. The practical question is which present obligation earns the structure and which existing contract it must preserve.

## J1 — Preserve and identify extension ownership

**Context/choice.** `agent-zero @ 7e1d9ad2a4a3d186e337a89433ccc5128bdc754d` changes `helpers/extension.py` from flattened module/qualname names to `_functions/<module>/<qualname>/{start|end}`, migrates shipped hook files, and adds startup-migration extension dispatch in `helpers/migration.py`. The accompanying `docs/developer/extensions.md` explicitly says deep paths avoid collisions. Mutable input/result/exception hooks remain part of the decorator contract.

**Decision/tradeoff.** Recorded reason: unique namespace identity. Inference (medium, framework scope): make extension ownership explicit even at the cost of deeper directories and a coordinated migration. Moving a decorated method changes an externally discoverable path; extracting code is not merely internal cleanup. **Counterexample:** this precedent does not require decorating every helper or retaining accidental internals. Today's DOX and real extension users decide what is public. Observation confidence: high.

## J2 — Layer specialization rather than copy the framework

`agent-zero @ 7df19619ac30f82d1339872536f48aa165bba9aa : python/helpers/files.py` adds ordered fallback directories for prompt lookup and recursive includes; the previous path had a single source. Missing files still raise a meaningful error. Recorded subject: “UI improvements, prompt inheritance.” Inference (medium): specialize at the existing resolution boundary rather than fork the full system prompt. Tradeoff: precedence and include resolution become contracts and need validation. Counterexample: this old implementation is not today's API; current `helpers/files.py.dox.md`, profile discovery and include restrictions govern. It does not authorize arbitrary absolute includes. Observation: high.

## J3 — Reconsider the first fix when the native initializer is the real owner

`agent-zero @ fac49e854bfe5736e945f7be08f6dd36b6af94ea : python/tools/call_subordinate.py` deep-copies the parent's configuration to fix sharing. Nine minutes later `d5fc0a32e79891b634cdb105c33a20def2ed45bb` replaces that copy with `initialize_agent()`, applies an explicit profile before creation and removes later mutation of an existing child profile.

Recorded: a config-copy bug and the two actual revisions. Inference (medium): prefer independently resolved native configuration when a new agent lifecycle begins; copying mutable state is a repair, not necessarily the right ownership model. Cost: reinitialization resolves current defaults instead of blindly inheriting every parent value. Counterexample: current subordinate code deliberately preserves selected chat overrides and scoped presets; the 2025 change must not erase modern inheritance requirements. Observation: high.

## J4 — Remove a queue only after isolation exists

`agent-zero @ 1eb78607c9adaa36db929dda11e5f1359d02714e : plugins/_plugin_scan/webui/plugin-scan-store.js`, `api/plugin_scan_queue.py` and README remove `_queue`, `_running`, queued state and the next-job drain. Each run already creates a fresh context; runs now start immediately. Validation, failure toasts, generation checks and bounded polling remain. The commit explicitly describes independent temporary chat contexts as the reason parallel scans are possible.

Inference (medium): let independent native contexts own their work rather than overlay a serialization mechanism with no shared-state requirement. Tradeoff: concurrency/resource pressure increases. Counterexample: dependent writes, scarce external resources and rate limits can justify serialization. This change is evidence about plugin scans; it does not establish authorship of today's native `parallel` tool. Observation: high.

## J5 — Use native Git while retaining recovery; respect durable/image boundaries

`agent-zero @ eafe51a688c02aea277a4f244a1fe61965f0b614 : docker/run/fs/exe/self_update_manager.py` replaces custom recursive file synchronization/protected-path machinery with Git checkout/fetch/stash operations. Added code protects tracked and nonignored untracked changes, restores branch/detached state, leaves ignored data in place and retains the stash if restoration fails. Recorded rationale: native Git and rollback protection. Inference (medium): deleting custom mechanics is worthwhile only when their preservation obligations are covered; the replacement actually adds recovery structure.

Two days later `e0dae52b7fa20601c3d59b940fae8aae2b94d662 : helpers/self_update.py` removes copying repository updater files into the durable `/exe` runtime. It inspects the durable manager first for `latest` support, falls back to the repo copy only when needed, hides unsupported choices and rejects unsupported requests. Tests explicitly cover old durable/new repository combinations. Tradeoff: some users need a concrete version or new image rather than being promised a capability they lack.

Counterexamples: source-text capability inspection was this narrow solution, not a universal protocol. Current rollback DOX now requires immutable stash object IDs; do not copy the old reflog-selector implementation. Do not execute update/cleanup operations just to study history. Observations: high; broader preference: medium.

## J6 — Extract proven shared mechanics without breaking imports

`agent-zero @ 89d4b8913f400d92ac00e4d143c17d3e76ad9f25 : helpers/modules.py`, `helpers/extract_tools.py`, `helpers/api.py`, `helpers/extension.py`, `helpers/files.py`, `helpers/plugins.py`, `helpers/ws.py` moves module/class loading to a cohesive owner and updates actual callers. `extract_tools.py` retains imports explicitly marked “for backwards compatibility.” Plugin module refresh gains namespace purging rather than requiring a whole-process reload for every change.

Recorded: shared loader consolidation and compatibility export. Inference (medium): extraction is justified by real cross-module responsibility; compatibility shims can be appropriate when they protect existing consumers. Tradeoff: one additional module and a temporary old import surface. Counterexample: a one-use helper does not earn a new abstraction from this precedent; obsolete exports may be removed only with current consumer/compatibility evidence. Observation: high.

## J7 — Add substantial structure when delivery requires it, then narrow its scope

`agent-zero @ 0329003b659bd6d51c64745c3d2a72f668cae641 : helpers/ui_bundler.py`, `helpers/ui_server.py`, `webui/sw.js`, `webui/index.html`, tests and file DOX adds recursive text-asset collection, versioned bundles, authenticated delivery, gzip/ETag handling, a service worker and extension readiness. The code bounds eligible content, constrains asset roots/symlink escapes, excludes external URLs and versions caches. The commit explains the delivery flow; it does not contain a measured speedup, so none is claimed here.

`bebe6826cf8a654d1423a9aa0f1c118116a3bc0e` the next day changes discovery from broad component/plugin scanning to caller-supplied entry sets plus actual runtime-injected extension entries, caches by entry set and lets unrelated assets stay lazy. File-size policy also changes from 40 KiB to 512 KiB; those constants were situational.

Inference (medium): Jan accepts a sizeable subsystem when it serves a concrete startup-delivery obligation, and refines it around the true dependency graph instead of preloading everything. Cost: caching, invalidation and worker lifecycle complexity. Counterexample: a single static page may need none of this; this is not a blanket preference for bundles or custom caching. Observation: high.

## J8 — Put state at the lifetime that needs isolation

`agent-zero @ 68ba6e9ecfefdfea696a66093b2d5d598c020967 : agent.py` introduces `AgentContext` with per-chat log, paused state, streaming agent and process, replacing class-level pause/streaming state and adding multiple contexts. Recorded subject/body: context separation, async, multiple chats. Inference (medium): add a state owner when independent users of existing global state require isolation. Tradeoff: registry/lifecycle bookkeeping and more explicit context plumbing. Counterexample: immutable shared services need not be copied per chat; this is not today's persisted child-context implementation. Observation: high.

## J9 — Keep optional dependency policy with the plugin

`agent-zero @ 247c8d845ffab8acbf4db5d3b93cf343557a080c : requirements.txt`, `plugins/_telegram_integration/requirements.txt`, `helpers/dependencies.py` and lifecycle callers moves aiogram out of global requirements into Telegram-owned loading. The helper checks availability, serializes install attempts with a lock, invalidates import caches, verifies installation and reports failures. Constants are separated from the handler so hook imports do not pull its full dependency graph.

Recorded: optional lazy dependency loading; default update-backup location also moves outside `/a0/tmp`. Inference (medium): plugin ownership includes dependency cost and readiness, not merely UI policy. Tradeoff: feature activation can pay installation latency; synchronization is justified around an actual shared install. Counterexample: core-required dependencies belong in core and image/self-update paths must both be covered. Do not copy this installer or install anything without current authorization. Observation: high.

## J10 — A tiny intervention can be proportional; protect output boundaries explicitly

`agent-zero @ b9e1120a8e8f8812e19dfe41e3c79af40e222e65 : main.py`, `requirements.txt` adds a 0.1-second yield to the key-capture loop and removes uvloop under the recorded “windows slowdown and compatibility fix.” It supplies no benchmark or causal breakdown; do not claim a measured improvement. Inference (low, one early case): try the direct lifecycle/dependency correction before a scheduling redesign.

`6181ac9c204e27290608bbe83bf0ec0b20fe5f01 : plugins/_code_execution/tools/code_execution_tool.py` masks values through the context's secrets manager before the final display truncation. Recorded intent is to prevent secret exposure in command logs. Inference (medium): reuse the existing context boundary for sensitive output rather than scatter redaction among callers. This is a scoped display change, not proof that every possible secret was covered. Observations: high.

## J11 — Proportion and evidence limits are part of the style

`agent-zero @ 175baa49db36ea102e426fa69e78bd0cae1c45b9 : AGENTS.md`, “Add AGENTS.md DOX files and migrate docs,” establishes binding hierarchy, reading before editing, ownership, indexes and the post-edit DOX pass. Current file-level `*.dox.md` rules go further and remain authoritative. Inference (medium): documentation is part of the working architecture, not a diary appended after code.

One-line and large-system examples coexist; no global line-count target follows. Historical mistakes and revisions remain evidence of fallibility, not style to emulate. Proportionality does not excuse omitted security, data preservation or requested acceptance criteria.

## J12 — Cross-repository attribution must stay narrow

Launcher: `90ac706dbd161cecf48ab74c6b902300aabba8c1 : .github/workflows/build.yml` adds arm64/x64 build commands and predictable output names; it also accidentally contains conflict markers. `053245e6035c80f78070c1fa1d42f8070575b2a9` removes those markers two minutes later. `e84aca052f01fa2b662055640e45ee90e64b4f57` and `7a80a8b60e14efcbfd775c3b4e82cb444b0f70af : forge.config.js` cover packaging/signing, with the latter hardcoding notarization. These are limited build precedents, not evidence for today's Docker Manager, renderer or gateway design. Do not generalize a hardcoded signing switch into a modern configuration rule. Present-day release contracts have changed.

Connector: `aa2c06dbf5ab47cd2f9dd7218b03c7716f01bd14` contains only `.gitignore` and `LICENSE`; no CLI architecture can be attributed from it. These commits do not establish authorship of Responses or native parallel work. Inference confidence for transferring Agent Zero criteria to these products: low-to-medium, depending on the actual boundary; direct authorship evidence for those modern features: absent.

## Source boundaries

The separate `engineering-delivery/references/chat-lessons.md` is a public-safe paraphrase of maintainer feedback. It is not Jan-authored Git evidence and provides no private conversation locators. Keep its L/D lesson IDs separate from the J cases here.

## Public commit references

These links locate the inspected diffs. They establish source changes, not runtime test results or personal approval.

- [agent-zero 7e1d9ad2a4a3](https://github.com/3clyp50/agent-zero/commit/7e1d9ad2a4a3d186e337a89433ccc5128bdc754d)
- [agent-zero 7df19619ac30](https://github.com/3clyp50/agent-zero/commit/7df19619ac30f82d1339872536f48aa165bba9aa)
- [agent-zero fac49e854bfe](https://github.com/3clyp50/agent-zero/commit/fac49e854bfe5736e945f7be08f6dd36b6af94ea)
- [agent-zero d5fc0a32e798](https://github.com/3clyp50/agent-zero/commit/d5fc0a32e79891b634cdb105c33a20def2ed45bb)
- [agent-zero 1eb78607c9ad](https://github.com/3clyp50/agent-zero/commit/1eb78607c9adaa36db929dda11e5f1359d02714e)
- [agent-zero eafe51a688c0](https://github.com/3clyp50/agent-zero/commit/eafe51a688c02aea277a4f244a1fe61965f0b614)
- [agent-zero e0dae52b7fa2](https://github.com/3clyp50/agent-zero/commit/e0dae52b7fa20601c3d59b940fae8aae2b94d662)
- [agent-zero 89d4b8913f40](https://github.com/3clyp50/agent-zero/commit/89d4b8913f400d92ac00e4d143c17d3e76ad9f25)
- [agent-zero 0329003b659b](https://github.com/3clyp50/agent-zero/commit/0329003b659bd6d51c64745c3d2a72f668cae641)
- [agent-zero bebe6826cf8a](https://github.com/3clyp50/agent-zero/commit/bebe6826cf8a654d1423a9aa0f1c118116a3bc0e)
- [agent-zero 68ba6e9ecfef](https://github.com/3clyp50/agent-zero/commit/68ba6e9ecfefdfea696a66093b2d5d598c020967)
- [agent-zero 247c8d845ffa](https://github.com/3clyp50/agent-zero/commit/247c8d845ffab8acbf4db5d3b93cf343557a080c)
- [agent-zero b9e1120a8e8f](https://github.com/3clyp50/agent-zero/commit/b9e1120a8e8f8812e19dfe41e3c79af40e222e65)
- [agent-zero 6181ac9c204e](https://github.com/3clyp50/agent-zero/commit/6181ac9c204e27290608bbe83bf0ec0b20fe5f01)
- [agent-zero 175baa49db36](https://github.com/3clyp50/agent-zero/commit/175baa49db36ea102e426fa69e78bd0cae1c45b9)
- [a0-launcher 90ac706dbd16](https://github.com/3clyp50/a0-launcher/commit/90ac706dbd161cecf48ab74c6b902300aabba8c1)
- [a0-launcher 053245e6035c](https://github.com/3clyp50/a0-launcher/commit/053245e6035c80f78070c1fa1d42f8070575b2a9)
- [a0-launcher e84aca052f01](https://github.com/3clyp50/a0-launcher/commit/e84aca052f01fa2b662055640e45ee90e64b4f57)
- [a0-launcher 7a80a8b60e14](https://github.com/3clyp50/a0-launcher/commit/7a80a8b60e14efcbfd775c3b4e82cb444b0f70af)
- [a0-connector aa2c06dbf5ab](https://github.com/agent0ai/a0-connector/commit/aa2c06dbf5ab47cd2f9dd7218b03c7716f01bd14)
