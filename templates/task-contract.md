# Radiant - Task Contract Template

**Version:** 0.2\
**Status:** Operational template\
**Base:** Radiant Project Generation System v0.2 + Radiant Engineering Baseline v0.1

> Use this template for relevant agentic implementation work.\
> Remove sections that are clearly `N/A`.\
> The contract must stay bounded.

---

# Radiant Task Contract - [Project] - [Iteration / Task]

**Contract ID:** `[id]`\
**Project:** `[project]`\
**Iteration:** `[iteration]`\
**Status:** `READY | HOLD | IN_PROGRESS | VERIFY | DONE | FAIL`\
**Owner:** `[human/agent]`\
**Risk tier:** `0 | 1 | 2 | 3`\
**Capability:** `default | deep | standard | light` - one-line justification when different from default\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `[project profile/version | none]`

---

## 1. Objective

Describe a single observable change.

> **[What should become true when this task ends?]**

---

## 2. Why this task exists

Reference the higher intent without rewriting the project.

**Source plan/spec:**

- `[document / section]`

**Hypothesis or risk reduced:**

- `[what uncertainty this task reduces]`

---

## 3. Inputs

The agent may assume as input:

- `[file / spec / decision]`
- `[existing code / command]`
- `[other required context]`

Do not infer missing inputs that would materially change the solution.

---

## 4. Allowed scope

### Paths allowed to change

```text
[path]
[path]
```

### Paths read-only

```text
[path]
```

### External systems allowed

- `[none / list]`

### Network

`DENIED | ALLOWED FOR: [purpose]`

### Execution units

