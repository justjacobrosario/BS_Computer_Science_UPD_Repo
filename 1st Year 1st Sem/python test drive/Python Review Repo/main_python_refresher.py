""" ■■■■■■■ GENERAL SYNTAX ■■■■■■■ """

# 1. Indentation-sensitive
# 2. Newline allowed for collection data types
    like_this = [1,
    2,
    3
    ]


""" ■■■■■■■ VARIABLES ■■■■■■■ """

'''◩◩◩ BASE DATA TYPES ◩◩◩'''

_str = "Hello World"
_int = 67
_float = 3.14
_boolean = True
_null = None

    #◩◩◩ STRING ◩◩◩#

    # Concatenation (add at the end)
        flower = "bulak" + "lak" # bulaklak

    # Multiplication (no. of str copies)
        flowers = flower * 2 # bulaklakbulaklak

    # Membership (in)
        lak_here = "lak" in flower # True

    # String Indexing & Slicing
        # python is zero-indexed

        # Indexing ( <var>[nth index] )
            name = "Python"
            first, last = (name[0], name[-1]) # negative starts from end # also I did destructuring bind

        # Complex Indexing ( <var>[ start (inclu.) : end (exclu.) : step(negative if reversed) ])
            am = name[2:4] # th
            enam = name[::-1] # nohtyP

        # Slicing <var>[ inclusive start : exclusive end ]
            first_3 = name[:3] # Pyt # notice that it exclusively chose 0th, 1th, 2th index (no 3th)
            last_3 = name[:3] # hon

        # Copying <var>[:]
            x = [1]
            y = x[:] # y is a separate list from x
            y.append(2)
            print(x, y) # [1] [1, 2]

    # Charac & ASCII
        # ord() char to ascii
            ascii_name = ord(name)
        # cr() ascii to char
            char_name = cr(ascii_name)

    # Formats
        str = 'abcdefghij'
        # alignments :>n, :<n, :^n
        print(f'{str:>11}') # left aligment, 11 slots

    # Things to recall

        # 1. use .strip() to remove unwanted edge spaces

    #▤▤▤ INTEGERS ▤▤▤#

    # Formats
        int = 123
        #int = 30
print(f'{int:011b}')
print(f'{int:011c}')
print(f'{int:011}')


    #▤▤▤ TUPLES ▤▤▤#

    # tuple()
        not_a_tuple = [1, 2]
        now_a_tuple = tuple(not_a_tuple) # (1, 2)

    # Trailing-commas for one-uple
        di_tuple = (1)
        tuple_ito = (1,)

    # Destructuring-bind
        x_val, y_val = (2, 1)

    # .join() connect tuple elements as str
        tuple_1 = ('super', 'hero')
        wat = "_".join(tuple_1) # super_hero



'''◩◩◩ CONTAINER DATA TYPES ◩◩◩'''

_tuple = (x, y) # immutable, ordered
_frozenset = frozenset(3, 1, 2) # immutale, unordered

_list = [1, 2, 3] # mutable, ordered
_set = {3, 1, 2} # mutable, unordered
_dict = {a : 3, b : 1, c : 2} # mutable, unordered, input-output pair


""" ■■■■■■■ OPERATORS ■■■■■■■ """

'''◩◩◩ ARITHMETIC ◩◩◩'''

_plus = 1 + 1
_minus = 1 - 1
_multiply = 1 * 1
_divide = 1 / 1
_floor_div = 1 // 1
_modulo = 1 % 1

dividend, divisor = (5, 2)
_ceiling_div = (dividend + divisor - 1) // divisor

'''◩◩◩ COMPARISONS ◩◩◩'''

eyy = " < > <= >= == != "

'''◩◩◩ COMPARISONS ◩◩◩'''

conjunction = " x and y "
disjunction = " x or y "

""" ■■■■■■■ CONDITIONALS ■■■■■■■ """

# processing order layer

if 1 + 1 == 2: # 1st process
    return ...
elif:               # 2nd process if 1st process are False
    return ...
if 3 + 3 == 6: # 1st process
    return ...
else:                    # 3rd process if all are False
    ...

""" ■■■■■■■ NOTHINGNESS ■■■■■■■ """

none_value = None

if none_value:
    pass # skips
    ... # skips as well


""" ■■■■■■■ MULTIPLE VARS, ARGS (SPLAT) ■■■■■■■ """
# Splatting = Ungrouping

'''◩◩◩ SPLATTING VARIABLES ◩◩◩'''
# Splatting variables returns an ungrouped elements

names = ("Jacob", "JB", "Clyde")
not_splatted = (names,) # (("Jacob", "JB", "Clyde"),) # returns the whole name tuple
splatted = (*names,) # ("Jacob", "JB", "Clyde") # returns the splatted elements

'''◩◩◩ SPLATTING ARGS INSIDE FUNCTION BODY ◩◩◩'''
# Splatting variables assigns a single parameter to a tuple

num = (1, 2, 3)
def func(num):
    print(*num)

func(num) # 1 2 3 instead of (1, 2, 3)

'''◩◩◩ SPLATTING ARGS IN FUNCTION PARAMS ◩◩◩'''
# Splatting params ungroups args into separate params

func(*[1, 2]) == func(1, 2)

# Double-splatting params convrts dicts into kwargs

func(*{a:1, b:2}) == func(a=1, b=2)

""" ■■■■■■■ PYTHONIC FEATURES & SHORTCUTS ■■■■■■■ """

'''◩◩◩ TRUTHY AND FALSY COLLECTIONS ◩◩◩'''
# non-empty -> True , empty -> False

x, y = ([], [1])
if y: # instead of if len(y) > 0:
    print('ey')

'''◩◩◩ NEGATIVE INDEXING = REVERSED ◩◩◩'''

name = 'python'
print(name[-1]) # instead of name[len(name) - 1]

'''◩◩◩ STRING INTERPOLATION INSTEAD OF CONCATENATION ◩◩◩'''

a, b = ('kala', 'pati')

print(f'{a}{b}') # kalapati ; instead of a + b

'''◩◩◩ ONE-LINER CONDITIONAL STATEMENTS ◩◩◩'''

n = 2
print(f'{n} is even') if n%2 == 0 else print(f'{n} is odd')

'''◩◩◩ DESTRUCTURING BIND ◩◩◩'''

    # instead of
        a = 1
        b = 2
    # use destructuring bind
        a, b = (1, 2)

'''◩◩◩ SPLATTING ◩◩◩'''

    '''▤▤▤ LISTS & TUPLES ▤▤▤'''
    a, b  = ([20, 30], [50, 60])
    # instead of
    c = [10] + a + [40] + b
    # use splatting
    c = [10, *a, 40, *b]

    '''▤▤▤ DICTIONARIES (USE **) ▤▤▤'''
    a, b = ({'x' : 1}, {z : 3})
    # instead of
    c = a | {'y' : 2} | b
    # use double splatting
    c = {**a, 'y'}

""" ■■■■■■■ ALGORITHMS IN PYTHON ■■■■■■■ """
'''
____ _    ____ ____ ____ _ ___ _  _ _  _ ____                                                                                                                 
|__| |    | __ |  | |__/ |  |  |__| ||/| [__                                                                                                                  
|  | |___ |__] |__| |  | |  |  |  | |  | ___]
'''

""" ■■■■■■■ RECURSION ■■■■■■■ """
if base_case:
    return base_case_result
else:
    return recursive_case

# e.g.

num = 123

def digit_sum(n):
    if n == n%10: # base_case
        return n # base_case_result (final output)
    else:
        last_d = n%10 
        return last_d + digit_sum(n//10) # recursive_case

print(digit_sum(num))

