---
year: 1
subject: CS12
field: programming
---
[[L6_OOP’s SOLID Principle]]
[[L7_SingleInheritance]]
[[L8_SubtypeVariance_FunctionSubtyping]]
[[L9_BehavioralSubtyping]]
[[L10_OOPDesignPatterns]]
[[L11_GameProgrammingBasics]]
[[L12_MVC_w_Pyxel]]

1: OOP NOT-SO-DEFINITION
========================

: programming approach where you use classes (objects) to solve several concerns

2: PRIVATE AND PUBLIC ATTRIBUTES
================================

: attributes are personal values of an object
: some attributes must only be accessed inside the class (private, secured, like passwords)
: some must be accessed by other outer objects (public, like name and nickname)

## 1. Private Attributes using ( _ )

: add '_' in the beginning of private attribute names
: this denotes that this attr can only be accessed and modified inside the object

## 2. Public Attributes using @property

: to make private attr to public attr, we use @property decorator and define a function returning the private attr

e.g.
```python
class Juan:
	def __init__(self, address: str, password: str, name: str) -> None:
		self._name = name
		self._address = address # private attr
		self._password = password
	
	# private attr made to be public
	@property
	def name(self) -> str:
		return self._name
```


3: OOP BUZZWORDS
================

## 1. [[Abstraction]]

: using abstract objects (Protocols or ABCs) to interface subtype classes with similar properties

## 2. Encapsulation

: group block of codes that addresses a common concern into a class

## 3. Polymorphism

: aka subtyping

## 4. Inheritance

: inherit parent class' type, attr, and methods

4: DEPENDENCY INJECTION
=======================

: if a class A needs to use class B, instead of making an attribute of an instance of B, you parameterize it

```python
class B:
	def f(self) -> None:
		print('fahh')

# WRONG, instead of this
class A:
	def __init__(self):
		self.b = B
		
# do this
class A:
	def __init__(self, b: B):
		self.b = B
```

5: STATIC METHOD FACTORY
========================

6: FORWARDING
=============

: when you D.I.ed class B in class A and you use a method of B, only 'forward' the needed values to the called method.

```python
class B:
	def f(self) -> None:
		print('fahh')
		
class A:
	def __init__(self, b: B):
		self.b = B
		
	def print_fah(self):
		self.b.f()
```

7: COMPOSITION PRINCIPLE
========================

: Do D.I. and Forwarding only when necessary to maximize cohesion and minimize coupling