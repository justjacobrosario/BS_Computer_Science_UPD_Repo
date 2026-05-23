#include <stdio.h>
#include <stdlib.h>


int main() {
	int x;
	char y;

	printf("x:");
	scanf("%d", &x);

	printf("y: ");
	scanf("%c", &y);
	printf("output: %d %c\n", x, y);
}

