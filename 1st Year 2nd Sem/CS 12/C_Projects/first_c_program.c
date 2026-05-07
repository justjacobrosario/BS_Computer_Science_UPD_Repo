#include <stdio.h>
#include <stdint.h>


#define N 100
int16_t x_16_bit = 123456789;
int32_t y_32_bit = 123456789;


int main(){

    int32_t widen_x = x_16_bit;
    int16_t narrowed_y = y_32_bit;
    printf("x: %d\n", widen_x); 
    printf("y: %d", narrowed_y); 
}