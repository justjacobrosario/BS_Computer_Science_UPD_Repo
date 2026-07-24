def my_subarray(seq, k):
    res = []
    for start in range(len(seq)):
        for end in range(start, len(seq)):
            if start == end:
                subarray = [seq[start]]
            else:
                subarray = seq[start:end+1]
            if len(subarray) == k:
                res.append(sum(subarray))
    return res

def new_subarray(seq, k):
    for i in range(len(seq) - k + 1): # -k + 1 to not be outof bounds
        start = i
        end = i + k
        yield sum(seq[start:end])

def faster_subarray(seq, k):
    pinakauna = sum(seq[:k]) # base item
    yield pinakauna
    for i in range(len(seq) - k):
        pinakauna = pinakauna - seq[i] + seq[i+k] # next item using base item
        yield pinakauna


print([*faster_subarray([3, 1, 4, 1, 5, 9], 3)])

"""print(my_subarray([3, 1, 4, 1, 5, 9], 3))
print([*new_subarray([3, 1, 4, 1, 5, 9], 3)])"""


def my_subrange_sums(seq, intervals):
    for (i, j) in intervals:
        yield sum(seq[i:j])

# USE PREFIX RANGE SUMSSSS (range starting from 0)

def prefix_sum(seq): # get sum from 0 rightwards
    res = [0]
    for items in seq:
        res.append(res[-1] + items)
    return res

# APPLY TO NONPREFIX RANGES
# e.g. 3 to 5 = (0 to 5) - (0 to 3)
# s.t. i to j = (0 to j) - (0 to i)
# s.t. i to j = (prefx_sum of j) - (prefx_sum of i)
def faster_subrange_sums(seq, intervals):
    for (i, j) in intervals:
        prefix_sum_list = prefix_sum(seq)
        yield prefix_sum_list[j] - prefix_sum_list[i]

print([*faster_subrange_sums(([3, 1, 4, 1, 5, 9]),[(0, 3), (1, 5), (2, 4), (4, 5), (4, 4)],)])


def thanos_check_existence(seq, x):
    # base values:
    l = 0
    r = len(seq) - 1

    #loop:
    while l <= r:
        m = (l + r) // 2
        #positive case
        if x == seq[m]:
            return True # if meron
        #negative case
        else:
            # loop left
            if x < seq[m]:
                r = m - 1
            # loop right
            else:
                l = m + 1

    return False # if wala

print(thanos_check_existence([1, 3, 5, 7, 9, 11, 13], 11))

def thanos_find_smallest_num_equal_or_after_x(seq, x):
    # base values
    l = 0
    r = len(seq) - 1
    res = None

    while l <= r:
        m = (l + r)//2
        midpoint = seq[m]
        # positive case:
        if x <= midpoint:
            res = midpoint
            r = m - 1
        # negative case:
        else:
            if x > midpoint:
                l = m + 1

    return res

print(thanos_find_smallest_num_equal_or_after_x([1, 3, 5, 7, 9], 6))



