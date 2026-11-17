# Test pyramid and test strategy

- Id: `test-strategy`
- Serves: [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests)

Prove behavior at the smallest useful level, with integration and end-to-end
checks for boundaries that smaller tests cannot establish.

## Applies when

Any change has behavior to prove.

## Does not apply when

A documentation-only change is verified by readback and reference checks.

## Violation signals

A behavior is covered only through slow UI tests. Unit tests mock both sides
of an integration, or a production boundary has no executable check.

## Verification

Map each risk to a test level; run focused unit, integration and critical
end-to-end paths. Review duration, flakiness and what each level actually
proves.

## Source

Mike Cohn, [Succeeding with Agile: Software Development Using
Scrum](https://www.informit.com/store/succeeding-with-agile-software-development-using-scrum-9780321770387)
(2009).

Ham Vocke, [The Practical Test
Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
(2018).
