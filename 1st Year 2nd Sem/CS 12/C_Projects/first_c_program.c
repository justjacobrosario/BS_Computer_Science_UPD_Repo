#include <stdio.h>

void increm_each(int *pList, int n) {
    for (int i = 0; i < n; i ++){
        pList[i]++;
    }
}

int main(){
    int lis[] = {1, 2, 3};
    increm_each(lis, 3);
    for (int k = 0; k < 3; k++){
        printf("%d\n", lis[k]);
    }
}