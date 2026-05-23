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

int main() {
	int id;
	char msg[67];

	while (1) {
		printf("Input id: ");
		scanf("%d", &id);

		// add this to remove remaining \n
		fgetc(stdin);

		printf("Input message: ");
		scanf("%s", msg);

		// add this to continue reading after the spaces
		fgets(msg, sizeof(msg), stdin);

		printf("ID: %d, MSG: %s\n", id, msg);
	}
}


