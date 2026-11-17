# Stack packs

A stack pack is a shared set of engineering conventions for a runtime and
package manager. Its version is the consumer's Radiant pin, without a separate
pack version. Read it together with the Engineering Baseline and the project's
Engineering Profile.

A pack id is a lowercase kebab slug matching `[a-z0-9]+(?:-[a-z0-9]+)*`
and equals its Markdown file stem. Never rename or reuse an id. `none` is
reserved; `README.md` is the index, not a pack.

Select at most one pack in the Profile, outside fenced blocks:

```text
- Stack pack: `typescript-bun`
```

Use `none` or omit the line when no pack applies. A Profile with only the
selection and no overrides is enough when all pack defaults fit.

Override a section in a `Pack overrides` table with columns `Pack section`,
`Override` and `Reason`, one row per changed section. Sections without a row
retain the pack default. The Profile is a canonical project artifact and wins
over a pack, a shared body, under the
[Constitution's precedence](../../constitution/CONSTITUTION.md#3-order-of-precedence).
Neither can lower a Baseline minimum without the explicit human decision and
reason required by [section 2](../../constitution/CONSTITUTION.md#2-normative-language).
Overrides are not machine-validated.

| Pack id | Shared conventions |
| --- | --- |
| [typescript-bun](typescript-bun.md) | Strict TypeScript on Bun, tests, Biome and CI |

Use the [Profile form](../../templates/engineering-profile.md) and the
[Demerzel example](../../docs/engineering-profile.example.md). The
[Spec form](../../templates/spec.md) describes behavior and points to the
Profile for engineering constraints. The
[pin gate](../../docs/integration.md#project-map) checks the selection, not
override content or pack structure.
