def num_of_evens(tup):
    if len(tup) == 1:
        if tup[0] % 2 == 0:
            return 1
    else:
        if tup[0] % 2 == 0:
            return 1 + num_of_evens(tup[1:])
        elif tup[0] % 2 != 0:
            return num_of_evens(tup[1:])

#2, 4, 6, 8
print(num_of_evens((1, 2, 3, 4, 5, 6, 7, 8)))