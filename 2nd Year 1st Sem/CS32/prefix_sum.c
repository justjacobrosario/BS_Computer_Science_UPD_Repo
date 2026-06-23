#include <stdio.h>
#include <stdlib.h>

int main(){
    
    typedef struct DynamicArray{
        int size;
        int cap;
        int* a;
    } DynamicArray;

    DynamicArray *l = (DynamicArray*)malloc(sizeof(DynamicArray));
    (*l).size = 0;
    (*l).cap = 3;
    (*l).a = (int*)malloc((*l).cap * sizeof(int));

    for (int i = 0; i < ((*l).cap); i++){
        (*l).a[i] = i;
    }

    
    // --------


    int try[3] = {0, 1, 2};
    int i = 0;
    while (i > (*l).size){
        printf("%d", try[i]);
        i ++;
    }


    printf("yes: %d", try[1]);
    printf("Donneeee");



    return 0;
}