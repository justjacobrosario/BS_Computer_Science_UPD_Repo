#include <stdio.h>
#include <stdint.h>


#define N 100
int32_t x = 10;
int64_t y = 50;


int main(){
    //N--; errorr
    int64_t new_x = x;
    int32_t new_y = y;
    printf("x: %d\n", new_x); 
    printf("y: %d", new_y); 
}