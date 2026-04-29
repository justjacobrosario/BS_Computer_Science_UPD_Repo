import Browser
import Html exposing (Html, div, button, p, input, text)
import Html.Events exposing (onClick, onInput)
import Html.Attributes exposing (value, selected, id)
import Dict exposing (Dict)
import Set exposing (Set)

type alias Box =
  { id : Int
  , content : String}

type alias Model =
  { inputVal : String
  , boldBox : String
  , boxes : List Box
  , currId : Int}
  
init : Model
init = 
  { inputVal = ""
  , boldBox = ""
  , boxes = []
  , currId = 1}
  
type Msg 
  = NewBox
  | SaveText
  | UpdateText String

update : Msg -> Model -> Model
update action model =
  case action of
    NewBox -> 
      {model | boxes = model.boxes ++ [{id = model.currId + 1, content = "new paragraph"}], currId = model.currId + 1}
    SaveText -> {model | boxes = List.map (\box -> 
      if box.id == model.currId then {box | content = model.inputVal}
      else box)
      model.boxes}
    UpdateText newText -> {model | inputVal = newText, boldBox = newText}
    
view : Model -> Html Msg
view model =
  div [] 
  [ input [onInput UpdateText, value model.inputVal] []
  , p [] [text model.boldBox]
  , button [onClick SaveText ] [ text "save"]
  , button [onClick NewBox ] [ text "add box"]
  , p [] [text (String.fromInt model.currId)]
  , div [] (List.map (\box -> p [id (String.fromInt box.id)] [text ((String.fromInt box.id) ++ box.content)]) model.boxes)
  ]
  
main : Program () Model Msg
main =
  Browser.sandbox
    { init = init
    , update = update
    , view = view}
      
      
      