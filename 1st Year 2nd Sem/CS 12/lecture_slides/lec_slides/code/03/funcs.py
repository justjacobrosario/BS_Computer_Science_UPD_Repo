def sum_until(n: int) -> int:
    return n * (n + 1) // 2


# abstraction
# 1^3 + 2^3 + ... + n^3
def sum_cubes_until(n: int) -> int:
    return sum_until(n) ** 2
