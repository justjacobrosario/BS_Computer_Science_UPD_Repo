
def partitions(n):

    def helper(n, k):
        if n == 0:
            return [[]]

        elif n<0 or k == 0:
            return []

        with_k = []

        for rest in helper(n-k, k):
            with_k.append([k] + rest)

        without_k = helper(n, k-1)

        return with_k + without_k

    return helper(n, n)


print(partitions(4))