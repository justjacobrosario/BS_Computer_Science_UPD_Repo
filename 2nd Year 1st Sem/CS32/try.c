#include <stdio.h>
#include <stdlib.h>

typedef struct DynamicArray{
    int size;
    int cap;
    int *p_arr;
} DynamicArray;

DynamicArray *make_da(){
    DynamicArray *d_arr = malloc(sizeof(DynamicArray));
    (*d_arr).size = 0;
    (*d_arr).cap = 1;
    (*d_arr).p_arr = malloc(sizeof(int) * (*d_arr).cap);

    return d_arr;

}

void append_da(DynamicArray *d_arr, int val){
    int val_idx = (*d_arr).size; 
    (*d_arr).size++; // new size

    if ((*d_arr).size <= (*d_arr).cap){
        (*d_arr).p_arr[val_idx] = val;
    }
    else{
        (*d_arr).cap = (*d_arr).cap * 2;
        
        int *new_arr = malloc(sizeof(int) * (*d_arr).cap); // make new_arr with double the size
        for (int i = 0 ; i < ((*d_arr).size - 1); i++){ // copy values of prev arr per index
            new_arr[i] = (*d_arr).p_arr[i];
        } 
        new_arr[val_idx] = val;
        (*d_arr).p_arr = new_arr;
    }

}

void pop_da(DynamicArray *d_arr, int idx){
    if (idx <= ((*d_arr).size)){ // within bounds
        (*d_arr).size--; // only process popping if within bounds

        if (idx < ((*d_arr).size)){
            for (int i = idx; i < (*d_arr).size; i++){
                (*d_arr).p_arr[i] = (*d_arr).p_arr[i+1]; 
            }
        }

    }

}

void set_da(DynamicArray *d_arr, int idx, int val){
    printf("prompt: idx = %d, size = %d",  idx, (*d_arr).size);
    int size = (*d_arr).size;
    if (idx <= size){
        if (idx == size){ // basically appending on the last part
            append_da(d_arr, val);
        }
        else{ // adding a new value before the last element

            if (size+1 <= (*d_arr).cap){ // if new size is within the cap
                for (int i = size; i > idx; i--){ // shift values at the right of the chosen idx rightwards
                    (*d_arr).p_arr[i] = (*d_arr).p_arr[i-1];
                }
                (*d_arr).p_arr[idx] = val; // set the val to the idx-th element
                (*d_arr).size++; // increase the sie after adding the new val
            }
            else{
                (*d_arr).cap = (*d_arr).cap * 2;
                int *temp_arr = malloc(sizeof(int) * (*d_arr).cap);
                // assign the values before the idxth element
                for (int j = 0; j < idx; j++){
                    temp_arr[j] = (*d_arr).p_arr[j];
                }
                // assign the val to the idxth element
                temp_arr[idx] = val;
                // assign the remaining values after the idxth element
                for (int k = idx + 1; k <= size; k++){
                    temp_arr[k] = (*d_arr).p_arr[k-1];
                }
            }
            

        }

        
    }
// a, b, c, d, e
}




int main() {
    DynamicArray *sample_da = make_da();
    append_da(sample_da, 0);
    append_da(sample_da, 1);
    append_da(sample_da, 2);
    append_da(sample_da, 3);
    append_da(sample_da, 4);
    
    printf("size : %d, cap : %d\n", (*sample_da).size, (*sample_da).cap);
    int size = (*sample_da).size;
    printf("\narray: ");
    for (int i = 0; i < size; i++){
        printf("%d", (*sample_da).p_arr[i]);
    }
    printf("\n");

    set_da(sample_da, 3, 8);
    set_da(sample_da, 3, 8);
    set_da(sample_da, 3, 8);
    set_da(sample_da, 3, 8);

    size = (*sample_da).size;
    printf("\narray: ");
    for (int i = 0; i < size; i++){
        printf("%d", (*sample_da).p_arr[i]);
    }
    printf("\n");
    printf("size : %d, cap : %d\n", (*sample_da).size, (*sample_da).cap);
}