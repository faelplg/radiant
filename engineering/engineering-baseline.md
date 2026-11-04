# Radiant - Engineering Baseline

**Version:** 0.1\
**Status:** Initial operational baseline\
**Nature:** Radiant's engineering standard\
**Application:** Projects built with Radiant\
**Principle:** Engineering proportional to risk, impact and reversibility

---

## 1. Goal

The **Radiant Engineering Baseline** defines the minimum set of engineering expectations that must guide implementation and verification of projects carried out with Radiant.

It exists so agents do not have to infer, on every iteration, what "good engineering" means.

The Baseline is not:

- a universal style guide;
- a fixed list of technologies;
- a requirement for complex architecture;
- a collection of dogmas such as "use SOLID everywhere";
- a substitute for technical judgment.

It defines **expected outcomes and minimum limits**.

How to meet them depends on the project.

> **The Baseline sets the minimum. The Engineering Profile puts it in context. The Task Contract applies it. Verify produces evidence.**

---

## 2. Proportionality rule

Not every rule needs the same depth in every task.

Application must consider:

- impact of the change;
- cost of reversal;
- external exposure;
- data handling;
- security surface;
- durability of the code;
- operational criticality;
- number of users or systems affected.

Each Baseline item may be marked in a Task Contract as:

- `REQUIRED`;
- `APPLICABLE`;
- `N/A`, with a short justification.

`N/A` does not mean the rule was forgotten.

It means not applying it was deliberate.

---

# 3. EB-01 - Deliberate complexity

## Rule

> **Implement the smallest solution that satisfies the current contracts without anticipating architecture that has no evidence of need yet.**

### Expected

- avoid speculative abstractions;
- avoid infrastructure without a current consumer;
- avoid generalizing from a single case;
- keep module boundaries understandable;
- prefer reversible decisions while uncertainty is high;
- make any increase in complexity an explicit decision.

### Signs of violation

- a framework introduced only because "it may be useful later";
- an intermediate layer with no behavior of its own;
- an abstraction that makes the flow harder to understand;
- a database, queue, cache, service or integration added before an observed limitation exists;
- duplicated architecture to support scenarios outside the current scope.

### Possible evidence

- a small, localized diff;
- an ADR when a relevant structural decision is needed;
- explicit justification of a new dependency or infrastructure;
- removal of code or abstraction when it did not prove necessary.

---

# 4. EB-02 - Correctness and explicit contracts

## Rule

> **Important behaviors must have observable contracts and fail in an understandable way when invariants are violated.**

### Expected

- relevant invariants represented in code, schema or tests;
- validation at system boundaries;
- invalid states rejected early when reasonable;
- unhandled errors must not be used as normal flow;
- destructive or mutating operations must have clear semantics;
- idempotency must be sought when the operation can be safely repeated.

### Signs of violation

- behavior depends on undocumented implicit state;
- invalid input is silently accepted;
- an error is swallowed without evidence;
- a partially completed operation leaves ambiguous state;
- the contract described in the spec diverges from real behavior without a documentation update.

### Possible evidence

- schema validation;
- invariant tests;
- error cases;
- readback;
- an update to the Spec or ADR when the contract changes.

---

# 5. EB-03 - Risk-driven verification and tests

## Rule

> **Every change must have a proportional way to show that the expected behavior works and that relevant regressions were avoided.**

### Expected

- test behavior, not accidental implementation;
- fix bugs with a regression test when reasonable;
- use unit, integration, contract or end-to-end tests according to the boundary that needs to be proven;
- do not rely only on the implementing agent to declare completion;
- run readback when files or artifacts are generated;
- keep the suite fast enough to be used continuously.

### Not required

- 100% coverage;
- E2E for every feature;
- extensive snapshots;
- mocks that internally reproduce every dependency.

### Minimum evidence

The Task Contract must declare:

1. what needs to be proven;
2. how it will be proven;
3. which command or procedure produces the evidence.

---

# 6. EB-04 - Security, privacy and data control

## Rule

> **The solution must operate with the least access needed and treat secrets, private data and egress as explicit boundaries.**

### Expected

- secrets kept out of code and common artifacts;
- input validation at relevant boundaries;
- principle of least privilege;
- default deny when a sensitive permission is ambiguous;
- distinction between local reading and egress authorization;
- paths, commands and destructive operations treated as security surfaces;
- sensitive data must not appear in logs, error messages or real fixtures;
- dependencies that execute code or access the network must receive proportional scrutiny.

### Raising rigor

Changes that affect:

- authentication;
- authorization;
- egress;
- secrets;
- production;
- personal data;
- remote execution;
- filesystem access outside the authorized root;

must receive specific security verification.

---

# 7. EB-05 - Maintainability and readability

## Rule

