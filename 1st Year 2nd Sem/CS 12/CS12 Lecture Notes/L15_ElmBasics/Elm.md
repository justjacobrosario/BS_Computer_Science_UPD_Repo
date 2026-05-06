---
field: programming
---
# Immutable Data Types and Collections in Elm

> Based on CS 12 lecture discussions and personal notes.  
> Some concepts and examples are adapted and expanded from course materials.

# 1. Modules

A **module** is a collection of related:

- functions
    
- types
    
- values
    

Similar to Python imports.

---

## 1.1 Importing Specific Functions or Types

```elm
import ModuleName exposing (Type1, func1, func2)
```

Example:

```elm
import Array exposing (Array, fromList)
```

This imports:

- `Array`
    
- `fromList`
    

without needing to prefix them with `Array.`

---

## 1.2 Importing Everything from a Module

```elm
import ModuleName exposing (..)
```

Example:

```elm
import List exposing (..)
```

This imports everything from `List`.

---

## 1.3 Importing Only the Module

```elm
import ModuleName
```

Example:

```elm
import Array
```

Functions must then be accessed using the module prefix:

```elm
Array.fromList [1,2,3]
```

---

## 1.4 Modules Imported by Default

Elm automatically imports these modules:

1. `Basics exposing (..)`
    
2. `List exposing (List, (::))`
    
3. `Maybe exposing (Maybe(..))`
    
4. `String exposing (String)`
    
5. `Char exposing (Char)`
    
6. `Tuple`
    
7. `Debug`
    

---

# 2. Lambda Functions

Lambda functions are anonymous functions.

Syntax:

```elm
\x -> expression
```

Example:

```elm
\x -> x ^ 2
```

This means:

```elm
f x = x ^ 2
```

but without naming the function.

---

## 2.1 Using Lambdas with `List.map`

`List.map` applies a function to every element of a list.

```elm
squareEach : List Int -> List Int
squareEach givenList =
    List.map (\x -> x ^ 2) givenList
```

Example:

```elm
squareEach [1,2,3]
-- [1,4,9]
```

Important:

- `List.map` transforms elements
    
- the number of elements stays the same
    
- `map` does NOT filter elements
    

---

# 3. Lists

## 3.1 List Basics

```elm
List a
```

A list containing values of type `a`.

Lists are:

- ordered
    
- homogeneous (all elements must have the same type)
    
- immutable
    

Examples:

```elm
List Int
List String
List (List Int)
```

---

# 3.2 Creating Lists

```elm
[]
[1,2,3]
["a", "b"]
```

---

## 3.3 `List.repeat`

```elm
List.repeat : Int -> a -> List a
```

Creates a list containing the value repeated `n` times.

Example:

```elm
List.repeat 3 "hi"
-- ["hi", "hi", "hi"]
```

---

## 3.4 `List.range`

```elm
List.range : Int -> Int -> List Int
```

Creates a list from `start` to `end` inclusive.

Example:

```elm
List.range 1 5
-- [1,2,3,4,5]
```

```elm
List.range 5 1
-- []
```

---

## 3.5 The Cons Operator `(::)`

```elm
(::) : a -> List a -> List a
```

Pronounced:

> “cons”

Adds an element to the FRONT of a list.

---

### Function-call Style

```elm
(::) 1 [2,3,4]
-- [1,2,3,4]
```

---

### Infix Style

```elm
1 :: [2,3,4]
-- [1,2,3,4]
```

---

Lists can be viewed as chains of cons operations:

```elm
[1,2,3]
== 1 :: (2 :: (3 :: []))
```

---

# 3.6 Common List Functions

## `List.append`

```elm
List.append : List a -> List a -> List a
```

Combines two lists.

```elm
List.append [1,2] [3,4]
-- [1,2,3,4]
```

Similar to Python list concatenation.

---

## `List.concat`

```elm
List.concat : List (List a) -> List a
```

Flattens a list of lists.

```elm
List.concat [[1,2],[3,4]]
-- [1,2,3,4]
```

