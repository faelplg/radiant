---
name: radiant-cycle
description:
  Run planning, execution or verification of a development cycle under
  Radiant, linking intent, contract, evidence and learning. Use when starting
  or resuming a Radiant delivery; a one-off question does not require running
  the whole cycle.
metadata:
  version: "0.1.5"
---

# Radiant operational cycle

This skill holds the reusable procedure. The
[Constitution](../../constitution/CONSTITUTION.md) defines the higher rules. The
project's artifacts define the product and the delegation; the skill does not
replace them. Commands, paths, the active contract and implementation state
come from the consumer project's operational map.

## Entry and resumption

1. Identify the current request: analyze/plan, change documentation,
   implement or verify. Preserve decisions already authorized in the session.
2. Read the project map and the inputs you need. Check the contract through
   the active pointer, the real state of the files and earlier evidence; do
   not infer execution or completion only from metadata or from the existence
   of a plan.
3. Choose the mode below. A request for analysis does not authorize changes;
   explicitly requested documentation may be revised without inventing an
   implementation contract. Code requires the project's applicable delegation.
4. Report briefly: goal, mode, contract or documentation authorization,
   version of this skill, expected evidence and next action. Reuse context
   already loaded; do not restart completed steps without a new reason.
5. To coordinate roles or delegate work to subagents, read the
   [radiant-delegation skill](../radiant-delegation/SKILL.md). For continuous
   triage of a consumer, use the
   [radiant-maintenance skill](../radiant-maintenance/SKILL.md).

## Plan and frame

- Relate the real need to the Frame and look for existing knowledge and
  procedures before producing another body. Separate shared process from
  product-specific context and tool configuration.
- Do the Challenge on the decision itself: which hypothesis does this
  increment test, which evidence motivated its scope and which simpler
  alternative meets it? Record the answer in the responsible artifact when
  material; do not create a document per stage just to fill a flow.
- Compare Spec, Plan and reality. Route divergences to the responsible layer,
  respecting the current authorization. When the Spec depends on an external
  tool, probe the effect of each command and flag it uses, not just their
  presence in the help text.
- Define the observable usage path and the evidence that distinguishes
  technical implementation and operational success from product usefulness.
  In an experiment, each refutation condition ends supported, refuted or
  inconclusive.
- Give each Spec verification an owning increment in the Plan, including each
  part of a verification split across increments.
- Prepare or refine the contract before its execution, with inputs, outputs,
  paths, non-goals and executable verifications. Use the project's convention
  for identity and activation. Do not rewrite an already executed contract to
  fit a different result.
- Output: a concrete proposal or updated authorized artifacts, material open
  items and the next step. Planning a delivery does not approve it for
  execution.

## Execute a delivery

- Confirm that the active contract covers the task and that the existing
  authorization allows the next step. Do not ask again for a decision already
  granted. A proposed contract different from the active one is not selected
  for convenience.
- Start with the path the user will observe. For bug fixes, reproduce the
  failure on that path before editing. For a new capability, record the
  missing behavior without treating the absence as a bug.
- Implement within the delegated boundary and preserve existing work. Use
  specialized procedures when the task actually needs them; this skill does
  not replace domain, design or security knowledge.
- Verify the smallest relevant part as you work. If a material divergence or
  a need outside the delegation shows up, preserve the evidence and apply the
  appropriate constitutional state; do not widen the contract on your own.
- Output: an inspectable change and evidence ready for the next mode. Code
  produced is not yet a verification conclusion.

## Verify and learn

- Reread criteria and outputs from the contract and the Spec. Inspect the diff
  and the result as a consumer; check the completion claim against these
  inputs, not just against the implementer's account.
- When a later review finds a gap in an earlier acceptance, preserve the
  contract and the historical evidence. Record what the new evidence limits,
  which fix belongs to the current cycle and which criterion still needs
  proof; do not turn the review's `DONE` into a new acceptance of the
  examined delivery.
- Run the applicable real path and the project's gates. For documentation,
  check references, coherence of the instructions and the consequences of
  following them in real scenarios. Record the commands and results actually
  obtained, including blockers; do not turn a planned test into evidence
  obtained.
- Choose independence proportional to risk: deterministic verifiers, consumer
  inspection, another run or human review. Only use delegation when it is
  available and authorized. Say which method was used and its limitations; a
  self-reread is not an independent review. With delegated roles, follow the
  acceptance rule of the [delegation skill](../radiant-delegation/SKILL.md#rules).
- Relate each material finding, evidence, diagnosis and smallest `fixTarget`.
  Fix within the current authorization; otherwise record the open item.
  Distinguish a fix made, a fix verified and later reuse demonstrated. None of
  them automatically implies the others.
- End in `DONE`, `HOLD` or `FAIL` according to the Constitution. Record the
  execution data below where the contract allows; for a simple question, a
  short answer is enough. Do not create a permanent record for every
  interaction.

## Minimum evidence of a relevant cycle

The authorized report, existing or new, should make it possible to recover:

- goal, contract and version, or the documentation request that authorized
  the cycle;
- path and version of the skill used, plus the Git revision or a digest of the
  exact body when it is not committed yet;
- result, commands/checks and verification limitations;
- material findings, `fixTarget` and a reference to the fix when there is one;
- final state and next step, distinguishing product, process and reuse.

Do not duplicate the skill in reports or in tool memories. When reusing it in
another product, point to this canonical body and provide that product's
map/context. Shared changes do not rewrite earlier contracts or evidence;
record the version actually used and assess whether the next revision
applies.
