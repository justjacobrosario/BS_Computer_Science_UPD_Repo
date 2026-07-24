'''

'''

def zero_sum_counts(seq):
    seq = iter(seq)
    res = []
    lagayan = []

    for num in seq:
        lagayan.append(num)
        zero_sums = zero_sum_subarray(lagayan)
        yield zero_sums



def prefix_sum(seq):
    res = [0]
    for num in seq:
        res.append(res[-1] + num)
    return res

def zero_sum_subarray(seq):
    res = []
    count = 0
    pre_sum = prefix_sum(seq)

    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if i == j:
                if seq[i] == 0:
                    count += 1
                res.append(([seq[i]], seq[i]))
            else:
                
                res.append((seq[i:j+1], pre_sum[j+1] - pre_sum[i]))
                if pre_sum[j+1] - pre_sum[i] == 0:
                    count += 1

    return count

'''
def zero_sum_counts(seq):
    seq = iter(seq)
    lagayan = []
    res = []
    cache = {}

    def helper(indx):
        if indx in cache:
            return cache[indx]
        else:

            if indx >= len(lagayan):
                cache[indx] = 0
                return 0

            else:
                recursion = zero_sum_subarray(lagayan[0:indx]) + helper(indx + 1)
                cache[indx] = recursion
                return recursion

    for item in seq:
        lagayan.append(item)
        res.append(helper(0))

    return cache'''




#print(zero_sum_subarray([2, 4, -5, 2, -1, 1, 0, 3]))

print([*zero_sum_counts(iter((2, 4, -5, 2, -1, 1, 0, -3)))])
