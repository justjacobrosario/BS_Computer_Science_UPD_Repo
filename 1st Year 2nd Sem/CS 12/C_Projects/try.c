#include <stdio.h>
#include <stdlib.h>

typedef struct student Student;
    struct student {
        int baon;
        char name[123];
        char univ[123];
    };

void increm_baon2(Student *p){
    int *q = &((*p).baon);
    *q = (*p).baon + 1;
}

void increm_baon3(Student *p){
    int *q = &p->baon;
    *q = p->baon + 1;
}


void decrem_baon3(Student *p){
	int *q = &(p->baon);
	*q = p->baon - 1;
}

int main() {


    Student maria = {
        76,
        "Maria Clara",
        "UST"
    };

    printf("%d\n", maria.baon);

    decrem_baon3(&maria);

	printf("%d\n", maria.baon);
}