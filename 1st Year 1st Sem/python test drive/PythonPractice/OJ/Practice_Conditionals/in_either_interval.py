def in_either_interval(a, b, c, d, y):
    return (a <= y <= b) or (c <= y <= d)

print(in_either_interval(2024, 2034, 2028, 2038, 3000))

"""
Problem Statement
Scientists (?) predict that the sun will explode sometime between the years a
 and b
 inclusive. Your best friend (?) predicts that the sun will explode sometime between the years c
 and d
 inclusive.

If the sun explodes on year y
, will either the scientists or your best friend be right?

Task Details
Your task is to implement a function named in_either_interval, which should look like this:


def in_either_interval(a, b, c, d, y):
    return ...
Here, you only need to replace the ... part with a Python expression.

The function must return a bool denoting the answer.

Your source code must have at most 100
 bytes.

Examples
Example 1 Function Call

in_either_interval(2024, 2034, 2028, 2038, 2030)
Example 1 Return Value

True
Example 2 Function Call

in_either_interval(2024, 2034, 2028, 2038, 3000)
Example 2 Return Value

False

Constraints
The function in_either_interval will be called at most 104
 times.
1≤a≤b≤1050
1≤c≤d≤1050
1≤y≤1050
"""