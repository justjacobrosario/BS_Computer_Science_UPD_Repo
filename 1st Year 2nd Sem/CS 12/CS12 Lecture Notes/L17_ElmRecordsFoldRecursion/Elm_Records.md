## 1. Records 
: Collection of values with fixed key names (like dict in syntax but the keys are dynamic, and like a class where the keys are the properties)

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
: has subvalues (keys)
: like Protocols for classes in Python but for making records
: declare a certain set of  key-value_type pair with its type name

### 1) Defining a record type
```elm
type alias Track =
	{ artist : String
	, genre : Genre
	, title : String
	}
```


### 2) Instantiating/creating a record

: Simply set the record following the order of keys and the value type specified

```elm
x = 
	{ artist : "Eraserheads"
	, genre : Pop
	, title : "Huling el Bimbo"
	}
```

### 3) Extracting the value of a key in a record

`value_of_key = record_name.key`

```elm
-- lets say we have this
x = { artist : "Eraserheads"
, genre : Pop
, title : "Huling el Bimbo"
}

-- we can get the value of a key by
xs_genre = x.genre
```

### 4) Updating the value of a key in a record

`{record_name | key = new_val}`

```elm
-- lets say we have this
x = { artist : "Eraserheads"
, genre : Pop
, title : "Huling el Bimbo"
}

new_x = {x | title = "Magasin"}
```