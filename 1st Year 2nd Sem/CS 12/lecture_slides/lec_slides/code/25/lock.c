#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
 
int n = 0;
pthread_mutex_t lock;
 
void *plus(void *arg) {
  for (int i = 0; i < 10000; i++) {
    pthread_mutex_lock(&lock);
    n++;                          // Critical section
    pthread_mutex_unlock(&lock);
  }
 
  return NULL;
}
 
void *minus(void *arg) {
  for (int i = 0; i < 10000; i++) {
    pthread_mutex_lock(&lock);
    n--;                          // Critical section
    pthread_mutex_unlock(&lock);
  }
 
  return NULL;
}
 
int main() {
  pthread_t t1, t2;
  pthread_mutex_init(&lock, NULL);
 
  pthread_create(&t1, NULL, plus, NULL);
  pthread_create(&t2, NULL, minus, NULL);
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
 
  printf("n: %d\n", n);
}