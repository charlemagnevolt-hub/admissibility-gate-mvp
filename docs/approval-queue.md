# Approval Queue Concept

The Runtime Admissibility Gate may return `REQUIRE_APPROVAL`.

In the current MVP, actions requiring approval are suspended and not executed.

A future approval queue would store pending actions until a human or supervisory process resolves the decision.

## Conceptual Flow

```text
Proposed Action
      ↓
Admissibility Evaluation
      ↓
REQUIRE_APPROVAL
      ↓
Approval Queue
      ↓
Human Review
      ↓
ALLOW / BLOCK
      ↓
Execution Decision
      ↓
Execute / Stop
      ↓
Ledger Record
```

## Execution Decision

After human review, the suspended action must resolve into one of two outcomes:

* `ALLOW`
* `BLOCK`

If the action is approved, it may proceed to execution.

If the action is rejected, it must not execute.

In both cases, the final decision should be recorded in the ledger.

## Relation to Runtime Admissibility

The approval queue does not replace runtime admissibility.

It extends the `REQUIRE_APPROVAL` branch of the admissibility decision space.

```text
ALLOW
    → execute immediately

BLOCK
    → do not execute

REQUIRE_APPROVAL
    → suspend and route to review
```

## Future Evolution

A future implementation may support:

* approval workflows
* supervisory review
* multi-stage approvals
* policy-based escalation
* approval audit trails

These capabilities are outside the scope of the current MVP.

## Scope

This document describes the approval queue concept only.

The current MVP does not implement a full approval workflow UI.

The current MVP suspends actions that require approval and records the decision in the ledger.
