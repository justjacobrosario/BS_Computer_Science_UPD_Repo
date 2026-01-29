""" ■■■■■■■ WHAT MAKES A PROGRAM ELEGANT ■■■■■■■ """
# 1. Bug-free
# 2. Easy to understand
# 3. Easy to modify

""" ■■■■■■■ SYSTEMATIC DEBUGGING ■■■■■■■ """

'''■ ■ ■ EQUIVALENCE PARTITIONING ■ ■ ■'''
# Input Equivalence Partition : Set or range of vals that behaves similarly
                                # Produces same kind of output
# Output Equivalence Partition : Set or range of kinds of outputs

# e.g.
def my_abs(n : int) -> int:
    if n >= 0:
        return n
    else:
        return -n
# Equivalence Partition:
# Input : n >= 0, Output : n
# Input : n < 0, Output : -n

# ■ Types and Equivalence Partitions
data_type = possible partitions
int = positives, negatives, zero. odd, even
str = empty str, uppercase, lowercase, spaces, symbols, emojis
list, set, dict, tuple = empty, singleton, dupes, some equal, all equal, all unique

'''■ ■ ■ EDGE CASES ■ ■ ■'''