def intersection(seq1, seq2):
    if len(seq1) == 1:
        if contains(seq2, seq1[0]) == True:
            return seq1[0]
    if len(seq2) == 1:
        if contains(seq1, seq2[0]) == True:
            return seq2[0]
    else:
        if contains(seq1, seq2[0]) == True:
            return seq2[0] + intersection(seq1, seq2[1:])
        elif contains(seq1, seq2[0]) == False:
            return intersection

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
