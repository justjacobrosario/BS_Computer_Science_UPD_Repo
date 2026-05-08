#include <stdio.h>

int main(){

    // declare variable to make a pointer later
    int n;

    // NOTICE: ask FIRST the length of array
    printf("%s", "How many elements: ");
    scanf("%d", &n);

    // NOTICE: then declare the array itself
    int arr[n] = {};

    // just counts from 0 to n-1 as elements
    for (int i = 0; i < n; i++){
        arr[i] = i;
    }

    // printing purposes
    for (int k = 0; k < n; k++){
        printf("%d\n", arr[k]);
    }
}