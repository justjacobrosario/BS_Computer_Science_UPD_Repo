#include <stdio.h>

int main(){
    char lis[] = {'a', 'b', 'c'};
    char *plis = &lis[0];

    int x = 2;
    int *pX = &x;

    printf("%c\n", *plis);
    printf("%c\n", *(lis + 0));
    printf("%c\n", lis[0]);

}
