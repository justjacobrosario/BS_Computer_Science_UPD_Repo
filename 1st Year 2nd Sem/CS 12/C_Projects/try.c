#include <stdio.h>
#include <stdlib.h>

int *create67(){
	int *p = malloc(sizeof(int));
	*p = 67;
	return p;
}

int *first_negative(int *p, int n){
	for (int i = 0; i < n; i++){
		if (*(p + i) < 0) {
			return (p+i);
		}
	}
	return NULL;
}

int main() {
	int *p = NULL;
	int x = *p;
}

