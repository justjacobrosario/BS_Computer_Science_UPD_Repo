#include <stdio.h>
#include <stdint.h>


int main(){
    int lis[] = {1, 2, 3, 4}; // implicit length
    int lis2[4] = {2, 4, 6, 8}; // explicit length
    int lis5[8];
    for (int i = 0; i<4;i++){
        lis[1] = 10; // mutable but no append method
        printf("%d\n", lis5[i]);
    }
}