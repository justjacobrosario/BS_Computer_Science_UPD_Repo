"""
instruction: let's say max() is non existent, make my_max() for u
let n = (1, 2, 3, 4)
my_max(n) = 4

if 1st num of n (i.e. 1) is greater than the new 1st num of n[1:] (i.e. 1st num of (2, 3, 4) is 2), return the recent 1st num
else, if 1st num of n is less than n[1:] then do again the first if statement but instead of n, its n[1:] (i.e. the first num is removed) 

the base case is if the tuple only has one element left, so its techically the minimum number
"""

def my_max(a_tuple):
    if len(a_tuple) == 1:
        return a_tuple[0]
    else:
        if a_tuple[0] > my_max(a_tuple[1:]):
            return a_tuple[0]
        else:
            return my_max(a_tuple[1:])

print(my_max((10, 10, 10, 1, 2, 20, 3, 4, 5)))