---
year: 1
subject: CS12
field: programming
---


# 1: Collection of Functions and Types
#### 1] importing specific method
### `import ModuleName exposing (Type1, func1, func2, ...)`
#### 2] importing library completely
### `import ModuleName exposing (..)`

#### 4] no need to import libaries (builtin)
1. `Basics exposing (..)`
2. `List exposing (List, (::))`
3. `Maybe exposing (Maybe(..))` # Maybe type and all its variants
4. `String exposing (String)`
5. `Char exposing (Char)`
6. `Debug`


# 2: Lambda functions and map
## `(\x -> expression)`

: basically like in Python's lambda function, whenever you map a collection, you execute a certain function to each element, such that it returns True or False

: one usage of lambda functions is using `List.map` or `Array.map` or

e.g.

```elm
squareEach: List Int -> List Int
squareEach given_list =
    let 
        squared = List.map (\x -> x^2) given_list
        -- every element is ran in (\x -> x^2)
    in
        squared
```

# 3: List Syntax
: `List x` is a sequence of values of type  `x`
: List elements must have the same type (Homogenous)
e.g.
`List Int`, `List String`, `List (List Int)`

## 1. `List.repeat : Int -> a -> List a`

e.g.
```elm
List.repeat 3 "hi" -- ["hi", "hi", "hi"]
```

## 2. `List.range : Int -> Int -> List Int`

e.g.
```elm
List.range 1 5 -- [1, 2, 3, 4, 5]
List.range 5 1 -- [] : empty if higher first num
```

## 3. `(:) : a -> List a -> List a`
: pronounced cons
: prepends (adds to leftmost) `a` to the list

### 1) Function Call Style
```elm
x = (::) 1 [2, 3, 4] -- x = [1, 2, 3, 4]
```
### 2) Infix Style
```elm
x = 1 :: [2, 3, 4] -- x = [1, 2, 3, 4]
```

: essentially, lists is a chain of cons
```elm
[1, 2, 3] = 1 :: (2 :: [3])
```

## 4. Other `List` Functions

#### 1] `List.append : List a -> List a -> List a`
: combines two lst1, lst2
: different from python's .append(). It is more like .extend()

#### 2] `List.concat : List (List a) -> List a``
: flattens `List (List a) -> List a`

#### 3] `List.sort : List a` 
: simply sorts elements ascendingly

#### 4] `List.take: Int -> List a -> List a`
: takes the first leftmost n number of elements

e.g.
```elm
x = [4, 5, 6, 8, 9, 0]
List.take 3 x
-- [4,5,6] : First 3 elements taken
```

#### 5] `List.drop: Int -> List a -> List a`
: removes the first leftmost n number of elements

e.g.
```elm
x = [4, 5, 6, 8, 9, 0]
List.drop 3 x
-- [8, 9, 0] : First 3 elements dropped
```

: NOTE: using these functions does not mutate the list, it only makes a copy of it

#### 6] `List.maximum: List a -> Maybe`
: removes the first leftmost n number of elements

e.g.
```elm
x = [4, 5, 6, 8, 9, 0]
List.maximum x
-- Just 9 : Maybe number
y = []
List.maximum y
-- Nothing : Maybe comparable
```

#### 7] `List.filter : (a->Bool) -> List a -> List b`
: takes predicate (condition/s that must be True for an element to be kept) and a list

# 4: Maybe Syntax

: `Maybe a` : Container type representing the presence or abscence of `a`
: also called Option or Optional
: `Maybe` can have two possibilities:
1. `Just a` value: Presence of `a`
2. `Nothing`: Absent

```elm
x = Just 10 -- Maybe Int
y = Just "hello" -- y : Maybe String
z = Just [1, 2, 3] -- z : Maybe (List Int)
w = Nothing -- w : Maybe a

-- List.maximum : List Int -> Maybe Int
a = List.maximum [10,100,20,30] -- Just 100
b = List.maximum [] -- Nothing
```

### Handling `Maybe` Values
#### Option 1] Pattern matching via `case`
```elm
unwrap : Maybe a -> String
unwrap box =
	case box of
	Just gift ->
	"The box contains " ++ Debug.toString gift
	
	Nothing ->
	"The box is empty"
```

