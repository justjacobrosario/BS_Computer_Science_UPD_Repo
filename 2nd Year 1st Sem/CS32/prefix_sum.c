#include <stdio.h>

#define LEN(x) (sizeof(x) / sizeof(x[0]))


int* prefix_sums(int seq[]){
    int len = sizeof(seq) / sizeof(seq[0]);
    int* res = (int*)malloc(len * sizeof(int));

    if (res == NULL){
        return NULL;
    }

    for (int i = 0; i < len; i++){
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
        
    }
    printf("%ld", LEN(seq));


    return 0;
}