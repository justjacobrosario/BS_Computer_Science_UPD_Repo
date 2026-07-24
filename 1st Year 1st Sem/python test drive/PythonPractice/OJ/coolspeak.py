def distinct_letter_count(word):
    return len(frozenset(word))

print(distinct_letter_count("banana"))