#include <stdio.h>
#include <stdlib.h>

typedef struct DynamicArray {
    int cap;
    int size;
    int *arr;
} DynamicArray;

DynamicArray *make_darr(){
    DynamicArray *darr = malloc(sizeof(DynamicArray));
    (*darr).cap = 2;
    (*darr).size = 0;
    (*darr).arr = malloc((*darr).cap * sizeof(int));
}

void append_darr(DynamicArray *darr, int x){
    if ((*darr).cap >= ((*darr).size + 1)){
        (*darr).arr[(*darr).size] = x;
        (*darr).size++;
    }
    else{
        int new_cap = (*darr).cap * 2; // doubled it to reduce frequent arr duplication
        int *new_arr = malloc(new_cap * sizeof(int));

        for (int i = 0; i < (*darr).size; i++){ // duplicating
            new_arr[i] = (*darr).arr[i];
        }
        new_arr[(*darr).size] = x; // appending
        (*darr).size++;

        (*darr).arr = new_arr;
        (*darr).cap = new_cap; // update arr and cap


    }
}

void pop_arr(DynamicArray *darr){
    if ((*darr).size > 0){
        (*darr).size--;
    }
}

int main(){
    DynamicArray *d_arr = make_darr();
    
    int i = 0;
    for (int x = 0; x < 10; x++){
        if (x == 5){
            printf("popped\n");
            pop_arr(d_arr);
        }
        else{
            append_darr(d_arr, x);
        }
        

        printf("size: %d, cap: %d\n", (*d_arr).size,(*d_arr).cap);
        
        while ((*d_arr).size > i){
            printf("%d", (*d_arr).arr[i]);
            i++;
        }
        i = 0;
        printf("\n");
        printf("===\n");


    }




    return 0;
}