# A0 Engineering Team

A native Agent Zero project with six reusable agent profiles and three skills for coordinated software delivery. It uses Agent Zero's own agents, projects, skills and tools, with existing permissions and model settings.

## Contents

**Profiles (`agents/`)**

- `chief-of-staff`: owns several initiatives.
- `delivery-manager`: owns one complete outcome, even across repositories.
- `engineering-worker`: makes bounded writes to assigned paths.
- `engineering-reviewer` and `design-reviewer`: independent reviewers who report directly to the manager.
- `engineering-verifier`: an independent verifier who reports directly to the manager.

**Skills (`skills/`)**

- `engineering-delivery`: the shared team contract. All profiles read it through Agent Zero's `skills_tool`.
- `frdel`: planning evidence that managers load before choosing an approach. It covers 12 case groups and 20 authored commit references. It distinguishes recorded rationale, inference, applicability, tradeoff, confidence and counterexample. Paraphrased maintainer-feedback lessons are kept separate from recorded Git evidence.
- `engineering-review`: review guidance for the team.

Every profile preserves `{{include original}}` for native prompt inheritance. The historical study does not imply Jan Tomasek's endorsement.

## How the team works

- Use roles in proportion to the task. Not every task needs every role.
- Accepted corrections go back to the original worker. The manager continues that worker's native `context_id` with `reset:false`, then requests a focused recheck.
- Use parallel tools only for independent work.
- Roles grant no tool access, dependency installation, commit, push or publication permission. The current owner's explicit authorization controls those actions.
- Host tools depend on the connector capabilities that are actually authorized in your setup.

## Requirements

- A current Agent Zero version that supports the native tool schemas these profiles use. Older versions are not certified.
- Standard-library Python 3.10 or later for the installer and tests.
- No Codex installation or external symlinks.

## Install

Run these commands inside a normal Docker Agent Zero, from a fresh location:

```bash
cd /a0/usr/projects
git clone https://github.com/3clyp50/a0-engineering-team.git
cd a0-engineering-team
python3 scripts/install.py /a0
python3 scripts/install.py /a0 --check
```

As an alternative, clone or import this Git URL through Agent Zero Projects. The `.a0proj/` directory makes the repository discoverable as a native project.

You must install both the agents and the skills. The installer copies exactly 22 ordinary files into `/a0/usr/agents` and `/a0/usr/skills`. It never creates symlinks. It is idempotent and leaves unrelated profiles/skills untouched. It refuses changed existing files unless you inspect/back up local edits and deliberately pass `--replace`. It always refuses unexpected destination files and symlinks.

You do not need to restart Agent Zero for profile discovery. Start a fresh chat and select Chief of Staff for several initiatives or Delivery Manager for one outcome.

## Maintain the source

The versioned `agents/` and `skills/` directories are the source of truth. Deployed files are runtime copies. To update, edit the source, reinstall, then run `--check`.

## Select the development/test target

Use the explicitly configured development/test target when one is defined. Otherwise, use the current hosting instance. Missing configuration is a usable same-instance default. An invalid or unreachable explicit target is a problem to report, not a reason to silently switch elsewhere.

Record the hosting instance, selected write/test target, actual checkout and backing binds, branch/revision and write scope in your task record. The ignored root `runtime.local.md` can hold local target details; it is optional. Verify an explicitly configured different target and its actual backing paths. Never repurpose an unassigned neighboring instance by assumption.

Same-instance product writes and tests follow normal task and repository authorization. If a reload/restart would interrupt active workers on the selected target, checkpoint and coordinate their work using existing lifecycle mechanisms as needed. This project uses operational guidance; it does not provision or route instances.

## Branch and commit rules

Product staging branches:

- `agent-zero`: `ready`
- `a0-launcher`: `development`
- `a0-connector`: `development`

For each of these products, `main` is the main/release branch. Before writing, check the actual branch, worktree and dirty state, and preserve unrelated work. Do not substitute a feature-branch default. This mapping does not impose a staging branch on this standalone repository.

Every commit needs a meaningful subject and a description body, separated by an actual blank line. Write the message in a message file, then inspect it with `git log -1 --format=%B`. Literal backslash-n characters are not separators.

## Verification

To run the portable checks:

```bash
python3 -m unittest discover -s tests -v
```

These checks cover install idempotence, refusal of conflicting, unexpected or symlinked destinations, untouched unrelated content, native metadata, local reference resolution and profile inheritance. The native loading check runs with the framework interpreter and is documented in [docs/verification.md](docs/verification.md).

Static and native loading checks are separate from an earlier controlled coordination trial on a small helper task. That document describes the trial's limited results and the cases it did not test. The final instance, commit and branch guidance has not been exercised in a new autonomous trial. Static loading is not proof of autonomous delivery.

## License

Licensed under the [MIT License](LICENSE). Copyright (c) 2026 3clyp50.
