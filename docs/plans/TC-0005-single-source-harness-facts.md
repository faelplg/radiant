# Radiant Task Contract - Radiant - Demerzel synergy / single source of harness facts

**Contract ID:** `TC-0005`\
**Template version:** `0.4`\
**Project:** `radiant`\
**Iteration:** `Demerzel synergy milestone, issue #35`\
**Status:** `READY` - proposal; it does not authorize the Build\
**Owner:** `Fael (human); Build by an authorized agent`\
**Risk tier:** `2` - the change reaches `validators/check_dispatch.py`, the dispatch gate Demerzel calls through its pin, the routing format every user's `routing.json` follows, and `check_repository.py`, the CI gate of every Radiant change\
**Capability:** `default`\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `none`\
**Entry commit:** recorded at activation; the planning baseline is `4e4ff16d43ea83c589b3557cea99227029f7769a`\
**Tracking:** [issue #35](https://github.com/faelplg/radiant/issues/35), sub-issue of epic [#30](https://github.com/faelplg/radiant/issues/30); related [#29](https://github.com/faelplg/radiant/issues/29) (open), [#63](https://github.com/faelplg/radiant/issues/63) (closed by PR #75), [#64](https://github.com/faelplg/radiant/issues/64) (open, out of scope) and [faelplg/demerzel#60](https://github.com/faelplg/demerzel/issues/60) (the consumer follow-up)

