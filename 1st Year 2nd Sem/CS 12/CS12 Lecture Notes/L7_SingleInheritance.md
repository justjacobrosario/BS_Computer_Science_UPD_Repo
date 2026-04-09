---
year: 1
subject: CS12
field: programming
---


1: SUBCLASSING
==============

: act of inheriting the attr and methods of a base class to its child classes

```python
class Animal:
	def __init__(self, name: str) -> None:
		self.name = name
		
	def move(self):
		print('moves')
		
class Dog(Animal):
	pass

d = Dog(name = "Askal")
d.move()
```

2: METHOD OVERRIDING
====================

: when a subclass overrides a function, it will become a "derived function"
: derived functions don't influence base functions from the parent class and other siblings

3: METHOD RESOLUTION ORDERING
=============================

: when a function is called, function traces from the child class then its immediate parent class and so on until it traces the def of the func

```python

class A:
	def f(self) -> None:
		print('eyy')
	
class B(A):
	def f(self) -> None:
		print('fahh')
	
class C(B):
	pass
	
class D(C):
	pass

d = D()
d.f() # it will print the immediate latest def of f() which is 'fahh'
```

4: super() IN OVERRIDING INITIALIZER FUNC
=========================================

: when a child class overrides the __init__ function of its parent, its attributes won't be automatically inherited anymore
: you can manually inherit selected attr of parent's initializer using super().__init__(attr1, attr2,...)

5: COMPOSITION OVER INHERITANCE
===============================

: composition lightly uses a behavior of a class B to a class A
: injected class B can be easily changed by other subtypes of B that follows B's Interface as well

: inheritance will inherit every code block of B to A
: can't be changed, unless manually oerriding each method