def bacteria_counts(b, n):
    if n == 0:
        return ()
    else:
        current = ((int(b)),)
        return current + bacteria_counts(b * 2, n - 1)

print(bacteria_counts(3, 4))

    #3, 4
    #3, 6, 12, 24