"""
Part 5 — Dictionary Transformations (subtypes 5.1–5.3)

5.1 Invert Mapping — Problem: invert_mapping
Problem Statement
 Invert a mapping from key→value into value→list of keys.

Example Calls
 invert_mapping((("a",1),("b",2),("c",1))) → {1:["a","c"], 2:["b"]}
"""

def invert_mapping(seq):
    dic = {}
    for key, val in seq:
        if val not in dic:
            dic.update({val : [key]})
        else:
            dic[val].append(key)
    return dic

print("invert mapping:", invert_mapping((("a",1),("b",2),("c",1))))

"""
5.2 Filter by Value — Problem: filter_high_scores
Problem Statement
 Given dict of student:score, keep only entries where score ≥ threshold.

Example Calls
 filter_high_scores({"Ann":90,"Ben":70,"Cia":95}, 85) → {"Ann":90,"Cia":95}
"""

def filter_high_scores(dic, cutoff):
    new_dic = {}
    for key, val in dic.items():
        if val >= cutoff:
            new_dic.update({key : val})

    return new_dic

print("filter on cutoff:", filter_high_scores({"Ann":90,"Ben":70,"Cia":95}, 85))

"""
5.3 Scale Values — Problem: double_values
Problem Statement
 Return a new dict with all numeric values doubled.

Example Calls
 double_values({"x":2,"y":3}) → {"x":4,"y":6}
"""

def double_values(dic):
    for key, val in dic.items():
        dic[key] *= 2
    return dic

print(double_values({"x":2,"y":3}))

"""
5.4 Mapping to computed values — Problem: square_dict
Problem Statement:
 Given a list of numbers, return a dict mapping each number to its square.

Example Calls:
 square_dict([2,3,4]) → {2:4, 3:9, 4:16}
"""

def square_dict(seq):
    dic = {}
    for key in seq:
        dic.update({key : key**2})
    return dic

print("squre of eys:", square_dict([2,3,4]))

"""
2.6 Dictionary comprehension — Problem: even_squares_dict
Problem Statement:
 Return a dict mapping each even integer in a list to its square.

Example Calls:
 even_squares_dict([1,2,3,4]) → {2:4,4:16}
"""

def even_squares_dict(seq):
    dic = {}
    for item in seq:
        if item % 2 == 0:
            dic.update({item : item **2})
    return dic

print("squares of evens:", even_squares_dict([1,2,3,4]))

"""
5.6 Merging dictionaries — Problem: merge_sum_values
Problem Statement:
 Given two dicts with numeric values, merge them.
 If a key appears in both, sum their values.
Example Calls:
 merge_sum_values({"a":2,"b":3},{"b":4,"c":1}) → {"a":2,"b":7,"c":1}
 """

def merge_sum_values(dic1, dic2):
    new_dic = dic1
    for key, val in dic2.items():
        if key in new_dic:
            new_dic[key] += val
        else:
            new_dic.update({key : val})
    return new_dic

print("merge dics:", merge_sum_values({"a":2,"b":3},{"b":4,"c":1}))

"""
5.7 Conditional update — Problem: update_if_greater
Problem Statement:
 Given a dict scores and new dict updates, update only if the new value is greater.
Example Calls:
 update_if_greater({"a":3,"b":1}, {"a":5,"b":0}) → {"a":5,"b":1}
 """

def update_if_greater(dic1, dic2):
    new_dic = dic1
    for key, val in dic2.items():
        if key in new_dic:
            if new_dic[key] < val:
                new_dic[key] = val
        else:
            new_dic.update({key : val})  
    return new_dic  

print("update if greater:", update_if_greater({"a":3,"b":1}, {"a":5,"b":0}))