# Validators

Requirements: Python 3.9+ and Git. No external packages.

- `python3 validators/check_repository.py`: document integrity, local
  links/anchors, a single Constitution, Core portability and coherence between
  delegable profiles and each adapter's capability map, requirements and the
  adapters' `provides.json`, the template's units example and the routing
  example. It also validates practice cards, the catalog index and the practice
  ids in the Task Contract template's example. It applies the contract rules
  below to `docs/plans/TC-[0-9][0-9][0-9][0-9]-*.md`, against the catalog
  only, prefixing errors with each contract path. Practice citations stay
  optional. Read-only.
- `radiant_yaml.py` reads the restricted YAML of `radiant-units` blocks, and
  `dispatch_formats.py` validates units, `provides` and routing rules.
- `python3 <radiant-root>/validators/check_project.py <project-root>`: checks
  `.radiant.json`, the pin, a clean checkout, local paths and any
  [stack pack declaration](../docs/integration.md#project-map) in the
  Engineering Profile. The stack index is required; unknown, malformed or
  repeated selections are refused. A selected pack is appended to the PASS
  line without changing its prefix; no selection keeps the current output.
  Profile sections, overrides and pack structure are not validated. Read-only;
  divergences produce `HOLD` and exit 1. Structural success does not activate
  contracts.
- `python3 <radiant-root>/validators/check_dispatch.py units <contract|->` and
  `python3 <radiant-root>/validators/check_dispatch.py routing [<routing.json>]`:
  validate a contract's `radiant-units` block, read from the path or from
  standard input, and the user's routing rules, at the
  [routing](../docs/routing.md#where-they-live) path when omitted. Read-only.
  Success prints the parsed value as JSON and exits 0, so a dispatch operator
  uses this reader instead of another one; invalid content prints
  `{"errors": [...]}` and exits 1; a usage error exits 2.

- `python3 <radiant-root>/validators/check_contract.py <contract|-> [--profile <path>]`:
  validates one contract from a path or standard input. The explicit Profile
  contributes ids from its `Project practices` table; card links are compared,
  never opened. This is opt-in for consumers; adoption does not change the pin
  gate or dispatch gate. Read-only.
  Success prints `{"template_version": "0.4", "practices": ["tdd"]}` and exits
  0; an absent version prints JSON `null`, and practices keep table order.
  Invalid content or an unreadable contract or Profile prints
  `{"errors": [...]}` and exits 1; usage errors exit 2.

The contract rules live in `task_contracts.py`: sections `8. Engineering Check`
and `12. Acceptance criteria` are required. The Baseline table needs at least
one `REQUIRED` or `APPLICABLE` row with a known EB id and a decided status;
acceptance needs a concrete checklist item beyond placeholders and the four
fixed generic items in the form. Optional `### Practices` citations accept
bare ids, backticked ids, or links with backticked ids to relative paths ending
in `<id>.md`, without a scheme, query or fragment. Unknown and repeated ids,
invalid cells and empty Practices tables are refused. Profile project ids must
be valid, unique and distinct from catalog ids. From `Template version` `0.4`,
`18. Owner decisions` needs a non-blank body without the unedited date
placeholder; `None.` is accepted. Versions compare numerically and cannot
exceed this checkout's template. Fenced blocks are ignored; repeated required
headings and Practices headings are refused. Errors name the section and the
relevant id or field, and all content errors are returned together.

The semantic limits and the review of the paths are in
[Verification](../docs/verification.md). The checks do not validate factual
truth, AIKM egress policy, product execution or a model's obedience.
