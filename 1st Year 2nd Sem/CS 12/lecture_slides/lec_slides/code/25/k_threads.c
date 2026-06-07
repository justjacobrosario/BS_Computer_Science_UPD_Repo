#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
 
#define N 1000000000
#define K 8
 
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
 
  int chunk_size = N / K;
  int start_idx = chunk_size * n;
  int stop_idx = start_idx + chunk_size;
 
  int positive_local = 0;
  int negative_local = 0;
  int zero_local = 0;
 
  for (int i = start_idx; i < stop_idx; i++) {
    if (nums[i] < 0) {
      negative_local++;
    } else if (nums[i] > 0) {
      positive_local++;
    } else {
      zero_local++;
    }
  }
 
  pthread_mutex_lock(neg_lock);
  negative += negative_local;
  pthread_mutex_unlock(neg_lock);
 
  pthread_mutex_lock(pos_lock);
  positive += positive_local;
  pthread_mutex_unlock(pos_lock);
 
  pthread_mutex_lock(zero_lock);
  zero += zero_local;
  pthread_mutex_unlock(zero_lock);
 
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
 
  pthread_t thread[K];
  struct thread_data thread_data_arr[K];
 
  pthread_mutex_t pos_lock, neg_lock, zero_lock;
  pthread_mutex_init(&pos_lock, NULL);
  pthread_mutex_init(&neg_lock, NULL);
  pthread_mutex_init(&zero_lock, NULL);
 
  for (int i = 0; i < K; i++) {
    thread_data_arr[i] =
      (struct thread_data){.n = i,
                           .nums = nums,
                           .pos_lock = &pos_lock,
                           .neg_lock = &neg_lock,
                           .zero_lock = &zero_lock};
  }
 
  for (int i = 0; i < K; i++) {
    pthread_create(&thread[i], NULL, f, &thread_data_arr[i]);
  }
 
  for (int i = 0; i < K; i++) {
    pthread_join(thread[i], NULL);
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