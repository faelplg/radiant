# Validators

Requirements: Python 3.9+ and Git. No external packages.

- `python3 validators/check_repository.py`: document integrity, local
  links/anchors, a single Constitution, Core portability and coherence between
  delegable profiles and each adapter's capability map, requirements and the
  adapters' `provides.json`, the template's units example and the routing
  example. It also validates practice cards, the catalog index and the practice
  ids in the Task Contract template's example, without checking consumer
  contracts or requiring practice citations. Read-only.
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

The semantic limits and the review of the paths are in
[Verification](../docs/verification.md). The checks do not validate factual
truth, AIKM egress policy, product execution or a model's obedience.
