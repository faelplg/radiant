# Canonical reorganization report

State: **DONE** for organization, designed integration and local verification.
Completed on 2026-09-16. Actual global installation and adoption of the new
adapter by AIKM are not part of the external execution of this delivery.

Authority: the owner's request to turn this folder into an independent Radiant
repository, followed by authorization for two local commits. The
[analysis before the moves](migration-plan.md) preserves inventory, ownership,
decisions and risks. There was no push, remote or write to another project.

## Previous structure

A folder without Git, an empty `AGENTS.md`, thesis 0.2 and Constitution 0.1 at
the root, plus 12 AIKM documents in `aikm-context/` and a `.DS_Store`. The
Frame was 0.2.1; Spec/Plan, 0.3.1. The context held a closed TC-0001 and a
proposed TC-0002. The skill and adapter bodies referenced in those documents
were missing.

The bounded query to the existing AIKM recovered the original adapter and
skill 0.1.0 with a digest matching the reports. The external Constitution only
differed editorially; the source provided in this folder was kept as the
owner.

## Final structure

```text
radiant/
  README.md
  AGENTS.md
  .gitignore
  constitution/CONSTITUTION.md
  docs/
    project-generation-system.md
    capabilities.md
    integration.md
    contributing.md
    verification.md
    learn-back.md
    migration-plan.md
    repository-report.md
  skills/radiant-cycle/SKILL.md
  templates/
    README.md
    project-frame.md
    task-contract.md
    radiant-project.json
  contracts/README.md
  adapters/codex/
    README.md
    global.AGENTS.template.md
    project.AGENTS.template.md
    render_bootstrap.py
  validators/
    README.md
    check_repository.py
    check_project.py
  tests/test_integration.py
  migration/
    README.md
    AGENTS.md
    inventory.json
    historical-links.json
    aikm/  (snapshot received, unchanged)
  .local/codex-global.md  (generated, ignored by Git)
```

There are no `projects/`, `knowledge/`, `workflows/` or folders for future
adapters without a present function. The workflow is the real skill;
`docs/capabilities.md` only indexes it. The future Design Layer can add
capabilities without changing owners.

## Moved files

| From | To |
| --- | --- |
| `constitution.md` | `constitution/CONSTITUTION.md` |
| `project-generation-system.md` | `docs/project-generation-system.md` |
| `aikm-context/FRAME.md` | `migration/aikm/FRAME.md` |
| `aikm-context/SPEC.md` | `migration/aikm/SPEC.md` |
| `aikm-context/PLAN.md` | `migration/aikm/PLAN.md` |
| `aikm-context/WORKFLOW.md` | `migration/aikm/WORKFLOW.md` |
| `aikm-context/adrs/ADR-0001-technical-bootstrap.md` | `migration/aikm/adrs/ADR-0001-technical-bootstrap.md` |
| `aikm-context/contracts/README.md` | `migration/aikm/contracts/README.md` |
| `aikm-context/contracts/ACTIVE.md` | `migration/aikm/contracts/ACTIVE.md` |
| `aikm-context/contracts/TC-0001-iteration-00-bootstrap.md` | `migration/aikm/contracts/TC-0001-iteration-00-bootstrap.md` |
| `aikm-context/contracts/TC-0002-capture-search.md` | `migration/aikm/contracts/TC-0002-capture-search.md` |
| `aikm-context/learning/LR-0001-workflow-activation.md` | `migration/aikm/learning/LR-0001-workflow-activation.md` |
| `aikm-context/verification/VR-0001-workflow-setup.md` | `migration/aikm/verification/VR-0001-workflow-setup.md` |
| `aikm-context/verification/VR-0002-bootstrap-acceptance.md` | `migration/aikm/verification/VR-0002-bootstrap-acceptance.md` |
| `aikm-context/.DS_Store` | `migration/aikm/.DS_Store` (local only, ignored) |

## Created, preserved and adjusted

