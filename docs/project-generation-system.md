---
version: 0.2
status: Revised operational thesis
nature: Internal system for generating, developing, verifying and learning from projects
context: fael.tech / Longward
codename: Radiant
---

# Radiant - Project Generation System

## 1. Definition

**Radiant is the project generation and development system used to turn intent into real, verifiable systems that increase the capability of the cycles that follow.**

Radiant is not a final product.

Radiant is not a single agent.

Radiant is not just a documentation methodology.

Radiant is an operational layer that organizes how an intent is:

- questioned;
- framed;
- specified;
- planned;
- delegated;
- built;
- verified;
- turned into learning;
- folded back into the system itself.

Its main question is:

> **How do we turn an intent into a real system without losing clarity, context, evidence and learning along the way?**

---

## 2. Role in the ecosystem

Radiant has a role distinct from fael.tech, Longward and Foundation.

### fael.tech

Question:

> **What is worth exploring, building or learning?**

It is the personal lab where ideas can be born, investigated and turned into experiments.

### Longward

Question:

> **What deserves to become infrastructure for collective continuity?**

It is the institutional organization guided by Collective Continuity.

### Foundation

Question:

> **Should Longward exist to build something like this?**

It is Longward's institutional validation system.

### Radiant

Question:

> **How do we take this intent to a verifiable implementation and make the system learn from the result?**

Radiant does not decide the institutional destiny of an idea.

It receives a sufficiently clear intent and carries out its materialization.

---

## 3. The problem Radiant solves

The ability to produce software with artificial intelligence is growing quickly.

This lowers the cost of:

- writing code;
- generating documents;
- researching alternatives;
- creating tests;
- producing prototypes;
- running repetitive tasks;
- coordinating multiple agents.

At the same time, it creates new risks:

- building before understanding;
- accepting the first plausible solution;
- turning temporary prompts into permanent process;
- generating code without a clear hypothesis;
- producing documentation disconnected from the implementation;
- losing context between agents, tools and sessions;
- repeating decisions already made;
- validating one's own work without independent critique;
- recording lessons without fixing the system that failed;
- confusing memory with knowledge;
- confusing execution with evidence;
- duplicating rules across different agents;
- depending too much on a single model, IDE or vendor.

Radiant starts from a different hypothesis:

> **The main advantage of an agentic development system is not generating more code. It is reducing uncertainty in a disciplined way and increasing capability between cycles.**

---

## 4. Central thesis

Radiant's thesis is:

> **Better projects emerge when intent, specification, execution, verification and Learn Back are part of one continuous system.**

Radiant does not try to automate everything.

It tries to consciously organize:

- what needs to be understood;
- what needs to be questioned;
- what needs to be specified;
- what can be delegated;
- what needs to be verified;
- which evidence supports a conclusion;
- where an error needs to be fixed;
- what should remain available for the next project.

The expected result of a cycle is not just software.

It is:

> **delivered system + evidence + incorporated learning + accumulated capability.**

---

## 5. Intent before generation

Radiant does not start with code.

It starts with intent.

Before building, the system needs to be able to answer:

- What are we trying to change?
- For whom?
- What problem or opportunity exists?
- What is the central hypothesis?
- What is the smallest phenomenon we need to prove?
- What do we not need to build yet?
- What would make this hypothesis wrong?

A poorly framed idea is still poorly framed even when implemented quickly.

Therefore:

> **generation speed does not replace clarity of intent.**

---

## 6. The Radiant cycle

Radiant's initial operational cycle is:

> **Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify → Learn Back**

Each stage reduces a different kind of uncertainty.

---

### 6.1. Frame

Turns a broad intent into an initial contract of understanding.

Main artifact:

**Radiant Project Frame**

It should record:

- intent;
- problem;
- desired transformation;
- participant or user;
- central hypothesis;
- constraints;
- critical assumptions;
- smallest relevant experiment;
- minimum evidence of success;
- non-goals;
- open questions.

