# CS 12 Lectures 1-2

## [[ LECTURE 1 : TYPE HINTING IN PYTHON ]]

### [ ■ [1] [Type Hinting] ■ ]
: declares the type for vars, funcs, return vals, args, and kwargs.
: makes code more readable and allows type checking

### [ ■ [2] [Types of Type Checking] ■ ]

#### === 1. Static Type Checking ===
: Types are checked before running the code
: use pyright, pylance, etc

#### === 2. Dynamic Type Checking ===
: types are checked while code is running line by line
: default in Python

### [ ■ [3] [Basic Syntax for Type Hinting] ■ ]

#### === 1. Variables ===
: <var>: <type> = <val>
```python
num : int = 67
```

#### === 2. Sequences ===
: <var>: <seq[type]> = <val>
```python
flavor : list[str] = ["choco", "vanilla"]
```

#### === 3. Functions ===
: def <func>(<var> : <type>) -> <return_type>:
    ...
```python
def fib(n : int) -> int:
    ...
```
##### --- a. multiple return types (use |) ---
: def <func>(<var> : <type>) -> <return_type1 | return_type2>:
    ...
```python
def my_sqrt(n : int) -> int | float:
    ...
```
##### --- b. multiple arg types and return types (use |) ---
: def <func>(<var> : <type1> | <type2>) -> <return_type1 | return_type2>:
    ...
```python
def _add_elem(seq : set | list)) -> set | list:
    ...
```

### [  ■ [3] [LITERAL DATA TYPE]  ■ ]
: Literal() stores values as constants, not variables
: constants to data type

```python
from typing import Literal, get_args
type fixed_vals = Literal('pi', 'theta') # fixed_vals is a new data type

def is_constant(x : fixed_vals) -> float:
    if x == 'pi':
        return 3.14159
    else:
        return 60.0
```

### [ ■ [4] [TYPE ALIASES] ■ ]
: type <alias> = <data_type_combination>
; data type combinations to a single alias

```python
#instead of map : list[list[int]] = [[1, 2], [3, 4]]
type grid_matrix = list[list[int]]
map : grid_matrix = [[1, 2], [3, 4]]
```

## [[ LECTURE 2 : DEBUGGING AND UNIT TESTING ]]

### [ ■ [1] [ WHAT MAKES CODE ELEGANT ] ■ ]
1. Bug-Free
2. Easy to understand
3. Easy to modify

### [ ■ [2] [ DEBUGGING ] ■ ]

#### === 1. Equivalence Partitioning ===
*Input Equivalence Partition* : Set or range of vals that behaves similarly
                                # Produces same kind of output
*Output Equivalence Partition* : Set or range of kinds of outputs

: Debug by testing all cases of equivalence partitions

Different data types have natural partitions:

**`int` partitions:**
- Positive
- Zero
- Negative
- Very small/large integers

**`str` partitions:**
- Empty string
- Uppercase
- Lowercase
- Spaces
- Symbols
- Combinations of above
- Non-English characters
- Emoji

**`list[...]`, `set[...]`, `dict[...]` partitions:**
- Empty
- Singleton (one element)
- Duplicates
- Some equal elements
- All equal elements
- All unique elements

#### === 2. Edge Cases ===
: *Edge Cases*: Unusual inputs with limits or special behavior when operated
    e.g. empty str, 0
: *Boundary Values*: Edge case within or immediately around limits of input range
    e.g. 1 (boundary of all positive vals)

#### === 3. Search Space Reduction ===
1. Split Code into independent functions
2. Simplify Code

### [ ■ [2] [ UNIT TESTINTG ] ■ ]
: automated programs that test codes

1. Pytest
: Runs all functions named test_... in files named test_....py
```bash
pytest
# or
python -m pytest
```

**Basic Usage:**
```python
from main import count_vowels  # Import function to test

def test_count_vowels():
    assert count_vowels("Hello, world!") == 3
    assert count_vowels("aeiouaeiou") == 10
    assert count_vowels("Nymph") == 0
```

: 100% coverage of unit testing is not necessary
: 80%-90% is enough