| Created file(s) | Function |
| --- | --- |
| `README.md` | Human entry and index of the tree |
| `.gitignore` | Exclude Finder metadata, Python cache and local output |
| `docs/capabilities.md` | Discovery of available bodies |
| `docs/integration.md` | Three levels, local map and pin |
| `docs/contributing.md` | Evolution and Git identity |
| `docs/verification.md` | Gates and structural criteria |
| `docs/learn-back.md` | Real fix destinations |
| `docs/migration-plan.md` | Inventory and decisions before the moves |
| `docs/repository-report.md` | This report |
| `skills/radiant-cycle/SKILL.md` | Skill incorporated from the first experiment |
| `templates/README.md` | Use and ownership of the forms |
| `templates/project-frame.md` | Minimal intent form |
| `templates/task-contract.md` | Delegation form |
| `templates/radiant-project.json` | Portable consumer configuration |
| `contracts/README.md` | Generic convention extracted from the experiment |
| `adapters/codex/README.md` | Harness entry and bootstrap |
| `adapters/codex/global.AGENTS.template.md` | Portable source of the global block |
| `adapters/codex/project.AGENTS.template.md` | Consumer pointers |
| `adapters/codex/render_bootstrap.py` | Local generation without overwriting |
| `validators/README.md` | Validator commands and limits |
| `validators/check_repository.py` | Links, custody and portability |
| `validators/check_project.py` | Pin, clean checkout and consumer paths |
| `tests/test_integration.py` | Real paths of the scripts in an isolated environment |
| `migration/README.md`, `migration/AGENTS.md` | Ownership and protection of the custody |
| `migration/inventory.json` | SHA-256 of the originals and destinations |
| `migration/historical-links.json` | Exact exceptions for historical navigation |
| `.local/codex-global.md` | Generated local configuration, not a versioned source |

The existing `AGENTS.md` was filled in. The Constitution, 12 AIKM documents and
Finder metadata were preserved byte for byte. The thesis only lost the
normative duplication in section 9, replaced by a link; its remaining
conceptual text and version were preserved. The skill only changed its
editorial version and the link to the Constitution. No content was removed
without remaining in history.

