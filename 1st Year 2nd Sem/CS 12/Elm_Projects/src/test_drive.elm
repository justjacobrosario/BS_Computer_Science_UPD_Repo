module Test_drive exposing (..)
import Array

gridder : Int -> Int -> Array.Array number
gridder r c =
    let
        x = Array.fromList [1, 2, 3]
        grid = List.repeat r (List.range 1 c)
    in
        x