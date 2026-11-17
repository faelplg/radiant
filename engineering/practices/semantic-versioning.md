# Release and semantic versioning

- Id: `semantic-versioning`
- Serves: [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts), [EB-06](../engineering-baseline.md#8-eb-06---dependencies-and-supply-chain)

Communicate published API compatibility through versions and derive release
notes from intentional commit history.

## Applies when

A published interface has consumers that pin versions.

## Does not apply when

No interface is published, or consumers pin commits, as Radiant's do.
Conventional Commits still applies to this repository's history.

## Violation signals

A released artifact is replaced under the same version. An incompatible API
change receives a patch/minor release, or a breaking commit omits its breaking
marker.

## Verification

Compare the public API with the previous release, classify compatibility, and
check the version bump and generated notes against the commit history.

## Source

Tom Preston-Werner, [Semantic Versioning
2.0.0](https://semver.org/spec/v2.0.0.html) (2013).

Conventional Commits contributors, [Conventional Commits
1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) (2019).
