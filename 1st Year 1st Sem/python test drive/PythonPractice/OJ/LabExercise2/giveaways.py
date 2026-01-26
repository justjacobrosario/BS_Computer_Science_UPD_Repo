def gifts(c, n):
    return tuple(
        c[part - 1]
        for tup in n if tup[1] - tup[0] + 1 <= 100
        for part in range(tup[0], tup[1] + 1)
    )
"""
    for tup in n:
        for part in range(tup[0], tup[1]+1):
            print(c[part-1])

1. in converting for loop to comprehension, if a variabl is err as not defined:
 - check if the nexted for loops are in order
 2. always check for exceptions
 
"""
print(gifts(('dog', 'cat', 'car'), (
    (1, 2),
    (1, 3),
    (2, 3),
    (1, 2),
    (1, 1),
    (1, 1),
)))
