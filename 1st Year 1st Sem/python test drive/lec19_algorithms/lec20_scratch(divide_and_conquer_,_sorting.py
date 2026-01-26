# "find index of every target in the seq"

def find_indices(seq, targets):
    res = []
    for item in targets:
        res.append(_find_index(seq, item))
    return res

def _find_index(seq, x):
    l = 0
    r = len(seq) - 1

    while l <= r:
        m = (l + r) // 2

        if seq[m] == x:
            return m
        else:
            if x > seq[m]:
                l = m + 1
            else:
                r = m - 1

    return None


print(find_indices((10, 20, 15, 17, 21),(15, 14, 21, 50, 5, 10),))



# "find a contiguous subsequence with max sum"

def max_subarray_sum(seq):
    res = []
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if i == j:
                res.append((i, j+1))

            else:
                res.append((i,j+1))

    super_res = []
    pre_sum = prefix_sum(seq)
    for entry in res:
        i, j = entry
        super_res.append(pre_sum[j] - pre_sum[i])
    return max(super_res)

def prefix_sum(seq):
    res = [0]
    for item in seq:
        res.append(res[-1] + item)
    return res

print(max_subarray_sum([-2, 3, 2, -4, 2, -1, 4, -3, 1]))

# "find the values for each key in the query"

def find_values(dic_list, query):
    res = []
    sorted_dic_list = bubble_sort_on_key(dic_list)
    for key in query:
        value = (key_find(sorted_dic_list, key))
        res.append(value)
    return res


def key_find(sorted_dic_list, key):
    l = 0
    r = len(sorted_dic_list) - 1

    while l <= r:
        m = (l + r) // 2
        if key == sorted_dic_list[m][0]:
            return sorted_dic_list[m][1]
        else:
            if key > sorted_dic_list[m][0]:
                l = m + 1
            else:
                r = m - 1
    return None

# *we can use bubble sort on the keys

def bubble_sort_on_key(dic_list):

    change_upd = 1
    end = len(dic_list) - 1

    while change_upd != 0:
        change_upd = 0
        for i in range(end):
            if dic_list[i][0] > dic_list[i + 1][0]:   
                dic_list[i], dic_list[i + 1] = dic_list[i + 1], dic_list[i]
                change_upd += 1

        if change_upd != 0:
            end -= 1
    return dic_list


# "sorting logicss"

def bubble_sort(seq):
    end = len(seq) - 1 # babawasan yung end para bumukod yung mga detected max vals
    change_upd = 1 # kapag 0, walang iniba, so pwede na ireturn

    while change_upd != 0:
        change_upd = 0 # ireset para hindi magoverlap yung changes ng ibang loops
        for i in range(end): # icheck mula 0th to 2nd to the last
            if seq[i] > seq[i + 1]: # kapag mas malaki, iswap
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                change_upd += 1
        if change_upd != 0: # kapag may change, edi may nakuhang max, so bukurin yun
            end -= 1

    return seq 


def selection_sort(seq):
    res = []
    while len(seq) >= 1:
        _min = min(seq)
        res.append(_min)
        min_idx = seq.index(_min)
        seq.pop(min_idx)

    return res



"""def merge_sort(seq):
    if len(seq) == 1:
        return seq

    left = seq[:len(seq)//2]
    right = seq[len(seq)//2:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)

def _merge(left, right):
    res = []

    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            res.append(right[0])
            right.pop(0)
        else:
            res.append(left[0])
            left.pop(0)

    while len(left) != 0:
        res.append(left[0])
        left.pop(0)

    while len(right) != 0:
        res.append(right[0])
        right.pop(0)

    return res"""


def merge_sort(seq):
    if len(seq) == 1: # return lang kapag isa lang yung item
        return seq 
    else:
        kanan = seq[len(seq)//2:] # define
        kaliwa = seq[:len(seq)//2]

        kanan = merge_sort(kanan) # recurse
        kaliwa = merge_sort(kaliwa)

        return _merge_logic(kaliwa, kanan) # return logic

def _merge_logic(kaliwa, kanan):
    sagot = []

    while len(kaliwa) != 0 and len(kanan) != 0: # kapag puro may laman
        if kaliwa[0] < kanan[0]: # ilagay sa sagot yung maliit sa dalawang choices
            sagot.append(kaliwa[0])
            kaliwa.pop(0)
        else:
            sagot.append(kanan[0])
            kanan.pop(0)

    for natira in kaliwa: # kapag may laman nalang yung kaliwa
        sagot.append(natira)
    for natira in kanan: # kapag may laman nalang yung kanan
        sagot.append(natira)

    return sagot


#print(merge_sort([3, 5, 7, 9, 0, 8, 6, 4, 2, 1]))

#print(selection_sort([3, 5, 7, 9, 0, 8, 6, 4, 2, 1]))

print(find_values([(3, "three"), (1, "one"), (4, "four")], [1, 2, 4, 8]))

