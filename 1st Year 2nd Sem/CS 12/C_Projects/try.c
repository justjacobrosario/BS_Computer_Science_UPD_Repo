#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>
#include <stdlib.h>
 
void *make_contiguous_matrix(int rows, int cols, int element_size) {
  return calloc(rows * cols, element_size);
}
 
int main() {
  int (*matrix)[5] = make_contiguous_matrix(3, 5, sizeof(int));
 
  for (int r = 0; r < 3; r++) {
    printf("\nmatrix[%d] = %p (%p)\n", r, matrix[r], &matrix[r]);
    for (int c = 0; c < 5; c++) {
      printf("matrix[%d][%d] = %d (%p)\n", r, c, matrix[r][c], &matrix[r][c]);
    }
  }
}