---

## `List.sort`

```elm
List.sort : List comparable -> List comparable
```

Sorts values in ascending order.

```elm
List.sort [3,1,2]
-- [1,2,3]
```

---

## `List.take`

```elm
List.take : Int -> List a -> List a
```

Gets the first `n` elements.

```elm
List.take 3 [4,5,6,8,9]
-- [4,5,6]
```

---

## `List.drop`

```elm
List.drop : Int -> List a -> List a
```

Removes the first `n` elements.

```elm
List.drop 3 [4,5,6,8,9]
-- [8,9]
```

---

## `List.maximum`

```elm
List.maximum : List comparable -> Maybe comparable
```

Returns:

- `Just value` if the list is non-empty
    
- `Nothing` if the list is empty
    

Example:

```elm
List.maximum [4,5,6]
-- Just 6
```

```elm
List.maximum []
-- Nothing
```

---

## `List.filter`

```elm
List.filter : (a -> Bool) -> List a -> List a
```

Keeps only elements satisfying the predicate.

Example:

```elm
List.filter (\x -> modBy 2 x == 0) [1,2,3,4]
-- [2,4]
```

Important:

- `filter` can reduce the number of elements
    
- unlike `map`
    

---

# 3.7 Folding Lists

## `List.foldl`

```elm
List.foldl : (a -> b -> b) -> b -> List a -> b
```

Processes the list from LEFT to RIGHT.

Pattern:

```elm
List.foldl function initialValue list
```

Example:

```elm
List.foldl (+) 0 [1,2,3]
-- 6
```

Evaluation:

```text
1 + 0 = 1
2 + 1 = 3
3 + 3 = 6
```

---

## Reversing Using `foldl`

```elm
List.foldl (\x acc -> x :: acc) [] [1,2,3]
-- [3,2,1]
```

Explanation:

```text
[]
[1]
[2,1]
[3,2,1]
```

---

# 4. Maybe Type

## 4.1 What is `Maybe`?

```elm
Maybe a
```

A container representing:

- the presence of a value
    
- or the absence of a value
    

Two possibilities:

1. `Just value`
    
2. `Nothing`
    

---

## Examples

```elm
x = Just 10
-- Maybe Int
```

```elm
y = Just "hello"
-- Maybe String
```

```elm
z = Nothing
-- Maybe a
```

---

# 4.2 Handling `Maybe`

## Option 1: Pattern Matching

```elm
unwrap : Maybe a -> String
unwrap box =
    case box of
        Just gift ->
            "The box contains " ++ Debug.toString gift

        Nothing ->
            "The box is empty"
```

---

## Option 2: `Maybe.withDefault`

```elm
Maybe.withDefault : a -> Maybe a -> a
```

Returns:

- the contained value if it exists
    
- otherwise the default value
    

Example:

```elm
Maybe.withDefault 0 (String.toInt "-123")
-- -123
```

```elm
Maybe.withDefault 0 (String.toInt "abc")
-- 0
```

---

# 5. Arrays

## 5.1 Array Basics

Arrays are optimized for:

- random access
    
- indexed lookup
    

Compared to lists:

- arrays are better for indexing
    
- lists are better for recursive traversal
    

---

## Important Clarification

Arrays are NOT the same as Python tuples.

Elm arrays:

- are collections of same-type values
    
- are indexed
    
- are mutable in concept but immutable in implementation
    

Python tuples are:

- fixed ordered collections
    
- not specifically optimized for indexing structures like Elm arrays
    

---

## Creating Arrays

```elm
import Array
```

```elm
Array.fromList [1,2,3]
```

Type:

```elm
Array.Array Int
```

---

# 5.2 Array Functions

## `Array.get`

```elm
Array.get : Int -> Array a -> Maybe a
```

Gets the element at index `i`.

```elm
u = Array.fromList [4,5,6]
Array.get 0 u
-- Just 4
```

Important:

- similar to Python indexing (`arr[i]`)
    
