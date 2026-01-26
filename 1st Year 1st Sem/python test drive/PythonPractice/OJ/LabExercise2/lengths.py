def strings_by_length(word):
    if word == ():
        return ()

    word_len = frozenset(len(n) for n in word)
    min_len, max_len = min(word_len), max(word_len)


    return tuple(
        (x, tuple(y for y in word if x == len(y))) 
        for x in range(min_len, max_len + 1) 
        if x in word_len)


"""
1. pwede mag compre sa loob ng compre
2. assume properly, not all values from min to max is included
3. expect exceptions


    for x in range(min_len, max_len + 1):
        for y in word[0]:
            if x == len(y):
                print(x,y)
"""

print(strings_by_length(()))