def darts_landed(x1, y1, x2, y2, dart_coords):
    return darts_landed_with_i(x1, y1, x2, y2, dart_coords, 0)

def darts_landed_with_i(x1, y1, x2, y2, dart_coords, i):
    if i > len(dart_coords):
        return 0

    else:
        if dart_check(x1, y1, x2, y2, dart_coords[i]) == True:
            pasado = 1 
        else:
            pasado = 0 #uncertain sa 0
        return pasado + darts_landed_with_i(x1, y1, x2, y2, dart_coords[i+1], i+1)

def dart_check(x1, y1, x2, y2, dart_coords):
    x, y = dart_coords
    if (x1 <= x and x2 >= x) and (y1 <= y and y2 >= y):
        return True
    else: 
        return False

print(darts_landed(0, 0, 5, 5, ((1, 1))))

#print(dart_check(0, 0, 5, 5, (6, 2)))

"""def double(x):
    return len(x)

print(double(((2, 3), (3, 4), (4, 5))))"""