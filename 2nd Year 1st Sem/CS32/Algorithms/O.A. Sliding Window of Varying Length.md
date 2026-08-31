---
field: algorithms
problem type: optimization problem
data structure: array
---
## pseudocode

```text
ALGORITHM MinSubarrayLen(arr, n, target_s)

// Initialize variables
l = 0            // left window boundary
curr_sum = 0     // sum of elements inside [l...r]
min_len = n + 1  // dummy max value to track minimum length


// Goal: expand window right, shrink left when sum >= target_s


FOR r = 0 TO n - 1:

    curr_sum = curr_sum + arr[r]  // add right element to window

    WHILE (curr_sum >= target_s):

        current_len = r - l + 1   // calculate window size

        IF (current_len < min_len):
            min_len = current_len // update minimum length found
        END IF

        curr_sum = curr_sum - arr[l] // shrink window from left
        l = l + 1


// Return result or 0 if no valid subarray exists


IF (min_len == n + 1):
    RETURN 0
END IF

	RETURN min_len


```


## C Implementation

```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int64_t min_length_atleast_sum_s(int64_t *arr, int64_t n, int64_t s){
	int64_t l, r, m, n, min_len, curr_sum;

	if (n <= 0){
		return 0;
	}

	curr_sum = 0;

	l = 0;
	curr_sum = 0;
	min_len = n+1;

	for (int64_t r=0; r <n; r++){

		curr_sum += arr[r];

		while (curr_sum >= s){

			int64_t current_len = r-l+1;
			if (current_len < min_len){
				min_len = current_len;
			}

			curr_sum -= arr[l];
			l++;

		}

	}

	if (min_len == n+1){
		return 0;
	}
	else{
		return min_len;
	}

}
	

int main(){

	int64_t n = 10;
	int64_t arr[] = {3, -4, 5, 5, -2, 8, 4, 9, -1, 9};

	printf("%ld", min_length_atleast_sum_s(arr, n, s));

	return 0;

}

// 21
```