module Test_drive exposing (..)


insertAt : Int -> comparable -> List comparable -> List comparable
insertAt i x lst =
    let
        helper n (idx, new, elm_i, res) =
            if elm_i == idx then
                (idx, new, elm_i, n :: res)
            else
                (idx, new, elm_i + 1, res)

    in
    if i < 0 then
        lst
    else if i >= List.length lst then
        lst
    else
        lst
            |> List.foldl helper (i, x, 0, [])



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