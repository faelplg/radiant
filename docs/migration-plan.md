# Inventory and migration plan

Analysis done before the moves on 2026-09-15. The folder had no `.git`;
`AGENTS.md` was zero bytes. All 15 Markdown documents were read in full.
`.DS_Store` is Finder binary metadata, with no operational role.

## Full inventory and ownership

| Current path | Responsibility / classification | Canonical owner | Proposed destination | Action | Reason |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | Radiant adapter, empty | Radiant | `AGENTS.md` | Fill in | Agent entry into the system itself |
| `constitution.md` | Radiant normative | Radiant | `constitution/CONSTITUTION.md` | Move without editing | Unambiguous normative source |
| `project-generation-system.md` | Radiant Core, thesis 0.2 | Radiant | `docs/project-generation-system.md` | Move; deduplicate section 9 | Explanation distinct from the norm |
| `aikm-context/FRAME.md` | AIKM project state, 0.2.1 | AIKM | `migration/aikm/FRAME.md` | Move without editing | The consumer's intent |
| `aikm-context/SPEC.md` | AIKM project state, 0.3.1 | AIKM | `migration/aikm/SPEC.md` | Move without editing | The consumer's behavior |
| `aikm-context/PLAN.md` | AIKM project state, 0.3.1 | AIKM | `migration/aikm/PLAN.md` | Move without editing | The consumer's increments |
| `aikm-context/WORKFLOW.md` | AIKM project state / local adapter | AIKM | `migration/aikm/WORKFLOW.md` | Move without editing | Local map, not a shared procedure |
| `aikm-context/adrs/ADR-0001-technical-bootstrap.md` | AIKM project state | AIKM | `migration/aikm/adrs/ADR-0001-technical-bootstrap.md` | Move without editing | The AIKM stack is not the Radiant stack |
| `aikm-context/contracts/README.md` | Generic convention + AIKM context | AIKM (snapshot); Radiant (extracted convention) | `migration/aikm/contracts/README.md` | Preserve; extract the convention | Do not turn a historical instance into a living norm |
| `aikm-context/contracts/ACTIVE.md` | AIKM project state | AIKM | `migration/aikm/contracts/ACTIVE.md` | Move without editing | No active contract; TC-0002 not authorized |
| `aikm-context/contracts/TC-0001-iteration-00-bootstrap.md` | AIKM project state, closed contract | AIKM | `migration/aikm/contracts/TC-0001-iteration-00-bootstrap.md` | Move without editing | Preserve historical delegation and acceptance |
| `aikm-context/contracts/TC-0002-capture-search.md` | AIKM project state, proposal | AIKM | `migration/aikm/contracts/TC-0002-capture-search.md` | Move without editing | Do not activate or rewrite a proposal |
| `aikm-context/learning/LR-0001-workflow-activation.md` | AIKM project state, evidence | AIKM | `migration/aikm/learning/LR-0001-workflow-activation.md` | Move without editing | Learn Back provenance |
| `aikm-context/verification/VR-0001-workflow-setup.md` | AIKM project state, evidence | AIKM | `migration/aikm/verification/VR-0001-workflow-setup.md` | Move without editing | Do not attribute retroactive use |
| `aikm-context/verification/VR-0002-bootstrap-acceptance.md` | AIKM project state, evidence | AIKM | `migration/aikm/verification/VR-0002-bootstrap-acceptance.md` | Move without editing | Acceptance of an external implementation |
| `aikm-context/.DS_Store` | Historical/transitional, Finder metadata | Machine | `migration/aikm/.DS_Store` | Move; ignore in Git | Preserve without polluting history |

Previous directories: the root, `aikm-context/` and its children `adrs/`,
`contracts/`, `learning/`, `verification/`. There were no templates,
capabilities, skills, validators, workflows or independent examples in the
folder. No textual artifact was left classified as unknown; none was
classified as a permanent example.

## Complementary evidence inspected

The neighboring AIKM repository already exists. Only its artifacts related to
Radiant were consulted; no external write is part of this migration.

