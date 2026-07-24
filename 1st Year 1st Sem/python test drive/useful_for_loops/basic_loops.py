"""
1.1 Simple iteration — Problem: count_positive

Example Calls
count_positive(( -1, 0, 3, 5, -2 )) → 2
count_positive(()) → 0

"""

def count_positive(seq):
    res = 0
    for num in seq:
        if num > 0:
            res += 1
    return res

print(count_positive(( -1, 0, 3, 5, -2 )))

"""
1.2 Indexed iteration — Problem: replace_negatives

Problem Statement
Given a list of integers, produce a new list where every negative number is replaced by its absolute value, keeping other elements unchanged. You must use index-based updates (simulate in-place).

Example Calls : replace_negatives((3, -2, 0, -5)) → [3, 2, 0, 5]
"""

def replace_negatives(seq):
    res = []
    for num in seq:
        if num >= 0:
            res.append(num)
        else:
            res.append(num*(-1))
    return res

print(replace_negatives((3, -2, 0, -5)))


"""
1.3 Enumerated iteration — Problem: first_over_threshold

Problem Statement
Find the first value greater than a threshold and return its (index, value) pair. Use enumerate-style logic (index+value).

Example Calls
first_over_threshold((1,4,2,7), 5) → (3, 7)

"""

def first_over_threshold(seq, threshold):
    for i, num in enumerate(seq):
        if num > threshold:
            return (i, num)

print(first_over_threshold((1,4,2,7), 5))

"""
1.4 Dictionary iteration — Problem: invert_mapping_values

Problem Statement
Given a dictionary mapping strings to integers, invert it into a dictionary that maps each integer to a list of strings that had that integer (order preserved by iteration order of input mapping).

Example Calls
invert_mapping([("a",1),("b",2),("c",1)]) → {1: ["a","c"], 2: ["b"]}

"""

def invert_mapping(duples):
    res = {}
    for a, b in duples:
        if b not in res.keys():
                res = res | {b : [a]}
        else:
                res[b].append([a])
    return (res)

print(invert_mapping([("a",1),("b",2),("c",1)]))

"""
1.5 Nested loops — Problem: matrix_row_sums

Problem Statement
Given a rectangular matrix represented as a tuple of tuples of ints, compute the sum of each row and return a list of row sums.

Example Calls
matrix_row_sums(((1,2,3),(4,5,6))) → [6,15]
matrix_row_sums(((),)) → [0] (empty row sum = 0)

"""

def matrix_row_sums(rows):
    res = []
    for row in rows:
        row_sum = 0
        for cell in row:
            row_sum += cell
        res.append(row_sum)
    return res

print(matrix_row_sums(((1,2,3),(4,5,6))))

