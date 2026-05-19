module Prac exposing (..)
import Dict exposing (Dict)
import Array exposing (..)

my_sum : List Int -> Int
my_sum lst =
    let
        my_add next prev =
            next + prev
    in
        List.foldl my_add 0 lst


isPrime : Int -> Bool
isPrime n =
    if n < 2 then True
    else
        let
            possible_multiples = List.range 2 (n-1)
            divisors = List.filter (\x -> (modBy x n) == 0) possible_multiples
        in
            List.length divisors == 0


compositeBetween: Int -> Int -> List Int
compositeBetween f l =
    let
        candidates = List.range f l
        composites = List.filter (\cand -> isPrime cand == False) candidates
    in
        composites


---

swap : List ( String, List Int ) -> List ( Float, String )
swap studs =
    List.map (\(name, scores) -> ((toFloat (List.sum scores) / toFloat (List.length scores)), name)) studs


rankStudents : List ( String, List Int ) -> List String
rankStudents class =
    let
        sorted = List.sort (swap class)
        res = List.map (\ (ave, name) -> name) sorted
    in
        res

---


isAllowedVehicle: String -> Int -> Bool
isAllowedVehicle day n =
    case (String.toLower day) of
        "monday" ->
            case (modBy 10 n) of
                1 -> False
                2 -> False
                _ -> True
        "tuesday" ->
            case (modBy n 10) of
                3 -> False
                4 -> False
                _ -> True
        "wednesday" ->
            case (modBy n 10) of
                5 -> False
                6 -> False
                _ -> True
        "thursday" ->
            case (modBy n 10) of
                7 -> False
                8 -> False
                _ -> True
        "friday" ->
            case (modBy n 10) of
                9 -> False
                0 -> False
                _ -> True 
        _ -> False

---

compress : List a -> List a
compress lis =
    let
        compressBetween next prev =
            let
                arr = Array.fromList prev
                length = Array.length arr
                last = (Array.slice (length-1) length arr)
                new_lis =
                    if (last == (Array.fromList [next])) then Array.toList arr
                    else List.append (Array.toList arr) [next]
            in
                new_lis

    in
        List.foldl compressBetween [] lis


compress2 : List a -> List a
compress2 listahan =
    let
        helper next (prev, res) =
            case prev of
                Nothing ->
                    (Just next, [next])
                Just p ->
                    if (p == next) then (prev, res)
                    else (Just next, next :: res)

    in
        Tuple.second (List.foldr helper (Nothing, []) listahan)


 

---

insertAt : Int -> a -> List a -> List a
insertAt idx elem lst =
    if (idx < 0) then lst
    else if (idx >= (List.length lst)) then lst
    else
        let
            l = List.length lst
            helpa curr (curr_idx, res) =
                if ((curr_idx == (l-1)) && (curr_idx == idx)) then 
                    (curr_idx, List.append res (List.append [elem] [curr])) 
                else
                    if (curr_idx == idx) then
                        (curr_idx + 1, List.append res (List.append [elem] [curr]))
                    else
                        (curr_idx + 1, List.append res [curr])

        in
            Tuple.second (List.foldl helpa (0, []) lst)