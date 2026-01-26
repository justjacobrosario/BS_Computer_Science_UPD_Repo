def trace_square(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    return tuple((x, y) for x in range(x1, x2 + 1) 
        for y in range(y1, y2 + 1) 
        if ((x == x1) or (x == x2) or (y == y1) or (y == y2)))
"""
    print()

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x == ((x1+x2)//2)) and (y == ((y1+y2)//2)):
                print("1", end=" ")
            else:
                print("I", end=" ")
        print()
"""
print(trace_square((5, 5), (15, 15)))