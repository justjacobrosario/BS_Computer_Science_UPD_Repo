"""
Part 4 — Aggregation (subtypes 4.1–4.3)

4.1 Sum per Key — Problem: sum_sales_by_store
Problem Statement
 Given sales data as (store, amount), sum all amounts per store.
Task Details
 Implement sum_sales_by_store(pairs) returning {store: total_sales}.
Restrictions
 No comprehensions. Use .get().
Example Calls
 sum_sales_by_store((("A",100),("B",50),("A",20))) → {"A":120,"B":50}
 """

def sum_sales_by_store(seq):
    dic = {}
    for key, val in seq:
        if key not in dic:
            dic.update({key : val})
        else:
            dic[key] += val
    return dic

print("sum of vals:", sum_sales_by_store((("A",100),("B",50),("A",20))))

"""
4.2 Average per Category — Problem: average_scores
Problem Statement
 Given (subject, score) pairs, return a dictionary mapping each subject to its average score.
Task Details
 Implement average_scores(pairs) returning {subject: avg}.
Restrictions
 Use two dicts (sum and count). No comprehensions.
Example Calls
 average_scores((("Math",90),("Math",80),("English",70))) → {"Math":85,"English":70}
"""

def average_scores(seq):
    dic = {}
    for sub, score in seq:
        if sub not in dic:
            dic.update({sub : [score]})
        else:
            dic[sub].append(score)
    
    new_dic = {}
    for key, val in dic.items():
        if len(val) > 1:
            new_dic.update({key : sum(val) // len(val)})
        else:
            new_dic.update({key : val[0]})

    return new_dic

print("avg scores:", average_scores((("Math",90),("Math",80), ("Math",70),("English",70))))
print(sum([90, 80, 70]) // 3)

"""
4.3 Count and Sum per Key — Problem: aggregate_transactions
Problem Statement
 For each customer, compute both total transactions and number of transactions.

Example Calls
 aggregate_transactions((("Ann",50),("Bob",20),("Ann",70))) → {"Ann":{"count":2,"total":120},"Bob":{"count":1,"total":20}}
"""

def aggregate_transactions(seq):
    dic = {}
    for name, num in seq:
        if name not in dic:
            dic.update({name : { "count" : 1, "total" : num}})
        else:
            dic[name]["count"] += 1
            dic[name]["total"] += num

    return dic


print("aggregate transactions:", aggregate_transactions((("Ann",50),("Bob",20),("Ann",70))))

"""
4.4 Maximum key-value — Problem: max_value_key
Problem Statement:
 Return the key with the highest value.
Example Calls:
 max_value_key({"a":3,"b":9,"c":5}) → "b"
 """

def max_value_key(seq):
    biggest = ""
    biggest_val = 0
    for key, val in seq.items():
        if biggest_val == 0:
            biggest_val = val
            biggest = key
        elif val > biggest_val:
            biggest_val = val
            biggest = key
    return biggest

print("key of biggest value:", max_value_key({"a":3,"b":9,"c":5}))

"""
4.2 Minimum key-value — Problem: min_value_key
Problem Statement:
 Return the key with the lowest value.
Example Calls:
 min_value_key({"a":3,"b":9,"c":5}) → "a"
 """

def min_value_key(seq):
    smallest = ""
    smallest_val = 0
    for key, val in seq.items():
        if smallest_val == 0:
            smallest_val = val
            smallest = key
        elif val < smallest_val:
            smallest_val = val
            smallest = key
    return smallest

print("key of smallest value:", min_value_key({"a":3,"b":9,"c":5}))