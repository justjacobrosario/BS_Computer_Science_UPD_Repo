#include <stdio.h>
#include <stdlib.h>
 
void **make_noncontiguous_matrix(int rows, int cols, int element_size) {
  void **p = calloc(rows, sizeof(void *));
 
  for (int i = 0; i < rows; i++) {
    p[i] = calloc(cols, element_size);
  }
 
  return p;
}
 
int main() {
  int **matrix = (int **) make_noncontiguous_matrix(3, 5, sizeof(int));
 
  for (int r = 0; r < 3; r++) {
    printf("\nmatrix[%d] = %p (%p)\n", r, matrix[r], &matrix[r]);
    for (int c = 0; c < 5; c++) {
      printf("matrix[%d][%d] = %d (%p)\n", r, c, matrix[r][c], &matrix[r][c]);
    }
  }
}