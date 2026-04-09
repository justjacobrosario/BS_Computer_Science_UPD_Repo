---
year: 1
subject: CS12
field: programming
---

1: [S]ingle Responsibility Principle
====================================

: simply separation of concerns (Lecture 3)

2: [O]pen-Closed Principle
==========================

: Open for extension or adding, closed for modifying
: when an injected class B has many possible subtypes, instead of explicitly listing to class A, make an Interface where every subtype follows it.
: Thus class B subtypes, even if they increase in numbers, can still be parameterized to its Interface typehint

3: [L]ISKOV SUBSTITUTION PRINCIPLE
==================================   

: let there be classes X and Y, where Y <: X
: for all behavior b() in X, 
	if b() works in all values in X, 
	then b() must also works in all values in subtype Y
	
: aka, all typehints and behaviors of base class must all be kept by its subtype classes

: how? more info for Lecture 8 Behavioral Subtyping

4: [I]NTERFACE SEGREGATION PRINCIPLE
====================================

: only include necessary properties in Interfaces

5: [D]EPENDENCY INVERSION PRINCIPLE
===================================

: depend on abstractions when having multiple subtype objects instead of explicitly listing concrete classes