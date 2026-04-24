---
field: programming
---
## 1. Other tags via ELM 

### 1) `input` HTML element
`input : List (Attribute m) -> List (Html m) -> Html m`

: `input` is a tag that has attributes
	1. initial displayed text `value text_to_display`
	2. an event `onInput param`

: must import
```elm
import Html exposing (input)
import Html.Attribute exposing (value)
import Html.Events exposing (onInput)
```

e.g.

```elm
type Msg =
	-- ...
	| MsgChangeText String -- MsgChangeText carries new text

-- ...
div []
-- Elm will pass the new content to `MsgChangeText`
-- and will pass the result to `onInput`;
-- `value` contains displayed text in textbox
	[ 
	input [ value model.text, onInput MsgChangeText ] []
	input [ value model.text, onInput "Hello" ] []
	
	]
	
-- notice that the 1st input tag has a modifiable MsgChangeText, while the 2nd has a fixed text "Hello"
```
### 2) `Http.get` HTML element
`import Http`
`Http.get : { url : String, expect : Expect m } -> Cmd m`

: basically getting data from an API endpoint
: has attributes
	1. `url` : string of the URL
	2. `expect` : typically `Http.expectString MsgURLVal`
#### 1] Handling API fetching Errors via `Result`
: API fetching errors might come, so the `MsgURLVal` must either return the value or return an error message

: `Result` is like `Maybe` where it has two params
```elm
type Result error value
	= Ok value
	| Err error
```

: `MsgURLVal` must have a `Result` value like this in the Msg type
```elm
type Msg
	= MsgURLVal (Result Http.Error String)
```

: when implemented, like this
```elm
import Http

type Msg
	= MsgGotJoke (Result Http.Error String)

getJoke: Cmd Msg -- Cmd Msg object is the one fetching from the API and returning the data to Msg
getJoke =
-- Sends a GET request to specified URL
Http.get
{ url = "https://v2.jokeapi.dev/joke/programming?format=txt"
, expect = Http.expectString MsgGotJoke
}
```

#### 2] Cmd Msg
: like Model, Cmd Msg is an object (but is fetche from an API) that also updates through time

: Like Model, Cmd msg 