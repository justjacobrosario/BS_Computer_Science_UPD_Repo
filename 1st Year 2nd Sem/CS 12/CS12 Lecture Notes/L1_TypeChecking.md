---
year: 1
subject: CS12
field: programming
---
[[L2_Debugging_UnitTesting]]



1: TYPE HINTING
==============

- var : type = val
- def f(param : type) -> returntype:

2: TYPE CHECKING
=====================

## 1. Static Type Checking

: Data types are checked before running the program

## 2. Dynamic Type Checking

: Data types are checked while running the program

3: TYPE INFERENCES
==================

: Data types are sometimes complex with several datatypes in one thing
: below can be used:

## 1. Union ( | )

: Multiple discrete datatypes

## 2. Literal

: Grouping multiple types in a Literal object
```python

from typing import Literal

def f(unit: Literal["Celsius", "Kelvin"]) -> None:

```

## 3. Type aliases

: Making a custom datatype from existing datatypes
```python
type grid = list[list[str]]]

tictactoe: grid = ...
```

