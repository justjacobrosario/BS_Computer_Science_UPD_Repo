---
field: algorithms
problem type: function problem
data structure: grid
---



## Python Implementation

```python
grid = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]

def prefix_sum_grid(grid):
	pref_sum = [[0]*(len(grid)+1) for _ in range(len(grid)+1)]
	
	print(pref_sum)
	for r in range(1, len(grid)+1):

		for c in range(1, len(grid[0])+1):
			pref_sum[r][c] = 
			grid[r-1][c-1] + 
			pref_sum[r-1][c] + 
			pref_sum[r][c-1] - 
			pref_sum[r-1][c-1]


	return pref_sum

print(grid)

print(prefix_sum_grid(grid))

'''
[
[0, 0,  0,  0], 
[0, 1,  3,  6], 
[0, 5,  12, 21], 
[0, 12, 27, 45]]

'''

```