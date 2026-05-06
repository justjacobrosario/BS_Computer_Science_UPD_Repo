---
year: 1
subject: CS12
field: programming
---

# Lecture 17: Records, Fold, and Recursion

> Based on CS 12 lecture discussions and personal notes. Some concepts and examples are adapted and expanded from course materials.

---

# 1. Records

## 1.1 What is a Record?

A **record** is a collection of values with fixed, named keys. Think of it as a blend between:

- a Python **dict** (key-value pairs), but with **static** key names fixed at the type level
- a Python **class** where the keys are the instance properties

```elm
{ artist : "Eraserheads"
, genre : Pop
, title : "Huling El Bimbo"
}
```

---

## 1.2 `type` — Custom Types

Before defining a record, you may need to define custom types for its fields. `type` declares a new type with a fixed set of possible values — similar to Python's `Enum`.

```elm
type Genre
    = Pop
    | Rock
    | Indie
    | Other
-- A Genre value can only be Pop, Rock, Indie, or Other
```

---

## 1.3 `type alias` — Defining a Record Type

`type alias` gives a name to a specific record shape (a fixed set of key-type pairs). It is similar to a Protocol or dataclass in Python — it defines what keys a record must have and what type each key's value must be.

### Defining a record type

```elm
type alias Track =
    { artist : String
    , genre : Genre
    , title : String
    }
```

### Creating a record

Set each key to a value matching the declared type, in any order:

```elm
x =
    { artist = "Eraserheads"
    , genre = Pop
    , title = "Huling El Bimbo"
    }
```

### Accessing a field

Use dot notation: `record.key`

```elm
x = { artist = "Eraserheads", genre = Pop, title = "Huling El Bimbo" }

xsGenre = x.genre   -- Pop
xsTitle = x.title   -- "Huling El Bimbo"
```

### Updating a field

Records are immutable, so "updating" a field returns a **new record** with the changed value:

```elm
-- Syntax: { recordName | key = newValue }

x = { artist = "Eraserheads", genre = Pop, title = "Huling El Bimbo" }

newX = { x | title = "Magasin" }
-- x is unchanged; newX has title = "Magasin"
```

Multiple fields can be updated at once:

```elm
newX = { x | title = "Magasin", genre = Indie }
```

---

# 2. Fold

## 2.1 What is Fold?

**Fold** (also called _reduce_, _accumulate_, or _aggregate_) is an abstraction of the for-each aggregation pattern. It captures the common structure shared by loops that build up a result by repeatedly applying a function across the elements of a list.

The intuition: imagine folding a piece of paper. Each fold stacks on top of the previous one, accumulating thickness. Fold works the same way — a function runs on the first element and an initial value, then that result gets passed into the next call with the next element, and so on until the list is exhausted.

---

## 2.2 Fold Pattern in Python

Many common loops share the same underlying structure:

```python
# Sum
result = 0
for elem in nums:
    result = result + elem

# Product
result = 1
for elem in nums:
    result = result * elem

# String concat
result = ""
for elem in strs:
    result = result + elem
```

The common pattern extracted:

```python
def fold(reducer, starting_value, elems):
    result = starting_value
    for elem in elems:
        result = reducer(elem, result)
    return result

# reducer   -> the function applied each iteration
# starting_value -> the initial result (before any element is processed)
# elems     -> the list of elements to process

# Call order:
# reducer(1st_elem, starting_value) -> res1
# reducer(2nd_elem, res1)           -> res2
# reducer(3rd_elem, res2)           -> res3
# ...
# reducer(nth_elem, res_{n-1})      -> final result

# Equivalent nested form:
# reducer(nth_elem, ... reducer(2nd_elem, reducer(1st_elem, starting_value)) ...)
```

---

## 2.3 Left vs Right Fold

The direction of traversal matters when the reducer is **non-commutative** (i.e., `f a b ≠ f b a`).

**Left fold** — processes elements from leftmost to rightmost:

```python
# foldl on ["a", "b", "c"] with append and "" as starting value
append("c", append("b", append("a", "")))
# -> append("c", append("b", "a"))
# -> append("c", "ba")
# -> "cba"
```

