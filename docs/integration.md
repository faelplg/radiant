# Integration and revision reference

## Three levels

| Level        | Owner and content                                                     | Does not contain                                 |
| ------------ | --------------------------------------------------------------------- | ------------------------------------------------ |
| Radiant Core | This repository: Constitution, definition, capabilities, conventions  | Product state                                    |
| User         | Location of the checkout and entry of the harness adapter             | Core bodies or project knowledge                 |
| Project      | Opt-in, revision, paths, its own constraints and commands             | Copied Constitution or shared skills             |

The repository is the authority. The Core is logical, spread across the
directories listed in the [README](../README.md); it does not require an extra
`core/` folder. Global configuration can be rebuilt. The
[Codex](../adapters/codex/README.md) and
[Claude Code](../adapters/claude-code/README.md) adapters implement discovery
in each harness. Other harnesses may locate the same bodies with their own
adapters.

## Minimal discovery

The chosen mechanism is **an explicit local path in the user's bootstrap**. A
portable template generates that text from the checkout. The generated
configuration stays outside versioned content. Radiant requires no implicit
fallback through a sibling directory, registry, environment variable or
symlink.

This mechanism also works in an app opened outside a shell with exported
variables. It is enough for a shared local checkout and does not require an
installer that rewrites global preferences.

The project does not declare the machine's personal path. Its adapter finds
the root through the user's configuration. On another machine, generate the
bootstrap again. If the path is unreachable, resolve the location before
running under Radiant; do not use an old copy found by chance.

## Project map

At the consumer root, `.radiant.json` declares use of the system. Start from
the [form](../templates/radiant-project.json). Its initial schema is:

- `radiant_revision`: full Git commit, 40 or 64 hexadecimal digits.
- `frame`, `spec`, `plan`, `workflow`, `active_contract`: a file relative to
  the consumer root, or `null` while it does not exist.
- `engineering_profile`: a file relative to the consumer, or `null` when the
  Baseline is enough and there are no project-specific decisions.
- `contracts`, `adrs`, `verification`, `learning`: a relative directory or
  `null`.
- `maintenance`: optional; a relative directory ignored by Git where
  Maintenance writes its reports, or `null`. It may not exist yet: the
  [maintenance](../skills/radiant-maintenance/SKILL.md) skill creates it on
  the first run. A missing field is the same as `null`.

All fields are present except the optional `maintenance`; do not add absolute
paths, `..` or symlinks that escape the project. When an artifact is created,
update its pointer. `null` does not waive an input the task needs: the skill
identifies the gap and guides its framing. The structural validator does not
grant authorization.

The consumer's `AGENTS.md` points to that map and to the harness entry. The
engineering Baseline lives in Radiant; the Profile, when there is one, lives in
the consumer and must not copy the Baseline's body. Constraints, commands and
references to local ADRs may live in it or in `workflow`, depending on volume.
The list of active contracts exists only in the `ACTIVE.md` it points to,
never in the map and the adapter at the same time.

