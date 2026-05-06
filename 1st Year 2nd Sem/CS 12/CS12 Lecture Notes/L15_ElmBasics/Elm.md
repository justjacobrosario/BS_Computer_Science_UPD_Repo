---
field: programming
---

# Lecture 15: Elm Basics

> Based on CS 12 lecture discussions and personal notes. Some concepts and examples are adapted and expanded from course materials.

---

# 1. The Elm Programming Language

Elm is a functional programming language designed for building front-end web applications. It was created by Evan Czaplicki in 2012 and is available at [https://elm-lang.org/](https://elm-lang.org/).

Key characteristics:

- **Purely immutable** — data cannot be changed once defined
- **Statically typed** — all types must be consistent and are checked at compile time
- **No runtime errors** — the type system catches mistakes before the program runs
- **No loops** — `for` and `while` loops do not exist; recursion is used instead

---

## 1.1 Running Elm

There are two ways to use Elm:

1. **Online** — via [Ellie](https://ellie-app.com/), a browser-based Elm editor
2. **Locally** — by installing Elm and running `elm repl` in the terminal (similar to Python's interactive mode)

---

# 2. Built-in Data Types

|Type|Example Values|
|---|---|
|Bool|`True`, `False`|
|Int|`-140`, `0`, `150`|
|Float|`1.25`, `-1.0`|
|Char|`'a'`, `'\\'`, `'🙈'`|
|String|`"hello"`, `""`, `"""multi\nline\nstring"""`|

---

# 3. Operators

## Arithmetic

|Symbol|Operation|Notes|
|---|---|---|
|`+`|Addition||
|`-`|Subtraction||
|`*`|Multiplication||
|`/`|Division|Always returns `Float`|
|`//`|Floor Division|Returns `Int`|
|`^`|Exponentiation|Right-associative: `2^3^2 == 512`|

## Comparison

|Symbol|Operation|
|---|---|
|`==`|Equal|
|`/=`|Not equal|
|`<`|Less than|
|`<=`|Less than or equal|
|`>`|Greater than|
|`>=`|Greater than or equal|

> Note: `/=` is Elm's inequality operator, unlike Python's `!=`.

## Logical

|Symbol|Operation|
|---|---|
|`&&`|AND|
|`\|`|OR|
|`not`|NOT (this is a function, not an operator)|

---

# 4. Calling Functions

Functions are called by placing arguments directly after the function name — no parentheses needed.

```elm
toFloat 1           -- returns Float 1.0
round 1.5           -- returns Int 2
String.fromInt 1    -- returns "1"
String.fromFloat 0.1 -- returns "0.1"
Debug.toString True -- returns "True"
min 1.2 1.55        -- returns 1.2
```

More built-in functions: [https://package.elm-lang.org/packages/elm/core/latest/Basics](https://package.elm-lang.org/packages/elm/core/latest/Basics)

---

# 5. Variables

## 5.1 Naming Rules

- Must start with a **lowercase letter**
- Convention: use **camelCase** (e.g., `isWeekend`, not `is_weekend`)
- Must **not be indented** at the global level
- Indentation is significant

## 5.2 Immutability and Reassignment

Elm variables **cannot be reassigned**. Once a variable is bound to a value, it stays that way.

```elm
-- Invalid in Elm
year = 2023
year = year + 1  -- Error!
```

Since there is no reassignment, Elm also has **no `while` or `for` loops**. All repetition must be expressed through recursion or library functions.

---

# 6. Statements vs Expressions

A **statement** does not evaluate to a value and cannot be assigned to a variable.

A **expression** evaluates to a value and can be assigned.

> In Elm, almost everything is an expression.

Variable declaration itself is the main exception — it is a statement.

---

# 7. Conditionals

## 7.1 If Expression

`if` in Elm is an expression, so it always returns a value. An `else` branch is always required.

```elm
mood =
    if isWeekend then
        "happy"
    else
        "sad"

-- One-liner form
mood = if isWeekend then "happy" else "sad"
```

`else if` chaining is also supported:

```elm
mood =
    if isRaining then
        "gloomy"
    else if hasExam then
        "scared"
    else if isWeekend then
        "happy"
    else
        "sad"
```

---

## 7.2 Case Expression

`case` performs pattern matching against a value.

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
        _ -> "Unknown day"  -- catch-all; always include this
```

Rules:

- Patterns must be more indented than the `case` line
- All patterns must share the same level of indentation
- `_` is the wildcard/catch-all pattern

---

# 8. Let Expression and Scoping

`let` allows intermediate values to be declared within a local scope. The `in` keyword marks the body — the single expression that the whole `let` block evaluates to.

```elm
let
    varName1 = expression1
    varName2 = expression2
in
bodyExpression
```

Example:

```elm
z =
    let
        x = 11
        y = x + 1  -- earlier declarations can be referenced
    in
    x + y  -- x and y are only accessible here
```

> Variables declared inside `let` are not accessible outside it.

---

## 8.1 Shadowing

Elm flags **shadowing** — when a variable name defined in an inner scope matches one in an outer scope.

```elm
mood = "excited"  -- global definition

yourMood =
    let
        mood =  -- shadows global `mood`; this will be flagged
            if isRaining then "gloomy"
            else if hasExam then "scared"
            else if isWeekend then "happy"
            else "sad"
    in
    mood
```

Shadowing is typically a source of subtle bugs and should be avoided.

---

# 9. Declaring Functions

## 9.1 Basic Syntax

```elm
functionName arg1 arg2 ... argN =
    functionBody  -- single expression
```

Example — unary function:

```elm
double n =
    n * 2
```

Example — binary function:

```elm
combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den
```

---

## 9.2 Type Signatures

Type signatures describe the input and output types of a function. The last type listed is always the return type.

```elm
functionName : TypeArg1 -> TypeArg2 -> ReturnType
```

Examples:

```elm
double : Int -> Int
double n =
    n * 2

combination : Int -> Int -> Int
combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den
```

---

## 9.3 Type Inference

Elm can automatically infer types from usage, even without an explicit signature:

```elm
combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den
```

From this, Elm infers:

- `n` and `k` are `Int` (because `factorial` takes `Int`)
- The return type is `Int` (because `//` returns `Int`)

Passing the wrong types causes a compile-time error:

```elm
combination 4 "2"  -- Error: second argument must be Int, not String
```

---

# 10. Pipeline Operator

## 10.1 Forward Pipeline `|>`

`x |> f` is equivalent to `f x`. Think of it as the direction data flows.

```elm
-- Standard form
List.reverse (List.range 1 5)

-- Pipelined form
List.range 1 5
    |> List.reverse
```

This makes code read as a sequence of transformations, left to right, which is much clearer for multi-step operations.

## 10.2 Backward Pipeline `<|`

`f <| x` is also equivalent to `f x`, but flows right to left. This is useful for removing nested parentheses.

```elm
-- With parentheses
List.reverse (List.range 1 5)

-- With backward pipeline
List.reverse <| List.range 1 5
```

> `<|` is less commonly used than `|>`.