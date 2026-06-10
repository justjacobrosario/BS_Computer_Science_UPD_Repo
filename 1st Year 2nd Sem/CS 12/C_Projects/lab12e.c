#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>



#include "gollums_columns.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define GOLLUMS_COLUMNS_H

char **transpose(int r, int c, const char **grid){
	char **arr = malloc(c * sizeof(char *));
	for (int i = 0; i < c; i++){
		arr[i] = malloc((r+1) * sizeof(char));
	}

	for (int j = 0; j < c; j++){
		for (int k = 0; k < r; k++){
			arr[j][k] = grid[k][j];
		}
		arr[j][r] = '\0';

	}

	return arr;

}

int main(){
	const char *grid[] = {"mypre", "cious"};
    char **result = transpose(2, 5, grid);

    for (int i = 0; i < 5; i++){
        printf("%s\n", result[i]);
    }
}