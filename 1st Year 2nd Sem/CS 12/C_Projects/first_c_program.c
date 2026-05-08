#include <stdio.h>

int main(){

    // declare variable to make a pointer later
    int n;

    // ask the length of array
    printf("%s", "How many elements: ");
    scanf("%d", &n);

    // then declare the array itself
    int arr[n] = {};

    // 
    for (int i = 0; i < n; i++){
        printf("%dth-element (ints onlyy muna): " , i);
        scanf("%d", &arr[i]);
    }

    // printing purposes
    for (int k = 0; k < n; k++){
        printf("ee");
        printf("%d", arr[k]);
    }
}