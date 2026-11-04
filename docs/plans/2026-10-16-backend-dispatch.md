# Backend dispatch: implementation plan

> **For executing agents:** use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to run this plan task by task.
> The steps use checkboxes (`- [ ]`) for tracking.

**Goal:** implement in Radiant the part of ADR-0002 that is process: the
execution split in the contract, the requirements vocabulary, the adapters'
`provides`, the routing rules format, backend dispatch in the delegation skill
and the boundary records, with validators that read restricted YAML.

**Architecture:** two new modules in `validators/`, standard library only:
`radiant_yaml.py` reads a strict subset of YAML, and `dispatch_formats.py`
validates units, `provides` and routing rules. `check_repository.py` uses them
to check the vocabulary, the adapters, the template's example and the routing
example. The rest is text and data.

**Stack:** Python 3.9+ with the standard library only, Git, Markdown, JSON and
the restricted YAML defined in Task 1.

**Spec:** [ADR-0002](../adrs/ADR-0002-backend-dispatch-demerzel.md)

**Outside this plan:** Demerzel's repository, Frame, Spec, Plan and code (they
get a plan in their own repository, after the merge); push and PR; the "Where
each piece of information lives" table already present in
`docs/integration.md`, which goes in its own commit and PR before Task 1.

## Global constraints

- Python 3.9+, no external packages. No `match`, and no types with `|`; use
  `typing.Optional` and `typing.List` when annotating.
- New text in Portuguese, plain hyphen, no em dash and no horizontal
  dividers.
- Capabilities exactly `deep`, `standard`, `light`, read from `CAPABILITIES`
  in `check_repository.py`.
- Initial vocabulary exactly `browser`, `ios-simulator`, `computer-use`.
- Both adapters' `provides.json` start with an empty list: each item only
  comes in with smoke evidence in a terminal (ADR-0002, section 2).
- Units block: fence ` ```yaml radiant-units `, at most one per file.
- Unit ID: `^TC-\d{4}\.[1-9]\d*$`, all with the same `TC-xxxx` prefix.
- Routing rules: `schema` equal to `1`; rule ID `^[a-z0-9]+(-[a-z0-9]+)*$`;
  `approval` only accepts `"human"`; `harness` is the name of a directory in
  `adapters/`.
- Location of the routing instance: `$XDG_CONFIG_HOME/radiant/routing.json`,
  or `~/.config/radiant/routing.json` without the variable.
- Do not renumber the contract template's sections: the delegation skill cites
  section 16.
- Commits in Conventional Commits, without agent co-authorship.
- After each task: `python3 validators/check_repository.py`,
  `python3 -m unittest discover -s tests -v` and `git diff --check` pass.

## Review focus

1. A plain scalar with `: ` or ` #` in the middle, such as
   `done_when: passa: ok`: an error asking for quotes, never silent
   truncation. Test in Task 1.
2. A repeated key in a mapping: an error with the line, instead of keeping the
   last value as ordinary YAML does. Test in Task 1.
3. `writes` overlap between independent units with different spellings:
   `src/sync` and `src/sync/` overlap; `src/sync/` and `src/sync2/` do not.
   Test in Task 3.
4. A cycle in `depends_on` (`.1` → `.2` → `.1`): an error, never an infinite
   loop. Test in Task 3.
5. Two `radiant-units` blocks in the same file: an error, never the first one
   silently. Test in Task 3.

### Task 1: restricted YAML reader

**Files:**
- Create: `validators/radiant_yaml.py`
- Create: `tests/test_radiant_yaml.py`
- Modify: `contracts/README.md` (new "Execution units" section with the
  definition of the subset)

**Interfaces:**
- Produces: `radiant_yaml.load(text: str) -> object`, which returns a `dict`,
  `list`, `str`, `int`, `bool` or `None`; and `radiant_yaml.YamlError(ValueError)`,
  whose message starts with `linha <n>: `.

The subset accepts: block mappings with keys `[A-Za-z_][A-Za-z0-9_-]*`; block
sequences (`- item`), including `- key: value` with continuation aligned to
the key; flow lists of scalars (`[a, b]`, `[]`) without nesting; plain
scalars, double-quoted (escapes `\"`, `\\`, `\n`) or single-quoted (`''` as a
quote); typed `true`, `false`, `null` and integers; `#` comments at the start
of a line or after a space outside quotes; indentation with spaces only. It
refuses: tabs in indentation, repeated keys, `&`, `*`, `!`, `|`, `>`, `{`,
`---`, a plain scalar with `: ` or ending in `:`, and a plain scalar spanning
several lines.

