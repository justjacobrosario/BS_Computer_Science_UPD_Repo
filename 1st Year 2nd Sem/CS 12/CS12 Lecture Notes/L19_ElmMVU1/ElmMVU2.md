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

: