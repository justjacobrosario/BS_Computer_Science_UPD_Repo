import Browser
import Html exposing (Html, div, text, p, input, br)
import Html.Events exposing (onInput)

type Msg
  = MsgBox1 String
  | MsgBox2 String
  
type alias Model =
  { box1 : String
  , box2 : String
  , output : String
  }
  
init : { box1 : String , box2 : String , output : String }
init = { box1 = "", box2 = "", output = "Please enter two names."}

convertNumToFlames : Int -> String
convertNumToFlames num = 
  case (modBy 6 num) of
    1 -> "Friends"
    2 -> "Lovers"
    3 -> "Affectionate"
    4 -> "Married"
    5 -> "Enemies"
    0 -> "Siblings"
    _ -> ""
    
crossoutFlames : String -> String -> Int
crossoutFlames s1 s2 = 
  let
    s1Lower = String.toLower s1
    s2Lower = String.toLower s2
    s1Count = List.foldl 
                (\char acc -> 
                  case (not (String.contains (String.fromChar char) s2Lower)) of
                    True -> acc + 1
                    False -> acc
                ) 0 (String.toList s1Lower)
    s2Count = List.foldl
                (\char acc ->
                  case (not (String.contains (String.fromChar char) s1Lower)) of
                    True -> acc + 1
                    False -> acc
                ) 0 (String.toList s2Lower)
  in
  s1Count + s2Count

update : Msg -> Model -> Model
update msg model =
  let
    checkStrings : String -> String -> String
    checkStrings s1 s2 =
      let
        s1Alpha = String.filter (\char -> Char.isAlpha char) s1
        s2Alpha = String.filter (\char -> Char.isAlpha char) s2
      in
      case ( (s1Alpha /= "") && (s2Alpha /= "") ) of
        True -> s1 ++ " and " ++ s2 ++ " are " ++ convertNumToFlames (crossoutFlames s1Alpha s2Alpha) ++ "."
        _ -> "Please enter two names."
    updatedModel =
            case msg of
                MsgBox1 s1 ->
                    {model | box1 = s1}
                MsgBox2 s2 ->
                    {model | box2 = s2}
    newOutput = checkStrings updatedModel.box1 updatedModel.box2
  in
  { updatedModel | output = newOutput }

view : Model -> Html Msg
view model =
    div []
        [ p [] [text model.output]
        , input [onInput MsgBox1] [text model.box1]
        , br [] []
        , input [onInput MsgBox2] [text model.box2]
        ]
        
main : Program () Model Msg
main =
    Browser.sandbox
        { init = init
        , update = update
        , view = view
        }