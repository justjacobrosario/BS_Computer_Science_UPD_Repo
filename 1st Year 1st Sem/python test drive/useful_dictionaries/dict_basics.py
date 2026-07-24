"""
1.1 Key-Value Initialization — Problem: build_mapping
Problem Statement
 Given two lists of equal length, one containing keys and 
 the other containing values, build a dictionary that maps 
 each key to the corresponding value.
Example Calls
 build_mapping(("a","b","c"), (1,2,3)) → {"a":1,"b":2,"c":3}
 build_mapping((),()) → {}
"""

def build_mapping(keys, values):
    res = {}
    for i, k in enumerate(keys):
        for j, v in enumerate(values):
            if i == j:
                res.update({k : v})
    return res

print("dic builder:", build_mapping(("a","b","c"), (1,2,3)))

"""
1.2 Access & Membership — Problem: safe_lookup
Problem Statement
 Retrieve the value associated with a given key, returning "NOT_FOUND" if the key does not exist.
Example Calls
 safe_lookup({"a":1,"b":2}, "b") → 2
 safe_lookup({"a":1,"b":2}, "z") → "NOT_FOUND"
 """

def safe_lookup(dic, key):
    if key in dic:
        return dic[key]
    else:
        return "NOT FOUND"

print("key check:", safe_lookup({"a":1,"b":2}, "z"))

"""
1.3 Update or Add Key — Problem: set_or_update
Problem Statement
 Given a dictionary and a key-value pair, update the value if key exists, otherwise insert it.
Example Calls
 set_or_update({"x":10}, "x", 99) → {"x":99}
 set_or_update({"x":10}, "y", 20) → {"x":10, "y":20}
"""

def set_or_update(dic, key, val):
    dic.update({key : val})
    return dic

print("add / update:", set_or_update({"x":10}, "y", 20))  

"""
1.4 Delete Key Safely — Problem: remove_if_exists
Problem Statement
 Delete a key from a dictionary if it exists. Do nothing otherwise.
Example Calls
 remove_if_exists({"a":1,"b":2}, "a") → {"b":2}
 remove_if_exists({"a":1}, "x") → {"a":1}

"""

def remove_if_exists(dic, key):
    if key in dic:
        del dic[key]
        return dic
    else:
        return dic

print("remove if exists:", remove_if_exists({"a":1,"b":2}, "a"))

"""
1.5 Traversing keys — Problem: sum_of_values_with_prefix
Problem Statement:
 Given a dictionary mapping string keys to int values, and a string prefix, sum all values whose keys start with that prefix.
Example Calls:
 sum_of_values_with_prefix({"ab":3, "ax":2, "bb":5}, "a") → 5
"""

def sum_of_values_with_prefix(dic, prefix):
    res = 0
    for key in dic:
        if prefix in key:
            res += dic[key]
    return res

print("sum of values in key with a prefix:", sum_of_values_with_prefix({"ab":3, "ax":2, "bb":5}, "a"))

"""
1.4 Traversing items — Problem: invert_dict
Problem Statement:
 Given a dict d: str→int, invert it into int→list[str].
 Preserve the order of appearance.
Example Calls:
 invert_dict({"a":1,"b":2,"c":1}) → {1:["a","c"], 2:["b"]}
"""

def invert_dict(dic):
    new_dic = {}
    for key in dic:
        if dic[key] not in new_dic:
            new_dic.update({dic[key] : [key]})
        else:
            new_dic[dic[key]].append(key)
    return new_dic

print("invert:", invert_dict({"a":1,"b":2,"c":1}))

"""
1.5 Traversing values — Problem: average_value
Problem Statement:
 Compute the average of all values in a dictionary.
 Return 0 for an empty dict.
Example Calls:
 average_value({"a":2,"b":4}) → 3
 average_value({}) → 0
"""

def average_value(dic):
    if len(dic) == 0:
        return 0
    else:
        res = 0
        for value in dic.values():
            res += value
        return int(res // len(dic.values()))

print("avg val:", average_value({"a":2,"b":4}))

"""
1.6 Nested dictionary traversal — Problem: flatten_nested_dict
Problem Statement:
 Given a nested dict like {"a":{"x":1,"y":2},"b":{"z":3}}, return a flat dict mapping "a.x"→1, "a.y"→2, "b.z"→3.
Example Calls:
 flatten_nested_dict({"a":{"x":1},"b":{"y":2}}) → {"a.x":1, "b.y":2}
"""

def flatten_nested_dict(dic):
    flattened = {}
    for key in dic:
        for subkey in dic[key]:
            flattened.update({f"{key}.{subkey}" : dic[key][subkey]})
    return flattened

print(flatten_nested_dict({"a":{"x":1},"b":{"y":2}}))
