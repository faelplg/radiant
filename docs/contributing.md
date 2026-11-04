# Evolution and versioning

Changes follow the [Constitution](../constitution/CONSTITUTION.md) and the
[operational cycle](../skills/radiant-cycle/SKILL.md). Keep a reviewable
relation between intent, diff, evidence and, when there is one, the
originating finding.

Before creating a new body, check the [index](capabilities.md). Fix the most
specific owner. An adapter only receives translation for its harness; shared
rules stay in the Core. Do not duplicate procedures in global documentation.

Use changes small enough to tell apart moves, editorial adjustments and
behavior changes. Check the [repository criteria](verification.md). Commit
messages follow Conventional Commits, without automatic agent co-authorship.
Record motivation and the Learn Back reference in the body when relevant.

Documentation, metadata, code comments and command output are written in
English.

## Initial identity

Radiant's state is identified by a full Git commit. There is no formal release
or API compatibility contract that would justify SemVer for the system at this
stage. Do not add `VERSION` just to repeat the thesis.

The thesis keeps its version 0.2. The Constitution follows the policy in its
section 9, which applies to that document; version 0.1.1 is the English
translation of 0.1. Skills may have their own editorial version; it is
auxiliary metadata and does not replace the revision of the whole set.

Tags and releases may name reviewed commits when there are consumers and clear
criteria. For now, Git provides authorship, previous state, diff and
motivation. Do not edit CHANGELOG.md manually; future generation may use that
history. There is no release or publication automation in this task.

Consumers adopt changes through the [pin policy](integration.md). A commit in
Radiant does not silently change an older project. Do not rewrite historical
contracts or reports to claim they used a new revision.

## Learn Back as change

Use the [routing](learn-back.md) to justify shared changes. Compare the
verification before and after. Constitutions evolve through the existing
constitutional process; do not automatically promote a local preference or
error to a universal principle.
