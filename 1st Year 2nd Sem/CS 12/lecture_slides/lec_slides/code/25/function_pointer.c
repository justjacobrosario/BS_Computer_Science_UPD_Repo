#include <stdio.h>

int add(int a, int b) { return a + b; }

int main() {
    int (*ptr)(int, int) = add;  // Assignment
    int result = ptr(10, 20);    // Calling through pointer
    printf("%d\n", result);
    return 0;
}