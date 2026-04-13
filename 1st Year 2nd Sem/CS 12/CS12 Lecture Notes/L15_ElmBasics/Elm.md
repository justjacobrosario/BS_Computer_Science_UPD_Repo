---
field: programming
---
## 1. Elm Programming Language

: Functional programming language for front-end web apps
: Safe type system (since no runtime errors)

### 2) Functional Programming Language
: Purely immutable data (cannot mutate, modify a value of an element)
: Statically typed (Type-hint must always be reflected by its value)
: No for and while loops, only recursion

### 3) Installment
#### 1] Online via Ellie
#### 2] Locally via installing it in terminal

### 4) Elm Interactive Mode
: to code using elm in terminal, type `elm repl`
: counterpart of `python3 interactive mode`

## 2. Elm Syntax

### 1) Main Function
: Like python, defines various functions and then generally runs a main function

e.g. Note: Don't focus the specific  syntax and words, there, this is just to show that there exists a main function
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

### 2) importing libraries
: Like in python, elm also imports libraries via `import _library_name exposing (_methods)`

: useful html libraries
#### 1] `import Html exposing (_html_tags)`
 
### 3) Built-in Data Types

| Type  | Values                                  |
| ----- | --------------------------------------- |
| Bool  | True, False                             |
| Int   | 1, -1                                   |
| Float | -1.0, 1.23                              |
| Char  | 'a', '\', '😃'                          |
| Str   | 'hello', <br>'''multi-line<br>string''' |

### 4) Operators

- Arithmetic

| Symbol | Operation            |
| ------ | -------------------- |
| +      | add                  |
| -      | subtract             |
| *      | multiply             |
| /      | divide               |
| //     | floor divide         |
| ^      | exponent (raised to) |
- Comparison

| Symbol | Operation   |
| ------ | ----------- |
| ==     | equal       |
| /==    | unequal     |
| <=     | gt or equal |
| <      | gt          |
| >=     | lt or equal |
| >      | lt          |
- Logical

| Symbol | Operation |
| ------ | --------- |
| &&     | AND       |
| \|\|   | OR        |
|        |           |