---

### 6.2. Challenge

Questions assumptions before they turn into architecture.

Typical questions:

- Do we really need a product?
- Do we really need this interface?
- Is there a smaller solution?
- Are we solving the problem or implementing the first shape we imagined?
- Which assumption could invalidate a large part of the project?
- What are we adding only because the technology allows it?

Radiant may implement this function through a skill or agent provisionally called **Grill**.

Its goal is not to block.

It is to keep speed from being mistaken for conviction.

---

### 6.3. Spec

Describes the expected behavior before deciding every implementation detail.

It may produce:

- Implementation Spec;
- Domain Spec;
- Workspace Spec;
- Interface Contract;
- invariants;
- states;
- events;
- acceptance criteria;
- non-functional requirements;
- safety limits.

The specification works as an intermediate contract between intent and code.

---

### 6.4. Design

Defines how the system will be structured and how the experience will be perceived, understood and used.

Radiant recognizes two conceptually distinct tracks, which may coexist in the same project:

#### 6.4.1. System Design

Concerns the internal structure of the system:

- architecture;
- domain model;
- components;
- contracts;
- persistence;
- integrations;
- technical decisions;
- trade-offs;
- ADRs.

#### 6.4.2. Experience Design

Concerns how people perceive, understand and use the system:

- experience intent;
- information architecture;
- journeys and flows;
- states and interactions;
- responsiveness;
- accessibility;
- visual expression;
- behavior and feedback;
- coherence between intent and implementation.

Radiant's Design Layer formalizes this separation without creating a parallel process. The Design stage must preserve the difference between system structure and user experience. The specialized canonical body is in [Radiant Design Layer](design-layer.md).

Radiant should favor reversible decisions while uncertainty is high and keep formality proportional to risk.

---

### 6.5. Plan

Turns the spec into executable increments.

Main artifact:

**Implementation Plan**

A good plan is not a long list of tasks.

It is a sequence of increments able to:

- reduce risk;
- produce observable behavior;
- generate evidence;
- allow early stopping when the hypothesis turns out weak.

---

### 6.6. Contract

Before delegating relevant agentic work, Radiant may generate a **Task Contract**.

The contract exists to keep agents from freely interpreting a broad intent.

A Task Contract should declare, in proportion to the task:

- task identity;
- goal;
- inputs;
- exact outputs;
- canonical paths;
- owner;
- constraints;
- non-goals;
- completion criteria;
- verification method;
- HOLD or FAIL conditions;
- safety limits;
- external blockers;
- execution limit when applicable.

The contract should be small.

Its job is to make delegation verifiable.

---

### 6.7. Build

Executes the increments.

Agents may:

- implement;
- generate tests;
- refactor;
- research APIs;
- update documentation;
- prepare migrations;
- review changes;
- run checklists.

Building must never disconnect from Frame, Spec and Contract.

---

### 6.8. Verify

Radiant treats verification as a stage of its own.

Not as an automatic consequence of Build.

It may involve:

- automated tests;
- static analysis;
- acceptance criteria;
- architectural review;
- manual execution;
- security;
- performance;
- accessibility;
- readback of artifacts;
- review by another agent;
- human evaluation;
- comparison between intent, spec and implementation.

The principle is:

> **whoever creates should not be the only entity responsible for declaring it correct.**

---

### 6.9. Learn Back

Radiant should not only record lessons.

It should determine:

> **which part of the system needs to be fixed so the next execution is better?**

Examples:

- intent problem → fix the Frame;
- poorly tested assumption → fix the Challenge;
- ambiguity → fix the Spec;
- bad architectural decision → fix the Design or an ADR;
- inadequate decomposition → fix the Plan;
- insufficient instruction → fix the Task Contract or Skill;
- recurring execution failure → fix the Procedure;
- inadequate verification → fix the Verification Rule;
- wrong or obsolete knowledge → fix Knowledge;
- misunderstood context → fix Context;
- rule needed in every execution → promote a pointer to Operational Memory.

