---
field: algorithms
problem type: decision problem
data structure: array
---

## context:

: IFF array is nondecreasing

: instead of checking all elements O(n), you iterate array in half O(log n)

: useful for:
- existence check
- first/last occurence
- smallest/largest element satisfying function f


## pseudocode:

```text

binary_search(*arr, n, x):
	int left, mid, right
	
	// init
	left = 0
	right = n-1
	mid = (left + right) / 2
	
	// iterate dividing in half until we cant 
	WHILE (left != right):
		
		// check x's existence in mid
		IF (mid == x):
			return true
			
		// mid > x implies x on the left half
		IF (mid > x):
			rigth = mid - 1
		
		// mid < x implies x on the right half
		ELSE:
			left = mid + 1
			
		// update mid for every iteration 
		mid = (left + right) / 2

	// since we cant iterate anymore, declare x doesnt exist
	return false
```


## C implementation

```c
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

bool binary_search(int64_t *arr, int64_t n, int64_t x){
	int64_t l, r, mid;
	l = 0;
	mid = n / 2;
	r = n-1;


	int i = 0;
	while (r != l && i < 10){

		if (mid == x){
			return true;
		}

		if (mid > x){
			r = mid - 1;
		}
		else{
			l = mid + 1;
		}

		mid = (r + l) / 2;


		i++;

	}

	return false;
}



int main(){

	int64_t n = 10;
	int64_t arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	int64_t x = 3;
	if (binary_search(arr, n, x) == true){
		printf("%ld is in the array", x);
	}
	else{
		printf("%ld is not in the array", x);
	}

	return 0;
}

// 3 is in the array



```
