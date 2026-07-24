"""
instruc: get the sum of all positive even number at most an integer n
e.g. let n = 10
0 + 2 + 4 + 6 + 8 + 10 = 20
or 10 + 8 + 6 + 4 + 2 + 0 = 20 (countdown to 0 recursion)
n + (n-2) + (n-4) + ... 0
"""

def sum_of_evens_atmost(n):
    if n == 0: #base case
        return 0
    elif (n > 0) and (n%2 == 0): #if n is positive and is even, do n + (n-2) + (n-4) + ... + 0
        return n + sum_of_evens_atmost(n-2)
    else: #if n is positive and is odd, make it even by n-1
        return sum_of_evens_atmost(n-1)

print(sum_of_evens_atmost(1))