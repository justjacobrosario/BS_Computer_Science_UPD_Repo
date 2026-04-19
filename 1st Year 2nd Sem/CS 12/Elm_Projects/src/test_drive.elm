module Test_drive exposing (..)

compress : List comparable -> List comparable
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
                    (Just n, [n])
    in
    lst
        |> List.foldr upd (Nothing, [])
        |> Tuple.second