# Roles, capabilities and delegation: implementation plan

> **For executing agents:** use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to run this plan task by task.
> The steps use checkboxes (`- [ ]`) for tracking.

**Goal:** implement ADR-0001 in Radiant: agnostic roles and capabilities in
the core, a delegation skill, a maintenance skill, a Claude Code adapter and a
Codex adapter delegating from the same core.

**Architecture:** the core gets two procedural bodies
(`skills/radiant-delegation/`, `skills/radiant-maintenance/`) and a
machine-readable registry of the delegable profiles (`agents.json`). Each
adapter declares `capabilities.json` (capability → full model ID) and
templates; a single generator renders the global bootstrap and subagents per
adapter. The validators ensure core and adapters do not diverge.

**Stack:** Python 3.9+ with the standard library only, Git, Markdown, JSON and
TOML.

**Spec:** [ADR-0001](../adrs/ADR-0001-delegation-roles.md)

**Outside this plan:** the AIKM pilot (TC-0019 and TC-0020), installing the
subagents in the user's global directories, push and PR. Each one is a
separate owner decision.

## Global constraints

- Python 3.9+, no external packages; tests with `unittest` and real commands
  in temporary directories, as in `tests/test_integration.py`.
- New text in Portuguese, plain hyphen, no em dash and no horizontal
  dividers.
- Capabilities exactly `deep`, `standard`, `light`. Contract field:
  `Capability`. `Risk tier` does not change.
- Full model IDs, never aliases. Claude Code: `deep` → `claude-opus-5-5`,
  `standard` → `claude-sonnet-5-5`, `light` → `claude-haiku-5-5`. Codex:
  `deep` → `gpt-6-astra`, `standard` → `gpt-6.1-sol`, `light` → `gpt-6-luna`.
- Delegable profiles and default capability: `radiant-research` (`light`),
  `radiant-grill` (`deep`), `radiant-design` (`standard`), `radiant-dev`
  (`standard`), `radiant-verifier` (`deep`), `radiant-maintenance`
  (`standard`).
- Generated files never overwrite or follow symlinks; a refusal writes no
  file.
- Do not edit `docs/repository-report.md` or the bodies in `migration/aikm/`.
- Commits in Conventional Commits, without agent co-authorship.
- After each task: `python3 validators/check_repository.py`,
  `python3 -m unittest discover -s tests -v` and `git diff --check` pass.

## Review focus

1. A Radiant root with a space and `ç` inside TOML and YAML frontmatter: the
   escaping must produce files the harness can read. Test in Task 3
   (`tomllib` when available).
2. A single subagent already present at the destination: none of the six may
   be written. Test in Task 3.
3. `maintenance` pointing to a file or to a symlink that escapes the project:
   `HOLD`, even with the rule that accepts a missing directory. Test in
   Task 1.
4. A new adapter without a complete `capabilities.json`: the validator must
   fail before anyone generates agents without a model. Test in Task 2.
5. An older consumer without the `maintenance` field: still passes the gate.
   Test in Task 1.

## Task 1: optional `maintenance` field in the consumer map

**Files:**
- Change: `validators/check_project.py`
- Change: `templates/radiant-project.json`
- Change: `docs/integration.md` ("Project map" section)
- Test: `tests/test_integration.py`

**Interfaces:**
- Produces: `.radiant.json` accepts `maintenance` missing, `null` or a
  relative directory path, which may not exist.

- [ ] **Step 1: write the failing tests**

In `IntegrationTests`:

