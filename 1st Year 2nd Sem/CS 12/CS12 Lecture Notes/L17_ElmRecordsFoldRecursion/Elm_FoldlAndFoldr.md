

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
func(init_val, 1st_elem) -> res
func(res, 2nd_elem) -> res
func(res, ..._elem) -> res (final)

its like func(func(func(init_val, 1st_elem), 2nd_elem)), ..._elem)
'''
```


