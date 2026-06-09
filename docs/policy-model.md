# Runtime Admissibility Policy Model

## Purpose

This document defines the policy model used by the Runtime Admissibility Gate.

Within the formal model:

```text
Adm : S × A × C → D
```

the set:

```text
C
```

represents the applicable constraints under which a proposed action is evaluated.

The policy model defines the structure and interpretation of these constraints.



## Policy Objective

The objective of a policy is not to determine whether an action is useful.

The objective is to determine whether an action is admissible.

Policies define the conditions under which actions may:

* execute
* be blocked
* require approval



## Constraint Set

The constraint set is represented as:

```text
C = {c₁, c₂, ..., cₙ}
```

where each constraint:

```text
c ∈ C
```

evaluates a property of the proposed action or execution context.

Examples include:

* approval requirements
* sensitivity requirements
* recipient restrictions
* compliance obligations
* operational limitations



## Policy Evaluation

Each policy evaluates a proposed action against one or more constraints.

Conceptually:

```text
Policy(a,s) → Decision
```

The result contributes to the overall admissibility decision.



## Decision Space

Policies may return one of three outcomes:

```text
ALLOW
BLOCK
REQUIRE_APPROVAL
```

### ALLOW

The policy permits execution.

### BLOCK

The policy prohibits execution.

### REQUIRE_APPROVAL

The policy requires additional authorization before execution.

---

## Policy Precedence

When multiple policies apply simultaneously, the most restrictive decision takes precedence.

The precedence order is:

```text
BLOCK
    ↓
REQUIRE_APPROVAL
    ↓
ALLOW
```

Examples:

```text
ALLOW + BLOCK
    = BLOCK
```

```text
ALLOW + REQUIRE_APPROVAL
    = REQUIRE_APPROVAL
```

```text
REQUIRE_APPROVAL + BLOCK
    = BLOCK
```

---

## Example Policy

Email Sensitivity Policy:

```text
IF recipient_type = external
AND contains_sensitive_data = true
AND approved_by_human = false

THEN REQUIRE_APPROVAL
```

Result:

```text
Adm(s,a,C) = REQUIRE_APPROVAL
```

---

## Policy Categories

The model does not assume any specific domain.

Policies may govern:

### Disclosure

Examples:

* external communication
* data sharing
* information release

### Modification

Examples:

* database updates
* record changes
* workflow updates

### Execution

Examples:

* API invocation
* infrastructure changes
* automation triggers

### Financial Actions

Examples:

* payments
* transfers
* purchasing actions



## Policy Independence

Policies should be independent from application domains.

The same admissibility framework should support:

* email systems
* CRM systems
* enterprise workflows
* autonomous agents
* financial systems

without modifying the admissibility model itself.



## Relation to Runtime Admissibility

The admissibility function:

```text
Adm : S × A × C → D
```

evaluates:

* system state
* proposed action
* applicable constraints

and returns a decision.

The policy model defines the structure of:

```text
C
```

and therefore determines how admissibility is resolved before execution.



## Relation to Control Before Consequence

Within the broader framework:

```text
Control Before Consequence
        ↓
Runtime Admissibility
        ↓
Policy Model
        ↓
Admissibility Gate
        ↓
Reference Applications
```

The policy model provides the constraint layer through which admissibility decisions are derived.