Routing: the Build runs as `radiant-dev` at `standard`, the build tier, on
the Codex harness. The independent critique runs as `radiant-verifier` at
`deep`, on a model from a vendor different from the Build's, as section 11
defines. Model IDs go only in the provenance lines of the Completion report,
as [radiant-delegation](../../skills/radiant-delegation/SKILL.md#provenance)
requires.

Activation: none yet. The owner answers the questions in
[section 5](#5-required-outputs) and authorizes the Build; the activation
commit then records the answers in [section 18](#18-owner-decisions), the
entry commit, the Demerzel commit of section 3 and the move out of `READY`.

## 1. Objective

> **Each adapter's `capabilities.json` and `provides.json` are the only place in Radiant that holds harness kinds, models and efforts; the routing format separates policy (unit type to capability and constraints) from resolution (to harness, model and effort); `docs/routing.example.json` validates in the new schema; and resolving today's rules, including the 2026-11-24 owner routing in `docs/routing.md`, gives the same harness, capability, model, effort and approval as at the planning baseline, as a golden table test shows for schema 1 and schema 2.**

## 2. Why this task exists

**Source plan/spec:**

- [Issue #35](https://github.com/faelplg/radiant/issues/35): goal, scope,
  out of scope and acceptance. The verifier-vendor rule lives only in
  [#64](https://github.com/faelplg/radiant/issues/64); Demerzel gets a note
  here and its change in
  [faelplg/demerzel#60](https://github.com/faelplg/demerzel/issues/60).
- [Issue #63](https://github.com/faelplg/radiant/issues/63), closed by PR #75:
  "#35 requires the same result as today, so today's routing has to be
  current first". [docs/routing.md](../routing.md#owner-routing-2026-11-24)
  and [the example](../routing.example.json) at the planning baseline are
  that "today".
- [Issue #29](https://github.com/faelplg/radiant/issues/29): the `agy`
  adapter has not landed; only `adapters/codex` and `adapters/claude-code`
  exist. Its 2026-11-24 comment records the `agy` assignments.
- [ADR-0002](../adrs/ADR-0002-backend-dispatch-demerzel.md), section
  "Routing rules format": the schema 1 format this contract evolves.
- [radiant-delegation](../../skills/radiant-delegation/SKILL.md#provenance):
  "Model IDs appear only in these reports and in the adapters."

**Hypothesis or risk reduced:**

- Today a harness fact changes in several places: a new effort level or a
  new harness touches Demerzel code, `adapters/render_bootstrap.py` and the
  docs, and a model rename touches `docs/routing.md` as well as the adapter
  (it happened on 2026-11-24). A routing rule also mixes "what this unit
  type needs" with "how this machine serves it", so a rule such as front end
  carries `capability: deep` only to reach one harness's larger model.
  Moving the facts into the adapter files and splitting the format makes
  each change land in one file, and lets `agy` arrive as adapter files.
- What would refute it: the split cannot reproduce today's resolution for
  every rule and unit floor, or keeping Demerzel working requires changing
  the shape of `capabilities.json` or of the `check_dispatch.py routing`
  output. The Build then stops on HOLD instead of changing the expected
  table or a consumer's reader.

## 3. Inputs

The agent may assume as input:

- the documents in section 2, [routing](../routing.md),
  [integration](../integration.md#demerzel-boundary),
  [the validators README](../../validators/README.md) and
  [verification](../verification.md);
- `adapters/*/capabilities.json`, `adapters/*/provides.json`,
  `adapters/render_bootstrap.py`, `validators/check_dispatch.py`,
  `validators/dispatch_formats.py`, `validators/check_repository.py` and
  their tests, as the code, output and test style to follow;
- the planning baseline's `docs/routing.example.json`, the schema 1 file
  that the golden table describes (section 11);
- Demerzel, read-only, at the commit the activation records. Planning read
  the `main` working tree at `67215da9f0b0c5b1beca1451f161872ff7d62645`;
  Demerzel's `.radiant.json` pins Radiant at
  `93d61c0e1f39025e55cc10049cc82c9854c04434`. Under question 10 (A), the
  Build reads Demerzel only with `git -C <checkout> show <commit>:<path>`,
  and the request supplies the checkout's absolute root; the contract does
  not carry it, because the repository check refuses personal paths.

The owner's `routing.json` is not an input of the Build: it lives in the
owner's dotfiles and #35 does not change it. Planning did not read its
content. Section 11 has the orchestrator, not the Build, check it read-only.

Do not infer missing inputs that would materially change the solution.

### Inventory of duplicated harness facts

Line references are to the planning baseline for Radiant and to the Demerzel
commit above.

| # | Fact | Where it is today | Problem | Fate in this contract |
| --- | --- | --- | --- | --- |
| 1 | Which harnesses exist | `adapters/render_bootstrap.py:9-14` (keys of `ADAPTERS`) and `:73` (`--adapter` choices); `validators/check_dispatch.py:20,46-47` (a directory with three files); `validators/check_repository.py:74,91,98` (any directory); Demerzel `src/herdr/backend.ts:16` (keys of `KIND`) and `:104` | Three Radiant definitions of "an adapter", two of them different, and a Python list next to them | One discovery function in `validators/adapters.py`; `render_bootstrap.py` uses it; Demerzel note |
| 2 | Harness CLI, the herdr launch kind | Demerzel `src/herdr/backend.ts:16` (`claude-code` to `claude`, `codex` to `codex`); ADR-0002 lines 51-55 list herdr kinds as history | Radiant does not hold it, so a consumer must | `provides.json` gains `cli` |
| 3 | Accepted effort levels | Demerzel `src/herdr/backend.ts:17-20`; Radiant accepts any non-empty text, `validators/dispatch_formats.py:172-174`; `docs/routing.md:28-29` describes dropping an unaccepted one | Radiant cannot say whether an effort is valid | `provides.json` gains `efforts` |
| 4 | Subagent rendering per harness | `adapters/render_bootstrap.py:10-13` (agent template, extension, read-only line) | A new adapter needs a Python edit | `provides.json` gains `subagents` |
| 5 | Model per capability | Source: `adapters/codex/capabilities.json:2-4`, `adapters/claude-code/capabilities.json:2-4`. Copies: `docs/routing.md:56-59,65-74` (model IDs, and the prose at `:65-70` that restates both maps); `docs/routing.example.json:8,14` (model IDs in `why`) | Each model rename edits docs too; the delegation skill keeps model IDs in adapters and reports | `capabilities.json` unchanged and read-only; the copies go under question 5 |
| 6 | Policy mixed with resolution | `docs/routing.example.json:4-36` (every rule's `use` names harness, capability and effort); `:19` (`capability: deep` only to reach the larger model, explained at `docs/routing.md:65-68`); format at `docs/routing.md:32-50`; validator at `validators/dispatch_formats.py:152-208` | A machine fact is restated in every rule that needs it | Schema 2, section 5 |
| 7 | The resolution algorithm | Described at `docs/routing.md:16-30`; implemented only in Demerzel `src/radiant/route.ts:23-64` | Radiant cannot test "same result as today" | A reference resolver in Radiant, used by the golden test |

Compatibility constraints, not duplicates, that the design keeps:

- Demerzel `src/radiant/catalog.ts:44-45` refuses a `capabilities.json`
  whose values are not all strings; `:46-47` reads only `provides` from
  `provides.json` and ignores other keys; `src/radiant/route.ts:56` reads
  `models[capability]`.
- Demerzel `src/radiant/validators.ts:144-169` reads the stdout of
  `check_dispatch.py routing` as `{rules: [{id, use, approval}], default}`
  with candidates `{harness, capability, effort}`, and `:28` matches the
  message text `harness without an adapter`.

## 4. Allowed scope

### Paths allowed to change

```text
adapters/codex/provides.json
adapters/claude-code/provides.json
adapters/codex/README.md
adapters/claude-code/README.md
adapters/render_bootstrap.py
validators/adapters.py
validators/routing_resolution.py
validators/dispatch_formats.py
validators/check_dispatch.py
validators/check_repository.py
validators/README.md
tests/test_adapters.py
tests/test_routing_resolution.py
tests/fixtures/routing-schema1.json
tests/test_dispatch_formats.py
tests/test_check_dispatch.py
tests/test_repository.py
tests/test_integration.py
docs/routing.md
docs/routing.example.json
docs/integration.md
docs/verification.md
docs/adrs/ADR-0004-routing-policy-and-resolution.md
docs/adrs/ADR-0002-backend-dispatch-demerzel.md
docs/plans/TC-0005-single-source-harness-facts.md
```

`validators/adapters.py`, `validators/routing_resolution.py`,
`tests/test_adapters.py`, `tests/test_routing_resolution.py` and
`tests/fixtures/routing-schema1.json` are new. The two ADR paths apply only
under question 9 (A), and `ADR-0002` then takes only its
`Partly superseded by` header line, as it did for ADR-0003. Adapter READMEs,
`docs/integration.md` and `docs/verification.md` take pointer sentences only.
In `tests/test_integration.py`, existing tests change only where they read
the adapter list.

### Paths read-only

```text
adapters/*/capabilities.json
adapters/*/agent.template.*
adapters/global.template.md
constitution/
skills/
templates/
engineering/
validators/check_project.py
validators/check_contract.py
validators/task_contracts.py
validators/practice_cards.py
validators/radiant_yaml.py
docs/adrs/ADR-0001-delegation-roles.md
docs/adrs/ADR-0003-demerzel-independent-core.md
docs/history/
docs/plans/ (every file except this contract)
README.md
docs/capabilities.md
the Demerzel checkout of section 3
the owner's routing.json
```

`adapters/global.template.md` stays read-only under question 8 (A).

### External systems allowed

- None for the Build. GitHub, through `gh`, only for the orchestrator to open
  this contract's PR after the owner authorizes it.

### Network

`DENIED` except the authorized push and PR.

### Execution units

```yaml radiant-units
units:
  - id: TC-0005.1
    role: radiant-dev
    requires: []
    objective: Move harness facts into each adapter provides.json and read adapters through one discovery module.
    writes: [adapters/codex/provides.json, adapters/claude-code/provides.json, adapters/render_bootstrap.py, validators/adapters.py, validators/dispatch_formats.py, validators/check_dispatch.py, validators/check_repository.py, tests/test_adapters.py, tests/test_dispatch_formats.py, tests/test_repository.py, tests/test_integration.py]
    depends_on: []
    done_when: The suite passes, rendered subagents match the entry commit byte for byte, and a fixture adapter passes every check with no code change.
  - id: TC-0005.2
    role: radiant-dev
    requires: []
    objective: Add routing schema 2 with policy separate from resolution, the fold and the reference resolver, and migrate the example.
    writes: [validators/dispatch_formats.py, validators/routing_resolution.py, validators/check_dispatch.py, validators/check_repository.py, docs/routing.example.json, tests/test_routing_resolution.py, tests/fixtures/routing-schema1.json, tests/test_dispatch_formats.py, tests/test_check_dispatch.py, tests/test_repository.py]
    depends_on: [TC-0005.1]
    done_when: The golden table test passes for schema 1 and schema 2, and schema 1 output is byte for byte the entry commit output.
  - id: TC-0005.3
    role: radiant-dev
    requires: []
    objective: Document the facts, the two schemas, the migration path and the note for Demerzel.
    writes: [docs/routing.md, docs/integration.md, docs/verification.md, validators/README.md, adapters/codex/README.md, adapters/claude-code/README.md, docs/adrs/ADR-0004-routing-policy-and-resolution.md, docs/adrs/ADR-0002-backend-dispatch-demerzel.md, docs/plans/TC-0005-single-source-harness-facts.md]
    depends_on: [TC-0005.2]
    done_when: The repository check passes and every inventory row of section 3 has its fate in the diff.
```

The units run in order; each depends on the one before, so their shared
paths do not overlap in time. Under question 9 (B), an amendment removes the
two ADR paths from TC-0005.3.

## 5. Required outputs

1. `adapters/<harness>/provides.json`, for both adapters: the harness facts
   of the data shape below, with `provides` unchanged.
2. `validators/adapters.py`: the one adapter discovery and fact reader that
   `check_dispatch.py`, `check_repository.py` and `render_bootstrap.py` use,
   with tests in `tests/test_adapters.py`.
3. `validators/dispatch_formats.py`: `validate_provides` for the new keys,
   and `validate_routing` for schema 1, unchanged, and schema 2.
4. `validators/routing_resolution.py`: `fold`, from schema 2 to the
   schema 1 shape, and `resolve`, the reference implementation of the
   algorithm in `docs/routing.md`, with the golden table test in
   `tests/test_routing_resolution.py` and its baseline in
   `tests/fixtures/routing-schema1.json`.
5. `validators/check_dispatch.py`: `routing` accepts both schemas; its
   output follows question 2.
6. `docs/routing.example.json` in schema 2.
7. Docs: `docs/routing.md` (facts, both schemas, how they are applied,
   migration), the Demerzel note in `docs/integration.md`,
   `validators/README.md`, pointers in the adapter READMEs and
   `docs/verification.md`, and, under question 9 (A), ADR-0004.

Do not create additional artifacts without an observed need.

### Data shape: adapter facts

`capabilities.json` keeps its shape and values: exactly `deep`, `standard`
and `light`, each mapped to one full model ID. It stays the only place for
models, and Demerzel's `catalog.ts:44-45` and `render_bootstrap.py` keep
reading it unchanged.

`provides.json` (question 1, option A) gains three required keys:

| Key | Rule |
| --- | --- |
| `provides` | Unchanged: requirement terms from `requirements.json` |
| `cli` | Non-empty text without whitespace: the command that starts the harness, which is also the herdr launch kind |
| `efforts` | List of unique, non-empty effort levels the harness CLI accepts, from lowest to highest; may be empty when the harness has no effort control |
| `subagents` | `null` when Radiant renders no subagents for the harness; otherwise `{template, extension, read_access}`: a template file in the adapter's directory, an extension starting with `.`, and the text a read-only profile gets |

For the two adapters, values move from where they are today, with no new
fact:

```json
{
  "provides": [],
  "cli": "codex",
  "efforts": ["minimal", "low", "medium", "high", "xhigh"],
  "subagents": {
    "template": "agent.template.toml",
    "extension": ".toml",
    "read_access": "sandbox_mode = \"read-only\"\n"
  }
}
```

```json
{
  "provides": [],
  "cli": "claude",
  "efforts": ["low", "medium", "high", "xhigh", "max"],
  "subagents": {
    "template": "agent.template.md",
    "extension": ".md",
    "read_access": "tools: Read, Grep, Glob, WebFetch, WebSearch\n"
  }
}
```

`cli` and `efforts` come from Demerzel `src/herdr/backend.ts:16-20`, whose
comment says they are "only effort levels already checked on the installed
CLI"; `subagents` comes from `adapters/render_bootstrap.py:10-13`.

An adapter is a directory in `adapters/` with `README.md`,
`capabilities.json` and `provides.json`, as `check_dispatch.py:44-47` already
says; `check_repository.py` keeps reporting a directory that misses one of
them, as its current tests require.

### Data shape: routing schema 2

```json
{
  "schema": 2,
  "policy": {
    "rules": [
      { "id": "build", "when": "Standard implementation and Build units",
        "resolve": "implementation", "why": "Owner routing (2026-11-24): Codex at medium effort" },
      { "id": "bug-fix", "when": "Bug investigation and fix units",
        "resolve": "investigation",
        "why": "High effort first; after 2 failures the orchestrator may escalate effort or switch harness (retry policy, not expressed by the static fallback list)" },
      { "id": "frontend", "when": "Front-end interface units",
        "resolve": "interface", "why": "Claude Code at medium effort on its deep model" },
      { "id": "plans-and-contracts", "when": "Planning and non-docs Task Contracts",
        "capability": "deep", "resolve": "judgment",
        "why": "Second opinion uses agy once its adapter exists" },
      { "id": "independent-critique", "when": "Critique of a Codex Build",
        "capability": "deep", "approval": "human", "resolve": "judgment",
        "why": "Stand-in until the agy adapter can serve this rule" }
    ],
    "default": "implementation"
  },
  "resolution": {
    "implementation": [{ "harness": "codex", "effort": "medium" }],
    "investigation": [{ "harness": "codex", "effort": "high" }],
    "interface": [{ "harness": "claude-code", "capability": "deep", "effort": "medium" }],
    "judgment": [{ "harness": "claude-code", "effort": "high" }]
  }
}
```

The `why` texts above follow question 5 (A); each `id` and `when` is the
planning baseline's, so the golden table compares them.

| Field | Rule |
| --- | --- |
| `schema` | `1` or `2`; any other value is refused |
| `policy` | Exactly `rules` and `default` |
| `policy.rules[]` | Exactly the keys `id`, `when`, `resolve` and the optional `capability`, `approval` and `why`; `id`, `when`, `approval` and `why` keep their schema 1 rules |
| `policy.rules[].capability` | Optional: the capability this unit type resolves at, used by every candidate of its resolution that has no capability of its own. A policy constraint: "plans need judgment" |
| `policy.rules[].resolve`, `policy.default` | The name of an entry in `resolution` |
| `resolution` | Kebab-case names to non-empty candidate lists; every entry is referenced by a rule or by `default` |
| candidate | Exactly the schema 1 keys `harness`, `capability` and `effort`. A candidate's `capability` is harness-specific resolution, such as front end on `claude-code`, and is never below the `capability` of a rule that references the entry. Under question 3 (A), an `effort` outside the adapter's `efforts` is refused |

Model IDs stay out of both schemas; the model comes from the adapter's
`capabilities.json` for the resolved capability.

`fold` turns schema 2 into the schema 1 shape: each policy rule becomes
`{id, when, use, approval?, why?}`, where `use` is its resolution's
candidate list and each candidate without `capability` takes the rule's
`capability` when the rule has one; `default` becomes its resolution's list.
The fold loses nothing that resolution uses, so one resolver serves both
schemas, and the folded view is the output question 2 (A) proposes.

`resolve(view, rule_id or none, floor, requires, adapters)` follows
`docs/routing.md:16-30` and Demerzel `route.ts:23-64`: walk the rule's
candidates, or `default` without a rule; skip a harness without an adapter,
one whose `provides` does not cover `requires` and one whose capability,
the candidate's or else the floor, is below the floor; the first viable
candidate gives `{harness, capability, model, effort, approval}`, where
`model` is the adapter's `capabilities.json` value and an effort outside the
adapter's `efforts` is returned as omitted with its reason. Without a viable
candidate it returns `HOLD` with one reason per candidate. An unknown rule
id is an error, not `default`. Choosing the rule stays orchestrator
judgment, as today.

### Backward compatibility and migration

- **Schema 1 keeps validating and resolving.** `check_dispatch.py routing`
  on a schema 1 file prints the same bytes as at the entry commit, and
  `resolve` gives the golden table for it. No existing `routing.json`
  breaks, including the owner's, which stays on schema 1 until the owner's
  dotfiles migrate it in their own change, outside this contract, as #29
  also leaves it.
- **Demerzel at its current pin** (`93d61c0`) sees nothing until it bumps
  the pin ([no silent update](../integration.md#no-silent-update)).
- **Demerzel after a pin bump, before #60.** `capabilities.json` keeps its
  shape, so `catalog.ts:44-45` reads it; `catalog.ts:46-47` ignores the new
  `provides.json` keys; under question 2 (A), `check_dispatch.py routing`
  prints the schema 1 shape for either schema, so `validators.ts:144-169`
  reads it and `route.ts` resolves as before; the message
  `harness without an adapter` keeps its text. Under question 2 (B),
  Demerzel refuses a schema 2 file loudly, with `routing-invalid`, until #60
  reads the new output; schema 1 files keep working.
- **AIKM and other consumers** reach Radiant through the pin,
  `check_project.py` and the opt-in `check_contract.py`; neither changes.
  Planning did not inspect AIKM.
- **Migration path:** (1) this contract lands with both schemas;
  (2) faelplg/demerzel#60 reads `cli` and `efforts` and bumps its pin;
  (3) the owner's dotfiles move `routing.json` to schema 2, following the
  per-rule mapping `docs/routing.md` gains: each schema 1 rule becomes a
  policy rule with the same `id`, `when`, `approval` and `why`, whose
  `resolve` names an entry holding its `use` list; (4) removing schema 1
  follows question 7.

### Adding an adapter, and checking it without `agy`

With this design, adding a harness whose CLI serves one model per Radiant
capability needs only its directory: `README.md`, `capabilities.json`,
`provides.json` and, when `subagents` is not `null`, its agent template. No
validator, resolver, renderer, schema or test changes. Two limits remain,
stated rather than hidden: the navigation pointers that already name each
adapter (the global block, which `check_repository.py:73-76` checks under
question 8 (A), `README.md` and `docs/capabilities.md`) get one line each;
and a harness that needs more than one model per capability, which `agy`
may, depends on question 6.

Without an `agy` adapter, a test proves the property on a fixture: in an
isolated copy of the tree, as `tests/test_repository.py` builds, it adds
`adapters/fixture-harness/` with the three files and a template, plus the
global block line, and shows that `check_repository.py` passes,
`check_dispatch.py routing` accepts schema 1 and schema 2 files naming it,
`resolve` returns its model and effort, and `render_bootstrap.py --adapter
fixture-harness` renders its subagents, with no file outside
`adapters/fixture-harness/` and that one line changed.

### Note for Demerzel

The follow-up is [faelplg/demerzel#60](https://github.com/faelplg/demerzel/issues/60),
in its own repository and session; this Build changes no Demerzel file. The
note, which `docs/integration.md` points to from the Demerzel boundary, says
what Radiant now offers:

- `src/herdr/backend.ts:16` (`KIND`) can read `cli` and
  `src/herdr/backend.ts:17-20` (`EFFORT`) can read `efforts` from
  `adapters/<harness>/provides.json` of the pinned checkout, and the harness
  list can come from the adapters it finds.
- Launch mechanics stay Demerzel's: the flags in `modelArgs`
  (`src/herdr/backend.ts:237-245`) and the Claude Code worktree hook
  (`:233`, `:375`) are backend code, not harness facts. A harness listed by
  Radiant without launch code in the backend is refused with a message that
  names it.
- `src/radiant/route.ts:23-64` repeats the resolution algorithm; whether it
  calls a Radiant command instead follows question 4.

### Questions for the owner

Each question is a plain choice; option (A) is the recommended one. The
Build does not start until the owner answers them, and the answers go into
[section 18](#18-owner-decisions).

1. **Where the new harness facts live.**
   - (A) In `provides.json`, as section 5 shows. Consequence: the issue's
     two files hold every fact; Demerzel's current reader ignores the new
     keys; `provides.json` holds more than requirement terms.
   - (B) In a new `adapters/<harness>/harness.json`. Consequence: a file
     per concern, but a third file the issue did not name, and every
     discovery rule and test gains it.
2. **What `check_dispatch.py routing` prints for schema 2.**
   - (A) The folded schema 1 shape, `{"schema": 2, "rules": [...], "default": [...]}`.
     Consequence: Demerzel dispatches a schema 2 file with no code change;
     the success output is a derived view, not the parsed file, and the
     docstring and README say so.
   - (B) The parsed schema 2 value. Consequence: the output stays "the
     parsed value"; Demerzel refuses schema 2 files until #60 adapts.
3. **An effort the adapter does not list, in schema 2.**
   - (A) Refused by validation, naming the rule, harness and effort.
     Consequence: a typo fails before dispatch; a CLI that gains an effort
     level waits for the adapter update. Schema 1 keeps accepting any
     non-empty effort.
   - (B) Accepted, and `resolve` omits it with a reason, as schema 1 does.
     Consequence: one behavior for both schemas; mistakes surface only at
     dispatch.
4. **How the reference resolver is exposed.**
   - (A) As a library function used by the tests only. Consequence: the
     golden table is checkable now; Demerzel keeps `route.ts`; a command is
     decided with #60.
   - (B) Also as `check_dispatch.py resolve <rule|-> --capability <c> [--requires <term>...] [rules]`.
     Consequence: #60 can drop its copy of the algorithm; one more public
     command and output to keep stable.
5. **Model IDs outside the adapters.**
   - (A) `docs/routing.md` and the example name no model ID: the owner
     routing section names harness, capability tier and effort, points to
     the adapters for models, and points to #29's 2026-11-24 comment for the
     `agy` assignments until that adapter lands. Consequence: a model rename
     touches only the adapter; the dated section is rewritten in place.
   - (B) The "Owner routing (2026-11-24)" section, merged in PR #75, stays
     as written. Consequence: the owner's record stays word for word; the
     model IDs there stay a copy to update by hand.
6. **More than one model per capability, which `agy` may need.**
   - (A) Not in this contract. Both current adapters serve one model per
     capability; #29 settles `agy`'s model and effort facts on the CLI and,
     if it needs more, adds an adapter-declared field with its own tests.
     Consequence: no unverified shape now; until then, the "adapter files
     only" property holds for one-model-per-capability harnesses.
   - (B) Add now an optional adapter-declared map of named model variants,
     selectable by a resolution candidate. Consequence: `agy` arrives as
     adapter files only, but the shape is designed before the `agy` facts
     are checked, and Demerzel at its current code would launch the
     capability's model instead of a variant until #60.
7. **How long schema 1 is accepted.**
   - (A) With no end date; removing it needs a later owner decision and its
     own issue, after Demerzel and the dotfiles move. Consequence: nothing
     breaks; two readers stay in the validator.
   - (B) Deprecated now, with removal planned before the v1.0.0 tag
     ([#54](https://github.com/faelplg/radiant/issues/54)). Consequence: a
     date to plan by; the owner's `routing.json` must move first.
8. **The adapter list in the global bootstrap block.**
   - (A) Kept as a hand-written line, which `check_repository.py:73-76`
     already checks. Consequence: a new adapter adds one line there; the
     block every user copies does not change.
   - (B) Rendered from adapter facts. Consequence: no manual line, but every
     user's global block changes at the next render, and the adapter needs a
     display name fact.
9. **ADR.**
   - (A) A new ADR-0004 records the policy and resolution split and the
     harness facts, and partly supersedes ADR-0002's "Routing rules format";
     ADR-0002 gets only its `Partly superseded by` header line. Consequence:
     the structural decision lives where `AGENTS.md` says structural
     decisions live.
   - (B) No ADR; `docs/routing.md` and this contract record it.
     Consequence: one document fewer; ADR-0002 keeps describing schema 1
     only.
10. **Demerzel compatibility probe.**
    - (A) The Build reads, read-only, `src/radiant/catalog.ts`,
      `src/radiant/validators.ts`, `src/radiant/route.ts` and
      `src/herdr/backend.ts` at the Demerzel commit recorded at activation,
      confirms the line references of section 3, and reports in section 16.
      Consequence: the compatibility tests mirror the real readers; the
      sandbox needs read access to that checkout.
    - (B) No probe; the compatibility tests mirror the references as planned.
      Consequence: no consumer access; a drift in Demerzel since planning is
      found at its pin bump.

### Build order

Each step is one commit; after each, every automated check of section 11
passes. New files are staged before the full test run:
`tests/test_repository.py` copies only `git ls-files` into its fixtures.

1. **Adapter facts, test-first (TC-0005.1).** Tests for discovery, the new
   `provides.json` rules, render output and the fixture adapter; see them
   fail; implement; see them pass. Commit:
   `refactor(adapters): hold harness facts in provides.json`.
2. **Schema 2 and the golden table, test-first (TC-0005.2).** Add the
   baseline fixture first and the golden test against schema 1, which
   fails only because `routing_resolution.py` does not exist; then schema 2
   validation, fold and resolver; then migrate the example. Commit:
   `refactor(routing): separate policy from resolution in schema 2`.
3. **Docs (TC-0005.3).** Commit:
   `docs(routing): document harness facts and routing schema 2`.

## 6. Non-goals

This task must **not**:

- add or check the rule that the verifier's vendor differs from the
  author's, or any vendor constraint; that is #64;
- add the `agy` adapter or any `agy` fact (#29);
- change any file in Demerzel, AIKM or another consumer, or the owner's
  `routing.json` or dotfiles;
- change any `capabilities.json` value or shape, any agent template or the
  subagents and global block that `render_bootstrap.py` produces;
- change `check_project.py`, `check_contract.py` or their output;
- add policy constraints other than `capability` and `approval`, such as
  `requires` per rule;
- add a schema 1 to schema 2 conversion command;
- update the living pages in `faelplg/design-systems`; `AGENTS.md` asks for
  that after an adapter or ADR change, so the orchestrator tracks it as a
  follow-up issue.

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

# 7. Functional requirements

- [ ] `validators/adapters.py` lists as adapters exactly the directories of `adapters/` that hold `README.md`, `capabilities.json` and `provides.json`, and reads each one's models and facts; `check_dispatch.py`, `check_repository.py` and `render_bootstrap.py` use it, and no adapter name is written in their code.
- [ ] `provides.json` without `cli`, `efforts` or `subagents`, with an unknown key, a `cli` with whitespace, a repeated or empty effort, or a `subagents` whose template is not a file of that adapter, is refused, naming the file and the key.
- [ ] `render_bootstrap.py --adapter` offers the adapters whose `subagents` is not `null`, and for codex and claude-code renders files byte for byte equal to the entry commit's.
- [ ] A schema 1 `routing.json` validates with the same errors as at the entry commit, and `check_dispatch.py routing` prints the same bytes for it.
- [ ] A schema 2 file is refused, naming the rule or entry, for: an unknown key at any level, a `resolve` or `default` naming no entry, an unreferenced entry, a rule `capability` outside the three, a candidate capability below a referencing rule's capability, a harness without an adapter (with the text `harness without an adapter`), and, under question 3 (A), an effort outside the adapter's `efforts`.
- [ ] `fold` of a schema 2 file gives the schema 1 shape, with the rule's `capability` on each candidate that lacks one; `fold` of the new example equals the baseline fixture in every field except `schema` and `why`.
- [ ] `resolve` gives the golden table of section 11 for the baseline fixture and for the new example, for every rule and default, every floor and `requires` of `[]` and `["browser"]`; an unknown rule id is an error.
- [ ] `check_dispatch.py routing` on a schema 2 file prints the output question 2 chose.
- [ ] `docs/routing.example.json` is schema 2 and passes `check_repository.py` and `check_dispatch.py routing`.
- [ ] Adding the fixture adapter of section 5 needs no change outside its directory and the global block line.
- [ ] After the Build, the Radiant tree outside `adapters/*/capabilities.json`, `docs/plans/` and `docs/history/` names no model ID, under question 5 (A).

# 8. Engineering Check

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED`       | Three facts in an existing file, one discovery module, one schema with a fold back to the old shape; no variants, no new command unless the owner asks | Diff review against section 5 |
| EB-02 Correctness and contracts   | `REQUIRED`       | Same resolution for every rule, floor and requirement set; schema 1 output byte for byte; Demerzel's readers keep their inputs | Golden table test; byte comparison in section 11 |
| EB-03 Verification and tests      | `REQUIRED`       | Test-first, failing-before evidence, mutation proof of every new rule and of the golden test | Commands in section 11 |
| EB-04 Security and privacy        | `REQUIRED`       | Validators stay read-only; a `subagents.template` never leaves its adapter directory; the owner's file is read only by the orchestrator | Tests with `../` and absolute template paths; readback |
| EB-05 Maintainability             | `REQUIRED`       | Each fact in one file; resolution in one function; no adapter name in code | `rg` for adapter names in `validators/` and `adapters/render_bootstrap.py`; review |
| EB-06 Dependencies                | `REQUIRED`       | Standard library only | Diff review |
| EB-07 Diagnosis                   | `REQUIRED`       | Every refusal names the file, rule or entry and the key; HOLD lists one reason per candidate | Assertions on message text |
| EB-08 Experience and efficiency   | `APPLICABLE`     | A user migrates a schema 1 file from the mapping in `docs/routing.md` alone | Readback of the migration section against the baseline fixture |

### Practices

| Practice | Serves | Why it applies here | Evidence |
| --- | --- | --- | --- |
| `tdd` | EB-03 | The golden table is known before any code moves | Failing runs before each implementation, in the Completion report |
| `test-strategy` | EB-03 | Rules are unit tested; the gates are proven at their CLI boundary in an isolated tree | `tests/test_adapters.py`, `tests/test_routing_resolution.py`, `tests/test_check_dispatch.py`, `tests/test_repository.py` |
| `solid-ocp` | EB-05 | A new harness extends Radiant through data, not code | The fixture adapter test |
| `adr` | EB-05 | The routing format of ADR-0002 changes | ADR-0004 under question 9 (A), or the owner's choice of (B) in section 18 |

# 9. Project-specific constraints

Taken from `AGENTS.md` and the earlier contracts:

- Python 3.9+, standard library only; no `match`, no `X | Y` types.
- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- Validators stay read-only.
- No absolute personal path in any Markdown file; the repository check
  refuses them.
- Model IDs only in the adapters and in reports; tests read models from the
  adapters, as `tests/test_integration.py` already does.

# 10. Dependency policy

### New runtime dependency allowed?

`NO`

# 11. Verification plan

## Automated

```text
PYTHONDONTWRITEBYTECODE=1 python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
python3 validators/check_contract.py docs/plans/TC-0005-single-source-harness-facts.md
python3 validators/check_dispatch.py units docs/plans/TC-0005-single-source-harness-facts.md
python3 validators/check_dispatch.py routing docs/routing.example.json
git diff --check
git diff --cached --check
```

## Golden table

The baseline is `tests/fixtures/routing-schema1.json`, a byte copy of the
planning baseline's example:
`git show 4e4ff16:docs/routing.example.json | cmp - tests/fixtures/routing-schema1.json`
exits 0. If the example changes on `main` before activation, the Build stops
on HOLD. In the model column, `codex:deep` means the `deep` value of
`adapters/codex/capabilities.json`, which the test reads from the file and
never writes as an ID.

With `requires` `[]`:

| Rule | Floor | Harness | Capability | Model | Effort | Approval |
| --- | --- | --- | --- | --- | --- | --- |
| `build` | `deep` | `codex` | `deep` | `codex:deep` | `medium` | none |
| `build` | `standard` | `codex` | `standard` | `codex:standard` | `medium` | none |
| `build` | `light` | `codex` | `light` | `codex:light` | `medium` | none |
| `bug-fix` | `deep` | `codex` | `deep` | `codex:deep` | `high` | none |
| `bug-fix` | `standard` | `codex` | `standard` | `codex:standard` | `high` | none |
| `bug-fix` | `light` | `codex` | `light` | `codex:light` | `high` | none |
| `frontend` | `deep` | `claude-code` | `deep` | `claude-code:deep` | `medium` | none |
| `frontend` | `standard` | `claude-code` | `deep` | `claude-code:deep` | `medium` | none |
| `frontend` | `light` | `claude-code` | `deep` | `claude-code:deep` | `medium` | none |
| `plans-and-contracts` | `deep` | `claude-code` | `deep` | `claude-code:deep` | `high` | none |
| `plans-and-contracts` | `standard` | `claude-code` | `deep` | `claude-code:deep` | `high` | none |
| `plans-and-contracts` | `light` | `claude-code` | `deep` | `claude-code:deep` | `high` | none |
| `independent-critique` | `deep` | `claude-code` | `deep` | `claude-code:deep` | `high` | `human` |
| `independent-critique` | `standard` | `claude-code` | `deep` | `claude-code:deep` | `high` | `human` |
| `independent-critique` | `light` | `claude-code` | `deep` | `claude-code:deep` | `high` | `human` |
| default | `deep` | `codex` | `deep` | `codex:deep` | `medium` | none |
| default | `standard` | `codex` | `standard` | `codex:standard` | `medium` | none |
| default | `light` | `codex` | `light` | `codex:light` | `medium` | none |

With `requires` `["browser"]`, every row above is `HOLD`, with the reason
that the adapter's `provides` does not cover `browser`. An unknown rule id
is an error.

The test asserts the table for `resolve(baseline fixture)`, for
`resolve(fold(docs/routing.example.json))` and for each `routing.json` that
`tests/test_check_dispatch.py` writes from the example. The plans and
critique rows at `standard` and `light` need the new rule-level
`capability`; the front end rows need the candidate's own `capability`; the
build and default rows at `deep` show that a single "capability to harness"
map would have changed today's result.

## Focused verification

- Every item of section 7 has a test. Format tests run on data; command and
  repository tests run the real command in a temporary directory, as
  `tests/test_check_dispatch.py` and `tests/test_repository.py` do.
- Failing-before: each new test is run before its implementation and seen
  to fail, and the Completion report shows each run. Tests of new modules
  fail with `ModuleNotFoundError`, which proves only that they reach the new
  code; each rule's own proof is its mutation below. Tests of existing files
  fail on the missing behavior while every existing test passes.
- Mutation proof, after each commit and one change at a time: drop the
  rule capability in `fold`; ignore the candidate capability in `resolve`;
  let a candidate below the floor win; skip the `provides` check; accept an
  effort outside `efforts` (question 3 (A)); return `default` for an unknown
  rule; fold schema 1 too, which changes its bytes; discover adapters with
  `is_dir()` only; hard-code the render table again; accept a template path
  outside the adapter. Commit before mutating; see the named test fail;
  restore with `git checkout -- <file>`; see the suite pass; gate each step
  on the exit code. The report names the test each mutation broke.
- Byte comparisons, saved at the entry commit and at the end and compared
  with `cmp`: `check_dispatch.py routing tests/fixtures/routing-schema1.json`
  against the entry commit's `check_dispatch.py routing docs/routing.example.json`;
  `check_dispatch.py units templates/task-contract.md`; and
  `render_bootstrap.py`, its `--adapter codex` and `--adapter claude-code`
  outputs, compared with `diff -r`.
- Demerzel compatibility, in `tests/test_adapters.py` and
  `tests/test_check_dispatch.py`: every `capabilities.json` value is a
  string; `provides.json` keeps `provides` as a list of strings; the
  `routing` output for both schemas has `rules` with `id`, `use` and
  optional `approval`, and candidates with only `harness`, `capability` and
  `effort`. Under question 10 (A), the Build confirms these against the
  recorded Demerzel commit.
- The orchestrator, not the Build, runs
  `python3 validators/check_dispatch.py routing` with no argument, on the
  owner's file, at the entry commit and at the end, and compares the two
  stdouts with `cmp`; the Build never opens the file.
- `rg` over `validators/` and `adapters/render_bootstrap.py` finds no
  adapter name in code. Under question 5 (A), `rg` over the tree, outside
  `adapters/*/capabilities.json`, `docs/plans/` and `docs/history/`, finds
  no model ID from the adapters; the test reads the IDs from the files.

## Readback

After execution:

- reopen each changed file, both `provides.json`, the example, every error
  message and the migration section of `docs/routing.md`;
- confirm that no path outside the Allowed scope changed, against the entry
  commit, including committed, staged, unstaged and untracked changes
  (`git diff --name-only <entry>..HEAD` and `git status --porcelain`).

## Independent critique

`REQUIRED`

- `radiant-verifier` at `deep`, independent of the author as
  [Article VIII](../../constitution/CONSTITUTION.md#article-viii---creation-and-critique-must-be-separated-when-that-increases-confidence)
  requires: neither the Build session nor the session that wrote this
  contract. Following the 2026-11-24 owner routing, it runs on a model from
  a vendor different from the Build's, through `agy` or, while that has no
  adapter, through `claude-code`; this is a routing choice, not a rule this
  contract adds ([delivery flow](../delivery-flow.md#5-independent-critique)).
  It checks the result against this contract, issue #35's acceptance and
  section 18, and re-derives at least the `frontend`, `plans-and-contracts`
  and `build` at `deep` rows of the golden table by hand.
- Launched and collected by the orchestrator, never by the Build. The
  orchestrator records role, capability, harness, full model ID and command
  in the Completion report's provenance.
- External prerequisites: the chosen harness installed and authenticated on
  the owner's machine.

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [ ] `python3 validators/check_dispatch.py routing docs/routing.example.json` exits 0 on the schema 2 example, and `check_repository.py` passes (issue #35);
- [ ] `python3 -m unittest discover -s tests -p test_routing_resolution.py` passes, asserting every row of the golden table for the schema 1 baseline and the schema 2 example (issue #35);
- [ ] `cmp` shows that `check_dispatch.py routing` on the baseline fixture prints the same bytes as the entry commit on its example, and that rendered subagents and the global block are unchanged;
- [ ] `rg` finds no adapter name in `validators/` code or `adapters/render_bootstrap.py`, and `cli`, `efforts` and `subagents` appear only in `adapters/*/provides.json` and their readers (issue #35);
- [ ] the fixture adapter test passes with no change outside its directory and the global block line;
- [ ] `git diff --name-only <entry>..HEAD` shows no `adapters/*/capabilities.json` change and no file outside the Allowed scope;
- [ ] `docs/integration.md` has the note for Demerzel, linking faelplg/demerzel#60 (issue #35);
- [ ] the orchestrator's before and after runs on the owner's `routing.json` print the same bytes;
- [ ] all applicable checks in section 11 pass;
- [ ] there was no change outside the Allowed scope;
- [ ] relevant limitations are recorded;
- [ ] the final evidence was read, not just presumed from the exit code.

# 13. HOLD conditions

Stop and ask for a decision when:

- any question of section 5 has no recorded answer;
- the golden table cannot hold for schema 1 or schema 2 without changing a
  row, or the baseline example changed on `main` since planning;
- keeping Demerzel working needs a change to `capabilities.json`'s shape,
  to the `routing` output beyond question 2, or to any Demerzel file;
- a fact needs a value that no current source holds, such as an effort level
  not in Demerzel's checked lists;
- the design needs a vendor rule (#64), an `agy` fact (#29) or a change to
  the owner's `routing.json`;
- the agent would need to write outside the authorized paths;
- the minimal solution no longer fits the contract.

`HOLD` is a valid result.

# 14. FAIL conditions

Mark `FAIL` when:

- acceptance criteria cannot be met;
- resolution of any golden row changes;
- schema 1 output, rendered subagents or the global block change;
- verification shows a material regression in the existing checks;
- an external blocker makes the goal impossible within this contract.

Do not disguise `FAIL` as `DONE WITH NOTES`.

# 15. Change budget

The agent may:

- refactor adapter discovery in `check_dispatch.py`, `check_repository.py`
  and `render_bootstrap.py` into `validators/adapters.py`;
- update directly affected tests and pointers.

The agent may not, without HOLD:

- change `capabilities.json`, an agent template or the global block;
- add commands, schema keys or output fields that section 5 and the owner's
  answers do not name;
- refactor validators beyond the routing and adapter code.

# 16. Completion report

### Status

`DONE | HOLD | FAIL`

### Changed

- `[path]: [what changed]`, with line references cited alongside the commit

### Verification evidence

```text
[commands and results, including failing-before runs, mutations and byte comparisons]
```

### Engineering notes

- `[relevant trade-off or N/A]`

### Remaining limitations

- `[known limitation or none]`

### Learn Back candidate

- `[what this task taught that may deserve change elsewhere, or none]`

### Provenance

- `[one line per round: role, capability, harness, full model ID, state, usage metric or its absence]`

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

# 18. Owner decisions

None.

The questions in section 5 await the owner's answers. Each answer is
recorded here from the owner's own message, with its date and contract
impact, before the Build starts.
