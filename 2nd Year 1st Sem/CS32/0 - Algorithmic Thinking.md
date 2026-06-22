
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
