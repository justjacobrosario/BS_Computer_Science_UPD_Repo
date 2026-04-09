---
year: 1
subject: CS12
field: programming
language: python
---

# Python Syntax & Algorithms Notes

## ■■■■■■■ GENERAL SYNTAX ■■■■■■■

1. **Indentation-sensitive** - Python uses indentation to define code blocks
2. **Newline allowed for collection data types**
```python
like_this = [1,
    2,
    3
]
```

---

## ■■■■■■■ VARIABLES ■■■■■■■

### ◩◩◩ BASE DATA TYPES ◩◩◩

```python
_str = "Hello World"
_int = 67
_float = 3.14
_boolean = True
_null = None
```

#### ◩◩◩ STRINGS ◩◩◩

**1. Concatenation** (add at the end)
```python
flower = "bulak" + "lak"  # bulaklak
```

**2. Multiplication** (number of string copies)
```python
flowers = flower * 2  # bulaklakbulaklak
```

**3. Membership** (in)
```python
lak_here = "lak" in flower  # True
```

**4. String Indexing & Slicing**

Python is zero-indexed

** Indexing **: `var[nth index]`
```python
name = "Python"
first, last = (name[0], name[-1])  # negative starts from end
```

** Complex Indexing **: `var[start(inclu.):end(exclu.):step]`
```python
am = name[2:4]     # th
enam = name[::-1]  # nohtyP (reversed)
```

** Slicing **: `var[inclusive start:exclusive end]`
```python
first_3 = name[:3]  # Pyt (0th, 1st, 2nd index only)
last_3 = name[3:]   # hon
```

** Character & ASCII **
```python
# ord() - char to ascii
ascii_name = ord(name)

# chr() - ascii to char
char_name = chr(ascii_name)
```

** Formats **
```python
str = 'abcdefghij'
# Alignments: :>n (right), :<n (left), :^n (center)
print(f'{str:>11}')  # right alignment, 11 slots
```

#### ◩◩◩ INTEGERS ◩◩◩

**1. Formats**
```python
int = 123
print(f'{int:011b}')  # binary
print(f'{int:011o}')  # octal
print(f'{int:011}')   # decimal
```

#### ◩◩◩ TUPLES ◩◩◩

**1. Creating tuples**
```python
# tuple()
not_a_tuple = [1, 2]
now_a_tuple = tuple(not_a_tuple)  # (1, 2)

# Trailing-commas for one-tuple
di_tuple = (1)     # Not a tuple!
tuple_ito = (1,)   # This is a tuple
```

**2. Destructuring-bind**
```python
x_val, y_val = (2, 1)
```

**3. .join()** - connect tuple elements as string
```python
tuple_1 = ('super', 'hero')
wat = "_".join(tuple_1)  # super_hero
```

---

#### ◩◩◩ CONTAINER DATA TYPES ◩◩◩

**Immutable (Tuples and Frozensets) **
```python
_tuple = (x, y)                    # immutable, ordered
_frozenset = frozenset({3, 1, 2})  # immutable, unordered
```

**Mutable (Lists, Sets, Dictionaries)  **
```python
_list = [1, 2, 3]               # mutable, ordered
_set = {3, 1, 2}                # mutable, unordered
_dict = {a: 3, b: 1, c: 2}      # mutable, unordered, key-value pairs
```

---

## ■■■■■■■ OPERATORS ■■■■■■■

### ◩◩◩ ARITHMETIC ◩◩◩

```python
_plus = 1 + 1
_minus = 1 - 1
_multiply = 1 * 1
_divide = 1 / 1
_floor_div = 1 // 1
_modulo = 1 % 1

# Ceiling division
dividend, divisor = (5, 2)
_ceiling_div = (dividend + divisor - 1) // divisor
```

### ◩◩◩ COMPARISONS ◩◩◩

```python
# < > <= >= == !=
```

### ◩◩◩ LOGICAL OPERATORS ◩◩◩

```python
conjunction = "x and y"
disjunction = "x or y"
```

---

## ■■■■■■■ CONDITIONALS ■■■■■■■

Processing order layer:

```python
if 1 + 1 == 2:    # 1st process
    return ...
elif:             # 2nd process if 1st is False
    return ...
if 3 + 3 == 6:    # 1st process (independent)
    return ...
else:             # 3rd process if all are False
    ...
```

---

## ■■■■■■■ NOTHINGNESS ■■■■■■■

```python
none_value = None

if none_value:
    pass  # skips
    ...   # skips as well
```

---

## ■■■■■■■ MULTIPLE VARS, ARGS (SPLAT) ■■■■■■■ 

**Splatting** = Ungrouping

### ◩◩◩ SPLATTING VARIABLES ◩◩◩
Splatting variables returns ungrouped elements

```python
names = ("Jacob", "JB", "Clyde")
not_splatted = (names,)   # (("Jacob", "JB", "Clyde"),)
splatted = (*names,)      # ("Jacob", "JB", "Clyde")
```

### ◩◩◩ SPLATTING ARGS INSIDE FUNCTION BODY ◩◩◩
Splatting variables assigns a single parameter to a tuple

```python
num = (1, 2, 3)
def func(num):
    print(*num)

func(num)  # 1 2 3 instead of (1, 2, 3)
```

### ◩◩◩ SPLATTING ARGS IN FUNCTION PARAMS ◩◩◩'
Splatting params ungroups args into separate params

```python
func(*[1, 2]) == func(1, 2)

# Double-splatting converts dicts into kwargs
func(**{a: 1, b: 2}) == func(a=1, b=2)
```

---

## ■■■■■■■ ALGORITHMS IN PYTHON ■■■■■■■

### ■■■■■■■ RECURSION ■■■■■■■ 

**Pattern:**
```python
if base_case:
    return base_case_result
else:
    return recursive_case
```

**Example:**
```python
num = 123

def digit_sum(n):
    if n == n % 10:  # base_case
        return n     # base_case_result (final output)
    else:
        last_d = n % 10 
        return last_d + digit_sum(n // 10)  # recursive_case

print(digit_sum(num))
```