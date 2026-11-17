# Engineering Profile: Demerzel example

- Project: `faelplg/demerzel`
- Radiant revision: [full pin chosen explicitly when adopting this example]
- Baseline version: `0.1`
- Stack pack: `typescript-bun`

This is an adoption example, not a change to Demerzel's map or pin. It records
only differences and project-specific constraints, based on consumer commit
`8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0`. Start with the
[Profile form](../templates/engineering-profile.md) and read the selected
[pack](../engineering/stacks/typescript-bun.md).

## Pack overrides

| Pack section | Override | Reason |
| --- | --- | --- |
| Lint and format | No Biome or lint gate; use the existing typecheck and test aggregate. | The cited `package.json` scripts, lines 13-19, have no linter. Adding one is a separate consumer decision. |

## Commands

Run from the consumer root. Evidence: `AGENTS.md` lines 21-38 and
`package.json` lines 14-19 at the commit above.

| Command | Working directory and prerequisites | Evidence produced |
| --- | --- | --- |
| `DEMERZEL_RADIANT_ROOT=<clean-checkout-at-pin> bun run check` | Consumer root; Python 3.9+ and a clean Radiant checkout at the consumer's pin. | Typecheck, core isolation, herdr, CLI and Radiant tests. |
| `bun run test:core` | Consumer root; only Git and Bun on PATH, without Python. | Core isolation suite. |
| `bun run scenario:herdr` | Consumer root; real herdr on an isolated server. | Real backend scenario, outside the aggregate gate. |
| `DEMERZEL_SMOKE_REPO=<disposable-repository> bun run smoke:herdr` | Consumer root; orchestrator and owner present, real authenticated harnesses; uses model resources. | Real harness smoke, outside the aggregate gate. |

## Test strategy beyond the pack

Spec section 7 requires core import-boundary tests, refusals with no effects,
persistence and interruption proofs, lock contention, and marker-based egress
checks. Real herdr and harness scenarios have separate acceptance evidence;
fake-backend tests alone do not establish them.

## Dependency policy

No runtime dependencies (`AGENTS.md` line 18); the development dependencies
are pinned in the manifest and lockfile.

## Compatibility and performance

Bun 1.4.2 or newer, strict TypeScript, and both macOS and Ubuntu CI, as shown
by `package.json`, `tsconfig.json` and `.github/workflows/check.yml` at the
cited commit. No additional performance budget is inferred.
