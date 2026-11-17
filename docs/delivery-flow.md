# GitHub delivery flow

This document describes the end-to-end GitHub delivery flow for Radiant work
in order, from issue creation to post-merge cleanup. It complements the
[cycle skill](../skills/radiant-cycle/SKILL.md), the
[delegation skill](../skills/radiant-delegation/SKILL.md) and the
[lifecycle map](lifecycle.md).

## 1. Issue

Create or select a GitHub issue with:

- an assignee;
- one Conventional Commits type label (`feat`, `fix`, `docs`, `style`,
  `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`);
- a milestone, when the repository uses milestones for the current increment;
- a project status set on the project board.

## 2. Plan PR with a Task Contract

Relevant agentic builds must have an appropriate
[Task Contract](../templates/task-contract.md) (see the
[Constitution](../constitution/CONSTITUTION.md) and the
[contract convention](../contracts/README.md)); open a plan PR with the
contract before implementation. Documentation explicitly requested by the
owner may be revised without inventing an implementation contract.

## 3. Owner go and activation

Wait for explicit owner authorization before starting Build. A proposed plan
or contract in `READY` state does not authorize execution. Once authorized,
record the authorization and the Build's entry commit in the contract and move
it out of `READY` (see [activation](../contracts/README.md#activation) and
[readback](../templates/task-contract.md#readback)).

## 4. Build in a git worktree

Run Build in a dedicated git worktree and feature branch, with the worktree
location left to the adapter or project map. Follow the contract's
[verification plan](../templates/task-contract.md#11-verification-plan):

- when the change has testable behavior, record failing-before evidence for
  the targeted fix or missing behavior before changing implementation (see
  [tdd](../engineering/practices/tdd.md));
- prove regression tests by mutation so each test fails against the specific
  regression it names;
- stay within the contract's allowed paths and change budget.

## 5. Independent critique

The verifier accepts every contract once, at the end, and is brought forward
when `Risk tier` >= 2 or `Independent critique: REQUIRED` (see
[delegation rules](../skills/radiant-delegation/SKILL.md#rules) and
[Verifier role](../skills/radiant-delegation/SKILL.md#verifier)):

- launched and collected by the orchestrator or human, never by the Build;
- runs at `deep` by default, never below the author's capability (rule 2), and
  changed only through the contract's `Capability` field with a one-line
  justification (rule 3);
- independence follows
  [Constitution Article VIII](../constitution/CONSTITUTION.md#article-viii---creation-and-critique-must-be-separated-when-that-increases-confidence)
  and the contract's `Independent critique` field; a different-vendor critic is
  a routing choice set by [routing rules](routing.md), not a Core mandate (a
  practice for cross-vendor critique is tracked in
  [issue #64](https://github.com/faelplg/radiant/issues/64)).

## 6. Owner decisions

Record every decision the owner makes during the contract in the contract's
[Owner decisions](../templates/task-contract.md#18-owner-decisions) section:
date, the decision, and what it changes in the contract. The source must be the
owner's own message, never an agent's report of it; the entry may quote or
faithfully summarize that message.

## 7. Contract `DONE`

The orchestrator performs readback and acceptance
([Return](../skills/radiant-delegation/SKILL.md#return)) by checking the
diff, working tree state, and command results. Declare the contract `DONE`
only when the
[completion rule](../templates/task-contract.md#17-completion-rule) is met:
observable acceptance criteria, applicable engineering checks and verification
evidence all converge, with no unreported changes outside scope. If Copilot
review or CI later forces changes after `DONE`, run a fix round and re-verify
before merge.

## 8. Pull request

Open a pull request with:

- `Closes #N` in the description to link and close the governing issue;
- a Conventional Commits title;
- the owner as assignee and the matching Conventional Commits type label.

## 9. Copilot review

On code PRs, wait for Copilot review, inspect every comment against the real
code and contract, and answer and resolve every review thread before merge.
Documentation PRs may also receive a review, and every thread is still answered
and resolved before merge.

## 10. CI green

Confirm all required CI checks pass on the final commit of the PR branch.

## 11. Merge by the owner only

Only the owner merges the pull request. Agents never merge or push directly
to protected branches.

## 12. Project status and cleanup

After merge:

- update the issue's project status to its completed state;
- remove the dedicated git worktree;
- delete the local and remote feature branch.
