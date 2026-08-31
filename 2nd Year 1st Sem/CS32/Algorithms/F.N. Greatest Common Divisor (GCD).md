---
field: algorithms
problem type: function problem
data structure: numeric
---

## pseudocode:

```text

gcd(int a, int b){
	IF (a==0 or b==0):
		return 0
	
	// iterate gcd(a, b) to gcd(b, a%b) until b == 0
	WHILE (b != 0){
		int temp = b
		b = a%b
		a = temp
	}
	
	return a

}
	
```


## C implementation

```c
#include <stdio.h>
#include <stdint.h>

int64_t gcd(int64_t a, int64_t b){


	if (a == 0){
		return 0;
	}
	int64_t temp;

	while (b != 0){
		temp = b;
		b = a%b;
		a = temp;
	}

	return a;

}


int main(){

	printf("%ld", gcd(25, 35));

	return 0;
}
// 5
```
