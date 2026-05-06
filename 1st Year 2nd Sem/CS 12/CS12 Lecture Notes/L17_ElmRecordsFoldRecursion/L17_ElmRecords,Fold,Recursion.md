---
year: 1
subject: CS12
field: programming
---

# 1: Records 


## 1. Fold
: Abstraction of for-each aggregation pattern
: aka reduce, accumulate, aggregate
: basically a function runs an initial value and the first element of a list, then the function runs again the returned value to the next element, and so on

: imagine a function measuring thickness is like folding a paper from the initial fold up to the last fold, where each fold accumulates the thickness value until it returns the final thickness

## 2. Fold in Python

```python
# REDUCER as the function to be run for every iteration
def fold(REDUCER, STARTING_VALUE, elems):
	result = STARTING_VALUE

	for elem in elems:
		result = REDUCER(elem, result)
	
	return result
	
'''
fold(func, init_val, _list)

func(1st_elem, init_val) -> res # initial_val ALWAYS 2nd arg
func(2nd_elem, res) -> res
...
func(res, ..._elem, res) -> res (final)

its like func(func(func(init_val, 1st_elem), 2nd_elem)), ..._elem)
'''
```

## 3. Fold in Elm

### 1) `List.foldl : (a -> b -> b) -> b -> List a -> b`

: basically `List.foldl reducer init_val _list -> final_result`
: folds from leftmost element to rightmost element starting from the initial value
: init_val is also called as the "identity"
	 e.g. the identity  for sum is 0, for product is 1, for append is []
	 

```elm
my_sum : List Int -> Int
my_sum lst =
    let
        my_add next prev =
            next + prev
    in
        List.foldl my_add 0 lst -- my_add is reducer, 0 is init_val, lst is the list of elems

{-
lst = [1, 2, 3, 4]
List.foldl my_add 0 lst

my_add next prev
my_add 1 0 -> 1
my_add 2 1 -> 3
my_add 3 3 -> 6
	my_add 4 6 -> 10

-}

```


### 2) `List.foldr : (a -> b -> b) -> b -> List a -> b`

: like `List.foldl` but it is from rightmost element to leftmost element starting from the initial value

### 3) Intermediate State


# 2: Folds
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
