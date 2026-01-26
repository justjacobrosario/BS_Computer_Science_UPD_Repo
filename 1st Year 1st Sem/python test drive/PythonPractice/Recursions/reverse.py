def reverse(seq):
    if len(seq) == 1:
        return seq
    else:
        return (seq[-1],) + reverse(seq[:-1])

print(reverse((1, 2, 3)))