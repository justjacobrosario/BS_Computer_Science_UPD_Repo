#include <stdio.h>
#include <stdlib.h>

#define LEN(x) (sizeof(x) / sizeof(x[0]))

int get_len(int seq[]){
    return (sizeof(seq) / sizeof(seq[0]));
}

int* prefix_sums(int seq[], int size){
    int* res = (int*)malloc(size * sizeof(int));

    if (res == NULL){
        return NULL;
    }

    for (int i = 0; i < size; i++){
        if (i == 0){
            res[0] = seq[0];
        }
        else{
            res[i] = (seq[i] + seq[i-1]);
        }
    }

    return res;
}



int main(){
    
    int seq[] = {1, 2, 3};

    int len_seq = sizeof(seq) / sizeof(seq[0]);

    for (int i = 0; i < len_seq; i++){
        printf("%d", seq[i]);
    }



    return 0;
}