| External source | Responsibility | Decision |
| --- | --- | --- |
| AIKM `AGENTS.md` | First Codex adapter 0.2 | Navigation evidence; the new adapter does not copy its rules |
| AIKM `docs/radiant/CONSTITUTION.md` | Transitional copy | Differs only in frontmatter and dividers; the source provided in this folder wins |
| AIKM `docs/radiant/skills/radiant-cycle/SKILL.md` | Radiant capability 0.1.0 | Incorporate into `skills/radiant-cycle/SKILL.md`, fixing the link and editorial version |

Origin of the skill: AIKM commit `3e896d441a7ce3563531f923861ad1f109f809ce`,
SHA-256 `5b7c61260188afab1e7f9b561130829b655412b20aff6bd8bbb26660b8401c06`,
the same as recorded in VR-0001/VR-0002. The external adapter and the external
copies remain transitional until AIKM explicitly adopts them.

## Canonicality and decisions

- Constitution: one body in `constitution/CONSTITUTION.md`. The normative list
  repeated in section 9 of the thesis becomes a reference; the other ideas
  remain.
- Cycle: reuse the existing skill. `docs/capabilities.md` will be only an
  index; do not create a parallel workflow with the same body.
- Contracts: generic convention in `contracts/README.md`, form in
  `templates/task-contract.md`; contracts and activation belong to the
  consumer.
- Frame: a minimal form based on the thesis, without copying the AIKM Frame.
- Verification and Learn Back: procedures in the skill and specific criteria
  in `docs/verification.md` and `docs/learn-back.md`, subordinate to the
  Constitution.
- Integration: a path configured in the global bootstrap generated from a
  template; no registry, additional mandatory variable or package manager.
- Revision: a full Git commit per project and per cycle. Document versions do
  not identify the whole system. Do not adopt repository SemVer now.

## Risks and containment before execution

Internal moves are reversible. The Git index keeps the original state before
the changes; hashes verify preservation. Do not delete documents or edit
generated artifacts. Do not overwrite existing destinations.

Historical AIKM references assume `docs/project/` and `docs/radiant/` in the
original repository, already absent from this folder. They will be inventoried
in `migration/README.md` with an explicit resolution, without changing the
bodies of contracts or evidence. The validator will distinguish operational
links from known historical references, detecting new broken links in both.

The observed global `AGENTS.md` is a symlink managed by Nix. Generate a local
block for inspection and document its inclusion in the source configuration;
do not change the symlink or the store. A real installation is not a condition
of the requested architecture.

Final transfer of the AIKM documents and replacement of its Core copies stay
outside this execution. They require comparing with the state of the
destination repository and authorizing the change there. If there is a
material conflict in that future transfer, use HOLD; do not overwrite or infer
which version prevails.

Do not implement Experience Design, System Design or any artifact of the
future Design Layer. Directories will only be created with real operational
content.

## End of custody

Recorded on 2026-10-13. This section accepts the transfer planned in the six
separation steps of the former `migration/README.md` and removes the custody
from the working tree. The last state with the custody is commit
`2f81d6fd73928b52bab04aeaeb0b8d2b164188a1`, which remains reachable through
Git history.

| Step | Evidence in AIKM (`origin/main` at `f9052509b8caf7caff6134d2f18bb5e71cdc0149`) |
| --- | --- |
| 1. Compare destination and snapshots | The 12 snapshots have identical blobs reachable from `origin/main` |
| 2. Resolve conflicts | There is no conflict to resolve: AIKM evolved its own documents, archived the v1 records in the `v1-final` tag and removed them from `docs/project/` |
| 3. Adoption and pointers | `.radiant.json` with a reviewed pin, a neutral `AGENTS.md` with pointers to Radiant and no copy in `docs/radiant/` |
| 4. Operational navigation | The AIKM map points to the Radiant Core, without reassigning versions in reports |
| 5. Verified path | Pilot of [ADR-0001](adrs/ADR-0001-delegation-roles.md#pilot-result), stages 0 to 5 |
| 6. Removal | Removal of `migration/` and of the validator's custody checks |

The local `.DS_Store` was never versioned. The AIKM bodies still belong to
AIKM; Radiant no longer keeps a copy of them.
