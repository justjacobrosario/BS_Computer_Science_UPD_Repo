module Test_drive exposing (..)
import Array

gridder : Int -> Int -> Array.Array number
gridder r c =
    let
        x = Array.fromList [1, 2, 3]
        grid = List.repeat r (List.range 1 c)
    in
        x


evenOnly : List Int -> List Int
evenOnly list=
    let
        new_list = List.filter (\a -> (modBy 2 a) == 0) list
    in
        new_list


squareEach: List Int -> List Int
squareEach given_list =
    let 
        squared = List.map (\x -> x^2) given_list
    in
        squared

filterDivisibleBy: List Int -> Int -> List Int
filterDivisibleBy given_list n =
    let
        div_by_n = List.filter (\x -> (modBy n x) == 0) given_list
    in
        div_by_n
