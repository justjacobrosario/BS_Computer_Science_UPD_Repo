#include <stdio.h>

/*
int* prefix_sums(int seq[]){
    int res[]
}
    */


int main(){
    
    int seq[] = {1, 2, 3};

    int *pseq = &seq[];
    int dummy = 0;

    int len = *pseq;

    printf("%d", len);
    



    return 0;
}