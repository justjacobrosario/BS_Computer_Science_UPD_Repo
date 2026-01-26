
# [[[ LECTURE 22 ]]]
# === [ 1. DEFAULT VALUES ] ===
# === [ 2. ARGS AND KWARGS ] ===
# === [ 3. SORTED() KWARGS ]

seq = [3, 1, 4, 1, 5]
seq2 = ["Happy", "BIRTHDAY", "to", "you"]

    # I. default functions as key
sorted_by_length = sorted(seq2, key = len)

    # II. customized functions as key

def lower_first(s):
    return (s[0].isupper(), s[0].islower())

same_thing = sorted(seq2, key=lower_first)
same_thing2 = sorted(seq2, key = lambda s: (s[0].isupper(), s[0].islower()))

# === [ 4. PRINT() KWARGS ] ===

like_this = ... #print("Happy", "Birthday", sep = "...", end = '\n\n', file = None)


# === [ 5. VARIADIC ARGS AND KWARGS ] ===

def func(*args, **kwargs):
    return f"Args like {args} dont need variable names\nbut kwargs like {kwargs} do."


# === [ 6. LAMBDA ] ===

def hello_x(x):
    return f"hello {x}!"

hello_x_2 = lambda x : f"hello {x}!"

x = "Jacob"
hello1 = hello_x("Jacob")
hello2 = hello_x_2("Jacob")

# === [ 7. TYPE HINTING ] ===

def hello_world(name:str) -> str:
    return f"Hello {name}!"






# [[[ L E C T U R E  2 3  ]]]
# === [ 1. MAP ] ===

def squares(seq):
    for item in seq:
        yield item**2

same_thing = [*squares((3, 1, 4))]
    #              operation to do   sequence
same_thing2= [*map((lambda x: x**2), (3, 1, 4))]
get_len_for_each = [*map(len, ("Happy", "Birthday", "brrt"))]

# === [ 2. FILTER ] ===

def get_even(seq):
    for item in seq:
        if item % 2 == 0:
            yield item

same_thing = [*get_even([3, 1, 4])]
    #                  condition to be True    sequence
same_thing2= [*filter((lambda x: x % 2 == 0), [3, 1, 4])]

# === [ 3. CLOSURES ] === ( func returns another func with vars of orig func )

def make_adder(x): # parent func
    def addx(y): # daughter func (converts variables to func)
        return x + y # operation of previous x and current y
    return addx # no ()

add5 = make_adder(5) # variable to func
    #print(add5(10))



# [[[ L E C T U R E  2 4 ]]]
# === [ 1. Named Tuples ] ===

from collections import namedtuple

City = namedtuple('City', ['name', 'population'])
city_lists = [City(name = 'Manda', population = 1000),
City(name = "QC", population = 5000)]

# === [ 2. Dataclass ] ===

from dataclasses import dataclass

@dataclass
class City:
    region : str
    population : int

Manda = City(region = "NCR", population = 1000)

#print(Manda.region)



# [[[ L E C T U R E  2 5 ]]]
# === [ 1. with Keyword ] ===
'''with open("name.txt") as name_ng_file:
    read_line = name_ng_file.readline()
    read_nth_charac = name_ng_file.read(100)
    read_rest = name_ng_file.read()'''


# === [ 2. Enums ] ===

from enum import Enum

class any_var_with_value(Enum):
    Var_1 = ("valueee")
    Var_2 = ("valueee")
    Var_3 = ("valueee")
    ...


# [[[ L E C T U R E  2 6 ]]]

# === [ 1. Classes ] ===

class City:
    def __init__(self, region, population):
        self.region = region
        self.population = population

    def paalisin(self, n):
        self.population -= n

    def padagdagan(self, n):
        self.padagdagan += n


Mandaluyong = City(region = "NCR", population = 10000)
Mandaluyong.paalisin(30)
print(Mandaluyong.population)

