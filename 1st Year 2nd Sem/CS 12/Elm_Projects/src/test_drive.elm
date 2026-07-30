module Test_drive exposing (..)
import Dict exposing (Dict)

my_sum : List Int -> Int
my_sum lst =
    let
        my_add next prev =
            next + prev
    in
        List.foldl my_add 0 lst




removeAt : Int -> List comparable -> List comparable
removeAt i lst =
    let
        helper n (idx, res) =
            if idx == i then
                (idx - 1, res)
            else
                (idx + 1, n :: res)

    in
    if i < 0 then
        lst
    else if i >= List.length lst then
        lst
    else
        lst
            |> List.foldl helper (0, [])
            |> Tuple.second
            |> List.reverse






insertAt : Int -> comparable -> List comparable -> List comparable
insertAt i x lst =
    let
        helper n (idx, res) =
            if idx == i then
                (idx + 1, n :: x :: res)
            else
                (idx + 1, n :: res)
            

    in
    if i < 0 then
        lst
    else if i >= List.length lst then
        lst
    else
        lst
            |> List.foldl helper (0, [])
            |> Tuple.second
            |> List.reverse




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





-- ---------------------------



type Genre
    = Pop
    | Rock
    | Electronic
    | Other

type alias Track =
    { title : String
    , artist : String
    , genre : Genre
    , year : Int
    }

songsData : String                      -- TSV String (note that this can be changed)
songsData =
    "Genre\tTitle\tArtist\tYear\nPop\tPeaches\tJustin Bieber\t2021\nPop\tHold On\tJustin Bieber\t2021\nRock\tDreams\tFleetwood Mac\t1977\nPop\tGhost\tJustin Bieber\t2021\nElectronic\tMidnight City\tM83\t2011\nPop\tStay\tThe Kid LAROI\t2021\nPop\tDrivers License\tOlivia Rodrigo\t2021\nPop\tGood 4 U\tOlivia Rodrigo\t2021\nPop\tDeja Vu\tOlivia Rodrigo\t2021\nPop\tVampire\tOlivia Rodrigo\t2023"



stringToGenre : String -> Genre         -- converts a Genre String to a Tag Union
stringToGenre str =
    case str of
        "Pop" -> Pop
        "Rock" -> Rock
        "Electronic" -> Electronic
        _ -> Other



parseRow : String -> Track              -- helper function for parsing a single row of the TSV string to a Track entry
parseRow row =
    case String.split "\t" row of
        [ songGenre, songTitle, songArtist, songYear ] ->
            { title = songTitle
            , artist = songArtist
            , genre = stringToGenre songGenre
            , year = Maybe.withDefault 0 (String.toInt songYear)
            }

        _ ->
            { title = "Unknown", artist = "Unknown", genre = Other, year = 0 }


parseTSV : String -> List Track         -- parses the TSV string
parseTSV data =
    data
        |> String.split "\n"
        |> List.drop 1 -- Remove the header row
        |> List.map parseRow

countAtYear : List Track -> String -> Int
countAtYear lst yr_str =
    let
        yr_int = Maybe.withDefault 0 (String.toInt yr_str)
        new_lst = List.filter (\x -> (x.year) == yr_int) lst
    in
        List.length new_lst


-- ----------------------------



popSongs : List Track -> List String
popSongs lst =
    let
        just_pop = List.filter (\x -> x.genre == Pop) lst
        titles = List.map (\x -> x.title) just_pop
    in
        titles


-- --------------------------------

artistTracks : List Track -> String -> List Track
artistTracks tracks artistName =
    let
        isTargetArtist track =
            track.artist == artistName
    in
    List.filter (\x -> isTargetArtist x ) tracks

-- Fill in the blanks to complete the songsOfArtists function that uses the artistTrack helper function
songsOfArtists : List Track -> List String -> List String
songsOfArtists tracks artists =
    let
        accumulateTitles artistName currentTitles =
            let
                -- insert lines of code to get all track records of an artist
                foundTracks =
                    artistTracks tracks artistName

                -- extract the titles from those tracks
                foundTitles =
                    List.map .title foundTracks
            in
            -- combine the newly found titles with the previously found titles
            currentTitles ++ foundTitles
    in
    -- start with an empty list and accumulate all titles by going through each of the artist names
    List.foldl accumulateTitles [] artists



-- ---------------------------------------------------

sortedSongsOfArtist : List Track -> String -> List(String, Int)
sortedSongsOfArtist tracks artistName =
    let
        theirTracks = List.filter (\a -> a.artist == artistName) tracks
        dateTitle = List.map (\b -> (-b.year, b.title)) theirTracks
        sortedd = 
            dateTitle
                |> List.sort
                |> List.map (\(negYear, title) -> ( title, -negYear ))
    in
    sortedd