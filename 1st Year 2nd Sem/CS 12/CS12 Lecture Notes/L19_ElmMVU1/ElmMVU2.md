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
### 2) `Http.get` HTML element

: