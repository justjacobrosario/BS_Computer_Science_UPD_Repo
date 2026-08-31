---
field: algorithms
problem type: enumeration problem
data structure: numeric
---



```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

// made a struct to get the array and its length directly
typedef struct SizedArray {
	int64_t *array;
	int64_t length;
} SizedArray;

SizedArray *primes_until_n(int64_t n){
	
	// make truth array if idx val is prime
	bool *is_prime = malloc(sizeof(bool)*(n+1));

	for (int64_t i = 0 ; i <= n; i++){
		is_prime[i] = true;

	}


	// make 0 and 1 false (since theyre not prime)
	is_prime[0] = false;
	is_prime[1] = false;

	// use sieve by erastothenes
	for ( int64_t p = 2; p*p <= n; p++){

		if (is_prime[p] == true){
			for (int64_t k = 2; p*k <= n; k++){
				is_prime[p*k] = false;
			}

		}

	}


	int64_t prime_counter = 0;
	// count the primes
	for (int64_t i = 0 ; i <= n; i++){
		if (is_prime[i] == true){
			prime_counter ++;
		}
	}


	
	// make an array of only primes
	int64_t *primes = malloc(sizeof(int64_t) * prime_counter);
	int64_t p_idx = 0;
	for (int64_t i = 0; i <= n ; i++){
		if (is_prime[i] == true){
			primes[p_idx] = i;
			p_idx++;
		}
	}

	free(is_prime);

	SizedArray *res = malloc(sizeof(SizedArray));
	res->array = primes;
	res->length = prime_counter;


	return res;

	

}

int main(){

	int64_t n = 10;
	SizedArray *primes = primes_until_n(n);
	printf("length : %ld\n", primes->length);


	for (int i = 0; i < primes->length; i++){
		printf("%ld\n", primes->array[i]);
	}


	


	return 0;
}
```