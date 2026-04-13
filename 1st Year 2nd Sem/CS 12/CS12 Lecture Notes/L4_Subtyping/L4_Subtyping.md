---
year: 1
subject: CS12
field: programming
---

1: Subtype Polymorphism
=======================

: Subtype, as a subordinating type of a thing
: Poly, as many, morphism, as forms
: a subtype that has many forms

: S <: T means type S is a subtype of type T
: e.g. subtype of Sequence are list and tuple (aka list <: Sequence)

2: Interfaces of Classes
========================

: classes can be a subtype of a more general class (interfaces) where they have common properties
: interfaces acts as a blueprint checklist of relating properties
: interfaces can be the datatype (a type inference) for type hints of its subtypes

## 1. Implicit Interface (Protocol)

: Protocol class is a checklist for classes to follow to be a subtype of it
: It only implies the attr and method signatures (all of them must be manually implemented for its concrete classes)

```python
from typing import Protocol

# Protocols are abstract (ie not instantiatable class)
# Protocols checklist necessary attribute and method signatures in this way
# initializer no need to define the attr
def Animal(Protocol):
	name: str
	
	def move(self, distance:int) -> None:
		...

# Concrete classes (ie instrantiatable class)
# declared attr and methods in Protocol must at least be present to be a subtype of the protocol
def Dog():
	def __init__(self, name:str):
		self.name = name
		
	def move(self, distance:int) -> None:
		print("moving logic here")
```

## 2. Explicit Interface (Abstract Base Class)

: Also an abstract class (the name bruh), that checklists all necesary attr and methods for the classes to replicate to be its subtype
: There are two kinds of methods
: Abstract methods only implies the method signature (i.e. must manually implemented for its concrete classes)
: Concrete methods explicitly and automatically is implemented (i.e. its concrete classes automatically inherits concrete methods, no need to still implement it)

```python
from abc import ABC, abstractmethod

# ABCs are still abstract 
# ABCs checklist necessary attribute and method signatures in this way
def Animal(ABC):
	# initializer is now needed to declare attr
	# initializer is a concrete method, automatically inherited
	def __init__(self, name: str) -> None:
		self.name = name
	
	# conrete methods, automatically inherited
	def move(self, distance:int) -> None:
		print("moving logic here")
	
	#abstract methods, still need to implement
	@abstractmethod
	def make_sound(self, noise:str) -> None:
		pass
	

# Concrete classes
# declared attr and methods in ABC must at least be present to be a subtype of the protocol
def Dog(Animal):
	def __init__(self, name:str):
		self.name = name
		
	def make_sound(self, noise:str = "bark!") -> None:
		print(noise)
```