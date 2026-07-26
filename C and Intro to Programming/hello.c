#include <stdio.h>
#include <stdlib.h>

void f(int n, int *arr){

    int res = 0;
    int j = 0;
    while (j < (n - 2)){
        if ((arr[j] < arr[j+1]) && (arr[j+1] > arr[j+2])){
            res++;
        }
        j++;
    }
    printf("%d", res);

}

int main(){
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i <n ; i++){
        scanf("%d", &arr[i]);
    }

    f(n, arr);

    return 0;
}


/*
LEARNINGS:

scanf stops every space, tabs and \n if format specifier is %d / %f / %s
scanf DONT skip space, tabs and \n if %c / %[^\n]

*/