```python
def test_maintenance_is_optional_and_may_not_exist_yet(self):
    self.config.pop("maintenance", None)
    self.write_map()
    self.assertEqual(self.gate().returncode, 0)
    for value in (None, "ops/maintenance"):
        with self.subTest(value=value):
            self.config["maintenance"] = value
            self.write_map()
            self.assertEqual(self.gate().returncode, 0)
    (self.project / "ops/maintenance").mkdir(parents=True)
    self.assertEqual(self.gate().returncode, 0)

def test_maintenance_rejects_escapes_and_files(self):
    outside = Path(self.temp.name) / "outside-dir"
    outside.mkdir()
    (self.project / "escape-dir").symlink_to(outside)
    (self.project / "report.md").write_text("x\n", encoding="utf-8")
    for value in ("../outside-dir", str(outside), "escape-dir", "report.md", "", ".", 3):
        with self.subTest(value=value):
            self.config["maintenance"] = value
            self.write_map()
            self.assert_hold()
```

- [ ] **Step 2: run and watch it fail**

Run: `python3 -m unittest tests.test_integration -v`
Expected: FAIL in the two new tests (unknown field produces `HOLD`).

- [ ] **Step 3: implement in `validators/check_project.py`**

`OPTIONAL = ("maintenance",)`. The field check now requires
`FIELDS <= set(config) <= FIELDS | set(OPTIONAL)`. For `maintenance` present
and not null: the same string, absolute, `..` and containment validation as
the others; reject `.` (the whole project); if the destination exists, it
must be a directory; if it does not exist, accept it. Add
`"maintenance": null` at the end of `templates/radiant-project.json`.

- [ ] **Step 4: document in `docs/integration.md`**

In the schema list, one item: `maintenance`: a relative directory ignored by
Git or `null`; optional; may not exist, being created by the maintenance
skill. Cite `skills/radiant-maintenance/SKILL.md` in code; the link comes in
Task 5, when the file exists. Adjust the sentence "All fields are present" to
except `maintenance`.

- [ ] **Step 5: run the global checks and watch them pass**

- [ ] **Step 6: commit**

```bash
git add validators/check_project.py templates/radiant-project.json docs/integration.md tests/test_integration.py
git commit -m "feat(integration): accept optional maintenance directory in project map"
```

## Task 2: delegation core and adapter check

**Files:**
- Create: `skills/radiant-delegation/SKILL.md`
- Create: `skills/radiant-delegation/agents.json`
- Create: `adapters/codex/capabilities.json`
- Create: `adapters/claude-code/capabilities.json`
- Change: `validators/check_repository.py`
- Test: `tests/test_repository.py` (new)

**Interfaces:**
- Produces `agents.json`:
  `{"capabilities": ["deep", "standard", "light"], "agents": [{"name": str, "role": str, "capability": str, "description": str}]}`,
  with the six profiles from the global constraints. `role` is the anchor of
  the role's section in `SKILL.md`, in the format computed by the validator's
  `anchors()` (`ideation`, `design`, `dev`, `verifier`, `maintenance`;
  `radiant-research` and `radiant-grill` use `ideation`).
- Produces `adapters/<adapter>/capabilities.json`:
  `{"deep": str, "standard": str, "light": str}` with the IDs from the global
  constraints.
- Produces `check_repository.check_delegation(errors: list) -> None`, called
  by `check()`.

- [ ] **Step 1: write the failing tests**

`tests/test_repository.py`, class `RepositoryCheckTests`: `setUp` copies the
whole repository to a temporary directory with
`shutil.copytree(SOURCE, dest, ignore=shutil.ignore_patterns(".git", ".local", "__pycache__"))`
and defines `check(self)` running the copy's `validators/check_repository.py`
with the `run` helper from `tests/test_integration.py` (copy the helper; the
tests do not import each other).

```python
def test_current_tree_passes(self):
    self.assertEqual(self.check().returncode, 0)

def test_adapter_missing_a_capability_fails(self):
    path = self.root / "adapters/codex/capabilities.json"
    data = json.loads(path.read_text()); del data["light"]
    path.write_text(json.dumps(data))
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/codex/capabilities.json", result.stderr)

def test_adapter_without_capabilities_file_fails(self):
    (self.root / "adapters/claude-code/capabilities.json").unlink()
    self.assertEqual(self.check().returncode, 1)

def test_agent_with_unknown_role_or_capability_fails(self):
    for field, value in (("role", "missing"), ("capability", "turbo")):
        with self.subTest(field=field):
            path = self.root / "skills/radiant-delegation/agents.json"
            original = path.read_text()
            data = json.loads(original); data["agents"][0][field] = value
            path.write_text(json.dumps(data))
            self.assertEqual(self.check().returncode, 1)
            path.write_text(original)
```

