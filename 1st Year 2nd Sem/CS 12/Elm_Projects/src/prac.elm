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
    let
        case (String.toLower day) of
            "monday" ->
                case n of
                    1 -> ans = False
                    2 -> ans = False
                    _ -> ans = True
            "tuesday" ->
                case n of
                    3 -> ans = False
                    4 -> ans = False
                    _ -> ans = True
            "wednesday" ->
                case n of
                    5 -> ans = False
                    6 -> ans = False
                    _ -> ans = True
            "thursday" ->
                case n of
                    7 -> ans = False
                    8 -> ans = False
                    _ -> ans = True
            "friday" ->
                case n of
                    9 -> ans = False
                    0 -> ans = False
                    _ -> ans = True 
    in
        ans

