---
field: algorithms
problem type: optimization problem
data structure: array
---

## pseudocode:

```text

max_sum_at_length_k(arr, n, k):
	int l, r, max_sum, curr_sum
	
	// init
	l = 0 
	r = l+k-1
	max_sum = 0
	
	// shift l rightwards
	FOR int i from 0 to n-k-1:
		l++
		r = l + k - 1
		
		// sum elements from l to r
		// can be optimized by prefix sum
		curr_sum = 0
		FOR int p from l to r:
			curr_sum += arr[p]
		
		// if curr_sum > max_sum, thats the new max_sum
		IF (curr_sum > max_sum){
			max_sum = curr_sum
		}
	
	
```


## C implementation

```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int64_t max_sum_at_length_k(int64_t *arr, int64_t n, int64_t k){
	int64_t l, r, max_sum, curr_sum;
	l = 0;
	r = l + k - 1;
	max_sum = 0;

	for (int i = 0; i < n-k; i++){
		l ++;
		r = l + k - 1;

		curr_sum = 0;


		for (int p = l; p <= r; p++){
			curr_sum += arr[p];
		}

		if (curr_sum > max_sum){
			max_sum = curr_sum;
		}
	}

	return max_sum;

}


int main(){

	int64_t n = 10;
	int64_t arr[] = {3, -4, 5, 5, -2, 8, 4, 9, -1, 9};

	printf("%ld", max_sum_at_length_k(arr, 10, 3));

	return 0;
}

// 21
```


