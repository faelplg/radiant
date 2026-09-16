# ADR-0001: Technical bootstrap

Date: 2026-09-15

Status: Accepted for Iteration 00 under
[TC-0001 v0.2](../contracts/TC-0001-iteration-00-bootstrap.md).

## Context

[Plan section 5](../PLAN.md#5-iteração-00--bootstrap-técnico) requires a small
local CLI, tests, lint, formatting, and explicit technical choices. Filesystem
handling, startup time, safe parsing, reproducibility, and few operational
dependencies matter. The bootstrap must support later work without implementing
it.

## Delivered decisions

| Area               | Choice and reason                                                                                                                                                                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language/runtime   | TypeScript with strict checking, ESM, and Node 24.12+ within 24.x. Types help make metadata boundaries explicit as implementation develops. Native type stripping runs the CLI without a compiler or loader at runtime. This is the bootstrap stack, not an irreversible final product language decision (Spec section 73). |
| Local distribution | Source checkout with `npm run aikm -- --help`, or `node src/cli.ts --help`. No global install or publication. Pin the verified Node patch in `.nvmrc`.                                                                                                                                                                      |
| Dependencies       | npm 11, exact development versions, and the generated `package-lock.json`; reproduce with `npm ci`. No runtime packages. Disable install lifecycle scripts and automatic audit/funding requests. Initial dependency acquisition may require network access; runtime and checks are local.                                   |
| CLI                | Built-in `node:util.parseArgs` in strict mode. Only help exists, also shown for no arguments; invalid arguments receive stderr guidance and exit 2. No CLI framework or command registry is needed yet.                                                                                                                     |
| Tests              | Built-in `node:test` and `node:assert/strict`; launch the real entry point in subprocesses, check streams and exit codes, and exercise help outside the repository with an empty executable search path.                                                                                                                    |
| Static checks      | TypeScript `noEmit` with strict checks and `erasableSyntaxOnly` to keep accepted syntax executable by Node. No build output.                                                                                                                                                                                                |
| Lint/format        | Biome recommended lint rules, with warnings failing the gate; Prettier owns all formatting, including Markdown. Biome formatting and assists are disabled to avoid conflicting owners. Versions already present in the local npm cache are pinned as project dependencies.                                                  |
| Layout             | One executable source file, one CLI test file, and root package/tool configuration. No domain directories or future wrappers.                                                                                                                                                                                               |
| Git                | Optional source/history tooling only. No runtime Git invocation. Generated dependencies, coverage, logs, and compiler cache files are ignored.                                                                                                                                                                              |

## Selected approaches for later contracts

These choices satisfy the bootstrap planning requirement. None of the following
packages or product behaviors is installed or implemented in this iteration.

| Area                 | Selected approach and boundary                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Markdown/frontmatter | Preserve the Markdown body as text; parse only a delimited YAML header with the `yaml` package using YAML 1.2 core types, unique keys, no custom tags, and bounded alias expansion. Reject parse errors and non-mapping headers. Introduce parser limits and adversarial fixtures with the record contract; no Markdown renderer or full AST is needed for metadata. |
| Schema validation    | Zod strict object schemas at file/input boundaries, avoiding implicit coercion. Add it when a manifest or record first needs runtime validation. TypeScript alone does not validate external data. Domain fields remain governed by the applicable Spec and later contract.                                                                                          |
| Filesystem           | Built-in `node:fs/promises`, `node:path`, and URL/path conversion. No virtual filesystem or database abstraction. Write semantics and overwrite protection must be implemented and verified under the workspace contract.                                                                                                                                            |
| IDs                  | Use a maintained ULID implementation backed by cryptographic randomness, with the suggested `aikm:` prefix (Spec section 15). Preserve IDs across renames; do not derive them from titles. Package selection, collision checks, and record identity behavior are deferred to the record contract.                                                                    |

## Alternatives and trade-offs

- Python with argparse, pathlib, and unittest also fits a local file-oriented
  CLI. It would require a separate static typing workflow and Python environment
  management. Node supplies the CLI parser and subprocess test runner alongside
  TypeScript's static checks and a suitable YAML/schema ecosystem.
- Go offers a self-contained binary and fast startup. It adds compilation and
  platform-specific distribution to this source-checkout increment. That benefit
  is more relevant if distributing binaries becomes a requirement.
- Plain JavaScript removes the type checker but provides fewer checks as typed
  file boundaries emerge. TypeScript adds development tooling while leaving the
  runtime dependency set empty.
- Compiled TypeScript supports broader distribution; native stripping requires
  erasable syntax and cannot run TypeScript dependencies inside `node_modules`.
  Source-checkout use fits this contract. Publishing an installable package
  would require revisiting compilation and packaging under a later contract.
- Commander and a separate test framework offer richer interfaces, but built-in
  mechanisms cover the current behavior. ESLint is extensible; Biome supplies
  the current lint rules with fewer packages. Prettier handles Markdown as well
  as code. Neither tool owns canonical project document formatting here.
- JSON Schema/Ajv would favor language-neutral schema distribution; Zod favors a
  single typed definition within this bootstrap stack. Public schema exchange is
  not currently required. Full Markdown parsing and generic frontmatter engines
  would add transformations beyond header extraction.
- UUIDs are runtime-native, but ULIDs follow the Spec's suggested sortable ID
  shape. This means a later dependency; no ID generator is added to a help CLI.

The runtime still needs Node installed. Native stripping does not typecheck, so
the independent static check remains a required gate. Verification in this
iteration is on macOS; cross-platform validation and binary/package distribution
remain unverified. Workspace, record, search, AI, persistence, and adapter
behavior remain outside this decision's implementation scope.

## Verification

See [README](../../../README.md#development) for exact setup and verification
commands. The contract also requires independently invoking the CLI and reading
back dependencies, configuration, and the diff before reporting completion.

## References

- [Node TypeScript support](https://nodejs.org/api/typescript.html): native type
  stripping, required syntax restrictions, and distribution limitations.
- [Node argument parsing](https://nodejs.org/api/util.html#utilparseargsconfig).
- [Biome configuration](https://biomejs.dev/reference/configuration/).
