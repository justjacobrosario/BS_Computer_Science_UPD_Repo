#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
#define N 1000000000
 
int main() {
  srand(12);  // Makes RNG deterministic
 
  int *nums = malloc(N * sizeof(int));
 
  for (int i = 0; i < N; i++) {
    // [-1000, 1000]; warning: slightly biased
    nums[i] = (rand() % 2001) - 1000;
  }
 
  printf("Done generating integers\n");
 
  struct timespec start, end;
  clock_gettime(CLOCK_MONOTONIC, &start);
 
  int negative = 0;
  int zero = 0;
  int positive = 0;
 
  for (int i = 0; i < N; i++) {
    if (nums[i] < 0) {
      negative++;
    } else if (nums[i] > 0) {
      positive++;
    } else {
      zero++;
    }
  }
 
  clock_gettime(CLOCK_MONOTONIC, &end);
  double elapsed =
      (end.tv_sec - start.tv_sec)
      + (end.tv_nsec - start.tv_nsec) / 1e9;
 
  printf("Elapsed: %.6f seconds\n", elapsed);
 
  printf("Positive: %d\n", positive);
  printf("Negative: %d\n", negative);
  printf("Zero: %d\n", zero);
 
  free(nums);
}