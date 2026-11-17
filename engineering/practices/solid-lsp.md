# Liskov substitution

- Id: `solid-lsp`
- Serves: [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts)

An alternative implementation preserves the behavioral promises callers rely
on from the shared type.

## Applies when

Code substitutes implementations behind a shared type or interface.

## Does not apply when

No subtype or alternative implementation exists.

## Violation signals

Callers branch on concrete types to avoid broken behavior. A replacement
rejects previously valid inputs, weakens results or breaks a shared invariant.

## Verification

Run the same contract tests against every implementation, covering accepted
inputs, outputs, errors and state transitions. Review preconditions,
postconditions and invariants.

## Source

Barbara H. Liskov and Jeannette M. Wing, [A Behavioral Notion of
Subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf) (1994).
