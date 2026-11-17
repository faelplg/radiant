# Open-closed

- Id: `solid-ocp`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity)

Extend a stable variation point by adding a variant without changing the
existing variants.

## Applies when

A second real variant exists, the variation point is stable, and evidence
supports another variant.

## Does not apply when

Only one variant exists. An extension point built from one case is premature
generalization under EB-01.

## Violation signals

Every new variant edits the same dispatch conditional in several files. Git
history shows unrelated variants repeatedly changing existing implementations.

## Verification

Review the last variant diff: does it add the new behavior with at most one
registration change, while existing variant tests still pass?

## Source

Bertrand Meyer, [Object-Oriented Software
Construction](https://archive.eiffel.com/general/people/meyer/publications/publications.html)
(1988).

Robert C. Martin, [Agile Software Development, Principles, Patterns, and
Practices](https://www.informit.com/store/agile-software-development-principles-patterns-and-9780135974445)
(2002).

Robert C. Martin, [The Open Closed
Principle](https://blog.cleancoder.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)
(2014).
