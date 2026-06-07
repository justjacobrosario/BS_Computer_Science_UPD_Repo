module Main exposing (main)

import Html
import Array exposing (Array, slice, fromList)


double n =
    (*) n 2

factorial n =
    if n == 0 then
        1
    else
        n * (factorial (n - 1))

combination n k =
    let
        num = factorial n
        den = (factorial k) * (factorial (n - k))
    in
    num // den

zeroMatrix r c =
    -- List.repeat r (List.repeat c 0)
    List.repeat c 0
    |> List.repeat r

f r c =
    List.range 1 c
    |> List.repeat r

increment : Int -> Int
increment n = -- increment 10 == 11
    n + 1
x = [10, 20, 30]
y = List.map increment x -- [11,21,31]

main =
    let
        _ = Debug.log "" x 
        _ = Debug.log "" y
    in
    -- Ignore the line below
    Html.text ""