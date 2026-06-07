#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
 
#define N 1000000000
 
struct thread_data {
  int n;
  int *nums;
  pthread_mutex_t *pos_lock;
  pthread_mutex_t *neg_lock;
  pthread_mutex_t *zero_lock;
};
 
int negative = 0, zero = 0, positive = 0;
 
void *f(void *arg) {
  struct thread_data *data = arg;
  int n = data->n;
  int *nums = data->nums;
  pthread_mutex_t *pos_lock = data->pos_lock;
  pthread_mutex_t *neg_lock = data->neg_lock;
  pthread_mutex_t *zero_lock = data->zero_lock;
 
  int chunk_size = N / 2;
  int start_idx = chunk_size * n;
  int stop_idx = start_idx + chunk_size;
 
  for (int i = start_idx; i < stop_idx; i++) {
    if (nums[i] < 0) {
      pthread_mutex_lock(neg_lock);
      negative++;
      pthread_mutex_unlock(neg_lock);
    } else if (nums[i] > 0) {
      pthread_mutex_lock(pos_lock);
      positive++;
      pthread_mutex_unlock(pos_lock);
    } else {
      pthread_mutex_lock(zero_lock);
      zero++;
      pthread_mutex_unlock(zero_lock);
    }
  }
 
  return NULL;
}
 
int main() {
  srand(12); // Makes RNG deterministic
 
  int *nums = malloc(N * sizeof(int));
 
  for (int i = 0; i < N; i++) {
    // [-1000, 1000]
    nums[i] = (rand() % 2001) - 1000;
  }
 
  printf("Done generating integers\n");
 
  struct timespec start, end;
  clock_gettime(CLOCK_MONOTONIC, &start);
 
  pthread_t t1, t2;
 
  pthread_mutex_t pos_lock, neg_lock, zero_lock;
  pthread_mutex_init(&pos_lock, NULL);
  pthread_mutex_init(&neg_lock, NULL);
  pthread_mutex_init(&zero_lock, NULL);
 
  struct thread_data d1 = {.n = 0,
                           .nums = nums,
                           .pos_lock = &pos_lock,
                           .neg_lock = &neg_lock,
                           .zero_lock = &zero_lock};
  struct thread_data d2 = {.n = 1,
                           .nums = nums,
                           .pos_lock = &pos_lock,
                           .neg_lock = &neg_lock,
                           .zero_lock = &zero_lock};
 
  pthread_create(&t1, NULL, f, &d1);
  pthread_create(&t2, NULL, f, &d2);
 
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
 
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