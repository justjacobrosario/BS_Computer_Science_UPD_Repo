#include <stdio.h>
#include <math.h>

int main() {
    int age = 19;
    int *p_age = &age;

    printf("%d\n", age);

    printf("%d\n", &age);
    printf("%d\n", *p_age);


}