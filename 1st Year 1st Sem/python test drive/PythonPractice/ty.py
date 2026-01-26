def evens_and_odds(seq):
    evens = []
    odds = []
    res = (evens, odds)

    for x in seq:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    return res

print(evens_and_odds([3, 1, 4, 1, 5, 9, 2]))