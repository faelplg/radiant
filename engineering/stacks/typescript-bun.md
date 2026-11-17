# TypeScript on Bun

- Id: `typescript-bun`
- Grounded in `faelplg/demerzel` at `8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0`:
  [package.json](https://github.com/faelplg/demerzel/blob/8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0/package.json),
  [tsconfig.json](https://github.com/faelplg/demerzel/blob/8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0/tsconfig.json),
  [Spec](https://github.com/faelplg/demerzel/blob/8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0/docs/project/SPEC.md),
  [CI](https://github.com/faelplg/demerzel/blob/8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0/.github/workflows/check.yml).
- Grounded in `faelplg/aikm` at `a2cfd1bf6f415521567d0e48d8eebcc79a3e611d`:
  [package.json](https://github.com/faelplg/aikm/blob/a2cfd1bf6f415521567d0e48d8eebcc79a3e611d/package.json),
  [biome.json](https://github.com/faelplg/aikm/blob/a2cfd1bf6f415521567d0e48d8eebcc79a3e611d/biome.json),
  [Spec](https://github.com/faelplg/aikm/blob/a2cfd1bf6f415521567d0e48d8eebcc79a3e611d/docs/project/SPEC.md),
  [CI](https://github.com/faelplg/aikm/blob/a2cfd1bf6f415521567d0e48d8eebcc79a3e611d/.github/workflows/check.yml).

Use the [Profile form](../../templates/engineering-profile.md) to select this
pack; the [Demerzel example](../../docs/engineering-profile.example.md) records
a real override. Selection and precedence are in the [index](README.md).

## Layering and dependency rule

- Serves: [clean-architecture](../practices/clean-architecture.md), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity)

Use strict TypeScript. Keep domain policy independent of CLI and external
adapters; imports point toward inner-owned contracts. Add layers only when
there is behavior to separate. Demerzel's `src/core/` does not import
`src/radiant/` (Spec sections 2 and 3); AIKM separates pure resolution, policy
and rendering from I/O and keeps one module per adapter (Spec section 8).
The Profile names the project's actual boundaries and dependency checks.

## Test layout and commands

- Serves: [test-strategy](../practices/test-strategy.md), [tdd](../practices/tdd.md)

Use Bun's test runner, with tests outside `src/`. AIKM uses `tests/unit/` and
`tests/integration/`; Demerzel uses `test/` grouped by subsystem. Keep the
existing layout rather than moving tests solely to match another consumer.
Use `bun test` for the runner and `bun run check` for the project's aggregate
gate. Both manifests expose a typecheck via `bun run typecheck`. The Profile
records any prerequisites and extra verification beyond that gate. Choose
test levels by boundary and risk as the linked practices describe.

## Lint and format

- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability)

Default to Biome lint and format, included in `bun run check` through
`bun run lint`. This follows AIKM's manifest and `biome.json`, with recommended
lint rules and two-space indentation. Demerzel has no linter in its manifest;
its Profile must override this section rather than claim a lint gate exists.
Biome is the default because it makes style and lint checks repeatable.

## Error handling

- Serves: [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts), [EB-07](../engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability)

Validate data at TypeScript's external boundaries; static types do not prove
runtime input. Give CLI refusals a stable code, the affected resource and an
actionable next step. Preserve evidence of partial effects for recovery;
never turn a failed operation into success. Keep project-specific exit codes,
recovery protocols and public error shapes in the Spec, with executable
boundary tests, rather than prescribing one consumer's protocol to all.

## CI and release

- Serves: [ci-cd](../practices/ci-cd.md), [semantic-versioning](../practices/semantic-versioning.md)

On pull requests and pushes to `main`, install with
`bun install --frozen-lockfile` and run `bun run check`. Both cited workflows
use Bun 1.4.2; keep the chosen Bun version explicit and consistent with the
project's local requirements. AIKM runs on Ubuntu; Demerzel also checks macOS.
The Profile records platform requirements and external fixtures.

Use the release practice when publishing an interface with consumers; neither
cited workflow establishes a release pipeline. Do not infer release or deploy
authorization from a green CI run. Environment-specific deploy and operations
belong in the project's Profile, outside this pack.
