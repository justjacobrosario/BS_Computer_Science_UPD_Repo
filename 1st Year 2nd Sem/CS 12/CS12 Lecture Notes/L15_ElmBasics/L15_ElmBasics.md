---
year: 1 
subject: CS12 
field: programming
---


# 1: ELM PROGRAMMING LANGUAGE

: functional programming language for front-end web apps (Evan Czaplicki, 2012) 
: purely immutable and statically typed - practically no runtime errors 
: no for/while loops, only recursion

## 1. Running Elm

: online via https://ellie-app.com/ 
: locally via `elm repl` in terminal (like python3 interactive mode)

# 2: BUILT-IN DATA TYPES

|Type|Values|
|---|---|
|Bool|`True`, `False`|
|Int|`-140`, `0`, `150`|
|Float|`1.25`, `-1.0`|
|Char|`'a'`, `'\\'`, `'🙈'`|
|String|`"hello"`, `""`, `"""multi\nline\nstring"""`|

# 3: OPERATORS

## 1. Arithmetic

|Symbol|Operation|Notes|
|---|---|---|
|`+`|add||
|`-`|subtract||
|`*`|multiply||
|`/`|divide|always returns Float|
|`//`|floor divide|returns Int|
|`^`|exponent|right-associative: `2^3^2 == 512`|

## 2. Comparison

|Symbol|Operation|Notes|
|---|---|---|
|`==`|equal||
|`/=`|not equal|note: NOT `!=` like python|
|`<`|less than||
|`<=`|less than or equal||
|`>`|greater than||
|`>=`|greater or equal||

## 3. Logic

|Symbol|Operation|
|---|---|
|`&&`|AND|
|`\|`|OR|
|`not`|NOT (function, not operator)|

# 4: CALLING FUNCTIONS

: no parentheses, just place args after function name

```elm
toFloat 1           -- Float 1.0
round 1.5           -- Int 2
String.fromInt 1    -- "1"
String.fromFloat 0.1 -- "0.1"
Debug.toString True -- "True"
min 1.2 1.55        -- 1.2
```

# 5: VARIABLES

## 1. Naming Rules

: use camelCase
: must NOT be indented at global level 
: indentation-sensitive

## 2. Immutability

: elm variables CANNOT be reassigned

```elm
year = 2023
year = year + 1  -- Error
```

: since no reassignment - no while/for loops either
: all repetition must use recursion or library functions

# 6: STATEMENTS vs EXPRESSIONS

: statement - does NOT evaluate to a value, can't be assigned 
: expression - evaluates to a value, can be assigned 
: in elm, almost EVERYTHING is an expression 
: variable declaration is the main exception (its a statement)

# 7: CONDITIONALS

## 1. If Expression

: `if` in elm is an expression (always return a value) : `else` is always required

```elm
mood =
    if isWeekend then
        "happy"
    else
        "sad"

-- one-liner
mood = if isWeekend then "happy" else "sad"
```

: `else if` chaining

```elm
mood =
    if isRaining then "gloomy"
    else if hasExam then "scared"
    else if isWeekend then "happy"
    else "sad"
```

## 2. Case Expression

: pattern matching on a value 
: `_` is the catch-all (always include this) 
: patterns must be more indented than `case` line : all patterns must share the same indentation level

```elm
day =
    case n of
        1 -> "Sunday"
        2 -> "Monday"
        3 -> "Tuesday"
        4 -> "Wednesday"
        5 -> "Thursday"
        6 -> "Friday"
        7 -> "Saturday"
        _ -> "Unknown"
```

# 8: LET EXPRESSION AND SCOPING

: `let` -> where local intermediate variables are declared 
: `in` -> the single return expression of the whole block 
: variables in `let` are NOT accessible outside it

```elm
let
    varName1 = expression1
    varName2 = expression2  -- can reference earlier declarations
in
bodyExpression
```

e.g.

```elm
z =
    let
        x = 11
        y = x + 1
    in
    x + y  -- x and y only live here
```

## 1. Shadowing

: when inner scope reuse a name from outer scope - elm flags this 
: usually bugs, avoid

```elm
mood = "excited"  -- global

yourMood =
    let
        mood =  -- shadows global mood, will flag
            if isRaining then "gloomy"
            else if hasExam then "scared"
            else if isWeekend then "happy"
            else "sad"
    in
    mood
```

# 9: DECLARING FUNCTIONS

## 1. Basic Syntax

```elm
functionName arg1 arg2 =
    functionBody  -- single expression
```

e.g.

```elm
-- unary
double n =
    n * 2

-- binary
combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den
```

## 2. Type Signatures

: last type in signature is always the return type

```elm
-- functionName : ArgType1 -> ArgType2 -> ReturnType

double : Int -> Int
double n = n * 2

combination : Int -> Int -> Int
combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den
```

## 3. Type Inference

: elm infers types even without explicit signatures : e.g. for `combination n k`, elm knows n and k are Int (from factorial), return is Int (from //) : passing wrong types -> compile-time error (not runtime)

```elm
combination 4 "2"  -- Error: 2nd arg must be Int not String
```

# 10: PIPELINE OPERATOR

## 1. Forward Pipeline `|>`

: `x |> f` is same as `f x` : visualize as direction of data flow (left to right)

```elm
-- standard
List.reverse (List.range 1 5)

-- pipelined (reads as sequence of transforms)
List.range 1 5
    |> List.reverse
```

## 2. Backward Pipeline `<|`

: `f <| x` is same as `f x` : useful for removing nested parens, less common than `|>`

```elm
-- with parens
List.reverse (List.range 1 5)

-- with <|
List.reverse <| List.range 1 5
```