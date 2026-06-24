#include <stdio.h>
#include <stdlib.h>


typedef struct DynamicArray{
    int size;
    int cap;
    int *arr;
} DynamicArray;

DynamicArray *make_as_dynamic_arr(){
    DynamicArray *d_arr = malloc(sizeof(DynamicArray));
    (*d_arr).size = 0;
    (*d_arr).cap = 1;
    (*d_arr).arr = malloc((*d_arr).cap * sizeof(int));

    return d_arr;

}

int main(){

    DynamicArray *try_d_arr = make_as_dynamic_arr();
    (*try_d_arr).arr[0] = 1;
    printf("%d", try_d_arr[0]);















    return 0;
}