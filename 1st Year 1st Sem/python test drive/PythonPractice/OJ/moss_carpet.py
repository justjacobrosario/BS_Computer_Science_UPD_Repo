def carpet(r, c, r1, c1, i, j):
    return ((("." * c) + "\n") * i) + ((("." * j) + ("#" * c1) + ("." * (c - j - c1)) + "\n") * r1) + ((("." * c + "\n") * (r - i - r1)))


print(carpet(6, 9, 3, 4, 1, 2))