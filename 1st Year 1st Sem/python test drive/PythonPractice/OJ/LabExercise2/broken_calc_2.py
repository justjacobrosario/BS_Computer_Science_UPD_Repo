def broken_add(*nums):
    odd_set = tuple(x for x in nums if x % 2 == 1) 
    if (len(odd_set)) % 2 == 1:
        return sum(nums) + 1
    else:
        return sum(nums)

print(broken_add(1, 2))
# expr. for x in () if cond.


"""
Problem Statement
Yuuka's calculator broke again! She won't be able to finish all of her secretarial duties at this rate...

This time, Yuuka's calculator takes in any number of integers. When asked for the sum of the integers, the calculator still returns 1
 more than the actual sum if an odd number of these integers are odd. Otherwise, the calculator gives the correct sum.

Can you simulate Yuuka's calculator for her again?

Task Details
Your task is to implement a function named broken_add, which should have the following signature:


def broken_add(*nums):
The above says that it takes in a variable number of arguments nums. All arguments will be integers (int).

The function must return an integer (int) denoting the calculator's output.

Restrictions
The following symbols can now be used: min, max, sum, range, all, any.
recursion is disallowed.
comprehensions are allowed.
at most 6
 functions can be defined.
Your source code must have at most 250
 bytes.
Examples
Example 1 Function Call

broken_add(1, 2, 1)
Example 1 Return Value

4
Example 2 Function Call

broken_add(1, 2)
Example 2 Return Value

4
Constraints
The function broken_add will be called at most 100
 times.
For each argument a
 in nums, 0≤a≤1020
.
The sum of the lengths of nums across all calls to broken_add will be ≤104
.
Scoring
Note: New tests may be added and all submissions may be rejudged at a later time. (All future tests will satisfy the constraints.)

You get 25
 ❤️ points if you solve all test cases where:
The arguments in nums are either all even or all odd.
You get 25
 ❤️ points if you solve all test cases where:
Each argument in nums is either 0
 or 1
.
You get 100
 ❤️ points if you solve all test cases where:
The sum of the lengths of nums across all calls to broken_add will be ≤100
.
You get 50
 🔴 points if you solve all test cases."""