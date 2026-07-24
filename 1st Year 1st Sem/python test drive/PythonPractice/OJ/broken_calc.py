def broken_add(a, b, c):
    total = a + b + c
    truth_val = 0
    if a%2 != 0:
        truth_val = truth_val + 1
    if b%2 != 0:
        truth_val = truth_val + 1
    if c%2 != 0:
        truth_val = truth_val + 1

    if truth_val%2 == 0:
        return total
    else:
        return total + 1


print(broken_add(2, 2, 3))