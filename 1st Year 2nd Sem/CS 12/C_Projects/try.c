#include <stdio.h>
#include <stdlib.h>

/*
int main() {
	int id;
	char msg[67];

	while (1) {
		printf("Input id: ");
		scanf("%d", &id);

		printf("Input message: ");
		scanf("%s", msg);

		printf("ID: %d, MSG: %s\n", id, msg);
	}
}
*/

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
		.name = "Maria Clara",
		.baon = 76,
		.univ = "UST"
	};


	printf("%d\n", maria.baon);

	
}


