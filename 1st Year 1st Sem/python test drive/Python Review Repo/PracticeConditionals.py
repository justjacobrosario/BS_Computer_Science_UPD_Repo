
def greater(g, r):
    return g > r

def in_either_interval(a, b, c, d, y):
    return a <= y <= b or c <= y <= d


# Manhattan Distance Formula d = abs(dx) + abs(dy)
def will_get_boomed(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2-y1) <= 4

# Geometric progression Pattern : has same common ratio
# ❗UNSOLVED
def is_geometric_progression(r, g, y):
    return g/r == y/g if y != 0 and r != 0 and g != 0 else True

# ❗UNSOLVED
def is_pavivo(word):
    return (word[0] == word[-1] and word[0] in 'aeiou') or len(word) != 0
    #return (word.startswith('a') or word.startswith('e') or word.startswith('i') or word.startswith('o') or word.startswith('u')) and (word.endswith('a') or word.endswith('e') or word.endswith('i') or word.endswith('o') or word.endswith('u'))

# Standard distance formula
def are_kingly_adjacent(x1, y1, x2, y2):
    return int(((x2-x1)**2 + (y2-y1)**2)**(1/2)) == 1



def on_either_axis(a, b):
    return a == 0 or b == 0

def in_neither_half_interval(a, b, c, d, y):
    return not(a <= y <= (b - 1)) and not(c <= y <= (d - 1))

# ❗UNSOLVED
def possibly_triangular(a, b, c):
    return ((a+b) > c) or ((b+c) > a) or ((a+c) > b)
# ❗UNSOLVED
def pigeonhole(p, b, l):
    return p//b == l
