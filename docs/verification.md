# Verification scope

## Native coordination trial

On 16 October 2026, a native Agent Zero Delivery Manager completed a controlled duration-helper exercise using an implementation worker, independent engineering reviewer and verifier. The manager created three children and made five continuations of those exact child contexts through native tools. Accepted changes returned to the original worker; the same reviewers rechecked them. Context IDs remained usable after two history compressions.

The first requirement set passed 10 tests. A second, explicitly new requirement set added hour formatting and concise CLI errors; the preserved first snapshot still passed its 10 checks and the final helper passed 12. This was a pure helper in a task-owned workdir and separate process. It did not prove development-instance separation or safe controller restarts.

A child read an authorized host file through Agent Zero's native remote editor. A child also opened a task-owned counter page, observed zero, clicked and observed one through the native browser. Host writes and visual screenshot review were not tested. Neither operation used a Codex browser as a substitute for child capability.

The observed run took about 44.56 minutes and logged 196 main-agent model turns across manager, worker, reviewer and verifier. Those counts exclude utility requests and provider-internal activity. This is a coordination receipt, not a speed, cost or ordinary-delivery benchmark. Current handoff guidance includes a concise-report refinement added after that run; the whole model-driven trial was not repeated after it.

## Repository packaging

The repository strengthens the separate-instance rule, adds explicit commit subject/body and product staging-branch requirements, and removes private provenance pointers. The six portable checks and final native-loading checks passed after these revisions. The earlier exercise does not certify autonomous compliance with them.

Portable checks cover installation idempotence, refusal of conflicting/unexpected or symlinked destinations, untouched unrelated content, native metadata, local reference resolution and profile inheritance declarations. Framework checks cover native profile/catalog discovery, rendered prompts, skill load/reference reads and native project instruction assembly, without invoking a model.

No production product change, restart, multi-instance run, concurrent product writers, host write, visual screenshot assessment or unrestricted autonomous operation is certified. A distinct development/test instance is not configured in the initial local installation. No product branch was changed as part of packaging.

## Reproduce

From this repository, run `python3 -m unittest discover -s tests -v`. After installing into Agent Zero, run `python3 scripts/install.py /a0 --check` in its container. Then, from `/a0`, run:

```bash
PYTHONPATH=/a0 /opt/venv-a0/bin/python usr/projects/a0-engineering-team/scripts/verify_native.py --dockerized=true
```

Use the actual framework interpreter and project location if yours differs. This creates only temporary in-process validation contexts, removes them and makes no LLM request. It does not restart the controller or activate the project in existing chats.

The project was also discovered and loaded through Agent Zero's native project API, then activated in a fresh idle native chat with Delivery Manager selected. No model request was started for that opening check. The controller was not restarted; nine protected core/model files remained unchanged.

Private receipts are intentionally excluded. The historical decision study links public Git commits, identifies inference and counterexamples, and makes no claim of Jan's personal endorsement.
