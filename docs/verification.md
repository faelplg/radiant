# Verify changes to Radiant

The [Constitution](../constitution/CONSTITUTION.md) defines what completion
means. The [skill](../skills/radiant-cycle/SKILL.md), in its verify and learn
mode, defines the procedure. This page holds the concrete checks for this
repository.

Run at the root with Python 3.9+ and Git, without additional runtime
dependencies:

```sh
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
```

The first command checks local Markdown links and anchors, uniqueness of the
Constitution, absence of personal paths in the documents and coherence between
`agents.json`, the sections of the delegation skill and each adapter's
`capabilities.json`. It also checks the requirements vocabulary, each
adapter's `provides.json`, the units example in the contract template, read as
restricted YAML without dependencies, and the
[routing example](routing.example.json). The tests exercise the bootstrap and
subagent generator, the pin gate and the repository validator through their
real commands in temporary directories, including divergence, a dirty
checkout, invalid paths and refusal to overwrite.

## Structural review separate from the Build

Check the final files against these criteria, after the checks:

| Criterion | Evidence to inspect |
| --- | --- |
| Canonicality | A single Constitution; indexes and adapters point to owners |
| Core/adapter | No general rule exclusive to a harness |
| Global | Small, regenerable block, without bodies or local product state |
| Portability | Repeat the bootstrap at another path, including one with spaces |
| Project independence | Frame/Spec/Plan/Contracts in the consumer; pin checked |
| AIKM independence | Operational checks do not depend on running the product |
| Discoverability | The paths below reach real sources from the root |
| Versionability | Diff and Git reference make it possible to know the applied state |
| Minimalism | Each file has a function; no anticipatory empty folder |
| Extensibility | New capabilities fit the structure without introducing them now |
| Harness agnosticism | Roles and capabilities in the Core; models and mechanisms only in the adapters; every adapter maps the three capabilities |

Simulate A: enter through Radiant's AGENTS, find the Constitution, thesis,
capability and verification. Simulate B: an empty consumer, pin, bootstrap,
Frame and local state, contract and shared reading. Simulate C: an independent
AIKM with its documents, Learn Back and no ownership over the Core. Simulate
D: a new Claude Code session finds the global block, the adapter, the pin
gate, the Constitution and the delegation skill, and the generated subagents
point to that same revision.

Use deterministic verifiers as evidence independent of the wording and inspect
the consumer's paths. State whether there was another reviewer or only a
self-readback. Structural tests do not show that a model will obey the adapter
in a new session; a conceptual simulation is not a real E2E run of the
harness.

The validator does not ignore broken links and does not rewrite any document.

Record results and limits in the authorized report. If there is a material
failure, fix it within scope and repeat the affected verification. Do not
declare DONE just because tests pass.
