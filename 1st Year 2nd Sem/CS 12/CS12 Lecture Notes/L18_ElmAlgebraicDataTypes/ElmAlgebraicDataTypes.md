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

## 2. Algebraic Data Types
: Data types composing of other data types using AND and/or OR
: composed of sum and/or product  types

### 1) Tagged Union
: basically a sum type, where its values are called "tags"

```elm
type Subject
	= CS12 -- these are tags
	| CS31
	| Math22
	| GE
	| PE
```

: it can also compose of function calls

```elm
type CrsSectionSlots
	= WithSlots Int
	| Full
	| Overbooked Int
	| Dissolved

-- can be used like this
type alias CrsSection =
	{ course : String
	, section : String
	, capacity : Int
	, slots : CrsSectionSlots
	}
	
{-
example =
{ course = "CS 12"
, section = "TCD"
, capacity = 80
, slots = WithSlots 14 }
-}
```

: can also compose of records

```elm
type PageState
	= Loading
	| PageReady PageData -- Record
	| PageError ErrorData -- Record
```


### 2) Pattern Matching

```elm

toSlotStr : CrsSection -> String
toSlotStr section =
	let
		-- makes a string fraction for display
		StrFractionizer nume deno =
			(String.fromInt nume) ++ "/" ++ (String.fromInt deno) -- e.g. "20/40"
	in
	case section.slots of
		-- basically match what to return depending on value of section.slots
		WithSlots left ->
			"OPEN" ++ (StrFractionizer left section.capacity) --e.g. "OPEN 3/20"
		Full ->
			"FULL" ++ (StrFractionizer section.capacity section.capacity) --e.g. "FULL 20/20"
		Overbooked val ->
			"OVERBOOKED" ++ (StrFractionizer val section.capacity) --e.g. "OVERBOOKED 23/20"
		Dissolved ->
			"DISSOLVED" --e.g. "DISSOLVED"

```