The cycle only closes when the lesson changes the responsible system.

---

## 7. Learn Back as a structural principle

A system that only stores retrospectives does not necessarily learn.

Radiant considers learning real when an observation produces a change in a responsible layer.

Flow:

> **Outcome → Evidence → Diagnosis → Fix Target → Change → Reuse**

Every relevant failure should be able to answer:

1. What happened?
2. What evidence do we have?
3. Why do we believe it happened?
4. Which layer could have prevented it?
5. What needs to change?
6. How will we verify that the change worked?

This logic avoids a passive memory of errors.

---

## 8. Radiant Project Frame

The **Radiant Project Frame** is the initial contract between intent and building.

It is not a full PRD.

Its job is to keep a project from starting directly with features.

It should be small enough to be used.

And explicit enough to let another person or agent understand:

- why the project exists;
- what needs to be proven;
- what is deliberately left out.

---

## 9. Radiant Constitution

The [Radiant Constitution](../constitution/CONSTITUTION.md) is the canonical
normative source of the operational principles. This thesis explains the
system; it does not keep a second list of rules. See the Constitution for
precedence, articles, operational states and constitutional amendments.

### Engineering as an explicit constraint

Radiant does not replace engineering practices with the use of agents. Projects
may adopt a [Radiant Engineering Baseline](../engineering/engineering-baseline.md)
with minimum expectations and an Engineering Profile with specific adaptations.
The Baseline does not impose a universal architecture or stack; it applies in
proportion to risk, impact and reversibility.

Task Contracts reference these rules, Verify produces evidence of conformance
and Learn Back fixes the responsible layer when a rule proves insufficient.

## 10. Core and adapters

Radiant should separate:

```text
Radiant Core
    ↓
Capabilities / Skills
    ↓
Adapters
    ↓
Agent Runtime / Harness
    ↓
Model / Tool
```

### Core

Contains:

- Constitution;
- cycle;
- artifacts;
- verification rules;
- contracts;
- Learn Back;
- memory conventions;
- safety principles.

### Adapters

Connect Radiant to environments such as:

- Codex;
- Claude Code;
- IDE agents;
- CLI agents;
- local runtimes;
- future harnesses.

Adapters should not duplicate core rules.

They should point to them.

---

## 11. One body, everywhere else pointers

Radiant adopts the rule:

> **one canonical body; in other systems, only references when possible.**

Example:

- a shared skill lives in the canonical repository;
- Codex receives a pointer;
- Claude Code receives a pointer;
- a native memory may hold only the location and usage instruction;
- AIKM preserves origin, version, usage and learning.

This reduces:

- drift;
- duplication;
- conflicting rules;
- repeated maintenance.

---

## 12. Skills as units of capability

A **skill** encapsulates a reusable competence.

Examples:

- `grill-project-hypothesis`
- `write-implementation-spec`
- `model-domain`
- `create-implementation-plan`
- `create-task-contract`
- `review-security`
- `verify-acceptance-criteria`
- `extract-project-learning`
- `route-learn-back`

An ideal skill defines:

- goal;
- inputs;
- required context;
- process;
- constraints;
- output format;
- quality criteria;
- verification method;
- known failures;
- Learn Back target when relevant.

Skills turn operational experience into infrastructure.

---

## 13. Grill as a pressure mechanism

Radiant should have an explicit capability for adversarial critique.

**Grill** challenges:

- assumptions;
- the need for the solution;
- scope;
- complexity;
- architecture;
- dependencies;
- metrics;
- evidence;
- irreversibility.

Grill should happen before expensive decisions.

It can also be reapplied when the project starts accumulating unplanned complexity.

---

## 14. Spec-Driven Development

Radiant incorporates Spec-Driven Development as a mechanism, not as its whole identity.

Flow:

> **Intent → Spec → Contract → Implementation → Verification → Learn Back**

The spec is not frozen documentation.

