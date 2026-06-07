#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
 
int n = 0;
 
void *plus(void *arg) {
  for (int i = 0; i < 10000; i++) {
    n++; // not an atomic operation
  }
 
  return NULL;
}
 
void *minus(void *arg) {
  for (int i = 0; i < 10000; i++) {
    n--; // not an atomic operation
  }
 
  return NULL;
}
 
int main() {
  pthread_t t1, t2;
 
  pthread_create(&t1, NULL, plus, NULL);
  pthread_create(&t2, NULL, minus, NULL);
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
 
  printf("n: %d\n", n);
}