- NOT similar to Python `.index()`
    

Python `.index(x)` searches for the POSITION of `x`.

---

## `Array.set`

```elm
Array.set : Int -> a -> Array a -> Array a
```

Returns a NEW array with the modified value.

```elm
u = Array.fromList [4,5,6]
Array.set 0 1 u
-- Array.fromList [1,5,6]
```

---

## `Array.slice`

```elm
Array.slice : Int -> Int -> Array a -> Array a
```

Gets elements from index `start` to `end - 1`.

```elm
Array.slice 2 4 (Array.fromList [1,2,3,4,5])
-- Array.fromList [3,4]
```

---

## `Array.empty`

```elm
Array.empty : Array a
```

Creates an empty array.

```elm
Array.empty
```

---

## `Array.repeat`

```elm
Array.repeat : Int -> a -> Array a
```

Repeats a value `n` times.

---

## `Array.isEmpty`

```elm
Array.isEmpty : Array a -> Bool
```

Checks if an array is empty.

```elm
Array.isEmpty (Array.fromList [1,2,3])
-- False
```

```elm
Array.isEmpty Array.empty
-- True
```

---

## `Array.length`

```elm
Array.length : Array a -> Int
```

Returns the length.

---

## `Array.push`

```elm
Array.push : a -> Array a -> Array a
```

Adds an element to the END.

```elm
Array.push 8 (Array.fromList [4,5,6])
-- Array.fromList [4,5,6,8]
```

---

## `Array.toList`

```elm
Array.toList : Array a -> List a
```

Converts an array into a list.

---

## `Array.toIndexedList`

```elm
Array.toIndexedList : Array a -> List (Int, a)
```

Pairs each element with its index.

Example:

```elm
Array.toIndexedList (Array.fromList [10,20,30])
-- [(0,10),(1,20),(2,30)]
```

---

# 6. Immutability

Elm is a pure functional language.

This means:

- variables cannot mutate
    
- values cannot mutate
    
- containers cannot mutate
    

Operations such as:

- adding
    
- removing
    
- sorting
    
- updating
    

return NEW containers instead of modifying old ones.

Example:

```elm
x = Array.fromList [10,20,30]
y = Array.set 2 100 x
```

Result:

```elm
x == Array.fromList [10,20,30]
y == Array.fromList [10,20,100]
```

`x` remains unchanged.

---

# 7. Filtering Example

```elm
filterDivisibleBy : List Int -> Int -> List Int
filterDivisibleBy givenList n =
    List.filter (\x -> modBy n x == 0) givenList
```

Example:

```elm
filterDivisibleBy [1,2,3,4,5,6] 2
-- [2,4,6]
```

---

# 8. Tuples

Tuples store grouped values.

Examples:

```elm
(Int, String)
(Int, String, Bool)
```

Unlike lists:

- tuple elements may have different types
    
- tuples usually store a fixed number of related values
    

---

# 8.1 Tuple Destructuring

```elm
answer =
    let
        (x, _, z) = tupleData
    in
    x + z
```

`_` means:

> “ignore this value”

---

# 9. Key Differences Summary

|Feature|List|Array|
|---|---|---|
|Access Style|Sequential|Random access|
|Best For|Recursion / traversal|Indexing|
|Mutable?|No|No|
|Syntax Literal|Yes (`[1,2,3]`)|No|
|Indexed Access|Slow|Faster|

---

# 10. Important Corrections from Earlier Notes

## Correction 1

Incorrect:

> `List.map` returns True or False

Correct:

`List.map` transforms each element.

`List.filter` is the one commonly associated with predicates returning `Bool`.

---

## Correction 2

Incorrect:

> `Array.get` is similar to Python `.index()`

Correct:

`Array.get i arr` is similar to:

```python
arr[i]
```

Python `.index(x)` searches for the location of `x`.

---

## Correction 3

Incorrect:

> Arrays are similar to Python tuples

Correct:

Elm arrays are indexed collection structures.  
Python tuples are fixed grouped values.

