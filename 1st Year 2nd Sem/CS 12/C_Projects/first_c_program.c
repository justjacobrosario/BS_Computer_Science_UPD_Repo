#include <stdio.h>

int get_pointer_of_leftmost_one(int *pArr, int n){
    for (int i = 0; i<n;i++){
        if (pArr[i]) == 1{
            return &pArr[i];
        }
    return NULL;

    }
}

int main(){
    int arr[] = {0, 0, 0, 1, 0};
    printf("%d", get_pointer_of_leftmost_one(arr, 5));


}