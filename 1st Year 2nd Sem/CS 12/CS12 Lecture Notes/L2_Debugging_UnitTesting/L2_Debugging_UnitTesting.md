---
year: 1
subject: CS12
field: programming
---
[[L3_Separation_of_Concerns]]

1: IDEALS OF A PROGRAM
======================

1. Bug-free
2. Easy to understand
3. Easy to modify

2: DEBUG BY IDENTIFYING EQUIVALENCE PARTITIONS AND EDGE CASES
==============================================================

## 1. Equivalence Partitions (aka value intervals)

: range of values that has a common behavior to the function
: e.g. for int, negative numbers, zero, positive numbers, are equiv. partitions

## 2. Edge Cases

: trivial values that has a unique behavior in all equiv. partitions
: e.g. 0 as edge case for division functions

3: UNIT TESTING
===============

: from test_blabla.py, define multiple test_functionname() which tests each blocks of code
: consider equivalence partitions and edge cases

## Terminal checking

```bash
pytest --cov=file_name --cov-report=term-missing
```