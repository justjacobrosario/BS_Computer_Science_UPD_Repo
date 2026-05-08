#include <stdio.h>

int main(){
    int n;
    printf("%c", "How many elements: ");
    scanf("%d", &n);
    int arr[n] = {};

    for (int i = 0; i < n; i++){
        arr[i] = i;
    }

    for (int k = 0; k < n; k++){
        printf("%d", arr[k]);
    }
}