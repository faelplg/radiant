# Working on Radiant

This file is the map of the repository itself. Start with the
[Constitution](constitution/CONSTITUTION.md) and the
[system definition](docs/project-generation-system.md). The
[capability index](docs/capabilities.md) points to the reusable bodies.

For relevant planning, execution or review, read the
[radiant-cycle skill](skills/radiant-cycle/SKILL.md) and apply the mode that
fits the current authorization. The request that governs this reorganization
and its scope are recorded in the [migration plan](docs/migration-plan.md).

For changes to the system, follow [contributing and versioning](docs/contributing.md),
[verification](docs/verification.md) and [Learn Back](docs/learn-back.md).
Local commands: `python3 validators/check_repository.py` and
`python3 -m unittest discover -s tests -v`. Use Python 3.9+ and Git.

Integration with consumers is in [integration](docs/integration.md) and in the
[Codex](adapters/codex/README.md) and [Claude Code](adapters/claude-code/README.md)
adapters. The shared Core does not depend on an adapter. To coordinate roles
and delegate, read the [radiant-delegation skill](skills/radiant-delegation/SKILL.md);
Radiant's structural decisions live in [docs/adrs/](docs/adrs/ADR-0001-delegation-roles.md).
When working in this repository, the local tree is the editing target; a
consumer's pin does not prevent developing a new Radiant revision.

For quick context, three private pages on claude.ai summarize the system: the
[map](https://claude.ai/artifact/7QZWWNTBv5NSxrePFBiaWg) in arc42 and C4, the
[glossary](https://claude.ai/artifact/7aaAD9YCE2nkVTkm4EDa3L) and the
[use cases](https://claude.ai/artifact/PEKb9oaxypnxxsQ1FTtoAQ). They are
derived views: the text in this repository wins when they diverge. When you
change the Constitution, the thesis, a skill, an adapter, a template or an
ADR, update the affected page; the pages are generated and versioned in
`faelplg/design-systems`, in the `radiant-design-system/docs/` folder.
Propose evolutions citing their basis: a canonical document, code, evidence or
a named method.

The AIKM documents that were in custody here belong to the AIKM repository;
the closing is in the [migration plan](docs/migration-plan.md#end-of-custody).
Do not apply AIKM commands as Radiant gates.

A review of open items done here covers only Radiant. From AIKM, Demerzel and
other consumers, only the interface with Radiant comes in, seen from this
side: pin, `validators/check_dispatch.py` and adapters. A consumer's open item
is handled in a session opened in its repository, which follows the
`AGENTS.md` there; only one pointer per repository stays here. What comes back
to Radiant arrives as [Learn Back](docs/learn-back.md), not as the consumer's
work.

Write in English. Preserve historical bodies: a faithful translation keeps
their content and decisions, but do not rewrite them. Avoid mass reformatting
and do not edit generated files or CHANGELOG.md manually. New text uses a
plain hyphen and adds no horizontal dividers. Do not implement the future
Design Layer in this reorganization.