When reality contradicts the specification, Radiant should record:

- what changed;
- why it changed;
- which evidence justified the change;
- whether the Frame, Spec or Design need to be updated.

The goal is to keep implementation and intent from drifting apart silently.

---

## 15. Separate creation and critique

Whenever possible, Radiant separates generation and evaluation roles.

Examples:

- one agent implements and another reviews;
- one agent writes the spec and another looks for ambiguities;
- one agent proposes an architecture and another looks for risks;
- one agent produces an answer and another checks evidence;
- one agent generates tests and another checks whether the tests cover the criteria;
- one agent synthesizes a lesson and another identifies the right Learn Back layer.

This reduces self-confirmation.

---

## 16. Verification proportional to risk

Not every task needs the same rigor.

Radiant should choose the depth of verification based on:

- durability;
- reversibility;
- external exposure;
- impact;
- safety;
- factual importance.

An initial model may use four tiers:

### Tier 0 - Quick

Disposable, low-risk task.

Verify only what is needed to avoid reporting something materially wrong.

### Tier 1 - Durable

Artifact that will be reused.

Verify:

- adherence to the request;
- structure;
- integrity;
- provenance;
- readability;
- discoverability.

### Tier 2 - Deep

Architecture, research, proposal, important spec or publication.

Add:

- specific criteria;
- risk analysis;
- critical claims;
- a second reading.

### Tier 3 - High Impact

Security, production, sensitive data, irreversible decisions or high-consequence public outputs.

Add:

- explicit evidence;
- independent review;
- approval gates;
- a rollback plan when applicable.

Rigor should follow risk, not the length of the text.

---

## 17. Evidence

Radiant should distinguish:

- something retrieved;
- something actually inspected;
- something that supports a conclusion;
- something in conflict;
- something outdated.

Especially in research and technical decisions:

> **retrieval is not verification.**

A source that was found does not automatically support a decision.

Radiant may later structure evidence packets, but that capability should only be born when usage justifies it.

---

## 18. Task Contracts

Task Contracts are the operational unit between planning and agentic execution.

A contract exists to answer:

> **Does the agent know exactly what it must produce, where, under which limits and how completion will be verified?**

A good contract should avoid:

- implicit scope;
- vague outputs;
- "done" without readback;
- unauthorized changes;
- silent expansion;
- open-ended execution.

Task Contracts should not turn into a new PRD.

They should stay bounded.

Beyond functional limits, a contract may declare Baseline and Profile,
Engineering Check, dependency policy, verification commands and
engineering-specific HOLD conditions. The contract references these
documents; it does not copy their bodies.

---

## 19. Operational memory

Radiant needs to accumulate:

- decisions;
- patterns;
- failures;
- experiences;
- solutions;
- trade-offs;
- components;
- skills;
- contexts;
- evaluations;
- experiment results;
- prevention rules.

This memory should be organized by function.

Not everything needs to be loaded all the time.

Radiant should distinguish, at least conceptually:

### Knowledge

What we know.

### Context

What is true for a specific project, person or situation.

### Procedure

How to do something repeatedly.

### Operational Memory

Short, stable pointers that need to be known before acting.

### Action / Execution Evidence

What happened in a relevant execution.

### Evaluation

Failures, criteria and verifications.

This separation keeps "memory" from becoming an undifferentiated dump.

---

## 20. Relation to AIKM