- [ ] **Step 2: run and watch it fail**

Run: `python3 -m unittest tests.test_repository -v`
Expected: FAIL (files and check do not exist yet).

- [ ] **Step 3: write `skills/radiant-delegation/SKILL.md`**

Frontmatter: `name: radiant-delegation`, `description` (when to use:
orchestrate roles, delegate bounded work, choose a capability),
`metadata.version: "0.1.0"`. Sections, in this order, with the content of
sections 1 and 2 of the ADR, without copying the whole ADR and without citing
models: `## Capabilities`, `## Roles` with `### Orchestrator`,
`### Ideation`, `### Design`, `### Dev`, `### Verifier`, `### Maintenance`,
`## Rules` (the seven rules), `## Delegation package`, `## Return`,
`## Parallelism`, `## Provenance`. Each role's section says what it reads,
what it produces, the default capability, what it cannot decide and how it
returns. Link the Constitution, the Task Contract template and `agents.json`.
The `### Maintenance` section points to `skills/radiant-maintenance/SKILL.md`
in code (the link comes in Task 5).

- [ ] **Step 4: create `agents.json` and the two `capabilities.json`**

Short descriptions, one sentence each, saying when the orchestrator uses the
profile.

- [ ] **Step 5: implement `check_delegation` in `validators/check_repository.py`**

Errors, each naming the file: `capabilities` different from
`["deep", "standard", "light"]`; a repeated agent name or one without the
`radiant-` prefix; a `capability` outside the list; a `role` missing from
`anchors(SKILL.md)`; a directory in `adapters/` without `capabilities.json`,
with keys different from the capabilities or with a value that is not a
non-empty string.

- [ ] **Step 6: run the global checks and watch them pass**

- [ ] **Step 7: commit**

```bash
git add skills/radiant-delegation adapters/codex/capabilities.json adapters/claude-code/capabilities.json validators/check_repository.py tests/test_repository.py
git commit -m "feat(delegation): add roles, capabilities and adapter consistency check"
```

## Task 3: single bootstrap and subagent generator

**Files:**
- Move: `adapters/codex/render_bootstrap.py` → `adapters/render_bootstrap.py`
- Create: `adapters/claude-code/global.CLAUDE.template.md`
- Create: `adapters/claude-code/agent.template.md`
- Create: `adapters/codex/agent.template.toml`
- Change: `adapters/codex/README.md` (commands)
- Test: `tests/test_integration.py`

**Interfaces:**
- Consumes: `agents.json` and `capabilities.json` from Task 2.
- Produces a CLI:
  `python3 adapters/render_bootstrap.py --adapter {codex,claude-code} [--output FILE | --agents-dir DIR]`.
  `--adapter` is required. Without `--output` or `--agents-dir`, it prints the
  global block. `--agents-dir` writes `<name>.md` (Claude Code) or
  `<name>.toml` (Codex) for the six profiles.
- Produces functions: `render_global(root: Path, adapter: str) -> str`,
  `render_agents(root: Path, adapter: str) -> dict[str, str]` (file name →
  content), `write_exclusive(files: dict[Path, str]) -> None` (checks every
  destination before writing any of them).
- Template placeholders, all replaced with `json.dumps(...,
  ensure_ascii=False)`: `{{RADIANT_ROOT_JSON}}`, `{{NAME_JSON}}`,
  `{{DESCRIPTION_JSON}}`, `{{MODEL_JSON}}`, `{{INSTRUCTIONS_JSON}}`; and
  `{{INSTRUCTIONS}}`, the same text without escaping, for the Markdown body.
  The agent's instructions are assembled by the generator: role, absolute
  path of `skills/radiant-delegation/SKILL.md`, the role's anchor, the order
  "read your role's section and the package you received; do not delegate;
  return in the format of the Return section".

