
## 0.1. Algorithm
: An algorithm are a set of instructions to solve a particular problem

## 0.2. Algorithmic Solutions
: Sometimes problems tend to be solved by many different solutions

1. Use **Brute Force**: A good way to start is to solve it with **brute force**. This will deepen our understanding abt the problem.

2. Make it faster by only computing **Necessary Parts**: 

: Basically, instead of dealing every part with brute force, one can solve the problem by only computing the necessary parts.

>	e.g.
>	In a seq of n numbers, to add numbers from index i to j such that ( 0 <= i, j <= n-1), instead of adding those every time, we can utilize prefix sums (sum from 0th index number to j-th index number, then subtracting it to the sum from 0th index number to i-th index number) 


## 0.3. Efficiency

: An algorithm's efficiency is based on resource consumption (time and memory consumption).
: Efficiency is usually measured by comparing the rate of the growth of running time and and memory as the function's input enlarges.

## 0.4. Correctness
: Basically refers if the algorithm always output the correct answer for every possible inputs.

1. **Mathematical Proof**
: The best proof that an algorithm is correct, but it requires effort and time to construct

2. **Computer-aided Testing**
: Aside from proving a mathematical proof, asserting inputs to yield an expected output can be done. Once there exist an incorrect assertion, then the algorithm is not correct for all inputs.

A. **Assertions**
: In Python, we can gain confidence (but not absolution) that an algorithm is correct by doing assertions

>	`assert func(input) == expected_output`

: More inputs can be asserted to further prove its correctness

B. **pytest**
: using the **pytest** library can make error messaging cleaner

C. **Input Iteration**
: **Iterating inputs** is also a method of measuring correctness

D. **Random Input Iteration**
: Basically iterating random inputs within the scope


## 0.5. Algorithm sample : Getting the sum in between elements of a list

```c
#include <stdio.h>
#include <stdlib.h>

int* prefix_sums(int seq[], int size){
    int* res = (int*)malloc(size * sizeof(int));

    if (res == NULL){
        return NULL;
    }

    for (int i = 0; i < size; i++){
        if (i == 0){
            res[0] = seq[0];
        }
        else{
            res[i] = (seq[i] + res[i-1]);
        }
    }
    return res;
}

int sum_in_between(int pref[], int i, int j){
    return (pref[j] - pref[i-1]);
}



int main(){
    
    int seq[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int len_seq = sizeof(seq) / sizeof(seq[0]);
    int* sums = prefix_sums(seq, len_seq);

    int i = 3;
    int j = 5;

    printf("Sum from element %d to %d is %d", seq[i], seq[j], sum_in_between(sums, i, j));

    return 0;
}

```