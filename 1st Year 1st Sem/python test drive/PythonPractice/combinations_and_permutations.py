def combinations_recursion(tup, r):
    if r == 0:
        return ((),)
    elif r > len(tup):
        return ()
    else:
        with_first = add_first_to_start(tup[0], combinations_recursion(tup[1:], r-1))
        without_first = combinations_recursion(tup[1:], r)
        return with_first + without_first

def add_first_to_start(first, combo):
    if combo == ():
        return ()
    else:
        return ((first,) + combo[0],) + add_first_to_start(first, combo[1:])

#================

def combinations_comprehension_2(tup):
    n = len(tup)
    return tuple((tup[x], tup[y])
        for x in range(n)
        for y in range(x+1, n))


#=====================

def permutation_recursion_r(tup, r):
    if r == 0:
        return ((),)
    if len(tup)<r or tup==():
        return ()
    else:
        return perm_helper(tup, r, 0)

def perm_helper(tup, r, i):
    if len(tup) == i:
        return ()
    else:
        return add_first_to_start(tup[i], permutation_recursion_r(tup[:i] + tup[i+1:], r-1)) + perm_helper(tup, r, i+1)

def add_first_to_start(first, combo):
    if combo == ():
        return ()
    else:
        return ((first,) + combo[0],) + add_first_to_start(first, combo[1:])

print(permutation_recursion_r((1, 2, 3), 3))
#=======

def permutation_comprehension(tup):
    return tuple((tup[i]+ tup[j])
        for i in range(len(tup))
        for j in range(len(tup))
        if len({i, j}) == 2)



print(permutation_comprehension(("a", "c", "a")))