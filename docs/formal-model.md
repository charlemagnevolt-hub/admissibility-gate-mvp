# Runtime Admissibility Formal Model

## Purpose

This document introduces a minimal formal model for runtime admissibility.

The objective is to provide a precise description of how proposed actions are evaluated before execution.

Within the Control Before Consequence framework, runtime admissibility determines whether a proposed
action may become externally consequential under the current constraints.



## Core Concepts

### System State

The current state of the system is represented as:

```text
s ∈ S
```

where:

* `S` denotes the set of possible system states
* `s` denotes the current system state

Examples:

* user context
* workflow state
* approval status
* resource availability
* environmental conditions



### Proposed Action

A proposed action is represented as:

```text
a ∈ A
```

where:

* `A` denotes the set of possible actions
* `a` denotes a specific proposed action

Examples:

* send email
* update database record
* invoke API
* transfer funds
* delete resource

---

### Constraint Set

Applicable constraints are represented as:

```text
C
```

Examples:

* security policies
* compliance requirements
* approval requirements
* operational restrictions
* contextual limitations



### Decision Space

The admissibility decision space is defined as:

```text
D = {ALLOW, BLOCK, REQUIRE_APPROVAL}
```

where:

* `ALLOW` permits execution
* `BLOCK` prohibits execution
* `REQUIRE_APPROVAL` suspends execution pending review



## Runtime Admissibility Function

Runtime admissibility is defined as:

```text
Adm : S × A × C → D
```

The function evaluates:

* current state
* proposed action
* applicable constraints

and returns a decision.



## Execution Rule

Execution is permitted only if admissibility evaluates to ALLOW.

Formally:

```text
execute(a) ⇔ Adm(s,a,C) = ALLOW
```

Therefore:

```text
Adm(s,a,C) ≠ ALLOW
```

implies:

```text
¬execute(a)
```

---

## Control Before Consequence Property

The Control Before Consequence principle can be expressed as:

```text
∀a : execute(a) ⇒ Adm(s,a,C) = ALLOW
```

Meaning:

> No action may execute unless admissibility has been explicitly resolved.

This property establishes the execution-control boundary.



## Example

Consider:

```text
a = SendEmail
```

with:

```text
recipient_type = external
contains_sensitive_data = true
approved_by_human = false
```

The admissibility function evaluates:

```text
Adm(s,a,C) = REQUIRE_APPROVAL
```

Therefore:

```text
execute(a) = false
```

The action remains suspended until admissibility requirements are satisfied.



## Relation to the Framework

Within the broader framework:

```text
Control Before Consequence
        ↓
Runtime Admissibility
        ↓
Admissibility Gate
        ↓
Reference Applications
```

This document formalizes the Runtime Admissibility layer.

The Admissibility Gate MVP serves as the reference implementation of this model.



## Scope

This formal model focuses exclusively on execution control and admissibility evaluation.

It does not attempt to formalize:

* model training
* alignment techniques
* content moderation
* infrastructure security
* authentication systems

These concerns remain outside the scope of runtime admissibility.
