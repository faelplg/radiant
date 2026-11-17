# Dependency inversion

- Id: `solid-dip`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests)

At a module seam, policy owns the interface that a replaceable detail
implements.

## Applies when

A policy module directly imports volatile I/O, networking or a vendor SDK, and
needs an interface it owns to replace or fake that detail.

## Does not apply when

The dependency is stable, such as the standard library, or has one
implementation and no test seam is needed.

## Violation signals

A policy test needs live vendor access. Replacing the storage detail edits the
module's business rules or exposes vendor types in its interface.

## Verification

Inspect imports and interface ownership. Run policy tests with a fake
implementing that interface, without loading or contacting the concrete
detail.

## Source

Robert C. Martin, [Agile Software Development, Principles, Patterns, and
Practices](https://www.informit.com/store/agile-software-development-principles-patterns-and-9780135974445)
(2002).

Robert C. Martin, [Clean Architecture: A Craftsman's Guide to Software
Structure and
Design](https://www.pearson.com/en-us/subject-catalog/p/clean-architecture-a-craftsmans-guide-to-software-structure-and-design/P200000009528)
(2017).
