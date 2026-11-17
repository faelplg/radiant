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

When the work needs bounded delegation, open a plan PR containing a
[Task Contract](../templates/task-contract.md) following the
[contract convention](../contracts/README.md). Small documentation-only
changes that do not require bounded implementation delegation may proceed
without a Task Contract when explicitly requested.

## 3. Owner go

Wait for explicit owner authorization before starting Build. A proposed plan
or contract in `READY` state does not authorize execution.

## 4. Build in a git worktree

Run Build in a git worktree under `.claude/worktrees/` on a dedicated feature
branch. Follow the contract's
[verification plan](../templates/task-contract.md#11-verification-plan):

- record failing-before evidence for the targeted fix or missing behavior
  before changing implementation;
- prove regression tests by mutation so each test fails against the specific
  regression it names;
- stay within the contract's allowed paths and change budget.

## 5. Independent critique

When the contract requires independent critique (or at acceptance for higher
risk tiers), the orchestrator launches the verifier from a different vendor
than the author, at the verifier capability the contract asks (see
[Verifier role](../skills/radiant-delegation/SKILL.md#verifier)). The Build
never launches or collects its own critique.

## 6. Owner decisions

Record every decision the owner makes during the contract in the contract's
[Owner decisions](../templates/task-contract.md#18-owner-decisions) section:
number, date, the decision in the owner's words or a faithful summary, and what
it changes in the contract. Only the owner's own words count, never an agent's
report of them.

## 7. Contract `DONE`

Declare the contract `DONE` only when the
[completion rule](../templates/task-contract.md#17-completion-rule) is met:
observable acceptance criteria, applicable engineering checks and verification
evidence all converge, with no unreported changes outside scope.

## 8. Pull request

Open a pull request with:

- `Closes #N` in the description to link and close the governing issue;
- a Conventional Commits title;
- the owner as assignee and the matching Conventional Commits type label.

## 9. Copilot review

On code PRs, wait for Copilot review, inspect every comment against the real
code and contract, and answer and resolve every review thread before merge.

## 10. CI green

Confirm all required CI checks pass on the final commit of the PR branch.

## 11. Merge by the owner only

Only the owner merges the pull request. Agents never merge or push directly
to protected branches.

## 12. Project status and cleanup

After merge:

- update the issue's project status to its completed state;
- remove the git worktree under `.claude/worktrees/`;
- delete the local and remote feature branch;
- close the terminal tab used for the worktree session.