> **State note (2026-10-15):** the mentions of AIKM in sections 11, 20, 21, 32, 33, 37 and 42 describe AIKM v1, a knowledge preservation and retrieval layer. Since revision 2 of the AIKM Frame (2026-10-12), AIKM manages skills, context and MCP servers per project, and that knowledge layer is a non-goal. The current boundary is in [integration](integration.md#aikm-boundary); the text below remains as a record of thesis 0.2.

The **AI Knowledge Manager**, internally abbreviated as **AIKM**, is the candidate infrastructure for preserving and retrieving the operational assets produced by Radiant.

The roles remain distinct:

### Radiant

Orchestrates how projects are turned from intent into a system.

### AIKM

Preserves and retrieves the operational knowledge accumulated across those projects.

The desired relation is:

> **Radiant executes → produces evidence and learning → AIKM preserves → Radiant retrieves → the next cycle starts with more capability.**

This relation should not create duplication.

Radiant is process.

AIKM is knowledge infrastructure.

---

## 21. Intake and classification

Radiant should avoid requiring perfect classification at capture time.

A healthy architecture allows:

> **capture first → classify later → promote when there is enough evidence.**

This reduces friction.

It also allows distinguishing:

- raw material;
- synthesized knowledge;
- context;
- procedure;
- execution;
- evaluation;
- promoted learning.

AIKM may implement this intake and routing function.

---

## 22. Knowledge and lifecycle

AI-produced content should not become canonical automatically.

A useful conceptual lifecycle is:

```text
candidate
    ↓ explicit review
active / reviewed
    ↓ replacement
superseded
    ↓ end of life
deprecated / archived
```

The exact state may vary by artifact type.

The principle remains:

> **generated does not mean trustworthy; retrieved does not mean true; used does not mean canonical.**

---

## 23. Security and egress

Radiant should distinguish:

- the ability to read locally;
- permission to send to an external tool.

Something may be useful in local context and still not be allowed to leave the machine.

Therefore:

> **visibility does not imply egress permission.**

Pay special attention to:

- secrets;
- private code;
- personal data;
- business data;
- credentials;
- private conversations;
- client artifacts;
- internal documents.

Adapters and agents must respect this boundary.

---

## 24. Radiant artifacts

Radiant should only produce artifacts that have an operational function.

### Radiant Project Frame

Defines intent and experiment.

### Implementation Spec

Defines behavior, rules and criteria.

### Domain / Technical Spec

Goes deeper into areas that require precision.

### Implementation Plan

Organizes increments.

### Task Contract

Turns an increment into bounded agentic work.

### ADR

Records structural decisions.

### Verification Report

Records what was actually verified.

### Learning Record

Records outcome, evidence, diagnosis and Learn Back.

### Engineering Baseline

Defines the minimum engineering standard reusable across projects.

### Engineering Profile

Puts the Baseline in context for a project without duplicating it.

Not every project needs every artifact.

Formality is proportional to risk and complexity.

---

## 25. Artifacts as system state

The documents are not just reports.

They are part of the project's operational state.

Flow:

```text
Project Frame
    ↓
Implementation Spec
    ↓
Implementation Plan
    ↓
Task Contracts
    ↓
Build
    ↓
Verification Report
    ↓
Learning Record
    ↓
Learn Back
    ↓
Knowledge / Skill / Context / Rule
```

Each stage should be able to point to the previous one when that improves traceability.

---

## 26. Human-in-the-loop

Radiant does not assume full autonomy.

### Can be highly automated

- scaffolding;
- test generation;
- local refactors;
- derived documentation;
- lint;
- search;
- mechanical tasks;
- running checklists;
- structural validations.

### Requires more human participation

- intent;
- purpose;
- prioritization;
- economic choices;
- scope changes;
- ethical decisions;
- sensitive data;
- production;
- irreversible trade-offs;
- approval of canonical knowledge.

The system's job is not to remove the human.

It is to expand their capability without eliminating responsibility.

---

## 27. Model-agnostic and tool-agnostic

Radiant should work with different:

- models;
- IDEs;
- CLIs;
- coding agents;
- runtimes;
- providers;
- version control systems;
- documentation tools.

The process belongs to Radiant.

The execution belongs to the chosen runtime.

---

## 28. Security and execution limits

An agentic system needs to operate within explicit boundaries.

Radiant should consider:

- minimum permissions;
- isolated environments;
- secrets kept out of prompts;
- egress policy;
- review of destructive commands;
- restricted access to production;
- network limits;
- provenance of changes;
- selective logs;
- approval gates;
- rollback when relevant.

Autonomy should be proportional to reversibility.

---

## 29. Metrics

Radiant should not be evaluated by speed alone.

### Intention-to-Working-System

Time between a clear intent and the first working system.

### Spec Drift

Material difference between intent/spec and implementation.

### Verification Escape Rate

Problems that should have been caught before completion.

### Rework Rate

Rework caused by inadequate framing or specification.

### Knowledge Reuse Rate

Percentage of projects that reuse earlier knowledge.

### Learn Back Rate

Percentage of relevant failures that produce an explicit fix in the responsible layer.

### Learning Yield

Quantity and quality of reusable knowledge produced per cycle.

### Task Contract Compliance

Percentage of executions that stay within the agreed outputs and limits.

### Human Intervention Quality

Points where human participation materially changes quality or direction.

The main metric remains:

> **convergence between intent, delivered system, evidence and accumulated capability.**

---

## 30. What Radiant is not

> **State note (2026-10-16):** Radiant defines how agentic flows are split into units, routed to harnesses and accepted. Execution and observation belong to the harnesses and to an external operator, Demerzel, as set out in [ADR-0002](adrs/ADR-0002-backend-dispatch-demerzel.md), [ADR-0003](adrs/ADR-0003-demerzel-independent-core.md) and [integration](integration.md#demerzel-boundary). The text below remains as a record of thesis 0.2.

Radiant is not:

- an agent framework;
- an IDE;
- a coding agent;
- a collection of prompts;
- a substitute for engineering;
- an automatic startup generator;
- a rigid methodology;
- a heavy documentation system;
- an excuse to automate relevant human decisions;
- an isolated knowledge base.

Radiant is an operational layer on top of these capabilities.

---

## 31. Principle of proportionality

Small projects should generate little bureaucracy.

Larger or riskier projects should generate more structure.

### Small experiment

May require:

- Project Frame;
- short spec;
- short plan;
- optional Task Contract;
- build;
- verify;
- learning record.

### Higher-risk product

May require:

- domain spec;
- threat model;
- ADRs;
- task contracts;
- security review;
- observability;
- rollback strategy;
- more rigorous evidence;
- additional human review.

Radiant increases rigor as the cost of error increases.

For small experiments, the Baseline may be applied directly and the Profile
may be omitted. For products with multiple iterations, integrations, sensitive
data or operational risk, the Profile and engineering evidence become
recommended.

---

## 32. First implementation of Radiant

The first implementation of Radiant does not need to be a platform.

It can exist as a repository with:

```text
radiant/
  constitution/
  templates/
  skills/
  adapters/
  workflows/
  contracts/
  validators/
  projects/
  knowledge/
```

Recommended initial components:

1. Radiant Constitution;
2. Project Frame template;
3. Grill skill;
4. Implementation Spec skill;
5. Implementation Plan skill;
6. Task Contract template;
7. Verification skill;
8. Learn Back skill;
9. initial adapters for the harnesses in use;
10. gradual integration with AIKM.
11. Radiant Engineering Baseline and Profile template.

The infrastructure should grow from real use.

---

## 33. First test: AI Knowledge Manager

The first project carried out by Radiant is the **AI Knowledge Manager - AIKM**, incubated by fael.tech.

This test is suitable because:

- it solves a real pain;
- it has a controllable scope;
- it has prior conceptual reflection;
- it can be used by Radiant itself;
- it allows observing reuse across projects;
- it allows testing core-adapter separation;
- it allows testing Learn Back.

The initial cycle should produce:

### Project Frame

Defines intent and hypothesis.

### Implementation Spec

Defines the smallest necessary system.

### Implementation Plan

Splits it into increments.

### Task Contracts

Bound relevant agentic work.

### Build

Implements.

### Verify

Confirms behavior and hypothesis.

### Learn Back

Updates AIKM and Radiant with what was discovered.

---

## 34. Success criterion of the first test

Radiant will not be considered validated because it generated code.

The first test will be promising when we observe:

> An intent is framed.\
> Assumptions are questioned.\
> The spec guides the implementation.\
> The plan reduces the work to increments.\
> Agents receive bounded contracts.\
> The implementation is verified by criteria external to the generation itself.\
> Use produces real evidence.\
> A failure or discovery produces Learn Back.\
> Knowledge produced is reused in a later cycle.

The decisive point is:

> **the second cycle should start better because of the first.**

---

## 35. System evolution

Radiant should evolve through its own projects.

A capability only enters the core when:

- it shows up repeatedly;
- it has value in more than one project;
- it can be abstracted without erasing context;
- it has a verification method;
- its operational cost is lower than the rework it avoids.

This may produce new:

- skills;
- validators;
- templates;
- adapters;
- contracts;
- rubrics;
- Constitution rules.

The system should grow from the inside out.

---

## 36. Relation to publication

Radiant is an internal project.

It does not need to be presented publicly as a product.

Real lessons may lead to publications by fael.tech about:

- agentic development;
- Spec-Driven Development;
- core-adapter architectures;
- human-in-the-loop;
- verification;
- task contracts;
- Learn Back;
- operational memory;
- AI-assisted engineering.

Publication should come from the evidence produced by the work.

Not from a methodology presented as universal before it is tested.

---

## 37. Operational references and adoption limits

Radiant can learn from external systems for agentic engineering and knowledge management.

A relevant example is the **DECK6/akm** project, which demonstrates practices such as:

- separation between knowledge, context, procedure, action and evaluation;
- core-adapter separation;
- Learn Back;
- verification proportional to risk;
- task contracts;
- canonical knowledge separate from derived indexes;
- pointers instead of duplication;
- explicit lifecycle;
- distinction between local availability and egress.

Radiant should not copy its architecture wholesale.

Radiant's problem is different:

> **orchestrating project generation.**

AIKM's problem is:

> **preserving and retrieving operational knowledge.**

External references should improve our principles without erasing the specific nature of our systems.

---

## 38. Long-term hypothesis

If Radiant works, each new project should start with more capability than the previous one.

Not just because the models got better.

But because the system accumulated:

- better questions;
- better specs;
- better contracts;
- better procedures;
- better verification criteria;
- better patterns;
- better contexts;
- better retrieval mechanisms;
- knowledge about earlier failures.

Radiant comes to work as learning infrastructure for building software and products.

---

## 39. Operational mission

> **Turn intent into verifiable systems and turn each cycle into capability for the next one.**

---

## 40. Vision

Create an environment where humans and agents can develop projects without depending on disposable conversations, lost context or improvised generation.

A system where:

- intent stays visible;
- agents receive clear boundaries;
- specifications guide building;
- contracts make delegation verifiable;
- decisions preserve context;
- results are evaluated in proportion to risk;
- errors fix the responsible layer;
- learning is preserved;
- new projects reuse earlier capability.

Radiant should not only help build faster.

It should help:

> **build with continuity and learn operationally.**

---

## 41. Fundamental question

Every evolution of Radiant should answer:

> **Does this capability reduce uncertainty, improve verification, reduce duplication or turn experience into reusable capability?**

If it does none of these things, it probably does not belong in the system.

---

## 42. Current state

Radiant has a revised operational thesis.

The first experiment is still the **AI Knowledge Manager - AIKM**.

The next stage is to update the AIKM documents to reflect:

- intake and routing;
- separation between type and role of knowledge;
- execution evidence;
- Learn Back;
- lifecycle;
- core-adapter separation;
- verification;
- egress safety;
- simplifying the MVP when possible.

After that:

> **Frame → Spec → Plan → Contract → Build → Verify → Learn Back**

The thesis can now be summarized like this:

> **Radiant turns intent into building, building into evidence and evidence into accumulated capability.**
