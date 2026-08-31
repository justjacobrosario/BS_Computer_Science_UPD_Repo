---
field: algorithms
problem type: decision problem
data structure: numeric
---

## theorem:

for all 2 <= x < sqrt(n), if n%x != 0 then n is prime
## pseudocode:

```text

is_prime(int n):

	int x = 2
	
	// virtually same as while x < sqrt(n)
	WHILE (x*x < n): 
		// if n is divisible by x then not prime
		if (n%x == 0):
			return false
		x++
		
	return true
	
```


## C implementation

```c
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

bool is_prime(int64_t n){

	int64_t x = 2;

	while (x*x < n){
		if (n%x == 0){
			printf("$ at %ld\n", x);
			return false;
		}
		x++;
	}

	return true;

}


int main(){

	int64_t n = 13;
	if (is_prime(n) == true){
		printf("%ld is prime", n);
	}
	else{
		printf("%ld is not prime", n);
	}

	return 0;
}



```
