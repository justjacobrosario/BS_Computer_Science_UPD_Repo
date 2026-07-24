"""
intruc: let's say len() hasn't been made yet, so make a function that returns the number of characters/elements of a string/tuple
"""

def improvised_len(a):
    if a[1:] == (): #base case for tuples
        return 1
    elif a[1:] == '': #base case for strings
        return 1
    else:
        return 1 + improvised_len(a[1:])

print(improvised_len("hatdog"))