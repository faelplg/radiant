# Ports and adapters

- Id: `ports-and-adapters`
- Serves: [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests), [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability)

The application defines driving and driven ports; adapters translate between
those interactions and external technology.

## Applies when

More than one actor drives the application, such as UI, CLI and tests, or it
drives storage, networks or a harness through ports it defines.

## Does not apply when

A single driver and a single driven system have no replacement or test need.

## Violation signals

CLI and UI duplicate application rules. Tests enter through the UI or need a
real database because no application port can accept a substitute.

## Verification

Run the same application use case through a test driver and a real driver,
with a fake driven adapter. Review that external protocols stay in adapters.

## Source

Alistair Cockburn, [Hexagonal
architecture](https://alistair.cockburn.us/hexagonal-architecture) (2005).