To start, follow [Adopt in a project](#adopt-in-a-project). The filled form
becomes an instance; the skill body stays in Radiant.

## Adopt in a project

The orchestrator runs the adoption when the human asks and the project does
not have `.radiant.json` yet. The steps apply to new and existing projects.

1. **Check Radiant.** The global bootstrap points to a clean checkout, at a
   commit reachable from `main`. If the checkout is clean on `main` and only
   behind the remote, fast-forward to the chosen commit. In any other case (no
   checkout, dirty checkout, another branch or a commit outside `main`), stop
   in `HOLD` before writing: point to the adapter setup and do not switch the
   branch. Global configuration is done by the human.
2. **Diagnose, read only.** Gather, with path and line, the build, test, lint
   and typecheck commands (manifests, scripts and CI), the instructions that
   already exist (`AGENTS.md`, the harness file, README) and the recorded
   decisions. Do not run commands at this step. To classify a command as safe,
   read the script and the tests it runs; when in doubt, it is not safe.
3. **Propose.** Present the exact list of files and the content of each one:
   - `.radiant.json` with the proposed pin and `null` in every artifact that
     does not exist yet;
   - in `AGENTS.md`, a section between `<!-- radiant:begin -->` and
     `<!-- radiant:end -->` based on the [neutral map](../templates/project-agents.md),
     with the commands found. Create the file if it is missing and preserve
     everything else;
   - the harness instructions file, only if it does not exist, according to
     the adapter. If it exists without pointing to `AGENTS.md`, record it as a
     gap;
   - optional: `maintenance` and its entry in `.gitignore`;
   - gaps: missing Frame, Spec, Plan and Engineering Profile, routed to the
     [cycle skill](../skills/radiant-cycle/SKILL.md). Nothing is invented to
     fill them.

   In a public or shared repository, say in the proposal that the section and
   the harness file apply to every contributor, including those who do not
   use Radiant. The human decides whether the adoption goes into the
   repository.
4. **Write what was approved.** First, save `git status --porcelain --ignored`.
   Write only the approved files, on a branch, without push and without a
   commit yet.
5. **Verify.** `check_project.py` exits 0 without changing the pin. Compare
   `git status --porcelain --ignored` with the saved state: the difference,
   including untracked and ignored files, contains only the approved list, and
   the content of each new file matches the proposal. The check confirms the
   structure of the map and the cleanliness of the Radiant checkout, not the
   consumer's diff or the quality of the diagnosis.
6. **Commit.** Only after step 5, make the adoption commit. The body records
   the summarized diagnosis and the approved list; that is the evidence of the
   adoption.

The pin is a human decision. A command proposed as safe runs locally, without
network and without writing outside the project. The section and comments the
adoption writes are in English, like the neutral map, even in a project in
another language. Radiant writes only the files above; another tool in the
same project can coexist with it because the content outside the Radiant
section is preserved.

## Where each piece of information lives

Each piece of consumer information goes to the narrowest surface that carries
it when it is needed. What is always loaded has to justify its cost in every
session; the rest comes in by pointer, on demand. The table applies the memory
types of [section 19 of the thesis](project-generation-system.md#19-operational-memory)
and adapts eve's context control method
([context-control](https://github.com/vercel/eve/blob/5666d2f0d8b78690d01a40ce93cac5e472799901/docs/concepts/context-control.md),
[role-aware instructions](https://github.com/vercel/eve/blob/5666d2f0d8b78690d01a40ce93cac5e472799901/research/role-aware-instructions.md)).

| Information | Surface | When the agent sees it | Owner |
| --- | --- | --- | --- |
| Pointers and rules needed in almost every session to locate or use the system | The consumer's `AGENTS.md` | In every session | Consumer |
| Project constraints and commands that apply to most tasks | `AGENTS.md`, or the map's `workflow` when the volume grows | In every session, or when entering the cycle | Consumer |
| Procedure used only in some tasks | Skill | The description, when the harness loads the skill into a native catalog; outside it, the pointer in the map or the capability index. The body, when the task triggers it | Whoever maintains the skill |
| Product intent, behavior and decisions | Frame, Spec, Plan and ADRs the map points to | When the task needs them | Consumer |
| Boundary of the current increment | Task Contract pointed to by `ACTIVE.md` | Before changing implementation files | Consumer |
| Rule a tool can enforce | Configuration, linter or validator | Only the output of a failure, which states the reason and the fix | Consumer or Radiant |
| Specialist work with its own context | Subagent, according to [delegation](../skills/radiant-delegation/SKILL.md) | The parent agent sees only the return | Radiant and adapter |
| Operation on an external system | MCP server or CLI | The schema and the result of each call | Consumer |
| Execution and evaluation evidence | Contract verification, reports and Git | When verifying or diagnosing | Consumer |
| Personal or machine preference | The user's global configuration, outside the project | Depending on the harness | User |

When deciding:

- Only what an agent needs in almost every relevant session goes into
  `AGENTS.md`. If only some tasks need it, the information is a skill or a
  document it points to.
- A skill outside the harness's native catalog, such as Radiant's skills read
  by path, is only discovered through a pointer with its usage trigger in
  `AGENTS.md` or in an index it points to. When moving a procedure into a
  skill, keep that pointer.
- `AGENTS.md` points to Frame, Spec, skills and Contracts without copying their
  text ([Article XI](../constitution/CONSTITUTION.md#article-xi---one-canonical-source-pointers-everywhere-else)).
  File trees and large data stay in the files, which the agent reads with
  tools.
- Authored instructions carry rules. Retrieved, generated or fetched content
  comes in as data with its origin and is not pasted into instruction surfaces
  ([Articles IX and X](../constitution/CONSTITUTION.md#article-ix---generation-and-retrieval-do-not-confer-authority)).
- Secrets appear only as a reference to an environment variable, never in an
  instruction, skill or server definition.
- A tool that generates these surfaces from a catalog inherits the criterion:
  the kind of piece chooses the surface and, with it, the context cost. A
  fragment rendered into `AGENTS.md` goes through the same always-loaded test.

## No silent update

Before loading the Constitution and capabilities for a consumer, check:

1. The discovered checkout is a complete Radiant repository.
2. Its `HEAD` matches `radiant_revision` exactly.
3. There are no tracked or staged changes, or relevant untracked files, in
   that checkout. Ignored files such as `.local/` are not part of the Core.
4. The consumer's declared paths exist and stay inside it.

`python3 <radiant-root>/validators/check_project.py <project-root>` checks
these conditions. Any divergence puts consumption on HOLD, before reading new
rules. The adapter's bootstrap is only the mechanism for locating and
checking, not an authorization to apply the revision it finds.

A pin recorded without checking the checkout is not enough. Do not change the
pin to make validation pass. For projects at different revisions, one can
prepare a clean Git checkout/worktree of the required revision and regenerate
the global pointer for it. Checkouts are materializations of the same
canonical history, not independent bodies kept in each product. Do not
automatically switch the branch of a checkout that holds work in progress.

An update is an explicit cycle decision: compare revisions, assess the
affected Constitution/capabilities/adapter, record the reason, change the pin
and verify the new cycle. A contract in execution keeps the reference it
started with; material changes follow
[contract integrity](../contracts/README.md). Reports keep the applied commit,
even after the project updates its pin.

Future tags may be convenience names, resolved to a full commit. A branch,
`HEAD`, or a standalone version of the Constitution or the thesis are not
valid pins.

## Source and generated configuration

The template and its generator belong to the versioned adapter. The generated
text contains the local path and may be included in the source of the global
configuration. If that is managed by dotfiles/Nix, regenerate through that
manager; do not edit the generated output. The detailed setup and rollback are
in the adapter.

## AIKM boundary

Radiant works with Git and files without installing AIKM. Since revision 2 of
the AIKM Frame (2026-10-12), AIKM is a Radiant consumer and a tool that
generates, per project, each harness's native files for skills, context and
MCP servers. It does not preserve or retrieve cycle evidence or learning: that
v1 knowledge layer is a non-goal. Evidence and Learn Back live in the
consumer's artifacts and in Radiant's Git history. The body of the Radiant
capabilities stays in this repository; distributing a pointer or a generated
copy does not transfer ownership or authorize egress from its destination.

AIKM's project documents live in the AIKM repository. The custody that existed
here was closed according to the
[migration plan](migration-plan.md#end-of-custody).

## Demerzel boundary

Demerzel dispatches a contract's execution units, each in its own session of
the harness chosen by the [routing rules](routing.md). It reads contracts and
the user's rules and writes only its dispatch log. It does not change
contracts, does not accept deliveries and does not merge, push or change
scope. The request carries only paths; the launched harness reads the
contract and sends it to its provider, so routing is also an egress decision.

Demerzel's core does not depend on Radiant. The dependency lives in a Radiant
integration inside it: reading `radiant-units`, a pin gate through the same
`radiant_revision` as any project, routing through Radiant's rules and
adapters, and the return in `.radiant/reports/`, which the dispatching
consumer ignores in Git. The integration validates units and rules through the
pinned revision's `validators/check_dispatch.py`, without a second reader.
Radiant works without it; the decisions are in
[ADR-0002](adrs/ADR-0002-backend-dispatch-demerzel.md) and
[ADR-0003](adrs/ADR-0003-demerzel-independent-core.md).
