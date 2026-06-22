#include <stdio.h>

#define LEN(x) (sizeof(x) / sizeof(x[0]))

/*
int* prefix_sums(int seq[]){
    int res[]
}
    */


int main(){
    
    int seq[] = {1, 2, 3};

    int len_seq = sizeof(seq) / sizeof(seq[0]);

    printf("%d", LEN(seq[]));


    return 0;
}