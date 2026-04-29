import Browser
import Html exposing (Html, div, button, p, input, text, select, option)
import Html.Events exposing (onClick, onInput)
import Html.Attributes exposing (value, selected, id, style)
import Dict exposing (Dict)
import Set exposing (Set)

formats = Dict.fromList 
  [ ("default", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  , ("Bold (sans)", "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭")
  , ("Italic Bold (serif)", "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")
  , ("Italic Bold (sans)", "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕")
  , ("Medieval Bold", "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")
  , ("Double-Struck", "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")
  , ("Blocks", "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉")]

type alias Box =
  { id : Int
  , content : String}

type alias Model =
  { inputVal : String
  , formatted : String
  , chosen_format : String}
  
init : Model
init = 
  { inputVal = ""
  , formatted = ""
  , chosen_format = "default"}
  
type Msg 
  = UpdateText String
  | ChangeFont String

change_font : String -> String -> Model -> String
change_font orig font model =
  let
    format_char char_next prev =
      let
        next = String.fromChar char_next
        idx = Maybe.withDefault 0 (List.head (String.indexes next (Maybe.withDefault "" (Dict.get "default" formats))))
      in
      case model.chosen_format of
        "default" -> String.slice idx (idx + 1) (Maybe.withDefault "" (Dict.get "default" formats))
        "Bold (sans)" -> String.slice idx (idx + 1) (Maybe.withDefault "" (Dict.get "Bold (sans)" formats))
        _ -> String.slice idx (idx + 1) (Maybe.withDefault "" (Dict.get "default" formats))
          
  in
  String.foldl format_char "" orig


update : Msg -> Model -> Model
update action model =
  case action of
    UpdateText newText -> {model | inputVal = newText, formatted = (change_font model.inputVal model.chosen_format model)}
    ChangeFont newFont -> {model | chosen_format = newFont}
    
view : Model -> Html Msg
view model =
  div [style "padding-left" "10px", style "padding-top" "10px"] 
  [ p [style "font-family" "sans-serif"] [text "Type here:"]
  , input [onInput UpdateText, value model.inputVal] []
  , select [ onInput ChangeFont]
    [ option [ value "default", selected (model.chosen_format == "default")] [ text "default"]
    , option [ value "Bold (sans)", selected (model.chosen_format == "Bold (sans)")] [ text "Bold (sans)"]
    ]
  , p [] [text model.chosen_format]
  , p [style "font-family" "sans-serif"] [text model.formatted]

  ]
  
main : Program () Model Msg
main =
  Browser.sandbox
    { init = init
    , update = update
    , view = view}
      
      
      