def streaks(x1, y1, x2, y2, dart_coords):
    if dart_coords == ():
        return ()
    else:
        if (dart_coords[0][0] >= x1) and (dart_coords[0][0] <= x2) and (dart_coords[0][1] >= y1) and (dart_coords[0][1] <= y2) and (dart_coords[1][0] >= x1) and (dart_coords[1][0] <= x2) and (dart_coords[1][1] >= y1) and (dart_coords[1][1] <= y2):
            return (dart_coords[0], dart_coords[1]) + streaks(x1, y1, x2, y2, dart_coords[2:])
        elif (dart_coords[0][0] >= x1) and (dart_coords[0][0] <= x2) and (dart_coords[0][1] >= y1) and (dart_coords[0][1] <= y2):
            return (dart_coords[0],) + (streaks(x1, y1, x2, y2, dart_coords[1:]),)
        else:
            return streaks(x1, y1, x2, y2, dart_coords[1:])

print(streaks(-20, -10, 20, 10, (
    (0, 0),
    (500, 0),
    (1, 1),
    (1, 1),
    (-1, 9),
    (1, 1000),
    (20, 11),
    (1, 1),
    (2, 3),
)))

#(((0, 0),), ((1, 1), (1, 1), (-1, 9)), ((1, 1), (2, 3)),)