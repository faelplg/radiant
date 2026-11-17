# Single responsibility

- Id: `solid-srp`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability)

Keep the code serving one actor together, so another actor can change its
rules independently.

## Applies when

A module changes for more than one actor or independent business reason.

## Does not apply when

A script or module has parts that always change together; splitting it would
add coordination without isolating change.

## Violation signals

Changes requested by unrelated actors repeatedly edit the same module. A
reporting change breaks a calculation it did not intend to change.

## Verification

Review recent diffs and their requesting actors. Can each actor change its
rules without editing another actor's implementation? Record the coupled
files.

## Source

Robert C. Martin, [Agile Software Development, Principles, Patterns, and
Practices](https://www.informit.com/store/agile-software-development-principles-patterns-and-9780135974445)
(2002).

Robert C. Martin, [Clean Architecture: A Craftsman's Guide to Software
Structure and
Design](https://www.pearson.com/en-us/subject-catalog/p/clean-architecture-a-craftsmans-guide-to-software-structure-and-design/P200000009528)
(2017).

Robert C. Martin, [The Single Responsibility
Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
(2014).
