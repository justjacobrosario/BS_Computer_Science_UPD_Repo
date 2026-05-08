#include <stdio.h>

int main(){
    char lis[] = {'a', 'b', 'c'};
    char *pfirst = &lis[0]; // &lis[n]
    char *pfirst2 = lis + 0; // lis + n

    printf("%c\n", *pfirst);
    printf("%c\n", *pfirst2);
}
