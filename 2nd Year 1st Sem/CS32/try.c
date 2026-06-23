#include <stdio.h>
#include <stdlib.h>

int main(){

    int lis[3] = {2, 2, 3};

    //printf("%d", *lis);


    int size = 3;
    int *arr = malloc(size * sizeof(int));

    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;

    printf("%d\n", arr[1]);

    // lets try to change the size and copying the values of each element

    free(arr); // this frees up the memory of the previous arr array

    size = 10;
    int *temp_arr = malloc(size * sizeof(int));
    temp_arr[0] = 1;
    temp_arr[1] = 2;
    temp_arr[2] = 3;

    arr = temp_arr;
    free(temp_arr);

    printf("%d\n", arr[0]);
    














    return 0;
}