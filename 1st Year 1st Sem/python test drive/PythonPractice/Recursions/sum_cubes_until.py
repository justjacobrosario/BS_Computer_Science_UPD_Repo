"""
instruc: get the sum of n**3 where n is atmost n
e.g. let n  = 3
= 3**3 + 2**3 + 1**3 + 0**3
= 27 + 8 + 1 + 0 = 36
n**3 + (n-1)**3 + ... + 0**3 (countdown to zero recursion)
"""

def sum_cubes_until(n):
    if n == 0:
        return 0
    else:
        return n**3 + sum_cubes_until(n-1)

print(sum_cubes_until(3))
