---
year: 1
subject: CS12
field: programming
---

1: GENERIC TYPE
===============

: one type nests another type

2: TYPE VARIANCES
=================

## 1. Covariant

: if A <: B, T[A] <: T[B]

## 2. Contravariant

: if A <: B, T[B] <: T[A]

## 3. Invariant

: no implications
: list[anything] are covariant since it can be mutated

## 4. Bivariant

: if A <: B, (T[A] <: T[B]) and (T[B] <: T[A])

3: FUNCTION SUBTYPING
=====================

## 1. Subfunctions

: let there be subclass A, and superclass B such that B has function F

: if G from subclass A is an overriden function of F, then G is subfunction of F

## 2. Function Subtyping Principles

### a. Parameter type is contravariant

: parameter type of subfunction must be equal or less specific

### b. Return type is covariant

: return type of subfunction must be equal or more specific

