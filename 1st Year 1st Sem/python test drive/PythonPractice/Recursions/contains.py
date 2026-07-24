def contains(seq, val):
    if len(seq) == 1:
        if val == seq:
            return True
        else:
            return False
    else:
        if val == seq[0]:
            return True
        elif val != seq[0]:
            return contains(seq[1:], val)

print(contains((1, 2, 3, "d", 4), 1))