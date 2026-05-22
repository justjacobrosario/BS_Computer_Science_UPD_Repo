#include <stdio.h>

int main() {
	int nums[] = {10, 20, 30};
	int arr[5] = {};
	int sum = 0;


	for (int i = 0; i < 3; i++){
		printf("%d\n", nums[i]);
		sum += nums[i];
	}
	printf("sum is %d\n", sum);
}