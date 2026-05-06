---

## year: 1 subject: CS12 field: programming

[[Lec_16_Notes]]

# 1: RECORDS

: collection of values with FIXED key names : like a python dict but keys are static (not dynamic) : like a python class where keys are the properties

```elm
{ artist = "Eraserheads"
, genre = Pop
, title = "Huling El Bimbo"
}
```

## 1. `type` — Custom Types

: makes a new type with a set of possible values : like python's Enum

```elm
type Genre
    = Pop
    | Rock
    | Indie
    | Other
-- any Genre can only be Pop, Rock, Indie, or Other
```

## 2. `type alias` — Record Type Definition

: gives a name to a fixed set of key-type pairs : like a Protocol/dataclass in python but for records : defines what keys a record must have and their value types

### a. Defining

```elm
type alias Track =
    { artist : String
    , genre : Genre
    , title : String
    }
```

### b. Creating/Instantiating

```elm
x =
    { artist = "Eraserheads"
    , genre = Pop
    , title = "Huling El Bimbo"
    }
```

### c. Accessing a field

: `record.key`

```elm
x = { artist = "Eraserheads", genre = Pop, title = "Huling El Bimbo" }

xsGenre = x.genre  -- Pop
xsTitle = x.title  -- "Huling El Bimbo"
```

### d. Updating a field

: records are immutable so "updating" returns a NEW record : `{ recordName | key = newVal }`

```elm
x = { artist = "Eraserheads", genre = Pop, title = "Huling El Bimbo" }

newX = { x | title = "Magasin" }
-- x unchanged, newX has title = "Magasin"

-- can update multiple at once
newX = { x | title = "Magasin", genre = Indie }
```

# 2: FOLD

: abstraction of the for-each aggregation pattern : aka reduce, accumulate, aggregate : a function runs on the initial value and first element, returns a result, then runs again on that result and next element, and so on : like folding paper, each fold stacks onto the last one, accumulating thickness until the final fold

## 1. Common Loop Pattern in Python

: many loops share this same structure:

```python
# sum
result = 0
for elem in nums:
    result = result + elem

# product
result = 1
for elem in nums:
    result = result * elem

# string concat
result = ""
for elem in strs:
    result = result + elem
```

: extracted pattern:

```python
def fold(reducer, starting_value, elems):
    result = starting_value
    for elem in elems:
        result = reducer(elem, result)
    return result

# reducer       -> function applied each iteration
# starting_value -> initial result before any element processed
# elems         -> the list

# call order:
# reducer(1st_elem, starting_value) -> res1
# reducer(2nd_elem, res1)           -> res2
# ...
# reducer(nth_elem, res_n-1)        -> final

# nested equivalent:
# reducer(nth, ...reducer(2nd, reducer(1st, starting_value))...)
```

## 2. Left vs Right Fold

: matters when reducer is non-commutative (f a b != f b a)

```python
# foldl ["a","b","c"] with append, starting ""
# leftmost first:
append("c", append("b", append("a", "")))
# -> append("c", "ba")
# -> "cba"

# foldr ["a","b","c"] with append, starting ""
# rightmost first:
append("a", append("b", append("c", "")))
# -> append("a", "bc")
# -> "abc"
```

: for commutative ops (like addition), foldl == foldr result

## 3. Fold in Elm

: same signature for both

```elm
List.foldl : (a -> b -> b) -> b -> List a -> b
List.foldr : (a -> b -> b) -> b -> List a -> b
--            reducer        init  list     result

-- foldl -> left to right (leftmost first)
-- foldr -> right to left (rightmost first)
```

e.g.

```elm
mySum : List Int -> Int
mySum lst =
    let
        myAdd next prev =
            next + prev
    in
    List.foldl myAdd 0 lst

{-
lst = [1,2,3,4]

myAdd 1 0 -> 1
myAdd 2 1 -> 3
myAdd 3 3 -> 6
myAdd 4 6 -> 10
-}

myProduct : List Int -> Int
myProduct lst = List.foldl (*) 1 lst

myConcat : List String -> String
myConcat strs = List.foldr (++) "" strs
```

## 4. Identity (Starting Value)

: value for which the reducer just returns the other arg unchanged : also the correct result for an empty list

|Operation|Reducer|Identity|
|---|---|---|
|sum|`(+)`|`0`|
|product|`(*)`|`1`|
|concat|`(++)`|`""`|
|list cons|`(::)`|`[]`|

## 5. Reduction vs Accumulation

: reduction -> output type is SAME as element type (List a -> a) : accumulation -> output can be ANY type, more general (List a -> b) : no change in fold structure, just what types a and b are

```elm
-- reductions
sum     : List Int    -> Int
product : List Int    -> Int
concat  : List String -> String

-- accumulation (output type differs from element type)
length  : List a      -> Int
```

## 6. Intermediate State

: sometimes fold needs to track extra info alongside the answer : solution -> make accumulator a tuple (answer, extra_state), extract answer at end

e.g. `extend : String -> String` that repeats nth char n times

```
extend "abc" == "abbccc"
```

```elm
extend : String -> String
extend str =
    let
        -- acc = (answer_so_far, current_repeat_count)
        reducer : Char -> ( String, Int ) -> ( String, Int )
        reducer ch acc =
            let
                ( answer, k ) = acc
                nextAnswer = answer ++ String.repeat k (String.fromChar ch)
                nextK = k + 1
            in
            ( nextAnswer, nextK )

        ( finalAns, _ ) = String.foldl reducer ( "", 1 ) str
    in
    finalAns

{-
String.foldl reducer ("", 1) "abc"

reducer 'a' ("", 1)    -> ("a", 2)
reducer 'b' ("a", 2)   -> ("abb", 3)
reducer 'c' ("abb", 3) -> ("abbccc", 4)

finalAns = "abbccc"
-}
```

: note: String.foldl works on Char not String, so String.fromChar needed before repeating

# 3: DICT (BONUS)

: stores key-value pairs like python dict but IMMUTABLE : all operations return a new Dict : must import: `import Dict exposing (Dict)`

|Function|Signature|Description|
|---|---|---|
|`Dict.fromList`|`List (k,v) -> Dict k v`|build dict from list of pairs|
|`Dict.toList`|`Dict k v -> List (k,v)`|convert dict back to list of pairs|
|`Dict.get`|`k -> Dict k v -> Maybe v`|lookup key, returns Just v or Nothing|
|`Dict.insert`|`k -> v -> Dict k v -> Dict k v`|add or overwrite key|
|`Dict.remove`|`k -> Dict k v -> Dict k v`|remove key and its value|
|`Dict.member`|`k -> Dict k v -> Bool`|check if key exists|
|`Dict.isEmpty`|`Dict k v -> Bool`|check if dict is empty|