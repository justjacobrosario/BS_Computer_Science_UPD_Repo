
''' 1. Parts of Recursive Funcs '''

def div_by_9_between(a, b):
    if a > b: # base case
        return ()
    else: # recursive case
        if a % 9 == 0: # conditions
            current = (a,) 
        else:
            current = ()
        return current + div_by_9_between(a+1, b) # recursive return val



def floor_sum(n, a, b):
    if a > b:
        return 0
    else:
        addend = n//a
        return addend + floor_sum(n, a+1, b)

def darts_landed(x1, y1, x2, y2, dart_coords):
    if not dart_coords:
        return 0

    else:
        x, y = (dart_coords[0][0], dart_coords[0][1])
        if x1 <= x <= x2 and y1 <= y <= y2:
            return 1 + darts_landed(x1, y1, x2, y2, dart_coords[1:])
        else:
            return darts_landed(x1, y1, x2, y2, dart_coords[1:])


def fix_music(seq):
    if not seq:
        return ()
    else:
        current = seq[-1]
        return (current[::-1],) + fix_music(seq[:-1])

''' 2. Considering Data Types '''
# if the return value is a tuple of a data type, 
# just return (<that_data>,) + <recursive call>

# if the retun value is a tuple of tuples
# return ((<that_data>,),) + <recursive call>

def matches(a, b):
    if not a or not b:
        return ()
    else:
        a_player = a[0]
        b_player = b[0]
        return ((a_player, b_player),) + matches(a[1:], b[1:])

def buy_cheapest(seq):
    if ...:
        return ...
    else:
        current = seq[0]
        if current 


print(buy_cheapest((31, 41, 59, 26, 53)))