- [ ] **Step 1: write the failing tests**

In `tests/test_radiant_yaml.py`, import the module by inserting
`SOURCE / "validators"` into `sys.path`, with a `RadiantYamlTests` class:

```python
def test_units_example_round_trip(self):
    data = load("units:\n  - id: TC-0025.1\n    requires: []\n    writes: [src/a/, tests/a/]\n    capability: deep\n")
    self.assertEqual(data, {"units": [{"id": "TC-0025.1", "requires": [],
        "writes": ["src/a/", "tests/a/"], "capability": "deep"}]})

def test_scalars_are_typed(self):
    self.assertEqual(load("a: true\nb: null\nc: 3\nd: '3'\ne: \"x # y\"\n"),
                     {"a": True, "b": None, "c": 3, "d": "3", "e": "x # y"})

def test_comments_are_ignored(self):
    self.assertEqual(load("# top\na: b  # end\n"), {"a": "b"})

def test_plain_scalar_with_colon_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 1: .*aspas"):
        load("done_when: passa: ok\n")

def test_duplicate_key_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 2: .*repetida"):
        load("a: 1\na: 2\n")

def test_tab_indentation_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 2: .*tab"):
        load("a:\n\t- b\n")

def test_unsupported_features_are_refused(self):
    for text in ("a: &x 1\n", "a: *x\n", "a: !tag 1\n", "a: |\n  b\n", "a: {b: 1}\n", "---\na: 1\n", "a: [[b]]\n"):
        with self.subTest(text=text), self.assertRaises(YamlError):
            load(text)
```

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_radiant_yaml -v`
Expected: ERROR with `ModuleNotFoundError: No module named 'radiant_yaml'`.

- [ ] **Step 3: implement `load` in `validators/radiant_yaml.py`**

A recursive parser by indentation over the list of lines without comments.
Each level knows its column and returns `(value, next line)`. Remove comments
with a scanner that respects quotes before any other rule.

- [ ] **Step 4: confirm they pass**

Run: `python3 -m unittest tests.test_radiant_yaml -v`
Expected: 7 tests OK.

- [ ] **Step 5: document the subset**

In `contracts/README.md`, an "Execution units" section with one paragraph:
the `radiant-units` block uses restricted YAML, read by
`validators/radiant_yaml.py`; list what is accepted and what is refused, as
above. Every file valid in this subset is valid YAML, so readers with a full
parser, such as Demerzel, read the same value.

- [ ] **Step 6: commit**

```bash
git add validators/radiant_yaml.py tests/test_radiant_yaml.py contracts/README.md
git commit -m "feat(validators): read a strict YAML subset with the standard library"
```

### Task 2: requirements vocabulary and the adapters' `provides`

**Files:**
- Create: `validators/dispatch_formats.py`
- Create: `skills/radiant-delegation/requirements.json`
- Create: `adapters/claude-code/provides.json`, `adapters/codex/provides.json`
- Create: `tests/test_dispatch_formats.py`
- Modify: `validators/check_repository.py` (function `check_dispatch(errors)`,
  called in `check()` right after `check_delegation`)
- Modify: `tests/test_repository.py`

**Interfaces:**
- Produces: `dispatch_formats.load_requirements(path: Path) -> Set[str]`,
  which reads `{"requirements": {"<term>": "<description>"}}` and raises
  `ValueError` on an invalid format; `dispatch_formats.validate_provides(data:
  object, requirements: Set[str]) -> List[str]`, which only accepts
  `{"provides": [<term>, ...]}` without repetition and returns the error
  messages.
- Produces: `check_dispatch(errors: list) -> None` in `check_repository.py`,
  which Tasks 3 and 4 extend.

- [ ] **Step 1: write the failing tests**

In `tests/test_dispatch_formats.py`, class `ProvidesTests`:
`validate_provides({"provides": ["browser"]}, {"browser"}) == []`;
`{"provides": ["turbo"]}` produces a message containing `'turbo'`;
`{"provides": ["browser", "browser"]}` produces one containing `repetido`;
`{"outros": []}` produces one containing `provides`.

In `tests/test_repository.py`, in the `RepositoryCheckTests` class:

```python
def test_provides_with_unknown_requirement_fails(self):
    path = self.root / "adapters/codex/provides.json"
    path.write_text(json.dumps({"provides": ["turbo"]}), encoding="utf-8")
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/codex/provides.json", result.stderr)

