#recursion

def combination(tup, r):
    if r == 0:
        return ((),)
    elif r>len(tup):
        return ()
    else:
        with_first = addfirst(tup[0], combination(tup[1:], r-1))
        without_first = combination(tup[1:], r)
        return with_first + without_first

def permutation(tup, r):
    if r == 0:
        return ((),)
    elif r>len(tup) or tup==():
        return ()
    else:
        return helping_perm(tup, r, 0)

def helping_perm(tup, r, i):
    if i == len(tup):
        return ()
    else:
        return addfirst(tup[i], permutation(tup[:i]+tup[i+1:], r-1)) + helping_perm(tup, r, i+1)

def addfirst(first, combo):
    if combo == ():
        return ()
    else:
        return ((first,) + combo[0],) + addfirst(first, combo[1:])

#comprehension

def combination_compre(tup):
    return tuple((tup[i], tup[j], tup[k])
        for i in range(len(tup))
        for j in range(i+1, len(tup))
        for k in range(j+1, len(tup)))

def permutation_compre(tup):
    return tuple((tup[i], tup[j], tup[k])
        for i in range(len(tup))
        for j in range(len(tup))
        for k in range(len(tup))
        if len({i, j, k}) == 3)

print(permutation_compre((1, 2, 3)) == permutation((1, 2, 3), 3))