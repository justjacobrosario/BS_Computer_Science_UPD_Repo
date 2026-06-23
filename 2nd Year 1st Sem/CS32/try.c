#include <stdio.h>
#include <stdlib.h>

int main(){

    int lis[3] = {2, 2, 3};

    //printf("%d", *lis);


    int size = 3;
    int *arr = malloc(size * sizeof(int));

    arr[0] = 1;

    printf("%d", arr[1]);

    // lets try to change the size

    size = 10;
    int *arr = malloc(size * sizeof(int));

    printf("%d", arr[0]);
    














    return 0;
}