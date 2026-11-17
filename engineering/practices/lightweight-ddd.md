# Lightweight domain-driven design

- Id: `lightweight-ddd`
- Serves: [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts), [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability)

Use shared domain language, explicit context boundaries and value objects that
protect invariants. This is a modeling choice, not a layering rule.

## Applies when

A domain has real rules, experts share terms with the code, and words may have
different meanings across bounded contexts.

## Does not apply when

CRUD or plumbing has no domain rules. Aggregate and repository boilerplate
around simple CRUD would add heavy tactical ceremony.

## Violation signals

Experts and code use different names for the same rule. One model mixes
conflicting meanings, or primitive values repeatedly bypass the same
invariant.

## Verification

Read scenarios and names with a domain expert, map context boundaries, and
test invalid value construction. Record vocabulary disagreements and the
owning context.

## Source

Eric Evans, [Domain-Driven Design: Tackling Complexity in the Heart of
Software](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217)
(2003).

Vaughn Vernon, [Domain-Driven Design
Distilled](https://www.informit.com/store/domain-driven-design-distilled-9780134434995)
(2016).

Martin Fowler, [Bounded
Context](https://martinfowler.com/bliki/BoundedContext.html) (2014) and
[Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)
(2006).
