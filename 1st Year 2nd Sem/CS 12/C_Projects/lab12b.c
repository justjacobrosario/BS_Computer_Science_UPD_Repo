#include <stdio.h>


#include "operations_research_ii.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define OPERATIONS_RESEARCH_II_H

int num_good_subregions(int r, int c, int **region, int n, int s){
	int count = 0;

	for (int i = 0; i <= (r-n); i++){
		for (int j = 0; j <= (c-n); j++){

			int tot = 0;
			for (int row = (0+i); row < (i+n); row ++){
				for (int col = (0+j); col < (j+n); col ++){
					tot += region[row][col];
				}
			}

			if (tot <= s){
				count += 1;
			}


		}

	}


	
	return count;
}

int main(){
	int data[3][4] = {
    {3, 1, 4, 1},
    {5, 9, 2, 6},
    {5, 3, 5, 8}
	};
	int *matrix[3] = {data[0], data[1], data[2]};

	printf("%d",num_good_subregions(3, 4, matrix, 2, 21));
}