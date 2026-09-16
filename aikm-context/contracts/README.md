# Task Contracts

This directory contains the durable delegation records used by Radiant for the AIKM project.

Task Contracts translate an Implementation Plan increment into a bounded unit of agentic work.

## Canonical rules

### Stable identity

Each Task Contract receives a stable sequential ID:

```text
TC-0001
TC-0002
TC-0003
```

The ID is independent of the Implementation Plan iteration.

A single iteration may require more than one Task Contract.

### Stable filename

Use:

```text
TC-<id>-<short-slug>.md
```

Example:

```text
TC-0001-iteration-00-bootstrap.md
```

Do not include document version or execution status in the filename.

The path should remain stable so ADRs, verification records, learning records, and other contracts can reference it safely.

### Status is metadata, not location

Contracts remain in this directory regardless of status.

Do not create status folders such as:

```text
active/
completed/
failed/
```

Use contract metadata/status instead.

Recommended states:

```text
ready
active
done
held
failed
superseded
```

### Active contract pointer

`ACTIVE.md` identifies the Task Contract currently governing implementation work.

Harness adapters should read `ACTIVE.md` rather than infer the active contract from filenames, timestamps, or directory contents.

When the active work changes, update the pointer. Do not move or rename the previous contract.

### Execution integrity

Before execution starts, a contract may be refined normally.

After execution starts:

- do not silently rewrite objective, scope, outputs, boundaries, or verification criteria;
- small non-material clarifications may be recorded explicitly as an amendment;
- material changes require `HOLD` and a new or superseding Task Contract.

A contract may reference:

```text
supersedes: TC-0001
```

or:

```text
supersededBy: TC-0002
```

when appropriate.

### Versioning

The document version belongs inside the contract and in Git history, not in the filename.

Git records physical history. The contract ID records delegation identity.

### Completion evidence

A Task Contract defines what `DONE`, `HOLD`, and `FAIL` mean for its bounded work.

Verification Reports and Learning Records should reference the Task Contract ID/path rather than copy the contract body.

For new contracts, identify the reusable workflow and version when one governs
execution, with a link to the project's workflow map. Record the procedure
actually used, its version and Git revision or content digest in the execution
evidence. This identifies the instructions that guided the work; it does not
prove that following them produced a useful result.

Do not retrofit workflow usage into historical contracts or reports. A proposal
may be refined before execution; a later change in the shared skill must not
silently change the meaning of an already executing contract. Apply the same
execution-integrity rules above when the change is material.

## Current sequence

The first AIKM contract is:

```text
TC-0001-iteration-00-bootstrap.md
```

It governs Implementation Plan Iteration 00 — Technical Bootstrap.
