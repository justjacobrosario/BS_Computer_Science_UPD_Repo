#include <stdio.h>

int *do_not_do_this() {
    int x = 2025;

    return &x; // Allowed by C; mortal sin
}
int main() {
    int *p1 = do_not_do_this();
    printf("This should be 2025: %d\n", *p1);
}