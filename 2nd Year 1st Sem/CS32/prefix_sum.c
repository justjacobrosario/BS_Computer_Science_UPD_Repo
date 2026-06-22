#include <stdio.h>

#define LEN(x) (sizeof(x) / sizeof(x[0]))


int* prefix_sums(int i, int j, int seq[]){
    int len = sizeof(seq) / sizeof(seq[0]);
    int res[len] = {};
}



int main(){
    
    int seq[] = {1, 2, 3};

    int len_seq = sizeof(seq) / sizeof(seq[0]);

    printf("%ld", LEN(seq));


    return 0;
}