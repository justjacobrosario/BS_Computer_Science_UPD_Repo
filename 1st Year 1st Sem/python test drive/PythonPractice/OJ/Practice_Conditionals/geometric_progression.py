def is_geometric_progression(r, g, y):
    return (g != 0 and r != 0) and (g / r == y / g)

print(is_geometric_progression(1, 2, 4))

"""

    r = 2
    g = 4
    y = 8

    1(2) = 2
    2(2) = 4
    4(2) = 8

    """