def carpet(r, c, r1, c1, i, j):
    if r == 0:
        return ()
    else:
        return ("."*c,) * i + ("."*j + "#"*c1 + "."*(c - (j + c1)),) * r1 + ("."*c,) * (r - (i + r1)) 

print(carpet(6, 9, 3, 4, 1, 2))