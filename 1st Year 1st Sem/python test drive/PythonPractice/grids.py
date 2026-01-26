def grid_for_loop(row, column, symbol):
    for x in range(1, row + 1):
        for y in range(1, column + 1):
            print(symbol, end=" ")
        print()

def grid_compre(row, column, symbol):
    return ("\n".join(
        " ".join(symbol for x in range(column))
            for y in range(row)))


# x horizontal displacement
# y = vertical displacement
# start with (0,0)
def grid_coordinates_for_loop(x1, y1, x2, y2):
    highx, lowx = (my_max(x1, x2), my_min(x1, x2))
    highy, lowy = (my_max(y1, y2), my_min(y1, y2))
    row = highx - lowx + 1
    column = highy - lowy + 1

    for y_coor in range(1, column + 1):
        for x_coor in range(1, row + 1):
            print((x_coor, y_coor), end=" ")
        print()

def grid_coordinates_compre(x1, y1, x2, y2):
    highx, lowx = (my_max(x1, x2), my_min(x1, x2))
    highy, lowy = (my_max(y1, y2), my_min(y1, y2))
    row = highx - lowx + 1
    column = highy - lowy + 1

    return ("\n".join(
        " ".join(f"{(x_coor, y_coor)}" for x_coor in range(1, row + 1))
            for y_coor in range(1, column + 1)))

def diagonal_grid_compre(n, symbol):
    column = n
    row = n
    return "\n".join(
        " ".join(symbol if x == y else "." for x in range(column))
        for y in range(row))




def my_max(*seq):
    if len(seq) == 1:
        return seq[0]
    else:
        if seq[0] > my_max(*seq[1:]):
            return seq[0]
        else:
            return my_max(*seq[1:])

def my_min(*seq):
    if len(seq) == 1:
        return seq[0]
    else:
        if seq[0] < my_max(*seq[1:]):
            return seq[0]
        else:
            return my_max(*seq[1:])

print(grid_coordinates_for_loop(1, 1, 3, 4))
print(grid_coordinates_compre(1, 1, 3, 4))
#grid_for_loop(3, 4, "#")