def test_adapter_without_provides_fails(self):
    (self.root / "adapters/claude-code/provides.json").unlink()
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/claude-code", result.stderr)
```

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: an import ERROR in `test_dispatch_formats` and FAIL in the two new
repository tests.

- [ ] **Step 3: create the data**

`requirements.json` with the three terms and a one-line description each.
`browser`: needs to browse and inspect pages. `ios-simulator`: needs to run
and drive the iOS Simulator. `computer-use`: needs to control desktop apps.
Both `provides.json` with `{"provides": []}`.

- [ ] **Step 4: implement the functions and `check_dispatch`**

`check_dispatch` reads the vocabulary and, for each directory in `adapters/`,
requires a valid `provides.json`, with the relative path at the start of each
error, as `check_delegation` does.

- [ ] **Step 5: confirm they pass**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: all OK; validator at `PASS`.

- [ ] **Step 6: commit**

```bash
git add validators/ skills/radiant-delegation/requirements.json adapters/*/provides.json tests/
git commit -m "feat(delegation): declare requirements and what each adapter provides"
```

### Task 3: execution units in the contract template

**Files:**
- Modify: `validators/dispatch_formats.py`, `validators/check_repository.py`
- Modify: `templates/task-contract.md` (a `### Execution units` subsection at
  the end of section 4, without renumbering)
- Modify: `contracts/README.md` (integrity rules for the split)
- Modify: `tests/test_dispatch_formats.py`, `tests/test_repository.py`

**Interfaces:**
- Consumes: `radiant_yaml.load`, `YamlError` (Task 1); `load_requirements`,
  `check_dispatch` (Task 2).
- Produces: `dispatch_formats.extract_units_block(markdown: str) ->
  Optional[str]`, which returns the body of the single
  ` ```yaml radiant-units ` block, `None` without a block, and raises
  `ValueError` with `mais de um bloco` when there are two;
  `dispatch_formats.validate_units(data: object, agents: Dict[str, str],
  requirements: Set[str]) -> List[str]`, where `agents` maps profile name to
  default capability, read from `agents.json`.

Rules of `validate_units`, which is the normative schema of the ADR:
- a non-empty top level `{"units": [...]}`, without other keys;
- unit keys: `id`, `role`, `capability`, `capability_reason`, `requires`,
  `objective`, `writes`, `depends_on`, `done_when`; required `id`, `role`,
  `objective`, `writes`, `done_when`; an unknown key is an error;
- `id` follows the pattern in the global constraints, unique, the same prefix
  for all;
- `role` is a profile name in `agents`;
- `capability`, when present, is in `CAPABILITIES` and requires a non-empty
  `capability_reason`; `capability_reason` without `capability` is an error;
- `requires` is a list of vocabulary terms;
- `writes` is a non-empty list of relative POSIX paths, without `..` and
  without a leading `/`;
- `depends_on` only cites existing IDs, never its own, and the graph has no
  cycle;
- two units without a dependency path between them cannot have overlapping
  `writes`. Normalize by removing the trailing slash and compare by segment: a
  path overlaps another when it is equal to it or is its prefix followed by
  `/`;
- `objective` and `done_when` are non-empty strings.

- [ ] **Step 1: write the failing tests**

In `tests/test_dispatch_formats.py`, class `UnitsTests`, with a `VALID`
fixture that reproduces the two-unit example from section 2 of ADR-0002 and
`AGENTS = {"radiant-dev": "standard", "radiant-verifier": "deep"}`:

- `test_valid_units_pass`: `validate_units(VALID, AGENTS, {"browser"}) == []`.
- `test_overlap_between_independent_units_fails`: `.2` without `depends_on`
  and with `writes: [src/sources]` produces an error containing `sobrep`.
- `test_overlap_check_uses_segments`: `src/sync/` and `src/sync2/` in
  independent units produce no error.
- `test_dependency_cycle_fails`: `.1` depends on `.2` and `.2` on `.1`; an
  error containing `ciclo`, and the call terminates.
- `test_capability_requires_reason`: `capability: deep` without
  `capability_reason` produces an error containing `capability_reason`.
- `test_unknown_role_requirement_and_key_fail`: `role: radiant-x`,
  `requires: [turbo]` and a `harness` key each produce an error that cites
  the value or the key.
- `test_ids_must_share_prefix`: `TC-0025.1` with `TC-0026.2` produces an error
  containing `prefixo`.
- `test_escaping_write_path_fails`: `writes: [../x]` and `writes: [/x]`
  produce an error.
- `test_two_blocks_are_refused`: `extract_units_block` with two blocks raises
  `ValueError` containing `mais de um bloco`.

In `tests/test_repository.py`:

```python
def test_template_units_example_must_validate(self):
    path = self.root / "templates/task-contract.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("role: radiant-dev", "role: radiant-x", 1), encoding="utf-8")
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("templates/task-contract.md", result.stderr)
```

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: FAIL or ERROR in the new tests.

- [ ] **Step 3: implement `extract_units_block` and `validate_units`**

For the cycle and reachability, compute the transitive closure of
`depends_on` by depth-first search with visit marking; the same closure
decides which pairs are independent.

- [ ] **Step 4: write the subsection in the template**

`### Execution units` at the end of section 4: one paragraph saying the
subsection is optional and that, without it, the contract is a single unit;
the two-unit example from ADR-0002 inside the `yaml radiant-units` fence; a
pointer to `contracts/README.md#execution-units`. In
`contracts/README.md`, in the same section as Task 1, the integrity rules:
`id` stable and never renumbered; the sum of the units does not exceed the
contract; changing the split after the start is an amendment when the
boundary does not change and HOLD when it does.

- [ ] **Step 5: wire it into the validator**

`check_dispatch` extracts the block from `templates/task-contract.md`, reads
it with `radiant_yaml.load` and validates it with the profiles in
`agents.json`. `YamlError` and `ValueError` become an error with the
template's path at the start.

- [ ] **Step 6: confirm they pass**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: all OK; validator at `PASS`.

- [ ] **Step 7: commit**

```bash
git add validators/ templates/task-contract.md contracts/README.md tests/
git commit -m "feat(contracts): split a task contract into execution units"
```

### Task 4: routing rules format

**Files:**
- Create: `docs/routing.md`, `docs/routing.example.json`
- Modify: `validators/dispatch_formats.py`, `validators/check_repository.py`
- Modify: `tests/test_dispatch_formats.py`, `tests/test_repository.py`

**Interfaces:**
- Consumes: `check_dispatch` (Task 2).
- Produces: `dispatch_formats.validate_routing(data: object, adapters:
  Set[str]) -> List[str]`.

Rules: a top level with `schema`, `rules` and `default`, without other keys;
`schema` equal to `1`; `rules` is a list, possibly empty; a rule with `id`,
`when` and `use` required and `approval`, `why` optional; `id` follows the
pattern and is unique; `when` and `why` are non-empty strings; `use` and
`default` are non-empty lists of candidates; a candidate with `harness`
required in `adapters`, `capability` optional in `CAPABILITIES` and `effort`
optional as a non-empty string.

- [ ] **Step 1: write the failing tests**

Class `RoutingTests`: the ADR-0002 example passes with
`{"claude-code", "codex"}`; `harness: copilot` produces an error containing
`'copilot'`; `approval: "auto"` produces an error containing `approval`; two
equal `id`s produce an error containing `repetido`; `schema: 2` produces an
error containing `schema`. In `test_repository.py`,
`test_routing_example_with_unknown_harness_fails` replaces the first
`"claude-code"` of `docs/routing.example.json` with `"copilot"` and expects
exit code 1 with `docs/routing.example.json` in stderr.

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: FAIL or ERROR in the new tests.

- [ ] **Step 3: implement `validate_routing` and wire it into `check_dispatch`**

`adapters` are the names of the directories in `adapters/`.

- [ ] **Step 4: write `docs/routing.md` and the example**

`docs/routing.example.json` is the example from section 2 of ADR-0002.
`docs/routing.md` explains: the instance belongs to the user, at the location
in the global constraints, generated by dotfiles and outside any project; the
orchestrator chooses the rule with judgment, and the operator only filters
out candidates without an adapter or without the unit's requirements
(`provides.json`) and takes the first viable one; a candidate never uses a
capability below the unit's; an `effort` the harness does not accept is
recorded and left out of the launch; `approval: human` requires explicit
confirmation; each field, with the schema from Task 4.

- [ ] **Step 5: confirm they pass**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: all OK; validator at `PASS`.

- [ ] **Step 6: commit**

```bash
git add docs/routing.md docs/routing.example.json validators/ tests/
git commit -m "feat(routing): define user-level routing rules and validate the example"
```

### Task 5: backend dispatch in the delegation skill

**Files:**
- Modify: `skills/radiant-delegation/SKILL.md`

- [ ] **Step 1: write the "Backend dispatch" section**

After "Parallelism": dispatching through an external operator is an
alternative to the native subagent; the package is the contract path plus the
unit ID, as a pointer, plus the Radiant revision and absolute root; the
orchestrator chooses the routing rule, with a link to `../../docs/routing.md`,
and the operator resolves harness and model; requirements come from
`requirements.json`, and what each harness offers, from
`adapters/<harness>/provides.json`; the Build return is still the Completion
report, written to `.radiant/reports/<id>.md` in the worktree, a path the
consumer ignores in Git; rules 1 to 7 do not change.

- [ ] **Step 2: update the provenance and the version**

In "Provenance", the line per round now includes the harness and the dispatch
identifier when there is backend dispatch. `metadata.version` goes from
`0.1.1` to `0.2.0`.

- [ ] **Step 3: verify**

Run: `python3 validators/check_repository.py && python3 -m unittest discover -s tests -v`
Expected: `PASS` and all OK; the new section does not change the role
anchors checked by `check_delegation`.

- [ ] **Step 4: commit**

```bash
git add skills/radiant-delegation/SKILL.md
git commit -m "feat(delegation): dispatch execution units through a backend operator"
```

### Task 6: boundary records and the ADR's state

**Files:**
- Modify: `docs/integration.md` ("Demerzel boundary" section after "AIKM
  boundary")
- Modify: `docs/project-generation-system.md` (state note at the top of
  section 30)
- Modify: `docs/capabilities.md`, `README.md`, `docs/verification.md`
- Modify: `docs/adrs/ADR-0002-backend-dispatch-demerzel.md`

- [ ] **Step 1: write the records**

- "Demerzel boundary": Demerzel is a Radiant consumer that dispatches units
  through a backend; it reads contracts and the user's rules and writes only
  its dispatch log; it does not change contracts or merge, push or change
  scope; the dispatching consumer ignores `.radiant/reports/` in Git; Radiant
  works without it.
- A note in section 30, dated 2026-10-16, in the format of the note in
  section 20: Radiant defines how agentic flows are split, routed and
  accepted; execution and observation stay with the harnesses and an external
  operator; the text below remains as a record of thesis 0.2.
- `docs/capabilities.md`: a "Dispatch units through a backend" row pointing
  to the delegation skill and to `docs/routing.md`.
- `README.md`: a row for `docs/routing.md` in the "Find what you need" table.
- `docs/verification.md`: the validator also checks the vocabulary,
  `provides`, the template's units example and the routing example, and reads
  restricted YAML without dependencies.
- ADR-0002: an amendment dated 2026-10-16 recording that the validator reads
  the YAML subset with `validators/radiant_yaml.py`, at the owner's request,
  and that the planned files table includes `validators/radiant_yaml.py`,
  `validators/dispatch_formats.py`, `contracts/README.md` and the new tests.

- [ ] **Step 2: verify**

Run: `python3 validators/check_repository.py && python3 -m unittest discover -s tests -v && git diff --check`
Expected: `PASS`, all OK and no whitespace warning.

- [ ] **Step 3: commit**

```bash
git add docs/ README.md
git commit -m "docs: record the Demerzel boundary and backend dispatch"
```

### Task 7: living pages

Run after the merge, in `faelplg/design-systems`, in the
`radiant-design-system/docs/` folder, according to Radiant's `AGENTS.md`.

- [ ] **Step 1:** update the map, glossary and use cases with execution units,
  requirements, `provides`, routing, backend dispatch and Demerzel as a
  consumer.
- [ ] **Step 2:** run `build.py --check` and `build.py --artifact <dir>`
  without error.
- [ ] **Step 3:** commit and PR in that repository, with the owner's approval,
  and republish the three pages at their current URLs.
- [ ] **Step 4:** in Radiant, ADR-0002 becomes `accepted` with the reference
  to the PR and the merge commit, as with ADR-0001.
