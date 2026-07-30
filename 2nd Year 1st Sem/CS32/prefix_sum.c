#include <stdio.h>
#include <stdlib.h>

int main(){
    
    // STRUCT OF A DYNAMIC ARRAY
    typedef struct DynamicArray{
        int size;
        int cap;
        int* a;
    } DynamicArray;


    // INITIALIZING A DYNAMIC ARRAY
    DynamicArray *l = (DynamicArray*)malloc(sizeof(DynamicArray));
    (*l).size = 0;
    (*l).cap = 3;
    (*l).a = (int*)malloc((*l).cap * sizeof(int));


    // SETTING THEIR INDEX AS THEIR VALUES
    for (int i = 0; i < ((*l).cap); i++){
        (*l).a[i] = i;
        (*l).size++;
    }

    
    // --------


    int try[3] = {0, 1, 2};
    int i = 0;
    while (i < (*l).size){
        printf("%d", try[i]);
        i++;
    }

    printf("Donneeee");



    return 0;
}