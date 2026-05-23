#include <stdio.h>
#include <stdlib.h>

void increm_baon(int *baon){
    *baon = *baon + 1;
}

int main() {

    typedef struct student Student;

    struct student {
        int baon;
        char name[123];
        char univ[123];
    };

    struct student maria = {
        76,
        "Maria Clara",
        "UST"
    };

    printf("%d\n", maria.baon);

    return 0;
}