# Interface segregation

- Id: `solid-isp`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability)

Each consumer depends on the operations it needs, without inheriting unrelated
obligations.

## Applies when

An interface has several consumers using disjoint parts.

## Does not apply when

The interface has one consumer; splitting it has no demonstrated consumer
boundary.

## Violation signals

Implementations supply unused stubs or throw unsupported-operation errors.
Adding an operation for one consumer forces unrelated consumers to change.

## Verification

Review a consumer-to-method usage matrix and the last interface change. Can
each consumer compile and test against only the operations it uses?

## Source

Robert C. Martin, [Agile Software Development, Principles, Patterns, and
Practices](https://www.informit.com/store/agile-software-development-principles-patterns-and-9780135974445)
(2002).
