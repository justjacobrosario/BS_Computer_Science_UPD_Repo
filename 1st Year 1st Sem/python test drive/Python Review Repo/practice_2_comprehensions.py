def first_letters(seq):
    return tuple(x[0] for x in seq)

#print(first_letters(('can', 'i', "have", "this", "dance")))

def triangular_numbers(nums):
    return tuple(n*(n+1)//2*n*(n+1)//2 for n in nums)

#print(triangular_numbers((3, 1, 4, 1)))

def doublets(words):
    return tuple(x for x in words if x[:len(x)//2] == x[len(x)//2:])

#print(doublets(("haha", "paruparo")))

def odds_in_range(x, y):
    return frozenset(n for n in range(x, y+1) if n%2 != 0)

#print(odds_in_range(-8, -2))

def in_exactly_one(l, s1, s2):
    return tuple(x for x in l if (x in s1 or x in s2) and not(x in s1 and x in s2))

#print(in_exactly_one((3, 1, 4, 1, 5, 9, 2), frozenset((3, 0, 5, 6)), frozenset((2, 1, 5))))

def sets_containing_range(x, y, intsets):
    return tuple(set for set in intsets if set in frozenset(range(x, y+1)))

print(sets_containing_range(3, 6, (frozenset((3, 4, 5, 6, 7)), frozenset(()))))
print(frozenset((3, 4, 5)) <= frozenset(range(3, 7)))