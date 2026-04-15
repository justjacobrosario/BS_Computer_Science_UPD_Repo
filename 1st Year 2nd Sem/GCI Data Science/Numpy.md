



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

# 4: 1-Dimensional Arrays

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

#### 1] per element operations
: process the operations on all element
##### `np.exp(a)`,
: e^a
##### `np.log(a)`,
: log(a)
##### `np.sin(a)` and other trig funcs,
#### 2] index-based arithmetic operations
: adds/subtracts/multiply/divide an element of ndarray a to the element of the same index of ndarray b
##### `np.add(a, b)`, 
##### `np.subtract(a, b)`, 
##### `np.multiply(a, b)`, 
##### `np.divide(a, b)`,

```python
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
_sum = np.add(a, b) # [1+2, 2+4, 3+6] -> array([3, 6, 9])
```

#### 3] index-based comparison operations
: same thing, operations are index-based
##### `np.equal(a, b)`, 
##### `np.greater(a, b)`, 
##### `np.less(a, b)`, 

#### 4] scalar operations
: basically operates each element into the specified number
##### `an_np_ndarray + or - or * or / or // some_number`

```python
a = np.array([1, 2, 3])
b = a + 1
# b will be array([2, 3, 4]) since 1 is added to each element
```

#### 5] aggregate functions
: aggregates elements of an np.ndarray into a single value
##### `np.max(a)`
: max num
##### `np.mean(a)`
: mean num
##### `np.sum(a)`
: sum
##### `np.std(a)`
: standard deviation

#### 6] indexing and slincing `np.ndarray` objects
: basically same for list indexing and slicing


# 5: 2-Dimensional Arrays

## 1. Python's `list[list]`
: basically, to have 2-dimensions, u can nest a list to another list

```python
grid = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# or just grid = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

row, col = (0, 0)
print(grid[row][col]) # returns 1 (the 0th row and 0th column)
```

## 2. Numpy's `np.ndarray`
: yes, `np.ndarray` objects can be 1 or 2 dimensional

```python
grid = np.array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
])

row, col = (0, 0)
print(grid[row][col]) # returns 1 (the 0th row and 0th column)
```

### 1. Universal Functions
#### 1] All index-based operations
#### 2] All scalar operations

### 2. Axis