Optional. Without this subsection, the contract is a single unit. Use it to
split the Build into delegable units, each with role, capability and
requirements, that a dispatch operator or the orchestrator can configure
without reinterpreting the contract. The rules and the accepted YAML are in
[execution units](../contracts/README.md#execution-units).

```yaml radiant-units
units:
  - id: TC-0025.1
    role: radiant-dev
    requires: []
    objective: Fetch external sources by rev for the cache.
    writes: [src/sources/, tests/sources/]
    depends_on: []
    done_when: The tests in tests/sources pass and the cache refuses a mismatched digest.
  - id: TC-0025.2
    role: radiant-dev
    capability: deep
    capability_reason: Refusing a digest requires security judgment.
    requires: []
    objective: Wire digest verification into sync.
    writes: [src/sync/]
    depends_on: [TC-0025.1]
    done_when: bun run check passes and sync refuses content without a matching digest.
```

---

## 5. Required outputs

At the end, exactly the necessary outputs must exist:

1. `[output]`
2. `[output]`
3. `[tests / docs / ADR only if applicable]`

Do not create additional artifacts without an observed need.

---

## 6. Non-goals

This task must **not**:

- `[non-goal]`
- `[non-goal]`
- `[non-goal]`

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

---

# 7. Functional requirements

- [ ] `[behavior]`
- [ ] `[behavior]`
- [ ] `[error/edge case]`

---

# 8. Engineering Check

Apply only what is relevant to this task.

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED / N/A` | `[constraint]`           | `[how checked]`   |
| EB-02 Correctness and contracts   | `REQUIRED / N/A` | `[invariant/error]`      | `[test/readback]` |
| EB-03 Verification and tests      | `REQUIRED / N/A` | `[test strategy]`        | `[command]`       |
| EB-04 Security and privacy        | `REQUIRED / N/A` | `[security boundary]`    | `[test/review]`   |
| EB-05 Maintainability             | `REQUIRED / N/A` | `[specific concern]`     | `[review]`        |
| EB-06 Dependencies                | `REQUIRED / N/A` | `[dependency rule]`      | `[lock/ADR]`      |
| EB-07 Diagnosis                   | `REQUIRED / N/A` | `[error behavior]`       | `[test/readback]` |
| EB-08 Experience and efficiency   | `REQUIRED / N/A` | `[UX/perf]`              | `[demo/test]`     |

### N/A justification

Record only items marked `N/A` whose absence is not obvious:

- `[EB-xx: reason]`

---

# 9. Project-specific constraints

Taken from the Engineering Profile or Spec:

- `[constraint]`
- `[constraint]`
- `[constraint]`

Do not duplicate the whole Profile.

---

# 10. Dependency policy

### New runtime dependency allowed?

`NO | YES, only if condition below is met`

If a new dependency is proposed, record:

- the concrete problem;
- the alternative without the dependency;
- the operational cost;
- filesystem/network/execution risk;
- the final decision.

If the dependency changes architecture or distribution, create an ADR.

---

# 11. Verification plan

Verification must be defined before the Build.

## Automated

```text
[command: unit/integration tests]
[command: lint]
[command: typecheck]
[command: build]
```

Remove commands that do not apply.

## Focused verification

- `[acceptance test]`
- `[security case]`
- `[error case]`

Each regression test is shown failing against the regression it names, by
mutation, including in formulas and context selection, not only in error
paths. A test double used as evidence has the property that evidence depends
on, such as persistence or concurrency, checked by a test of its own.

With persistent state, treat atomic writes, mutual exclusion and recovery
after interruption separately. Prove writing and recovery through
deterministic interruption at fixed points, such as a file size limit or
`SIGKILL` after each write; a race between processes may not expose a partial
write.

## Readback

After execution:

- reopen the relevant generated/changed files;
- verify that the persisted output is the expected one;
- confirm that no path outside the scope was changed, against the Build's
  entry commit fixed in this contract, including committed, staged, unstaged
  and untracked changes (`git status --porcelain`).

## Independent critique

`REQUIRED | OPTIONAL | N/A`

When required:

- `[second agent / human / verification skill]`
- who launches and collects the critique: `[orchestrator / human]`, never the Build;
- external prerequisites: `[harness authenticated / service running]`.

---

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [ ] `[observable criterion]`
- [ ] `[observable criterion]`
- [ ] all applicable checks in section 11 pass;
- [ ] there was no change outside the Allowed scope;
- [ ] relevant limitations are recorded;
- [ ] the final evidence was read, not just presumed from the exit code.

Each criterion names its referent:

- distinguish the project's own behavior or text from what a dependency
  generates;
- in a criterion about an existing artifact (formatting, lint, links), measure
  against the baseline when the file already fails the rule, for example "no
  new divergence in the changed lines";
- check every external standard name (RFC, ISO) used in a criterion against
  the standard's text; if the project diverges from it, name a profile of its
  own;
- before activation, confirm that the requested evidence is observable in the
  real environment, for example whether the harness shows what the criterion
  requires; without that certainty, run a probe or write the criterion with
  the available evidence and the limitation made explicit.

---

# 13. HOLD conditions

Stop and ask for a decision when:

- the required behavior contradicts the Spec/Constitution;
- an unplanned destructive action becomes necessary;
- a real secret is needed and there is no authorized mechanism;
- a new structural dependency is needed;
- the agent would need to write outside the authorized paths;
- the task would require unauthorized egress;
- the minimal solution no longer fits the contract;
- a critical requirement is ambiguous and different interpretations would change the architecture.

`HOLD` is a valid result.

---

# 14. FAIL conditions

Mark `FAIL` when:

- acceptance criteria cannot be met;
- verification shows a material regression;
- security cannot be preserved;
- the implementation produces inconsistent state;
- an external blocker makes the goal impossible within this contract.

Do not disguise `FAIL` as `DONE WITH NOTES`.

---

# 15. Change budget

The agent may:

- locally refactor code that is directly needed;
- remove code made obsolete by the change itself;
- update directly affected tests and documentation.

The agent may not, without HOLD:

- redesign broad architecture;
- change the stack;
- swap a structural library;
- move large areas of the project;
- resolve adjacent technical debt;
- add features that were not requested.

---

# 16. Completion report

When finished, answer briefly in the format below. In
[delegation](../skills/radiant-delegation/SKILL.md), this report is the Build's
return to the orchestrator.

### Status

`DONE | HOLD | FAIL`

### Changed

- `[path]: [what changed]`, with line references cited alongside the commit

### Verification evidence

```text
[commands and results]
```

### Engineering notes

- `[relevant trade-off or N/A]`

### Remaining limitations

- `[known limitation or none]`

### Learn Back candidate

- `[what this task taught that may deserve change elsewhere, or none]`

---

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**
