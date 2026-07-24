"""
2.1 Linear search — Problem: find_first_divisible

Problem Statement
Return the index of the first element divisible by k. If none, return -1.

Example Calls
find_first_divisible((7,10,13,16), 5) → 1
"""

def find_first_divisible(seq, n):
    for i, num in enumerate(seq):
        if num % n == 0:
            return i
"""
2.2 Conditional search with flags — Problem: has_increasing_pair

Problem Statement
Return True if the list contains at least one strictly increasing adjacent pair (nums[i] < nums[i+1]); otherwise False. Use a flag variable.

Example Calls
has_increasing_pair((5,4,4,6)) → True
has_increasing_pair((3,2,1)) → False

"""

def has_increasing_pair(seq):
    for i, num in enumerate(seq):
        if i > 0:
            if seq[i] > seq[i-1]:
                return True
    return False

print(has_increasing_pair((3,2,1)))

"""
2.3 Find max/min — Problem: second_largest

Problem Statement
Return the second-largest distinct number in the sequence. If it does not exist, return None. Use single pass keeping track of largest and second.

Example Calls
second_largest((5,1,5,3)) → 3
second_largest((4,4)) → None

"""

"""def second_largest(seq):
    first_max_i = seq.index(max(seq))
    new_seq = seq[:first_max_i] + seq[first_max_i+1:]
    return seq.new_index(max(new_seq))
    

print(second_largest((5,1,5,3)))"""

#Not yet done

"""
2.4 Argmax / Argmin — Problem: argmin_distance

Problem Statement
Given a list of points on a line (ints) and a target t, return index of the point with minimum absolute distance to t (first such index if ties).

Example Calls
argmin_distance((2,6,4,8), 5) → 2 (|4-5|=1 is smallest)
argmin_distance((7,3), 5) → 0 (|7-5|=2, |3-5|=2 tie → first index 0)

"""

def argmin_distance(seq, target):
    res = []
    for i, num in enumerate(seq):
        res.append(abs(num-target))
    _min = min(res)
    _min_indx = res.index(_min)
    return _min_indx

print(argmin_distance((2, 4, 6, 8), 5))




