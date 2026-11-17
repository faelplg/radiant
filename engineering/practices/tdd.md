# Test-driven development

- Id: `tdd`
- Serves: [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests)

Write an expected behavior as a failing test, implement enough to pass, then
refactor with the suite green.

## Applies when

The expected result is known before coding, or a bug has a reproducible
failure.

## Does not apply when

A spike will be discarded, or exploration has not established an expected
result yet.

## Violation signals

A regression test passes before the fix. A deliberate removal of the protected
behavior still leaves its test green, or refactoring starts with a failing
suite.

## Verification

Record the initial failure and passing implementation. Mutate the protected
rule to make the regression test fail; restore it and rerun the suite.

## Source

Kent Beck, [Test Driven Development: By
Example](https://www.informit.com/store/test-driven-development-by-example-9780321146533)
(2002).

Martin Fowler, [Test Driven
Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) (2023
revision).