- [ ] **Step 1: write the failing tests**

Switch the `render` helper to `adapters/render_bootstrap.py` and add
`--adapter codex` to the existing global output test. New tests:

```python
def test_adapter_is_required(self):
    self.assertNotEqual(self.render().returncode, 0)

def test_codex_global_block_is_unchanged(self):
    template = (self.root / "adapters/codex/global.AGENTS.template.md").read_text()
    expected = template.replace("{{RADIANT_ROOT_JSON}}", json.dumps(str(self.root), ensure_ascii=False))
    self.assertEqual(self.render("--adapter", "codex").stdout, expected)

def test_claude_global_block_points_to_claude_adapter(self):
    out = self.render("--adapter", "claude-code").stdout
    self.assertIn("radiant:begin", out); self.assertIn("radiant:end", out)
    self.assertIn("adapters/claude-code/README.md", out)
    self.assertIn(str(self.root), out); self.assertLess(len(out.encode()), 1024)

def test_agents_render_one_file_per_profile(self):
    agents = json.loads((self.root / "skills/radiant-delegation/agents.json").read_text())["agents"]
    for adapter, ext in (("claude-code", ".md"), ("codex", ".toml")):
        with self.subTest(adapter=adapter):
            models = json.loads((self.root / f"adapters/{adapter}/capabilities.json").read_text())
            target = self.project / f"agents-{adapter}"
            self.assertEqual(self.render("--adapter", adapter, "--agents-dir", str(target)).returncode, 0)
            self.assertEqual(sorted(p.name for p in target.iterdir()),
                             sorted(a["name"] + ext for a in agents))
            for agent in agents:
                text = (target / (agent["name"] + ext)).read_text()
                self.assertIn(models[agent["capability"]], text)
                self.assertIn(str(self.root / "skills/radiant-delegation/SKILL.md"), text)
                self.assertNotIn(str(SOURCE), text)
                if adapter == "claude-code":
                    self.assertTrue(text.startswith("---\n"))
                    self.assertIn("disallowedTools: Agent", text)

@unittest.skipUnless(tomllib, "tomllib requires Python 3.11+")
def test_codex_agents_are_valid_toml(self):
    target = self.project / "agents"
    self.render("--adapter", "codex", "--agents-dir", str(target))
    for path in target.iterdir():
        data = tomllib.loads(path.read_text())
        self.assertEqual({"name", "description", "model", "developer_instructions"}, set(data))
        self.assertIn(str(self.root), data["developer_instructions"])

def test_agents_refuse_any_existing_or_symlinked_target(self):
    target = self.project / "agents"; target.mkdir()
    (target / "radiant-dev.md").write_text("keep\n")
    self.assertNotEqual(self.render("--adapter", "claude-code", "--agents-dir", str(target)).returncode, 0)
    self.assertEqual([p.name for p in target.iterdir()], ["radiant-dev.md"])
    self.assertEqual((target / "radiant-dev.md").read_text(), "keep\n")
    (target / "radiant-dev.md").unlink()
    (target / "radiant-grill.md").symlink_to(self.project / "elsewhere.md")
    self.assertNotEqual(self.render("--adapter", "claude-code", "--agents-dir", str(target)).returncode, 0)
    self.assertFalse((self.project / "elsewhere.md").exists())
```

At the top of the file: `try: import tomllib` / `except ImportError: tomllib = None`.

- [ ] **Step 2: run and watch it fail**

Run: `python3 -m unittest tests.test_integration -v`
Expected: FAIL (script still at the old path and without `--adapter`).

- [ ] **Step 3: move and generalize the generator**

`git mv adapters/codex/render_bootstrap.py adapters/render_bootstrap.py`;
`root = Path(__file__).resolve().parents[1]`. An internal table per adapter:
global template, agent template and extension. `--output` and `--agents-dir`
mutually exclusive. Refusal with a message in Portuguese and exit 1, in the
same style as the current one.

