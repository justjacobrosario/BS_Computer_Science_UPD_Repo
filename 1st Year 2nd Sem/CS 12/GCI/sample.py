import numpy as np


grid = np.array([
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]])

print(grid[0:2, 1])
print(grid[[0, 1], 1])

not_array = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(not_array[0:2][1])