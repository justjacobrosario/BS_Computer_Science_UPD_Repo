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

# 2: List Syntax
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
