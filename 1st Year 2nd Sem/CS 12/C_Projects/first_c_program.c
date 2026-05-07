#include <stdio.h>
#include <stdint.h>


#define N 100
int16_t x = 123456789;
int32_t y = 123456789;


int main(){
    //N--; errorr
    int32_t new_x = x;
    int16_t new_y = y;
    printf("x: %d\n", new_x); 
    printf("y: %d", new_y); 
}