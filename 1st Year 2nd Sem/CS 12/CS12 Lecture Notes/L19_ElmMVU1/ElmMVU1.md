---
field: programming
---

## 1. Elm for making webpages
: yes

## 2. Single-page web app (SPA)
: web app with only single page, yes
: lets say we are going to make a counter that starts from 0, then increments by +1 or decrements by -1

: steps
### 1) Represent State of App (Model type)
: what data must the app to keep track
: these are data that updates over time

: e.g. counterValue : Int
```elm
type alias Model = Int

init = 0 -- initial value

```

### 2) Identify How Users can affect State (Msg type)
: how can users interact
: it commonly called as `Msg`

#### 1] Represent all possibilies of interactions
: e.g. + button (increment by 1) and - button (decrement by -1)
```elm
type Msg
	= MsgIncrement
	| MsgDecrement
```

#### 2] Define how interactions change State
: basically define the logic in functions
```elm
update : Msg -> Model -> Model
update msg model =
	case msg of
		MsgIncrement ->
			model + 1
		MsgDecrement ->
			model - 1
```

### 3) Define UI based on state (view func)
: make a view function that presents states

```elm
-- import firstt
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)

view : Model -> Html Msg
view model =
	-- Will explain parts in detail later
	div []
		-- Children
		[ button [ onClick MsgIncrement ] [ text "+" ]
		, p [] [ text (String.fromInt model) ]
		, button [ onClick MsgDecrement ] [ text "-" ]
		]
		
```

### 4) Combine Model + View + Update + Msg + Main

```elm
import Browser
import Html exposing (Html, button, div, p, text)
import Html.Events exposing (onClick)

type alias Model = Int

init = 0

type Msg
	= MsgIncrement
	| MsgDecrement
	
--

view : Model -> Html Msg
view model =
	div []
		[ button [ onClick MsgIncrement ] [ text "+" ]
		, p [] [ text (String.fromInt model) ]
		, button [ onClick MsgDecrement ] [ text "-" ]
		]

--

update : Msg -> Model -> Model
update msg model =
	case msg of
		MsgIncrement ->
			model + 1
		MsgDecrement ->
			model - 1
			
--
-- main is like the controller (combines all components)
main =
	Browser.sandbox
		{ init = init
		, update = update
		, view = view } -- like pyxel in python
```

## 3. MVU (Model, View, Update)
: also called TEA (The Elm Architecture)
	- Model: State of the program
	View: UI based on state

• Update: State update via messages