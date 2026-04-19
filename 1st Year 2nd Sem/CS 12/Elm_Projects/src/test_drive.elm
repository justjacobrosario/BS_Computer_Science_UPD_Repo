module Test_drive exposing (..)
import Array

compress : List String -> List String
compress lst =
    let
        upd n (prev, res) =
            case prev of
                Just p ->
                    if p == n then
                        (prev, res)
                    else
                        (Just n, n :: res)
                Nothing ->
                    (n, [n])
    in
        (List.foldl upd (Nothing, []) lst)
