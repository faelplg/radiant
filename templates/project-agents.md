<!-- radiant:begin -->
# Project guidance

This project uses Radiant. Locate its checkout through the user's global
bootstrap and read there the README of the adapter for the harness in use, in
`adapters/<harness>/`, to validate the revision and load the Core. If the
pointer is missing, set it up before running under Radiant. Anyone who does
not use Radiant follows only the local commands and rules below. In harnesses
that read another instructions file, that file holds only an import of this
map; in Claude Code, `CLAUDE.md` with the line `@AGENTS.md`.

The state map and the chosen commit are in `.radiant.json` at this root. Read
the artifacts the task needs and the contract pointer given in the map. This
product's rules and commands belong to the local context indicated there.
When the map has an `engineering_profile`, read it together with the Baseline
in the Radiant checkout before starting a Build.

<Add only constraints, commands and references specific to this project.>
<!-- radiant:end -->
