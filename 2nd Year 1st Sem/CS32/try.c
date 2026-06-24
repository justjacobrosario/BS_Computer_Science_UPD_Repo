#include <stdio.h>
#include <stdlib.h>


typedef struct DynamicArray{
    int size;
    int cap;
    int *arr;
} DynamicArray;

DynamicArray *make_as_dynamic_arr(int *arr){
    DynamicArray *d_arr = malloc(sizeof(DynamicArray));
    (*d_arr).size = 0;
    (*d_arr).cap = 1;
    (*d_arr).arr = malloc((*d_arr).cap * sizeof(int));

    return d_arr;

}

void append(DynamicArray *d_arr, int val){
    if ((*d_arr).size = (*d_arr).cap){

        (*d_arr).size++;
        (*d_arr).cap++;

        int *temp_arr = malloc(((*d_arr).size++) * sizeof(int));

        int i = 0;
        while (i < ((*d_arr).size - 1)){
            temp_arr[i] = (*d_arr).arr[i];
            i++;
        }

        temp_arr[((*d_arr).size - 1)] = val;
        free((*d_arr).arr);
        (*d_arr).arr = temp_arr;
        free(temp_arr);

    }
}

int main(){

    int *try_d_arr;



    int size = 














    return 0;
}