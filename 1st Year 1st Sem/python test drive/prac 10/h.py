"""
single-lined
0 to n-1 packages

goal for every subarray, reverse their order


"""


def warehouse_rearrange(n, intervals):
    packages = []

    for p in range(n):
        packages.append(p)

    for i, j in intervals:
        packages[i : j + 1] = reversed(packages[i : j + 1])

    return packages


print(warehouse_rearrange(7, (
    (2, 5),
    (1, 3),
    (3, 6),
    (4, 4),
    (3, 4),
))
)