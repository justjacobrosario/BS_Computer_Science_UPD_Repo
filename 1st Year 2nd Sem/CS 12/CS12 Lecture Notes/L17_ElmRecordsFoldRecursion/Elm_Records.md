## 1. Records 
: Collection of values with fixed key names (like dict but the keys are dynamic)

```elm
{ artist : "Eraserheads"
, genre : Pop -- more on this later
, title : "Huling el Bimbo"
}
```
: but how to make one? go to num 3

## 2. `type`
: Basically makes a new type with set of possible values
: like Python's enums

```elm
type Genre
	= Pop
	| Rock
	| Indie
	| Other
-- any Genre can be either a Pop, Rock, Indie, Other
```

## 3. `type alias`
: like Protocols for classes in Python but for making records
: declare a certain set of  key-value_type pair with its type name

### 1) Declaring a record type
```elm
type alias Track =
	{ artist : String
	, genre : Genre
	, title : String
	}
```

### 2) Extracting the value of a key in a record

`record_name = `

```elm
-- lets say we have this
x = { artist : "Eraserheads"
, genre : Pop -- more on this later
, title : "Huling el Bimbo"
}

-- we can get the value of a key by
xs_genre = x.genre
```

### 3) Updating the value of a key in a record

`{record_name | key = new_val}`

```elm
-- lets say we have this
x = { artist : "Eraserheads"
, genre : Pop -- more on this later
, title : "Huling el Bimbo"
}

new_x = {x | title = "Magasin"}
```