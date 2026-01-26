def print_grid(rows):
    for row in rows:
        for item in row:
            print(item, end = "")
        print()

def print_with_indices(lst):
    for indx, item in enumerate(lst):
        print(indx, item)

def equal_consecutive_pairs(strng):
    res = 0
    for indx in range(len(strng)):
        if indx == 1:
            if strng[indx] == strng[indx-1]:
                res += 1
        elif indx > 1:
            if strng[indx] == strng[indx-1] and strng[indx-1] != strng[indx-2]:
                res += 1
    return res

def all_powers(pairs):
    res = []
    for pair in pairs:
        base, exp = pair
        res.append(base ** exp)
    return res

VOWELS = "aeiouAEIOU"

def all_vowels(strng):
    global VOWELS
    res = ""
    for letter in strng:
        if letter in VOWELS:
            res += letter
    return res[::-1]

def all_pairs(seq1, seq2):
    res = []
    for x in seq1:
        for y in seq2:
            res.append((x, y))
    return res

print(all_pairs((1, 2), (3, 4, 5)))


"""
print(all_vowels('paranoia'))"""
"""
print(all_powers(((1, 5), (2, 4), (3, 3))))"""
"""print(equal_consecutive_pairs('missssssissippi'))"""

"""
print_with_indices([3, 1, 4, 1])"""

"""
print_grid((
    (1, 2, 3),
    (4, 5, 6), 
    (7, 8, 9)))"""