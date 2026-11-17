# Clean Architecture and the dependency rule

- Id: `clean-architecture`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity)

Across concentric rings, source dependencies point inward toward domain
policy; outer mechanisms adapt to inner contracts.

## Applies when

A durable system needs domain rules to outlive frameworks, storage and
delivery mechanisms.

## Does not apply when

A small tool, script or prototype would have rings with no behavior of their
own.

## Violation signals

Domain code imports a web framework or database row type. A framework upgrade
changes use-case rules, or inner tests cannot run without outer
infrastructure.

## Verification

Review the dependency graph across rings and run domain/use-case tests without
frameworks or storage. Check that crossing data uses inner-owned
representations.

## Source

Robert C. Martin, [The Clean
Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
(2012).

Robert C. Martin, [Clean Architecture: A Craftsman's Guide to Software
Structure and
Design](https://www.pearson.com/en-us/subject-catalog/p/clean-architecture-a-craftsmans-guide-to-software-structure-and-design/P200000009528)
(2017).
