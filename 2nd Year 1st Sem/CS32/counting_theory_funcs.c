#include <stdio.h>
#include <stdlib.h>
#define LEN(arr) (sizeof(arr) / sizeof(arr[0]))

int factorial(int n){
    if (n==0){
        return 1;
    }
    else{
        int res = 1;
        while (n > 0){
            res = res * n;
            n--;
        }
        return res;
    }
}


void *pop(int *arr, int *new, int arr_size, int idx){
    printf("param size: %d\n", arr_size);
    if (idx < arr_size){
        for (int i = 0; i < idx ; i++){
            //printf("looped: %d\n", arr[i]);
            new[i] = arr[i];
        }
        for (int j = idx + 1; j < arr_size ; j++){
            new[j-1] = arr[j];
            //printf("looped: %d\n", arr[j]);
        }

    }
    

}


int *permutation(int *arr){
    int arr_size = LEN(arr); 

    if (arr_size <= 1){
        return arr;
    }
    else{
        int *perm_arr = malloc(factorial(arr_size) * sizeof(int));

        for (int i = 0; i < arr_size; i++){
            int curr = arr[i];
            int remaining[arr_size - 1];
            pop(arr, remaining, arr_size, i);

        }
    }


}


int main(){
    int try[5] = {1, 2, 3, 4, 5};
    int size = LEN(try);
    int new[4];
    pop(try, new, size, 2);
    

    
    //printf("size: %d\n", size);
    for (int i = 0; i < 4; i++){
        printf("%d\n", new[i]);
    }

    


    return 0;
}