- [ ] **Step 4: create the templates**

`global.CLAUDE.template.md`: same format as the Codex block, pointing to
`adapters/claude-code/README.md` and `docs/capabilities.md`.
`agent.template.md`: frontmatter `name`, `description`, `model`,
`disallowedTools: Agent`, body `{{INSTRUCTIONS}}`.
`agent.template.toml`: the four keys, values through the `_JSON`
placeholders.

- [ ] **Step 5: update commands in `adapters/codex/README.md`**

`python3 adapters/render_bootstrap.py --adapter codex` and the variant with
`--output .local/codex-global.md`.

- [ ] **Step 6: run the global checks and watch them pass**

- [ ] **Step 7: commit**

```bash
git add adapters tests/test_integration.py
git commit -m "feat(adapters): render bootstrap and subagents for codex and claude code"
```

## Task 4: adapter documentation and neutral consumer map

**Files:**
- Create: `adapters/claude-code/README.md`
- Change: `adapters/codex/README.md`
- Move: `adapters/codex/project.AGENTS.template.md` → `templates/project-agents.md`
- Create: `CLAUDE.md` (root)
- Change: `templates/README.md`, `migration/README.md` (template link, line 28), `AGENTS.md`, `README.md`, `docs/capabilities.md`, `docs/integration.md`

**Interfaces:**
- Consumes: the CLI from Task 3, `capabilities.json` from Task 2.
- Produces: a harness-neutral `templates/project-agents.md`; `CLAUDE.md` with
  exactly one line, `@AGENTS.md`.

- [ ] **Step 1: write `adapters/claude-code/README.md`**

Same structure as the Codex README (Agent entry, Set up the user, Set up the
consumer) plus: Capabilities (link to `capabilities.json`, without repeating
IDs), Subagents (generate with `--agents-dir` into the user's agents
directory; regenerate after changing IDs; override through the invocation's
`model` parameter; `disallowedTools: Agent`), Local maintenance (a scheduled
task on the machine; cloud out of scope), Optional external procedures (a
role → suggested skill table, with the rule that output goes to the paths in
`.radiant.json`), undo (remove the block and the six `radiant-*` files).

- [ ] **Step 2: update `adapters/codex/README.md`**

Analogous Capabilities and Subagents sections; record that the file's `model`
wins, so an override runs in the orchestrator's session; rule 7 in the
agent's instructions. Change the consumer template link to
`../../templates/project-agents.md`.

- [ ] **Step 3: move and neutralize the consumer template**

`git mv adapters/codex/project.AGENTS.template.md templates/project-agents.md`.
Replace "read `adapters/codex/README.md`" with "read the README of the
adapter for the harness in use in `adapters/<harness>/`". Add: consumers on
Claude Code create `CLAUDE.md` with the line `@AGENTS.md`.

- [ ] **Step 4: `CLAUDE.md`, indexes and maps**

`CLAUDE.md` at the root with `@AGENTS.md`. `AGENTS.md`: cite both adapters
and the delegation skill. `README.md`: rows for `skills/radiant-delegation`,
`adapters/claude-code/` and `docs/adrs/`. `docs/capabilities.md`: rows
"Orchestrate roles and delegate" and "Set up the harness".
`docs/integration.md`: "Codex adapter" becomes "adapters" where the sentence
is generic. `templates/README.md` and `migration/README.md`: the template's
new path.

- [ ] **Step 5: run the global checks and watch them pass**

Additional expectation: `check_repository.py` with no broken link after the
move.

- [ ] **Step 6: commit**

```bash
git add -A adapters templates CLAUDE.md AGENTS.md README.md docs migration/README.md
git commit -m "docs(adapters): add claude code adapter and harness-neutral consumer map"
```

## Task 5: maintenance, contract and cycle pointers

