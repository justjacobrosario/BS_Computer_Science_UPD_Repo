"""
instruc: get the sum of all fibonacci numbers until nth number
fibonacci: 0 + 1 + 1 + 2 + 3 + 5 + 8 + ...
let n = 5
= 8 + 5 + 3 + 2 + 1 + 1 + 0
(n-2) + (n-1)
4 + 5 = 9
7 + 8 = 15
= 
"""

def nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return nth_fibonacci(n-2) + nth_fibonacci(n-1)


print(nth_fibonacci(6))