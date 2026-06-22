#include <stdio.h>

/*
int* prefix_sums(int seq[]){
    int res[]
}
    */


int main(){
    
    int seq[] = {1, 2, 3};

    int *pseq = &seq[0];
    int dummy = 0;

    int *len = (void *)(&seq[0]);

    printf("%d", &seq[0]);
    



    return 0;
}