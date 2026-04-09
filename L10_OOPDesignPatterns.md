---
year: 1
subject: CS12
field: programming
---

1: WHAT'S OOP DESIGN PATTERNS
=============================

: templates that can be used to generally do OOP Programs depending on its goal

## 1. Strategy Pattern

: Allows interchangeable behaviors via
"composition" of objects to a main object

: refer image 1

### a. Strategy interface 
: Same method signature for behavior variations

### b. Strategy implementers (Varying classes)
: One class per behavior variant

### c. Strategy user (Main class)
: Contains common aspects

## 2. Template Method Pattern

: Delegates implementation of subset
of steps to subclasses

: Makes subclasses of different versions of an object via "inheritance"

### a. Abstract class 
: Exposes methods allowed to be implementedor overriden

### b. Implementers 
: Implements abstract methods, may override public concrete methods