The 12 unique historical links that escape the AIKM snapshot have a resolution
in the [custody map](https://github.com/faelplg/radiant/blob/2f81d6fd73928b52bab04aeaeb0b8d2b164188a1/migration/README.md).
They were not falsely fixed to open files of another project. All new
operational links are direct and verified; the historical bodies were not
rewritten.

## Canonical sources

- Thesis: [docs/project-generation-system.md](project-generation-system.md).
- Constitution: [constitution/CONSTITUTION.md](../constitution/CONSTITUTION.md).
- Cycle procedure/capability: [radiant-cycle](../skills/radiant-cycle/SKILL.md).
- Templates: [templates/](../templates/README.md).
- Contract system: [contracts/README.md](../contracts/README.md).
- Shared integration: [integration.md](integration.md).
- Harness: [adapters/codex/](../adapters/codex/README.md).
- Verification and Learn Back: their [checks](verification.md) and
  [destination map](learn-back.md), subordinate to the Constitution and the
  skill.

## Global configuration, project and AGENTS

The chosen mechanism is a path configured by the user. The generator fills a
small template with the checkout found by the script itself. It requires no
additional variable, symlink, registry or installing the Core elsewhere.
Changing machine or path only requires regenerating the block.

The block lives in the effective global instructions of the Codex profile,
through inclusion in the user's source configuration. The official
documentation, consulted through the OpenAI Docs skill, determined how the
profile and the override are handled; see the
[adapter](../adapters/codex/README.md). The current configuration is managed
by Nix: only `.local/codex-global.md` was generated, without changing its
source or output.

The global AGENTS locates the checkout and the adapter. Radiant's AGENTS guides
work in this repository. The consumer's AGENTS points to the adapter and its
`.radiant.json`, plus specific commands/constraints. None of them receives the
thesis, the Constitution or the skill as a copy.

## Versioning

Commit `471c65085ff5e9271c27e8fa24b62d37bd80ba0f` preserves the received state.
The second commit introduces this reorganization and this report. Its identity
is recoverable through `git log`, without an impossible self-reference in the
file itself.

A consumer records the full SHA in `radiant_revision`; cycle reports preserve
the revision actually used. The gate refuses a HEAD divergence and a changed
checkout. An update is an explicit adoption, never a silent effect of
`git pull`. There is no repository SemVer; the existing versions of the
thesis, Constitution and skill keep their own scopes.

## Review and simulations

There was one review pass after the Build against the criteria of the request
and of [Verification](verification.md). Evidence independent of the narrative
includes Git, SHA-256 of the earlier inputs and the skill's pre-existing
validator, plus running the scripts in subprocesses. There was no other
agent/reviewer; the self architectural readback is not presented as an
independent human review.

| Criterion | Observed result |
| --- | --- |
| Canonicality | A single Constitution; the thesis points to it; snapshots labeled historical |
| Core/adapter | Revision rules in the Core; discovery translation in Codex |
| Global | Block under 1 KiB; regenerable; no copy of bodies |
| Portability | Bootstrap and gate pass in a temporary checkout with spaces/accents |
| Independent project | Own state in the consumer; no Core copied |
| Independent AIKM | Consumption tests work without the custody folder |
| One body/pointers | Single living skill and convention; explicit historical exceptions |
| Discoverability | Paths A/B/C below inspected |
| Versionability | Recoverable baseline, verifiable renames, mandatory pin |
| Minimalism | No empty directory or speculative adapter |
| Extensibility | New capabilities can use the same owners/directories |

**A - Working on Radiant.** AGENTS leads to the Constitution, thesis and index;
the index leads to the skill. Review mode leads to the repository checks and
the Learn Back routing. The development checkout is not blocked by a
consumer's pin; changes are precisely the object of that session.

**B - New project.** The global bootstrap locates Radiant; the consumer's
AGENTS reads the adapter and its map. The commit is checked before loading
rules. The project creates its Frame, Spec and Plan and records the paths; it
creates contracts and `ACTIVE.md` locally. The skill stays in the shared
checkout. Tests exercised the initial map, state creation, relocation, gate
and explicit revision update.

**C - AIKM.** The read-only comparison confirmed that its 12 documents already
exist in the AIKM repository with content equal to the snapshots. Future
adoption can reference Radiant and keep those documents in place; it does not
need to move the product into this repository. Evidence and learning stay in
AIKM; a reusable fix can point to a Radiant file. AIKM does not become owner of
the system or a requirement of the bootstrap.

## Executed evidence and limits

- `python3 validators/check_repository.py`: passed; local links, anchors,
  explicit historical exceptions and preserved digests.
- `python3 -m unittest discover -s tests -v`: seven tests passed. They cover a
  new consumer, invalid paths and escape through a symlink, invalid/duplicate
  JSON, a divergent/symbolic pin, tracked/staged/untracked changes, explicit
  adoption after a new commit, portable generation and refusal to overwrite.
- `render_bootstrap.py --output .local/codex-global.md`: created local output;
  reading it confirmed the pointer to this checkout and the absence of Core
  bodies.
- `quick_validate.py skills/radiant-cycle`: `Skill is valid!`. The first
  attempt found PyYAML missing. PyYAML 6.0.3 was installed only in a temporary
  directory to run the verifier, with no dependency in Radiant.
- `git diff --check` and review of the index/diff: integrity of the change
  checked; previous content preserved in the baseline. Markdown hard breaks in
  the originals were not reformatted to satisfy import whitespace.
- Environment used: macOS, Python 3.14.7 and Git 2.55.0. The declared
  compatibility with Python 3.9+ uses only APIs from that base; other versions
  were not run.

The recovered skill 0.1.0 guided the planning. The incorporated 0.1.1 was read
for the review, SHA-256
`daaf24af79f42aad54a3e66f4854f586c7504758086507b1d7e87ace61af3f25`.
Skill Creator guided the validation of the minimal incorporation; Conventional
Commits guided the two history records.

No real new Codex session was started and the global block was not installed.
Scenarios A/B/C are conceptual simulations accompanied by real execution of
the scripts, not proof of the model's future behavior or of AIKM usefulness.

## Learn Back from this reorganization

Finding: references to the Core inside AIKM made its location depend on the
first consumer. Evidence: original links broken in this folder, the skill
missing and the adapter recovered in AIKM. Fix targets: repository,
integration and adapter. Fix: bodies owned by Radiant and consumption pointers
with an explicit revision. Verification: navigation, preservation and tests of
a relocated consumer. Reuse in a future product delivery remains to be
demonstrated.

Future findings stay local when specific; reusable ones may originate a change
in the responsible Radiant file, with reason, evidence and verification. A
Constitution amendment requires the cross-cutting justification set out in the
Constitution itself, never automatic promotion.

## Open questions and deferred work

No material decision blocks the delivered organization. Remaining for the
external adoption: the cycle/revision AIKM will choose, the inclusion of the
block in the user's Nix source and the later removal of the custody after
checking the destination.

Not implemented: Experience Design, System Design, the Design Layer and its
artifacts; other adapters; publication; releases/tags and automated
changelog; package management; automatic skill registration in the harness;
capture/retrieval integration with AIKM; changes to the product or activation
of TC-0002.
