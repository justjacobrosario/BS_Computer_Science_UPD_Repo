
row = 20
col = 20

grid = list(list("." for _ in range(col)) for _ in range(row))



def display(grid: Iteration[Iteration[str]]):
	for row in grid:
		line:str = ""

		for cell in row:
			line += cell
		print(line)
	print()

def manhattan(grid: Iteration[Iteration[str]], strength:int, i:int, j:int):
	row = len(grid)
	col = len(grid[0])

	for r in range(row):
		for c in range(col):
			if abs(i - r) + abs(j - c) <= strength:
				grid[r][c] = "#"

def hollow_manhattan(grid: Iteration[Iteration[str]], strength:int, i:int, j:int):
	row = len(grid)
	col = len(grid[0])

	for r in range(row):
		for c in range(col):
			if abs(i - r) + abs(j - c) == strength:
				grid[r][c] = "#"

def euclidean(grid: Iteration[Iteration[str]], strength:int, i:int, j:int):
	row = len(grid)
	col = len(grid[0])

	for r in range(row):
		for c in range(col):
			if ((i - r)**2 + (j -c)**2)**(1/2) <= strength:
				grid[r][c] = "#"


display(grid)
chebyshev(grid, 1, 10, 10)
display(grid)