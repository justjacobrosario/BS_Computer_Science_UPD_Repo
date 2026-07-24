"""
Part 3 — Grouping and Classification (subtypes 3.1–3.4)

3.1 Group by Remainder — Problem: group_by_modulo
Problem Statement
 Group integers by their remainder when divided by k.

Example Calls
 group_by_modulo((3,4,5,6,7), 3) → {0:[3,6], 1:[4,7], 2:[5]}
"""

def group_by_modulo(seq, x):
    dic = {}
    for num in seq:
        mod = num % x
        if mod in dic:
            (dic[mod]).append(num)
        else:
            dic.update({mod : [num]})
    return dic

print("grouped by modulo", group_by_modulo((3,4,5,6,7), 3))


"""
3.2 Group Words by First Letter — Problem: group_by_initial
Problem Statement
 Given a list of words, group them by their first letter (lowercased).

Example Calls
 group_by_initial(("bat","ball","apple")) → {'b':["bat","ball"],'a':["apple"]}
"""


def group_by_initial(seq):
    dic = {}
    for word in seq:
        if word[0] in dic:
            dic[(word[0])].append(word)
        else:
            dic.update({word[0] : [word]})
    return dic

print("group by initial:", group_by_initial(("bat","ball","apple")))

"""
3.3 Group Numbers by Sign — Problem: group_by_sign
Problem Statement
 Group integers into 'positive', 'negative', and 'zero' categories.

Example Calls
 group_by_sign((-1,0,5,-3,8)) → {'negative':[-1,-3], 'zero':[0], 'positive':[5,8]}
"""

def group_by_sign(seq):
    dic = {
    'negative' : [],
    'zero' : [],
    'positive' : []
    }
    for num in seq:
        if num == 0:
            dic["zero"].append(num)
        elif num > 0:
            dic["positive"].append(num)
        else:
            dic["negative"].append(num)
    return dic


print("group by sign:", group_by_sign((-1,0,5,-3,8)))

"""
3.4 Group by Length — Problem: group_words_by_length
Problem Statement
 Group words according to their string length.

Example Calls
 group_words_by_length(("hi","cat","dog","me")) → {2:["hi","me"], 3:["cat","dog"]}
"""

def group_words_by_length(seq):
    dic = {}
    for word in seq:
        if len(word) in dic:
            dic[len(word)].append(word)
        else:
            dic.update({len(word) : [word]})
    return dic


print("group by length:", group_words_by_length(("hi","cat","dog","me")))