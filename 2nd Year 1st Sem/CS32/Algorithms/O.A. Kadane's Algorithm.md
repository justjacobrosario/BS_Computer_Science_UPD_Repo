---
field: algorithms
problem type: optimization problem
data structure: array
---


## Pseudocode

to be noted
## Python Implementation
```python

def kadanes(arr):
	best = arr[0]
	curr = arr[0]

	for i in range(1, len(arr)):
		curr = max(curr + arr[i], arr[i])
		best = max(curr, best)
		

	return best


```