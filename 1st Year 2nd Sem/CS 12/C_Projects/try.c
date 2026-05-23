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
	int num[] = {1,2, 3, 6};
	int *f_nega = first_negative(num, 6);
	printf("%d\n", *f_nega);



	}