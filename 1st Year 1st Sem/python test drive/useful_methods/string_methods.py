"""
Part A — String Methods (split, join, strip, find, replace, lower/upper, startswith, isdigit, format, etc.)
A1 split — Problem: split_words

Problem Statement
Given a sentence, return a list of words split by whitespace (any amount).

Example Calls
split_words(" hello world ") -> ["hello","world"]
"""

def split_words(strng):
    return strng.strip().split(" ")


print(".split(" "):", split_words(" hello world "))


"""
A2 join — Problem: join_with_comma
Problem Statement
 Given a list of strings, return a single string of them joined by ", ".

Example Calls
 join_with_comma(["a","b","c"]) -> "a, b, c"
"""

def join_with_comma(seq):
    return ", ".join(seq)

print("join. : ", join_with_comma(["a","b","c"]))

"""
A3 strip / lstrip / rstrip — Problem: trim_lines
Problem Statement
 Given list of strings, trim whitespace from both ends of each line and return list.

Example Calls
 trim_lines([" hi ", "bye "]) -> ["hi", "bye"]
"""

def trim_lines(seq):
    new_seq = []
    for item in seq:
        new_seq.append(item.strip())
    return new_seq

print(".strip() each item: ", trim_lines([" hi ", "bye "]))

"""
A4 find / rfind — Problem: first_occurrence_index
Problem Statement
 Return index of first occurrence of substring pat in s, or -1 if not found. (Use str.find.)

Example Calls
 first_occurrence_index("hello world","lo") -> 3
 first_occurrence_index("abc","z") -> -1
"""

def first_occurrence_index(strng, pattern):
    return strng.find(pattern)

print("strng.find(x) to get indx of first x:", first_occurrence_index("hello world","l"))

"""
A5 replace — Problem: replace_bad_word
Problem Statement
 Replace all occurrences of bad with *** and return new string.

Example Calls
 replace_bad_word("this is bad and bad", "bad") -> "this is *** and ***"
"""

def replace_bad_word(strng, x):
    return strng.replace("***", x)


print("strng.replace(\"***\", \"bad\"): ", replace_bad_word("this is bad and bad", "bad"))

"""
A6 lower / upper / casefold — Problem: normalize_case
Problem Statement
 Return lowercase version of a string (normalize for comparisons).

Example Calls
 normalize_case("HeLLo") -> "hello"
 """

def normalize_case(strng):
    return strng.lower()

print(".lower():", normalize_case("HeLLo"))

"""
A7 startswith / endswith — Problem: filter_by_prefix
Problem Statement
 Given list of strings and a prefix, return list of those that start with that prefix.

Example Calls
 filter_by_prefix(["apple","bat","ant"], "a") -> ["apple","ant"]
"""

def filter_by_prefix(seq, pref):
    res = []
    for item in seq:
        if item.startswith(pref):
            res.append(item)
    return res

print("strng.startswith(x):", filter_by_prefix(["apple","bat","ant"], "a"))

"""
A8 isdigit / isalpha — Problem: separate_digits_and_words
Problem Statement
 From a list of tokens, produce dict {"digits":[...],"words":[...]} by testing tokens.

Example Calls
 separate_digits_and_words(["123","hi","45a"]) -> {"digits":["123"], "words":["hi"]}
 """

def separate_digits_and_words(seq):
    dic = {
    "digits" : [],
    "words" : []
    }

    for item in seq:
        if item.isalpha():
            dic["words"].append(item)
        elif item.isdigit():
            dic["digits"].append(item)
    return dic

print("filter digits and alphas:", separate_digits_and_words(["123","hi","45a"]))

"""
A9 format / f-strings — Problem: format_report
Problem Statement
 Given name and score, return "Name: <name>, Score: <score>" using format method.

Example Calls
 format_report("Ana", 95) -> "Name: Ana, Score: 95"
"""

def format_report(n, s):
    return f"Name: {n}, Score: {s}"

print("f-strng:", format_report("Ana", 95))

"""
A10 partition / split with maxsplit — Problem: head_and_rest
Problem Statement
 Return (head, rest) splitting by first comma; rest has the remainder string.

Example Calls
 head_and_rest("a,b,c") -> ("a","b,c")
 head_and_rest("no comma") -> ("no comma","") (or per partition spec)
 """

def head_and_rest(strng):
    return strng.split(",", 1)


print(head_and_rest("a,b,c"))
