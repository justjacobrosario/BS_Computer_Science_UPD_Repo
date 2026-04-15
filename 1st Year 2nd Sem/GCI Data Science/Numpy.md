



# 1: Dimensional Analysis

: basically how data is analysed, arranged, and marked.

#### 1] 1-Dimensional
: It goes leftmost to rightmost
e.g. `list`, `tuple`, ...

#### 2] 2-Dimensional
: Can go left to right, and up and down via rows and columns
e.g.  matrices, `list[list]]`, ...


# 2: Data Mining
: process of extracting useful info and inferences and patterns from large datasets


# 3: Numpy

`import numpy as np`
: `np` is just a shortcut to be used in calling numpy methods

: numpy is a third-party library including complex scientific computations in Python

## 1. Characteristics of Numpy
1. using `numpy.ndarray` efficiently handle N-dimensional arrays
2. universal functions allow complex calculations than manually using loops to iterate computations
3. fast calculations (C language made)

# 4: 1-Dimensional Analysis

## 1. Python `list`
: default datatype that  contains multiple values separated by commas

## 2. Numpy's `np.ndarray`

: numpy's version of `list`
: can only store values of same type
: easy arithmetic operations in between ndarrays

### 1) `np.array(a_list)`
: convert a `list` into a `np.ndarray`
```python
import numpy as np
a_list = [1, 2, 3]
an_array = np.array(a_list)
```

### 2) Universal functions for `np.ndarray` objects

#### 1] index-based operations
#### `np.add(a, b)`, 
#### `np.subtract(a, b)`, 
#### `np.multiply(a, b)`, 
#### `np.divide(a, b)`

: adds/subtracts/multiply/divide an element of ndarray a to the element of the same index of ndarray b

```python
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
_sum = np.add(a, b) # [1+2, 2+4, 3+6] -> [3, 6, 9]
```

