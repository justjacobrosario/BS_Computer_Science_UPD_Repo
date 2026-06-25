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

void append(DynamicArray *d_arr, int val){
    
    if ((*d_arr).size == (*d_arr).cap){
        (*d_arr).cap = (*d_arr).cap * 2; // multiply cap by 2 to not always malloc for every append
        int *temp_arr = malloc(((*d_arr).cap) * sizeof(int));

        int i = 0;
        while (i < ((*d_arr).size)){
            temp_arr[i] = (*d_arr).arr[i];
            i++;
        }

        temp_arr[((*d_arr).size)] = val;
        (*d_arr).size++;

        free((*d_arr).arr);
        (*d_arr).arr = temp_arr;
        free(temp_arr);
        printf("fahh");
    }

    else{
        (*d_arr).arr[(*d_arr).size] = val;
        (*d_arr).size++;
        
    }
}

void set(DynamicArray *d_arr, int idx, int val){

    if ((*d_arr).size + 1 >= (*d_arr).cap){
        (*d_arr).cap = (*d_arr).cap * 2;
    }


    (*d_arr).size++; // for the added value

    int *temp_d_arr = malloc((*d_arr).size * sizeof(int));

    int i = 0;
    while (i < idx){
        temp_d_arr[i] = (*d_arr).arr[i];
        i++;
    }

    temp_d_arr[i] = val;
    

    // notice that i is still = idx
    while (i < ((*d_arr).size - 1)){ // -1 bc we focus on the remaining elements (not including the new value)
        temp_d_arr[i + 1] = (*d_arr).arr[i]; // [i+1] bc we added the new value recently
        i++;
    }
    free((*d_arr).arr);
    (*d_arr).arr = temp_d_arr;
    free(temp_d_arr);


}


int main(){
    DynamicArray *try_d_arr = make_as_dynamic_arr();

    append(try_d_arr, 67);
    printf("size: %d, cap: %d\n", (*try_d_arr).size, (*try_d_arr).cap);
    append(try_d_arr, 420);
    printf("size: %d, cap: %d\n", (*try_d_arr).size, (*try_d_arr).cap);
    append(try_d_arr, 123); // why not work here
    printf("size: %d, cap: %d\n", (*try_d_arr).size, (*try_d_arr).cap);















    return 0;
}