# Project Frame: Radiant adoption

Frame revision: 4 (2026-10-16), closed at stage 2; the skill will not be created
Radiant reference: 604c2a0b5103005e54b6a6089433f42d10d31320

## Intent and participant

Adopting Radiant in a project today requires gathering steps from three
places: the [integration](../integration.md#project-map), the "Set up the
consumer" section of the adapters and the templates. None of these places
handles the case of a project that already exists, with its own commands, CI
and conventions. The
[adapter entry](../../adapters/claude-code/README.md#agent-entry) assumes a
`.radiant.json` is present.

Participants: the human who decides to adopt and the orchestrator who runs the
adoption.

Transformation: from the request "adopt Radiant here", the orchestrator
diagnoses the project, proposes the setup and writes only after approval. The
project ends with a valid map, real commands in `AGENTS.md` and the intent
gaps listed for the cycle.

Radiant alone defines the files it writes and does not depend on any other
tool. A tool that manages skills or context in the same project coexists with
it by preserving what is outside the Radiant section.

## Hypothesis and Challenge

Hypothesis: an adoption checklist, followed by the orchestrator, takes an
existing project to a correct setup without facts being invented.

The [thesis](../project-generation-system.md) only accepts a new capability
when it repeats and is valuable in more than one project. There is no recorded
pain yet, because the only consumer was adopted by hand. So the work moves in
stages and each one only starts with the evidence from the previous one.

| Stage | Delivery | Advances if |
| --- | --- | --- |
| 1. Documentation | An "Adopt" section in the integration and an adapter branch for a project without `.radiant.json` | Validator and tests pass; merge into `main` |
| 2. Measured adoption | Adoption of an existing project following stage 1 | The result shows a repeatable error, omission or friction |
| 3. Skill | `radiant-adopt`, with only what stage 2 showed to be missing | Repeating stage 2 in another project improves the result |

The Frame is refuted if stage 2 gets it right without friction. In that case,
the documentation is enough and the skill is not created.

## Smallest experiment

Stage 2 in the `faelplg/lab-ai-usage-quota` project. It has tests, typecheck
and CI, does not publish the repository as a site and does not have an
`AGENTS.md` yet.

1. The pin is the `main` commit that contains stage 1, with the main checkout
   clean at that commit. Nothing changes in the global bootstrap.
2. The orchestrator does the diagnosis read-only, and proposes the exact list
   of files and the content of each one.
3. The human reviews the proposal directly, marking what is wrong, what is
   extra and what is missing.
4. After approval, the orchestrator writes on a local branch, without push.

Evidence:

- the human's corrections in the review: errors, extras and omissions;
- invented facts, with a target of zero;
- files touched outside the approved list, with a target of zero, checked by
  the diff and by `git status --ignored`;
- `check_project.py` exiting 0, without changing the pin to pass;
- friction noted during the adoption.

Revision 3 removed the answer key written before the proposal. For a small,
local project, the cost was not worth it (Article XVII). The accepted loss is
that an omission may go unnoticed in the review.

`check_project.py` alone does not prove the adoption, because it accepts a
map that is all `null`. It only confirms the structure.

## Boundaries

Files the adoption writes:

- `.radiant.json`, with `null` in every artifact that does not exist yet;
- a `<!-- radiant:begin/end -->` section in `AGENTS.md`, creating the file if
  it is missing and preserving everything else;
- `CLAUDE.md` with `@AGENTS.md`, only if there is no `CLAUDE.md`;
- optionally, `maintenance` and an entry in `.gitignore`, if the human
  approves.

Constraints:

- Nothing is written before approval, and nothing outside the approved list.
- The pin is a human decision and must be reachable from `main`.
- Global configuration stays manual, through the adapter's commands.
- A command is only safe if it is local, without network and without writing
  outside the project.

Non-goals:

- Writing the product's Frame, Spec, Plan or Engineering Profile. These items
  stay in the gap list for `radiant-cycle`.
- Updating the pin of those who have already adopted.
- The Codex adapter. It comes in after stage 2, through the same text.
- Any integration with another skill or context management tool.

Open:

- What stage 2 reveals decides whether stage 3 exists and what its scope is.

## Stage 2 result

Adoption of `lab-ai-usage-quota` on 2026-10-16, at local commit `63576da` of
the `chore/radiant-adoption` branch, without push. Pin
`238190aa4918c74a7f1de99907e8215c7e96a443`.

| Evidence | Result |
| --- | --- |
| The human's corrections in the review | 0 |
| Invented facts | 0 |
| Files outside the approved list | 0: only `.radiant.json`, `AGENTS.md`, `CLAUDE.md` and `.gitignore` |
| `check_project.py` | Exit 0, pin intact |

Friction, all fixed in the [integration](../integration.md#adopt-in-a-project)
and in the [neutral map](../../templates/project-agents.md):

1. The checkout was behind the pin. Step 1 now says when to fast-forward.
2. The repository is public. The proposal now warns that the section applies
   to every contributor, and the map says what someone who does not use
   Radiant follows.
3. The project is in English and the map in Portuguese. The section stays in
   Portuguese.
4. There was no place for the evidence. It goes in the body of the adoption
   commit.
5. Classifying a command as safe required reading the tests. Step 2 now says
   so and says to treat doubt as not safe.

Human decision: there was no error or invention, and the friction was
resolved in the checklist. Stage 3 does not happen and `radiant-adopt` will
not be created.
