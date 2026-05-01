#include <stdio.h>
void print_square(int n){
    printf("%d\n", n*n); // n*n is seen as a single int, thats why only one %d
}

int main() {
    print_square(2);
}
