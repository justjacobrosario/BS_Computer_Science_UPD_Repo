#include <stdio.h>
#include <stdlib.h>

void *make_2d_grid(int row, int col, int cell_size){
	int *matrix = calloc((row*col), sizeof(cell_size));
	return matrix;
}

int main() {
	int r = 2;
	int c = 3;
	int (*p)[c] = make_2d_grid(r, c, sizeof(int));

	for (int i = 0; i < r; i++ ){

		for (int j = 0; j < c; j++)
			printf("grid[%d][%d]: %d\n", i, j, p[i][j]);

	}



}