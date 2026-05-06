#include <stdio.h>

char msg[] = {69, 69, 89, 0};
char yes[] = {'a', 'b', 'c', 'd'};


void foo(char *lis, int n){
    for (int i = 0; i < n; i++){
        printf("%c", lis[i]);
    }
}

int main(){
    foo(yes, 4);
}
