def num_subarrays(seq, p):
    pre_prod = prefix_prod(seq)
    count = 0
    for i in range(len(seq)):
        pre_prod_i = pre_prod[i]
        for j in range(i, len(seq)):
            if i == j:
                if seq[i] <= p:
                    count += 1
            else:
                if pre_prod[j+1] // pre_prod_i <= p:
                    count += 1
    return count


def num_subarrays(seq, p):
    L = 0
    prod = 1
    count = 0

    for R in range(len(seq)):

        prod *= seq[R]
        print("prod", prod)

        while prod > p and L <= R:
            prod //= seq[L]
            L += 1
            print("prod", prod, "L", L)

        count += (R - L + 1)
        print("count", count)
    return count


def prefix_prod(seq):
    res = [1]
    for item in seq:
        res.append(res[-1] * item)
    return res
