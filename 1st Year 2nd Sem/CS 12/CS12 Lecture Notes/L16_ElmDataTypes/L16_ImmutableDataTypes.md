---
year: 1
subject: CS12
field: programming
---

# 1: MODULES

: collection of related functions, types, and values : like python import

## 1. Import specific functions/types

```elm
import ModuleName exposing (Type1, func1, func2)

-- e.g.
import Array exposing (Array, fromList)
-- can use Array and fromList without Array.prefix
```

## 2. Import everything from module

```elm
import ModuleName exposing (..)

-- e.g.
import List exposing (..)
```

## 3. Import module only

```elm
import ModuleName

-- e.g.
import Array
-- must use prefix: Array.fromList [1,2,3]
```

## 4. Auto-imported by default

: elm import these automatically, no need to declare

1. `Basics exposing (..)`
2. `List exposing (List, (::))`
3. `Maybe exposing (Maybe(..))`
4. `String exposing (String)`
5. `Char exposing (Char)`
6. `Tuple`
7. `Debug`

# 2: LAMBDA FUNCTIONS

: anonymous function (no name)

```elm
-- syntax
\x -> expression

-- e.g.
\x -> x ^ 2
-- same as defining f x = x ^ 2 but unname
```

## 1. `List.map`

: applies a function to every element of a list : number of elements stay the same

```elm
squareEach : List Int -> List Int
squareEach givenList =
    List.map (\x -> x ^ 2) givenList

squareEach [1,2,3]
-- [1,4,9]
```

# 3: LISTS

: `List a` -> list of values of type `a` : ordered, homogeneous (same type), immutable

```elm
-- valid list types
List Int
List String
List (List Int)

-- creating
[]
[1,2,3]
["a", "b"]
```

## 1. `List.repeat`

```elm
List.repeat : Int -> a -> List a

List.repeat 3 "hi"
-- ["hi", "hi", "hi"]
```

## 2. `List.range`

```elm
List.range : Int -> Int -> List Int

List.range 1 5  -- [1,2,3,4,5]
List.range 5 1  -- []
```

## 3. Cons Operator `(::)`

: adds element to FRONT of list

```elm
(::) 1 [2,3,4]  -- function-call style
1 :: [2,3,4]    -- infix styl
-- both -> [1,2,3,4]

-- lists are just chains of cons:
[1,2,3] == 1 :: (2 :: (3 :: []))
```

## 4. Common List Functions

```elm
List.append : List a -> List a -> List a
List.append [1,2] [3,4]  -- [1,2,3,4]

List.concat : List (List a) -> List a
List.concat [[1,2],[3,4]]  -- [1,2,3,4]

List.sort : List comparable -> List comprable
List.sort [3,1,2]  -- [1,2,3]

List.take : Int -> List a -> List a
List.take 3 [4,5,6,8,9]  -- [4,5,6]

List.drop : Int -> List a -> List a
List.drop 3 [4,5,6,8,9]  -- [8,9]

List.maximum : List comparable -> Maybe comparable
List.maximum [4,5,6]  -- Just 6
List.maximum []       -- Nothing

List.filter : (a -> Bool) -> List a -> List a
List.filter (\x -> modBy 2 x == 0) [1,2,3,4]  -- [2,4]
-- note: filter CAN reduce count, unlike map
```

## 5. `List.foldl`

: processes list LEFT t RIGHT : more on fold -> Lec 17

```elm
List.foldl : (a -> b -> b) -> b -> List a -> b

List.foldl (+) 0 [1,2,3]
-- 1+0=1, 2+1=3, 3+3=6 -> 6

-- reversing using foldl
List.foldl (\x acc -> x :: acc) [] [1,2,3]
-- [3,2,1]
```

# 4: MAYBE TYPE

: `Maybe a` -> container that either has a value or doesnt : two possibilities: `Just value` or `Nothing`

```elm
x = Just 10    -- Maybe Int
y = Just "hi"  -- Maybe String
z = Nothing    -- Maybe a
```

## 1. Handling Maybe

### a. Pattern Matching

```elm
unwrap : Maybe a -> String
unwrap box =
    case box of
        Just gift ->
            "The box contains " ++ Debug.toString gift
        Nothing ->
            "The box is empty"
```

### b. `Maybe.withDefault`

: returns contained value if exists, else returns default

```elm
Maybe.withDefault : a -> Maybe a -> a

Maybe.withDefault 0 (String.toInt "-123")  -- -123
Maybe.withDefault 0 (String.toInt "abc")   -- 0
```

# 5: ARRAYS

: must import: `import Array`

: NOT the same as python tuple 
: elm array - indexed collection of same-type values, immutable 
: python tuples - fixed ordered collection, not index-optimized

```elm
Array.fromList [1,2,3]
-- type: Array.Array Int
```

## 1. Array Functions

```elm
Array.get : Int -> Array a -> Maybe a
-- gets element at index i (like arr[i] in python, NOT .index())
u = Array.fromList [4,5,6]
Array.get 0 u  -- Just 4

Array.set : Int -> a -> Array a -> Array a
-- returns NEW array with modified value
Array.set 0 1 u  -- Array.fromList [1,5,6]

Array.slice : Int -> Int -> Array a -> Array a
-- gets elements from index start to end-1
Array.slice 2 4 (Array.fromList [1,2,3,4,5])
-- Array.fromList [3,4]

Array.empty   -- empty array
Array.repeat : Int -> a -> Array a
Array.isEmpty : Array a -> Bool
Array.length : Array a -> Int

Array.push : a -> Array a -> Array a
-- adds to END
Array.push 8 (Array.fromList [4,5,6])
-- Array.fromList [4,5,6,8]

Array.toList : Array a -> List a
Array.toIndexedList : Array a -> List (Int, a)
-- pairs each element with its index
Array.toIndexedList (Array.fromList [10,20,30])
-- [(0,10),(1,20),(2,30)]
```

# 6: IMMUTABILITY

: elm is purely functional -> nothing mutates : add, remove, sort, update -> all return NEW containers

```elm
x = Array.fromList [10,20,30]
y = Array.set 2 100 x

-- x == Array.fromList [10,20,30]  <- unchanged
-- y == Array.fromList [10,20,100]
```

# 7: TUPLES

: stores grouped values of (optionally) different types : unlike lists (lists are homogeneous)

```elm
(Int, String)
(Int, String, Bool)
```

## 1. Tuple Destructuring

: use `_` to ignore a value

```elm
answer =
    let
        (x, _, z) = tupleData
    in
    x + z
```