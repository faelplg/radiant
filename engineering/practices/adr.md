# Architecture decision records

- Id: `adr`
- Serves: [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity), [EB-06](../engineering-baseline.md#8-eb-06---dependencies-and-supply-chain)

Record a significant decision with its context, alternatives and consequences
so later readers can assess its rationale.

## Applies when

A structural decision is costly to reverse or would make a later reader
question why it was chosen.

## Does not apply when

A local, reversible choice is already clear in the diff.

## Violation signals

A new dependency or storage boundary has no recorded rationale. An accepted
decision is overwritten, leaving no explanation of what superseded it.

## Verification

Review the decision against its originating diff: are constraints, rejected
options and consequences recoverable? Check links from a superseding record to
the earlier one.

## Source

Michael Nygard, [Documenting Architecture
Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
(2011).