> **The next human or agent must be able to understand the intent of the code without needlessly rebuilding the reasoning that created it.**

### Expected

- descriptive names;
- cohesive modules;
- small interfaces;
- understandable control flow;
- comments that explain non-obvious decisions, not retell the code;
- removal of dead code;
- duplication tolerated when abstracting early would be worse;
- abstraction when real repetition already reveals a stable concept;
- ecosystem conventions adopted by default.

### About well-known principles

SOLID, Clean Code, Clean Architecture, DRY, KISS and design patterns are useful references.

None of them is to be applied mechanically.

The right decision is the one that improves clarity, correctness, ability to change and verifiability in the real context.

---

# 8. EB-06 - Dependencies and supply chain

## Rule

> **Every dependency adds capability and also surface for maintenance, security and compatibility.**

### Expected

- introduce a dependency only when its value clearly exceeds the cost of owning it;
- use a lockfile or equivalent mechanism when the ecosystem offers one;
- avoid abandoned or needlessly privileged dependencies;
- prefer small, mature libraries for small problems;
- record structurally important dependencies in an ADR or equivalent documentation;
- update dependencies deliberately and verifiably;
- do not copy code of unknown provenance into the project.

### Before a new relevant dependency

Ask:

1. does the runtime or standard library already solve it?
2. which concrete problem does it remove?
3. what is the cost of removing it later?
4. does it execute code, access the filesystem or the network?
5. is there a smaller alternative?

---

# 9. EB-07 - Operability, diagnosis and observability

## Rule

> **When something fails, the system must provide enough information to locate the problem without guesswork.**

### Expected

- actionable errors;
- consistent exit codes when there is a CLI;
- logs only when they help operate or diagnose;
- no mandatory telemetry without an explicit decision;
- no sensitive information in logs;
- correlation between error, operation and affected resource when relevant;
- metrics, tracing and dashboards only when the kind of system justifies them.

### Proportionality

A local CLI may only need:

- clear error messages;
- paths;
- IDs;
- the violated rule;
- a suggested action.

A distributed service may require substantially more observability.

---

# 10. EB-08 - Experience quality and efficiency

## Rule

> **The system must respect the time, capacity and limitations of whoever uses it.**

### For human interfaces

Consider, when applicable:

- clarity;
- feedback;
- error prevention and recovery;
- accessibility;
- keyboard and screen readers;
- loading and failure states;
- understandable language.

### For CLIs and APIs

Consider:

- a useful `--help`;
- predictable commands;
- scriptable output when needed;
- messages stable enough for automation when declared as an interface;
- suitable exit codes;
- operations safe by default.

### For performance and resources

- do not optimize without evidence;
- avoid algorithms that are obviously unsuited to the expected volume;
- measure before introducing performance infrastructure;
- avoid work, network, storage or processing that does not produce observable value.

---

# 11. Engineering Profile per project

Each project may have an **Engineering Profile** that puts this Baseline in context.

The Profile may define:

- the project's default risk;
- stack and conventions;
- minimum quality per kind of change;
- test strategy;
- dependency policy;
- security boundaries;
- specific UX requirements;
- performance requirements;
- compatibility requirements;
- verification commands.

The Profile must not duplicate the Baseline.

It records only what is specific to that project.

---

# 12. Integration with Task Contracts

Every implementation Task Contract must reference:

- this version of the Engineering Baseline;
- the project's Engineering Profile, when there is one.

The contract does not need to copy the rules.

It must declare only:

- which rules are especially relevant;
- which have a specific adaptation;
- which are `N/A`;
- which evidence will be produced.

---

# 13. Integration with Verify

Verify must evaluate two things separately:

### Product correctness

> Was the requested behavior delivered?

### Engineering integrity

> Did the implementation respect the applicable engineering constraints?

A feature may work and still fail the second criterion.

Likewise, a technically elegant implementation that does not meet the hypothesis or acceptance criteria also fails.

---

# 14. Learn Back

When an engineering failure is observed, Learn Back must identify the right level.

Examples:

- rule missing for every project → update the Engineering Baseline;
- rule specific to AIKM → update the AIKM Engineering Profile;
- insufficient instruction in a single iteration → update the Task Contract;
- verification that did not catch a regression → update the Verify procedure;
- recurring implementation failure → create or update a skill/validator.

The Baseline must not grow with every isolated error.

A rule must enter here only when it is:

- recurring;
- applicable to multiple projects;
- verifiable;
- cheaper than the rework it avoids.

---

# 15. Final rule

> **Radiant must not replace engineering with generation. It must turn engineering into an explicit, proportional and verifiable constraint of the generation process.**

The goal of this Baseline is to let agents have autonomy to implement without getting freedom to silently redefine the quality standard.