---

## Correction 4

Incorrect:

```elm
List.filter : (a->Bool) -> List a -> List b
```

Correct:

```elm
List.filter : (a -> Bool) -> List a -> List a
```

Filtering keeps the SAME element type.

---

---

# 11. Elm Basics

> Based on CS 12 lecture discussions and personal notes.  
> Some concepts and examples are adapted and expanded from course materials.

---

## 11.1 The Elm Programming Language

Elm is a:

- functional programming language
    
- designed mainly for front-end web applications
    
- focused on safety and reliability
    

Main characteristics:

- purely immutable
    
- statically typed
    
- functional programming oriented
    
- emphasizes compile-time error checking
    

Elm is known for having very few runtime errors because of its strong type system.

---

## 11.2 Functional Programming Concepts in Elm

### Pure Immutability

Values and containers cannot be mutated.

This means:

- variables cannot change after creation
    
- lists/arrays are immutable
    
- operations return NEW values instead of modifying old ones
    

---

### Static Typing

Elm checks types at compile time.

Example:

```elm
x : Int
x = 10
```

If the value does not match the declared type, Elm will not compile.

---

### No Traditional Loops

Elm has:

- no `for` loops
    
- no `while` loops
    

Instead, Elm commonly uses:

- recursion
    
- `List.map`
    
- `List.filter`
    
- `List.foldl`
    
- `List.foldr`
    

---

## 11.3 Running Elm

### Online

Use:

- `https://ellie-app.com/`
    

---

### Local Installation

Elm can also be installed locally using the terminal.

---

## 11.4 Elm Interactive Mode

To start the Elm REPL:

```bash
elm repl
```

This is similar to Python interactive mode.

Example:

```python
python3
```

---

# 12. Elm Syntax Basics

## 12.1 Program Entry Point (`main`)

Elm programs commonly start from a `main` definition.

Example:

```elm
module Main exposing (main)

import Browser
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)


type alias Model =
    { count : Int }


initialModel : Model
initialModel =
    { count = 0 }


type Msg
    = Increment
    | Decrement


update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment ->
            { model | count = model.count + 1 }

        Decrement ->
            { model | count = model.count - 1 }


view : Model -> Html Msg
view model =
    div []
        [ button [ onClick Increment ] [ text "+1" ]
        , div [] [ text <| String.fromInt model.count ]
        , button [ onClick Decrement ] [ text "-1" ]
        ]


main : Program () Model Msg
main =
    Browser.sandbox
        { init = initialModel
        , view = view
        , update = update
        }
```

Important idea:

- `main` acts as the program entry point
    
- Elm applications are often structured using Model-View-Update (MVU)
    

---

## 12.2 Importing Libraries

Syntax:

```elm
import ModuleName exposing (functions)
```

Example:

```elm
import Html exposing (text)
```

---

# 12.3 Built-in Data Types

|Type|Example Values|
|---|---|
|`Bool`|`True`, `False`|
|`Int`|`1`, `-1`|
|`Float`|`1.25`, `-1.0`|
|`Char`|`'a'`, `'😃'`|
|`String`|`"hello"`, `""`, `"""multi-line"""`|

---

## Important Corrections

### Correction 1

Incorrect:

```elm
Str
```

Correct:

```elm
String
```

---

### Correction 2

Incorrect:

```elm
'hello'
```

Correct:

Elm strings use DOUBLE quotes:

```elm
"hello"
```

Single quotes are for `Char` values only.

---

# 12.4 Operators

## Arithmetic Operators

|Symbol|Meaning|
|---|---|
|`+`|Addition|
|`-`|Subtraction|
|`*`|Multiplication|
|`/`|Division (returns `Float`)|
|`//`|Integer division|
|`^`|Exponentiation|

---

## Comparison Operators

|Symbol|Meaning|
|---|---|
|`==`|Equal|
|`/=`|Not equal|
|`<`|Less than|
|`<=`|Less than or equal|
|`>`|Greater than|
|`>=`|Greater than or equal|

