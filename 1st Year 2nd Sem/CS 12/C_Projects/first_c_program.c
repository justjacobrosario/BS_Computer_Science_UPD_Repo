#include <stdio.h>

int main(){
    char str1[] = "Hello x";
    char str2[] = {'H', 'e', 'l', 'l', 'o', ' ', 'x', '\0'};
    char str3[] = {72,101,108,108,111,32,88,0};

    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);

}
