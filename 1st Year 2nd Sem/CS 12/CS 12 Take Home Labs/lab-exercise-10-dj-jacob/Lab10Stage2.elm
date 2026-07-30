import Browser
import Html exposing (Html, div, text, p, input, br, select, option)
import Html.Attributes exposing (value)
import Html.Events exposing (onInput)
import Dict exposing (Dict)
import Set exposing (Set)

type FlamesType
  = Crossout
  | Count
  
type Msg
  = MsgBox1 String
  | MsgBox2 String
  | MsgSetFlamesType FlamesType
  
type alias Model =
  { box1 : String
  , box2 : String
  , dropbox : FlamesType
  , output : String
  }
  
init : Model
init = { box1 = "", box2 = "", dropbox = Crossout, output = "Please enter two names."}

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
  
countFlames : String -> String -> Int
countFlames s1 s2 = 
  let
    s1Lower = String.toLower s1
    s2Lower = String.toLower s2
    dictTemplate = 
      s1Lower ++ s2Lower 
        |> String.toList 
        |> Set.fromList 
        |> Set.toList
        |> List.map (\char -> (char, 0))
        |> Dict.fromList
    s1Dict = String.foldl (\char acc -> Dict.update char (\value -> Just (Maybe.withDefault 0 value + 1)) acc) dictTemplate s1Lower
    s2Dict = String.foldl (\char acc -> Dict.update char (\value -> Just (Maybe.withDefault 0 value + 1)) acc) dictTemplate s2Lower
    totalCount = List.foldl
                  (\char acc ->
                    case (Dict.get char s1Dict, Dict.get char s2Dict) of
                      (Just a, Just b) -> acc + (abs (a - b))
                      _ -> acc
                  ) 0 (Dict.keys dictTemplate)
  in
  totalCount

update : Msg -> Model -> Model
update msg model =
  let
    checkStrings : String -> String -> FlamesType -> String
    checkStrings s1 s2 flamesType =
      let
        s1Alpha = String.filter (\char -> Char.isAlpha char) s1
        s2Alpha = String.filter (\char -> Char.isAlpha char) s2
      in
      case ( (s1Alpha /= "") && (s2Alpha /= "") ) of
        True -> 
          case flamesType of
            Crossout -> s1 ++ " and " ++ s2 ++ " are " ++ convertNumToFlames (crossoutFlames s1Alpha s2Alpha) ++ "."
            Count -> s1 ++ " and " ++ s2 ++ " are " ++ convertNumToFlames (countFlames s1Alpha s2Alpha) ++ "."
        _ -> "Please enter two names."
    updatedModel =
            case msg of
                MsgBox1 s1 ->
                    {model | box1 = s1}
                MsgBox2 s2 ->
                    {model | box2 = s2}
                MsgSetFlamesType flamesType ->
                    {model | dropbox = flamesType}
    newOutput = checkStrings updatedModel.box1 updatedModel.box2 updatedModel.dropbox
  in
  { updatedModel | output = newOutput }

convertValueToMsg : String -> Msg
convertValueToMsg val =
  case val of
    "Crossout" -> MsgSetFlamesType Crossout
    _ -> MsgSetFlamesType Count

view : Model -> Html Msg
view model =
    div []
        [  p [] [text model.output]
        , input [onInput MsgBox1] [text model.box1]
        , br [] []
        , input [onInput MsgBox2] [text model.box2]
        , br [] []
        , select [onInput convertValueToMsg] 
                [ option [value "Crossout"] [text "Crossout"]
                , option [value "Count"] [text "Count"]
                ]
        ]
        
main : Program () Model Msg
main =
    Browser.sandbox
        { init = init
        , update = update
        , view = view
        }