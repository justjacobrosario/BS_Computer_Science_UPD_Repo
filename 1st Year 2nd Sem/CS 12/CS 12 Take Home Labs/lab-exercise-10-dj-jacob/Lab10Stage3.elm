import Browser
import Html exposing (Html, div, text, p, input, br, select, option, button)
import Html.Attributes exposing (value, selected)
import Html.Events exposing (onInput, onClick)
import Dict exposing (Dict)
import Set exposing (Set)

type FlamesType
  = Crossout
  | Count
  
type ID = ID Int
  
type alias Box =
  { id : ID
  , content : String 
  }
  
type Msg
  = MsgBox ID String
  | MsgSetFlamesType FlamesType
  | MsgAddBox
  
type alias Model =
  { boxes : List Box
  , dropbox : FlamesType
  , output : List String
  , nextID: Int
  }
  
init : Model
init = { boxes = [{ id = ID 1, content = "" }, { id = ID 2, content = "" }], dropbox = Crossout, output = ["Please enter two names."], nextID = 3}

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
    checkStrings :  FlamesType -> Box -> Box -> String
    checkStrings flamesType box1 box2 =
      let
        s1Alpha = String.filter (\char -> Char.isAlpha char) box1.content
        s2Alpha = String.filter (\char -> Char.isAlpha char) box2.content
      in
      case ( (s1Alpha /= "") && (s2Alpha /= "") ) of
        True -> 
          case flamesType of
            Crossout -> box1.content ++ " and " ++ box2.content ++ " are " ++ convertNumToFlames (crossoutFlames s1Alpha s2Alpha) ++ "."
            Count -> box1.content ++ " and " ++ box2.content ++ " are " ++ convertNumToFlames (countFlames s1Alpha s2Alpha) ++ "."
        _ -> "Please enter two names."
    updatedModel =
            case msg of
                MsgBox targetID newContent ->
                  let 
                    updateBox currentBox =
                      if currentBox.id == targetID then
                        { currentBox | content = newContent }
                      else
                        currentBox
                  in
                  { model | boxes = List.map updateBox model.boxes }
                MsgSetFlamesType flamesType ->
                  {model | dropbox = flamesType}
                MsgAddBox ->
                  {model | boxes = model.boxes ++ [{ id = ID model.nextID, content = "" }], nextID = model.nextID + 1}
    anyEmpty = List.any (\box -> String.filter Char.isAlpha box.content == "") updatedModel.boxes
    newOutput =
      if anyEmpty then
        ["Please enter two names."]
      else
        List.map2 (checkStrings updatedModel.dropbox) updatedModel.boxes (List.drop 1 updatedModel.boxes)

    
  in
  { updatedModel | output = newOutput }

view : Model -> Html Msg
view model =
  let
    convertValueToMsg : String -> Msg
    convertValueToMsg val =
      case val of
        "Crossout" -> MsgSetFlamesType Crossout
        _ -> MsgSetFlamesType Count
    convertBoxToInput : Box -> Html Msg
    convertBoxToInput box =
      div [] [ input [onInput (MsgBox box.id)] [text box.content] ]
    convertParagraphToP : String -> Html Msg
    convertParagraphToP output =
      div [] [ p [] [text output] ]
  in
  div []
      ( [ button [onClick MsgAddBox] [text "Add name"] ]
      ++ (List.map convertBoxToInput model.boxes)
      ++ [ select [onInput convertValueToMsg] 
            [ option [value "Crossout", selected (model.dropbox == Crossout)] [text "Crossout"]
            , option [value "Count" , selected (model.dropbox == Count)] [text "Count"]
            ] ]
      ++ (List.map convertParagraphToP model.output)
      )
        
main : Program () Model Msg
main =
    Browser.sandbox
        { init = init
        , update = update
        , view = view
        }