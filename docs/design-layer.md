# Radiant Design Layer v0.1

## Role

Radiant's design layer defines how a project's intent turns into a coherent, understandable and verifiable experience before it becomes the final implementation.

The Design Layer does not replace Radiant's thesis or create a parallel process. It organizes the part of uncertainty that concerns the structure of the experience and how the system conveys meaning, behavior and responsibility to whoever uses it.

Its role is to answer:

> How does intent become a legible, coherent and verifiable experience without losing the project's hypothesis?

## System and experience

The design layer recognizes two conceptually distinct tracks:

### System Design

Concerns the internal structure of the system:

- architecture;
- domain and rules;
- components and interfaces;
- data and contracts;
- integrations;
- trade-offs;
- implementation constraints;
- ADRs and technical decisions.

### Experience Design

Concerns how people perceive, understand and use the system:

- experience intent;
- information architecture;
- journeys and flows;
- states and interactions;
- accessibility;
- feedback and clarity;
- visual expression;
- cooperation between behavior and language;
- consistency without artificial homogenization.

These tracks influence each other, but they are not synonyms. The system's structure does not decide the whole experience and the experience does not replace the architecture.

## When design is needed

Design must be applied in proportion to risk, reversibility and the relevance of the experience.

### Projects without a relevant experience

May use only System Design, focused on domain, data flow, architecture and delivery criteria.

### Small projects and reversible changes

May use only a Design Frame and criteria in the Contract, without a detailed Design Spec.

### Public products, critical flows or complex experiences

May require:

- Design Frame;
- Design Spec;
- accessibility review;
- prototyping or flow readback;
- validation with users or with real-use criteria.

The procedural requirement must grow with the product's relevance and the cost of error.

## Relation to the Radiant cycle

The Design Layer fits into Radiant's macro cycle:

> Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify → Learn Back

The difference is that the Design stage is now explicitly understood as two complementary tracks:

- System Design: structure and feasibility of the system;
- Experience Design: behavior, legibility and perceived outcome.

The Design Layer does not replace the Spec. It makes the intent of the experience operationally legible before implementation.

## Artifacts of the layer

### Design Frame

Used to frame the experience before detailing the solution. It must answer:

- what the experience needs to allow;
- who uses it and in which context;
- which perception or relationship we want to produce;
- which journeys and states are critical;
- which constraints exist;
- where the greatest risk of friction or confusion is;
- which decisions must stay simple;
- what will not be designed yet.

The Design Frame is not a mockup or a list of screens. It is a minimum contract of experiential intent.

### Design Spec

Used when the experience requires more precision. It may describe:

- information architecture;
- navigation and flows;
- states and transitions;
- feedback and errors;
- interaction rules;
- responsiveness patterns;
- accessibility;
- visual direction;
- indicators of coherence with the product;
- experience acceptance criteria.

The Design Spec must be implementable and verifiable, not a collection of screenshots without semantics.

## Design principles

The Design Layer operates with principles that reduce uncertainty before implementation:

- intent before interface;
- structure before style;
- experience before components;
- interaction as system behavior;
- accessibility as a design constraint;
- states as part of the design;
- consistency without artificial homogenization;
- implementation must preserve intent;
- design proportional to risk.

These principles can be inherited by projects or organizations without being duplicated in each instance. Radiant keeps the rule that there is one canonical body and the other environments receive pointers.

## Prototyping and review

The Design Layer accepts prototyping when it reduces uncertainty. But it does not require a prototype in every project. Prototyping serves to validate:

- the intent of the journey;
- clarity of flow;
- critical states;
- perception of hierarchy;
- labels, feedback and actions.

Design review must observe the system as a real experience, and not just as a set of components or a layout. It evaluates:

- intent;
- clarity of structure;
- coherence of interaction;
- accessibility;
- consistency;
- implementation and preservation of the original intent;
- unnecessary complexity.

## Verification and Learn Back

Design verification must include relevant evidence:

- contrast and legibility;
- clarity of flow;
- accessibility;
- states and errors;
- coherence with the Spec;
- preservation of intent against the implementation.

If the experience fails, the problem must go back to the responsible layer:

- intent problem → Frame or Design Frame;
- structure problem → Design Frame or Design Spec;
- flow problem → Design Spec;
- pattern problem → organizational principle or design system;
- implementation problem → Build and Verification;
- recurring accessibility or clarity problem → Design Principle, Verification Rule or process.

This mapping preserves Radiant's central rule: relevant learning must fix the responsible layer.

## Tools

The Design Layer is tool-agnostic. It does not require Figma, Penpot, Storybook, AI prototyping or a specific framework. Tools may be chosen as a project procedure, but they do not define the identity of the process.

## Limits

The Design Layer does not turn Radiant into an isolated UX methodology. It remains part of the project generation system, alongside Frame, Spec, Contract, Verify and Learn Back.

It also does not require a heavy layer of visual documentation for every project. Rigor follows risk, reversibility and impact.