**Files:**
- Create: `skills/radiant-maintenance/SKILL.md`
- Create: `templates/maintenance-report.md`
- Change: `templates/task-contract.md`, `skills/radiant-cycle/SKILL.md`,
  `skills/radiant-delegation/SKILL.md`, `docs/integration.md`,
  `docs/learn-back.md`, `docs/verification.md`, `templates/README.md`,
  `docs/capabilities.md`

**Interfaces:**
- Consumes: the `maintenance` field (Task 1), the `### Maintenance` section
  (Task 2).
- Produces: the `Capability` field in the Task Contract; the report format.

- [ ] **Step 1: write `skills/radiant-maintenance/SKILL.md`**

Frontmatter as in Task 2. Content of section 3 of the ADR: entry (read
`.radiant.json`, the workflow and its Maintenance section; without
`maintenance`, `HOLD`), sources, declared policy (safe commands, authorized
egress, recorded omissions), prioritization by risk, value and
reversibility, comparison with the previous report, up to three embedded
drafts, boundary (only write: the report; create the directory if missing; no
branch, PR, issue or commit), capabilities (`light` collection, `standard`
prioritization and orchestrator), "nothing material" as a valid result. Link
the delegation skill and the template.

- [ ] **Step 2: write `templates/maintenance-report.md`**

Metadata (date, Radiant revision, consumer commit, effective capability and
model), Sources (consulted, skipped by policy, failed), Candidates (table:
local ID, category, evidence, risk, value, reversibility, state
new/recurring/resolved), Drafts (up to three: goal, outputs, verification),
Omissions and limitations.

- [ ] **Step 3: `Capability` field in the Task Contract**

In `templates/task-contract.md`, after `Risk tier`:
`**Capability:** \`default | deep | standard | light\` - one-line justification when different from default`.
In section 16, without a format change: a note that it is the Build's return
according to the delegation skill.

- [ ] **Step 4: pointers**

`radiant-cycle`: at the entry, "to coordinate roles and delegate, read
radiant-delegation"; in Verify, a pointer to the acceptance rule; bump
`metadata.version` to `0.1.3`. `radiant-delegation`: replace the path in code
with the link to the maintenance skill. `docs/integration.md`: replace the
path in code with the link. `docs/learn-back.md`: rows for
`skills/radiant-delegation/`, `skills/radiant-maintenance/` and
`adapters/claude-code/`. `docs/verification.md`: simulation D (a new Claude
Code session finds the bootstrap, adapter, pin, Constitution and delegation
skill) and a "Harness agnosticism" row in the table. `templates/README.md`
and `docs/capabilities.md`: an entry for the maintenance report.

- [ ] **Step 5: run the global checks and watch them pass**

- [ ] **Step 6: commit**

```bash
git add skills templates docs
git commit -m "feat(maintenance): add propose-only maintenance skill and report template"
```

## Task 6: final verification of the delivery

**Files:**
- Change: `docs/adrs/ADR-0001-delegation-roles.md` only if verification
  reveals a material divergence from the implementation.

- [ ] **Step 1: full checks**

```bash
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check origin/main...HEAD
```

Expected: PASS and all tests OK; no whitespace warning.

- [ ] **Step 2: readback of the generated artifacts**

Generate both agent sets and both global blocks in a scratchpad directory and
reread each file: the right model per capability, the path of the real
checkout, instructions without copied rules. Do not install into global
directories.

- [ ] **Step 3: simulations A to D from `docs/verification.md`**

Walk each simulation from the root and record in the delivery summary the
paths actually reached.

- [ ] **Step 4: ADR coverage**

Check the ADR's "Planned files" table against `git diff --stat
origin/main...HEAD`. A missing item: go back to the owning task. An extra
item: justify or remove it.

- [ ] **Step 5: report**

State `DONE`, `HOLD` or `FAIL`, commands and results, limitations (tests do
not prove model obedience; the real session is left for the pilot) and next
steps that depend on the owner: push, PR, installing the subagents and
TC-0019 in AIKM.
