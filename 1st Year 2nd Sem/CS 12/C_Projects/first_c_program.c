#include <stdio.h>
void print_square(int n){
    printf("%d\n", n*n); // n*n is seen as a single int, thats why only one %d
    // i addded \n to just make a new line for aesthetics
}

int main() {
    print_square(2);
}
