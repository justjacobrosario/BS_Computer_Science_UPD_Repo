import time

def subseq(seq):
    res = [[]]
    i = 0
    while i < len(seq):
        new = []
        j = 0
        while j < len(res):
            parte = res[j]
            new.append(parte + [seq[i]])
            j += 1
        res += new
        i += 1
    return res
        
"""
subseq [1,2,3]
i=0
[]:[1]
i=1
[],[2]:[1],[1,2]
i=2
[],[3]:[2],[2,3]:[1],[1,3]:[1,2],[1,2,3]
i=3
return 
"""

def rec_subseq(seq):
    res = []
    def h_rec_subseq(parte, k):
        if k == len(seq):
            res.append(parte)

        else:
            h_rec_subseq(parte, k + 1)
            h_rec_subseq(parte + [seq[k]], k + 1)
    h_rec_subseq([], 0)
    return res

print(rec_subseq([1, 2, 3]))
'''
substring [1,2,3]
[1], [1,2], [1,2,3]
[2], [2,3]
[3]
'''
  

def rec_substring(seq):# mali pa itooo
    res = []

    def h_rec_substring(seq, k):
        if k > len(seq):
            k = 0 + 1
            h_rec_substring(seq[1:], k)
            return
        else:
            res.append(seq[:k])
            h_rec_substring(seq, k+1)

    h_rec_substring(seq, 0 + 1)
    return res



"""
def for_substring(seq):
    res = []
    for i in range(len(seq)): # from 0th to lastth index
        for j in range(i, len(seq)): # from ith to lastth index
            if i == j:
                res.append([seq[i]])
            else:
                res.append(seq[i:j+1]) # +1 since right slice is exclusive
    return res

"""
"""
def comp_substring(seq):
    res = []
    for i in range(len(seq)):
        res += [[seq[i]] if i == j else seq[i:j + 1] for j in range(i, len(seq))]
    return res
    """

"""
def wh_substring(seq):
    res = []
    i = 0
    while i < len(seq):
        j = i
        while j < len(seq):
            if i == j:
                res.append([seq[i]])
            else:
                res.append(seq[i:j+1])
            j += 1
        i += 1
    return res
    """



"""
[], [1]
[], [2],, [1], [1,2]
"""

