#include <stdio.h>
#include <stdlib.h>

int *create67(){
	int *p = malloc(sizeof(int));
	*p = 67;
	return p;
}

int main() {
	int *num = create67();
	printf("%d\n", *num);
	}