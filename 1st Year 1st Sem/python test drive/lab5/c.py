
def num_subarrays(a, p):
    count = 0
    pre_prod = prefix_prod(a)
    for i in range(len(a)):
        for j in range(i, len(a)):
            if i==j:
                if a[i] <= p:
                    count += 1
            else:
                if pre_prod[j+1] // pre_prod[i] <= p:
                    count += 1
    return count

def prefix_prod(seq):
    res = [1]
    for item in seq:
        res.append(res[-1]*item)
    return res

print(num_subarrays((2, 1, 2), 3))
