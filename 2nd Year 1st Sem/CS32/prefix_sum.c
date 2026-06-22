#include <stdio.h>
#include <stdlib.h>

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
            res[i] = (seq[i] + res[i-1]);
        }
    }
    return res;
}

int sum_in_between(int pref[], int i, int j){
    return (pref[j] - pref[i-1]);
}



int main(){
    
    int seq[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int len_seq = sizeof(seq) / sizeof(seq[0]);
    int* sums = prefix_sums(seq, len_seq);

    int i = 3;
    int j = 5;

    printf("Sum from element %d to %d is %d", seq[i], seq[j], sum_in_between(sums, i, j));

    return 0;
}