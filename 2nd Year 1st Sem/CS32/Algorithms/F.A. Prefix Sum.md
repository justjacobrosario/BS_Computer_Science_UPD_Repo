---
field: algorithms
problem type: function problem
data structure: array
---

## theorem:

suppose array {n1, n2, n3, n4, n5, ...}, then `sum(ni to nj) = prefix[j+1] - prefix[i]`

: this will optimize adding from i to j O(n) long, to just subtracting two elements in the prefix sum array O(1)

## pseudocode:

```text

prefix_sum(arr, n):
	int pref_arr[0]

	for i from 0 to n-1:
		pref_arr[i+1] = pref_arr[i] + arr[i]
		
	return pref_arr
```


## C implementation

```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int64_t *prefix_sum(int64_t *arr, int64_t n){
	int64_t *pref_arr = malloc(sizeof(int64_t)*(n+1));

	pref_arr[0] = 0;

	for (int i = 0; i < n ; i++){
		pref_arr[i+1] = pref_arr[i] + arr[i];

	}

	return pref_arr;

}



int main(){

	int64_t n = 10;
	int64_t arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int64_t *pref = prefix_sum(arr, n);

	for (int i = 0 ; i <= n; i++){
		printf("%ld\n", pref[i]);
	}
	free(pref);

	return 0;
}

/*
0
1
3
6
10
15
21
28
36
45
55
*/
```
