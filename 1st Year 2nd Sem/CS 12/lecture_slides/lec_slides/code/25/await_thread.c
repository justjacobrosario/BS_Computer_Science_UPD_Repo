#include <stdio.h>    // How does `pthread_join`
#include <stdlib.h>   // affect the output?
#include <pthread.h>
 
int global = 100;
 
void *fn(void *arg) {
  int *p = arg;
 
  printf("Thread got %d\n", *p);
  //pthread_join();
  global++;
  *p = *p + 1;
 
  return NULL;
}
 
int main() {
  int n = 12;
  pthread_t t1;
 
  pthread_create(&t1, NULL, fn, &n);
  pthread_join(t1, NULL);
 
  printf("n: %d\n", n);
  printf("global: %d\n", global);
}