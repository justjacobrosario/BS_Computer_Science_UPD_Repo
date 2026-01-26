"""
Part 3 — Filtering & Extraction (subtypes 3.1–3.3)
3.1 Filter by condition — Problem: primes_from_list

Problem Statement
Given a list of positive integers, return all primes among them (order preserved). Use naive primality test per element.

Example Calls
primes_from_list((4,5,6,7,11,12)) → [5,7,11]
primes_from_list((1,1,2)) → [2] (1 is not prime)

"""

def primes_from_list(seq):
    primes = []
    for num in seq: #checks all num in seq
        _is_prime_if_True = True #base condition, if proven composite, its False

        if num < 2: #base case, 0 and 1 is false
            continue

        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                _is_prime_if_True = False
                break

        if _is_prime_if_True == True:
            primes.append(num)

    return primes

print(primes_from_list((0, 1, -3, 2,4,5,6,7,11,12)))

"""
3.2 Reject/exclude items — Problem: remove_multiples_of_k

Problem Statement
Return the sequence with all numbers that are multiples of k removed.

Example Calls
remove_multiples_of_k((6,7,12,13,18), 6) → [7,13]
remove_multiples_of_k((), 2) → []
"""

def remove_multiples_of_k(seq, k):
    res = []
    for num in seq:
        if num % k != 0:
            res.append(num)
    return res

print(remove_multiples_of_k((6,7,12,13,18), 6))

"""
3.3 Unique filter using a set — Problem: preserve_first_unique

Problem Statement
Return the list of elements with duplicates removed while preserving first occurrence order.

Example Calls
preserve_first_unique((1,2,2,3,1)) → [1,2,3]
preserve_first_unique(("a","b","a")) → ["a","b"]

"""

def preserve_first_unique(seq):
    res = []
    for num in seq:
        if num not in res:
            res.append(num)
    return res

print(preserve_first_unique((1,2,2,3,1)))