**Right fold** — processes elements from rightmost to leftmost:

```python
# foldr on ["a", "b", "c"] with append and "" as starting value
append("a", append("b", append("c", "")))
# -> append("a", append("b", "c"))
# -> append("a", "bc")
# -> "abc"
```

For commutative operations (like addition), left and right fold give the same result.

---

## 2.4 Fold in Elm

Both folds share the same type signature:

```elm
List.foldl : (a -> b -> b) -> b -> List a -> b
List.foldr : (a -> b -> b) -> b -> List a -> b
--            reducer        init  list     result
```

- `List.foldl` — folds left to right (leftmost element first)
- `List.foldr` — folds right to left (rightmost element first)

### Examples

```elm
mySum : List Int -> Int
mySum lst =
    let
        myAdd next prev =
            next + prev
    in
    List.foldl myAdd 0 lst

{-
lst = [1, 2, 3, 4]

myAdd 1 0  -> 1
myAdd 2 1  -> 3
myAdd 3 3  -> 6
myAdd 4 6  -> 10
-}
```

```elm
myProduct : List Int -> Int
myProduct lst =
    List.foldl (*) 1 lst

myConcat : List String -> String
myConcat strs =
    List.foldr (++) "" strs
```

---

## 2.5 Identity (Starting Value)

The starting value is also called the **identity** of the reducer — the value for which the reducer simply returns the other argument unchanged.

|Operation|Reducer|Identity|
|---|---|---|
|Sum|`(+)`|`0`|
|Product|`(*)`|`1`|
|Concat|`(++)`|`""`|
|List cons|`(::)`|`[]`|

The identity is also the correct result when folding over an empty list (the single-element case naturally works out too).

---

## 2.6 Reduction vs Accumulation

**Reduction** is when the output type is the same as the element type — the list is "reduced" to a single value of the same kind:

```elm
sum     : List Int    -> Int
product : List Int    -> Int
concat  : List String -> String
```

**Accumulation** is the more general case — the output can be _any_ type, not necessarily matching the element type:

```elm
-- Output is a different type from the elements
length : List a -> Int
```

There is no change to the fold structure itself — the distinction is just in what types `a` and `b` are in the signature `(a -> b -> b) -> b -> List a -> b`.

---

## 2.7 Intermediate State

Sometimes the fold needs to track extra information across iterations — not just the accumulating answer, but some auxiliary state too. The solution is to make the accumulator a **tuple** that holds both, then extract only the answer at the end.

**Task:** Write `extend : String -> String` that repeats the _n_th character _n_ times for each character.

```
extend "abc" == "abbccc"
```

```elm
extend : String -> String
extend str =
    let
        -- acc is (answer_so_far, current_repeat_count)
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

reducer 'a' ("", 1)   -> ("a", 2)
reducer 'b' ("a", 2)  -> ("abb", 3)
reducer 'c' ("abb", 3) -> ("abbccc", 4)

finalAns = "abbccc"
-}
```

> Note: `String.foldl` works on `Char` elements (not `String`), so `String.fromChar` is needed to convert each character back before repeating it.

---

## 2.8 Dict (Bonus)

`Dict` stores key-value pairs similarly to a Python dict, but is **immutable** — all operations return a new `Dict`.

Must be imported: `import Dict exposing (Dict)`

|Function|Signature|Description|
|---|---|---|
|`Dict.fromList`|`List (k, v) -> Dict k v`|Build a dict from a list of pairs|
|`Dict.toList`|`Dict k v -> List (k, v)`|Convert a dict back to a list of pairs|
|`Dict.get`|`k -> Dict k v -> Maybe v`|Look up a key; returns `Just v` or `Nothing`|
|`Dict.insert`|`k -> v -> Dict k v -> Dict k v`|Add or overwrite a key|
|`Dict.remove`|`k -> Dict k v -> Dict k v`|Remove a key and its value|
|`Dict.member`|`k -> Dict k v -> Bool`|Check if a key exists|
|`Dict.isEmpty`|`Dict k v -> Bool`|Check if the dict is empty|