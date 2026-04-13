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

# 3: Maybe Syntax

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

# 4: Array Syntax
: builtin datatype (no need to import)
: a container for random-access 