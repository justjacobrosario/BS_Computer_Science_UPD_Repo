module Gridder exposing (..)

gridder : Int -> Int -> List (List Int)
gridder r c =
	let
		grid = List.repeat r (List.range 1 c)
	in
		grid