---

## Logical Operators

|Symbol|Meaning|
|---|---|
|`&&`|AND|
|`||
|`not`|Logical NOT|

---

## Important Corrections

### Correction 1

Incorrect:

```elm
/==
```

Correct:

```elm
/=
```

Elm uses `/=` for inequality.

---

### Correction 2

Several comparison descriptions were reversed.

Correct meanings:

```text
<=  less than or equal
>=  greater than or equal
<   less than
>   greater than
```

---

# 12.5 Calling Functions

Elm functions are called WITHOUT parentheses.

Examples:

```elm
toFloat 1
round 1.5
String.fromInt 1
min 1.2 1.55
```

---

# 12.6 Variable Naming

Elm variables:

- usually use `camelCase`
    
- must start with a lowercase letter
    
- cannot start with numbers
    
- are indentation-sensitive
    

Example:

```elm
studentName = "Jacob"
```

---

# 12.7 Variables and Reassignment

## Important Clarification

Elm variables CANNOT be reassigned.

Incorrect:

```elm
x = 2
x = 3
```

This is invalid in Elm.

Also invalid:

```elm
x = 3
x = x + 3
```

Elm variables are immutable.

---

# 12.8 Statements vs Expressions

## Statements

Statements do NOT evaluate to values.

Examples:

- variable declarations
    
- imports
    
- type declarations
    

---

## Expressions

Expressions evaluate to values.

In Elm:

- almost everything is an expression
    
- `if` is an expression
    
- `case` is an expression
    
- `let` is an expression
    

Example:

```elm
label =
    if x > 0 then
        "positive"
    else if x == 0 then
        "zero"
    else
        "negative"
```

---

## Important Correction

Incorrect:

```elm
funcName: Int -> Bool
```

was labeled as a statement.

More accurately:

- it is a TYPE SIGNATURE declaration
    
- not an expression
    

---

# 12.9 Case Expressions

Used for pattern matching.

Example:

```elm
day =
    case dayNum of
        1 -> "Sunday"
        2 -> "Monday"
        3 -> "Tuesday"
        4 -> "Wednesday"
        5 -> "Thursday"
        6 -> "Friday"
        7 -> "Saturday"
        _ -> "Unknown Day"
```

`_` acts as a catch-all pattern.

---

# 12.10 `let` / `in` Expressions

Syntax:

```elm
let
    variable = expression
in
bodyExpression
```

Important:

- variables inside `let` only exist inside that block
    
- the `in` section must evaluate to ONE expression
    

Example:

```elm
isPositive : Int -> String
isPositive x =
    let
        response =
            if modBy 2 x == 0 then
                "even"
            else
                "odd"
    in
    response
```

---

## Important Corrections

### Correction 1

Incorrect:

> `in` is the counterpart of Python return

More accurate:

`in` specifies the final expression produced by the `let` expression.

---

### Correction 2

Your earlier example had indentation and syntax issues.

Elm requires:

- proper indentation
    
- every branch to return expressions
    
- `let` blocks to remain inside expressions
    

---

# 12.11 Declaring Functions

## Function Syntax

```elm
functionName arg1 arg2 =
    expression
```

---

## Function Signatures

Syntax:

```elm
functionName : Type1 -> Type2 -> ReturnType
```

Example:

```elm
combination : Int -> Int -> Int
combination x y =
    let
        numerator = factorial x
        denominator = factorial (x - y) * factorial y
    in
    numerator // denominator
```

The LAST type refers to the return type.

---

# 12.12 Pipeline Operator `|>`

```elm
x |> f
```

means:

```elm
f x
```

Useful for readable transformation pipelines.

---

Example:

```elm
List.range 6 7
    |> List.sort
```

Equivalent to:

```elm
List.sort (List.range 6 7)
```

---

## Important Correction

Incorrect earlier example:

```elm
6 7
|> List.range
|> List.sort
```

This is invalid syntax.

Correct:

```elm
List.range 6 7
    |> List.sort
```