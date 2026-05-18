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

swap : List ( String, List Int ) -> List ( Int, String )
swap studs =
    let
        new = List.map (\(name, scores) -> (Maybe.withDefault 0 ((List.sum scores) / (List.length scores))), name ) studs
    in
        new

