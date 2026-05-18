module Prac exposing (..)
import Dict exposing (Dict)

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
            case (modby n 10) of
                1 -> False
                2 -> False
                _ -> True
        "tuesday" ->
            case (modby n 10) of
                3 -> False
                4 -> False
                _ -> True
        "wednesday" ->
            case (modby n 10) of
                5 -> False
                6 -> False
                _ -> True
        "thursday" ->
            case (modby n 10) of
                7 -> False
                8 -> False
                _ -> True
        "friday" ->
            case (modby n 10) of
                9 -> False
                0 -> False
                _ -> True 
        _ -> False


