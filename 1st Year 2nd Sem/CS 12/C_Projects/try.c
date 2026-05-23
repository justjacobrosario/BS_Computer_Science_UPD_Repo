#include <stdio.h>
#include <stdlib.h>


void increm_baon2(Student *p){
    *q = &((*p).year);
    *q = (*p).year + 1;
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

    increm_baon2(&maria);

	printf("%d\n", maria.baon);
}