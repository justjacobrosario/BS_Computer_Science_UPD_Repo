#include <stdio.h>    // What is the output when
#include <stdlib.h>   // executed on a machine with
#include <pthread.h>  // a multicore processor?
 
int global = 100;  // Global variables are shared
                   // between all threads
void *fn(void *arg) {
  int *p = arg;
 
  printf("Thread got %d\n", *p);
  global++;
  *p = *p + 1;
 
  return NULL;
}
 
int main() {
  int n = 12;
  pthread_t t1;
 
  pthread_create(&t1, NULL, fn, &n);
 
  printf("n: %d\n", n);
  printf("global: %d\n", global);
}