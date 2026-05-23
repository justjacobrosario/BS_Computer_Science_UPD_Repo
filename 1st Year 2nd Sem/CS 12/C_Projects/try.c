#include <stdio.h>
#include <stdlib.h>

int *make_range(int n){
	int *lis = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++){
		lis[i] = i;
	}

	return lis;
}

int main(){
	int n = 11;
	int *p = make_range(n);

	for (int i = 0; i < n; i++){
		printf("%d\n", *(p + i));
	}

}