#### Option 2] `Maybe.withDefault`

: `Maybe.withDefault : a -> Maybe a -> a` where `a` is a type (not a value)
: if `Maybe a` is `Just a` then `a`
: else it would be the 1st param `a`

```elm
x =
-- String.toInt "-123" : String -> Maybe Int
-- Maybe.withDefault 0 (String.toInt "-123")
Maybe.withDefault 0 (String.toInt "-123")
```

# 5: Array Syntax
: `import Array
: a container for random-access processing of a list of values
: faster in indexing than lists
: similar to python's tuple
: has no literal, its simply a version of a `List a` object

e.g. 
```elm
Array.fromList [1, 2, 3] -- not (1,2,3)
```

: `Array.fromList List a` has a type of `Array.Array a`

```elm
import Array
u = Array.fromList [4, 5, 6]
Array.fromList [4,5,6] -- Array.Array number
```

#### 5] `Array.get : Int -> Array a -> Maybe a`
: gets element of index i (first int param) 0-indexed
: similar to Python's .index()

e.g.
```elm
u = Array.fromList [4,5,6] -- another Array.Array number
y = Array.get 0 u
-- y = Just 4 : Maybe number
```

#### 6] `Array.set : Int -> a -> Array a -> Maybe a`
: sets/changes element of index i (first int param) 0-indexed into `a`
: it is only valid if the index i has an existing value

e.g.
```elm
u = Array.fromList [4,5,6] -- another Array.Array number
y = Array.set 0 1 u
-- y = Array.fromList [1, 5, 6] : Array.Array number
```

#### #### 7] `Array.slice : Int -> Int -> Array a -> Array a`
: slices a subarray starting from index i (first int param) to index j-1 (second int param - 1)

e.g.
```elm
z = Array.fromList [1, 2, 3, 4, 5, 6, 7, 8, 9] -- -- another Array.Array number
w = Array.slice 2 4 z
-- w = Array.fromList [3,4] : Array.Array number
```


#### #### 8] `Array.empty : Array a`
: gives an empty array

e.g.
```elm
> c = Array.empty
Array.fromList [] : Array.Array a
```


#### #### 9] `Array.repeat : Int -> a -> Array a`
: repeats `a` n times in an array


#### #### 10] `Array.isEmpty : Array a -> Bool`
: gives an empty array

e.g.
```elm
c = Array.fromList [1, 2, 3]
verdict = Array.isEmpty c
-- verdict == True
```

#### #### 10] `Array.length : Array a -> Int`
: gives length of arr
: basically like Python's len()

#### #### 11] `Array.push : a -> Array a -> Array a`
: adds `a` on the rightmost (last) position
: similar to Python's .append()

e.g.
```elm
u = Array.fromList [4,5,6]
new_u = Array.push 8 u
-- new_u = Array.fromList [4,5,6,8]
```


#### #### 12] `Array.toList : Array a -> List a`
: basically converts an `Array.Array a` into `List a`


#### #### 13] `Array.toIndexedList : Array a -> List (Int, a)`
: converts an `Array.Array a` into a `List (Int, a)` where each `a` is partnered with its index

e.g.
```elm
z = Array.fromList [1,2,3,4,5,6,7,8,9]
z_enumerated = Array.toIndexedList z

-- z_enumerated = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)] : List ( Int, number )
```


# 6: Immutability of Containers (Recalled)
: Remember that Elm is a pure language, where variables, values, and containers are strictly incapable of mutating
: adding, removing, sorting, and modifying an existing container does not mutate it, but it only returns a copy of it with its modification/s

# 7: List.Filter Examples

```elm
filterDivisibleBy: List Int -> Int -> List Int
filterDivisibleBy given_list n =
    let
        div_by_n = List.filter (\x -> (modBy n x) == 0) given_list
    in
        div_by_n
              
-- modBy n x = remainder of x/n. notice that the first param n must not be 0
-- notice that modBy n x is like x%n in Python
```

# 8: Tuples
## 1. Destructuring Bind in Tuples
: can only be done in the let block

```elm
answer =
	let
		(x, _, z) = tuple_data -- Underscore for "don't care"
	in
		x + z
```