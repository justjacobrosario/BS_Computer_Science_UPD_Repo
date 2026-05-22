module Main exposing (..)
import Html exposing (Html, div, p, br, input, button, text)
import Html.Events exposing (onClick, onInput)
import Html.Attributes exposing (value)
import Browser exposing (..)

type Msg = MsgInput
    | MsgSavePost
    | MsgSelectDate
    | MsgComment
    | MsgSaveComment
    
type alias Post = 
    { post_text : String
    , comments : List String
    , date : Int}

type alias Model = 
    { posts : List Post
    , dateSelected : Int
    , currentDate
    , text_input : String}
    
    
init: Model
init = {posts = [], dateSelected = 0, currentDate = 0, text_input = 0}