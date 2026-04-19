module Test_drive exposing (..)


insertAt : Int -> comparable -> List comparable -> List comparable
insertAt i x lst =
    let
        helper n (idx, res) =
            if idx == i then
                (i, x :: n :: res)
            else
                (idx + 1, n :: res)
            

    in
    if i < 0 then
        lst
    else if i >= List.length lst then
        lst
    else
        lst
            |> List.foldr helper (0, [])
            |> Tuple.second




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