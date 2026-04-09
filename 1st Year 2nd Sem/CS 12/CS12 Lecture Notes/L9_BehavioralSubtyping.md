---
year: 1
subject: CS12
field: programming
---

1: Liskov Substitution Principle
================================

: Subtypes/Subclasses should not break behavior expected of their supertype (aka behavioral subtyping)

: i.e. subtypes must act where all promises made by supertype is kept true4

: i.e. follow but function subtyping and behavioral subtyping

2: Generalized Behavioral Subtyping
===================================

## 1. Precondition must be contravariant

: preconditions (aka parameters and requirements promised before running) must be same or less strict

## 2. Postcondition must be covariant

: postconditions (aka conditions promised to follow after function called) must be same or more strict

## 3. Exceptions must be covariant

: exceptions of subtype must be same or more specific

## 4. Invariants must not be violated

: all rules in supertype must be followed by subtype

3: LSP in a nutshell
====================

### a. "dont require stricter"
: Func Subtyping: Contravariant Param Type
: Behav Subtyping: Contravariant Preconditions

### b. "dont give beyond whats promised
: Func Subtyping: Covariant Return Type
: Behav Subtyping: Covariant Postconditions AND Exceptions

### c. "stay true to your roots"
: Behav Subtyping: Follow invariants/rules promised by supertype
