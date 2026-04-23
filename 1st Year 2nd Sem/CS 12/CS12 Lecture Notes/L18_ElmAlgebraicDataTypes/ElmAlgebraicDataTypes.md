---
field: programming
---


## 1. Types as Sets
: think of types as sets of values
e.g. Bool = {True, False}

### 1) Composite Type
: Types composoed of other Types
: basically like generic types in Python
e.g. List String, Tuple Int

```elm
type alias Student =
	{didSleep: Bool
	, didntSleep: Bool}
	
{-
didSleep = {True, False} caridnality = 2

didntSleep = {True, False}
cardinality = 2
-}
```

#### 1] Product Type
: Composite types can also be seen as product types (since its a disjunction AND of types)
: Since a there is a type AND another type, the AND operation makes it a product of their cardinalities

in `Student` type alias, lit composes of `didSleep` AND `didntSleep`, which are both bools

so the cardinality |`Student`| = |`didSleep`| x |`didntSleep`| = 2 x 2 = 4

### 2) Union of Literal Types
: a Literal Type only has a single concrete value

in python:
```python
Student = Literal["Freshman"] # only "Freshman" is its value
```

in elm:
```elm
Sex = "Male" | "Female"
```

#### 1] Sum Type
: Union of literal types can be seen as a sum type (since its a conjunction OR of types)
: Since a there is a literal type OR another literal type, the OR operation makes it a sum of their cardinalities

in `Sex` it has cardinality of |`Sex`| = 1 + 1 = 2

