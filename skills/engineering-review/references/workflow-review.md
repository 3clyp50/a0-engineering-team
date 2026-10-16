# Review the user workflow

Read the relevant repo's current visual/component contracts. Agent Zero's WebUI, Launcher renderer and Connector TUI have different implementations; consistent product intent does not mean copying one widget implementation everywhere.

Start with a short user scenario: starting state, intent, action, expected saved/effective state. Exercise the available changed artifact. A screenshot can prove visual state, not persistence or correct privilege ownership. Report when interaction or vision is unavailable.

Check only relevant dimensions:

- **Path:** first-use setup, normal use and recovery should be obvious. Surface useful user decisions; keep internal services, Docker mechanics and model transport details out of the flow unless they help the user choose.
- **Language/components:** use current product vocabulary and official assets. Reuse local modal, notification, form, icon, spacing and focus patterns. Do not invent substitute logos or decorative nested cards.
- **State fidelity:** distinguish selected, inherited/default, effective/running, installed, available and busy. Observe save/reopen, reload, chat/profile switch, failure and cancellation when relevant. Show actual progress or honest indeterminate progress.
- **Interaction/accessibility:** keyboard reachability, focus/return, labels, readable contrast, compact-control overflow, disabled/empty/error states and the relevant viewport. Responsive emulation is not real-device proof.
- **Boundaries:** renderer requests intent; privileged owner validates and executes it. Existing permissions, consent, instance/workspace separation and host/container routing must remain intact.

Report user consequence before aesthetic preference. Use the sanitized design lessons D1–D4 in `engineering-delivery` where useful; current DOX controls exact branding and components. Do not reopen final product choices unless evidence reveals a failure against the user's goal.
