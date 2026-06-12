: we will be covering about number values in C
5.1. Numbers in Binary
5.2. Signed and Unsigned Numbers
5.3. Numeric Overflow
5.4. Decimal Numbers in Binary
## 5.1. Numbers in Binary

: Recall that numeric values are stored in the RAM in binary format.

: the **bit-length** is the number of bits (binary digits) needed to store a number.

: higher numbers require longer bit-length.

e.g.
5 is 101 (3-bits)
14 is 1110 (4-bits)

: an n-bit string can represent a number value of at most (2^n - 1).

e.g.
a 4-bit string can represent a value of at most (2^4) - 1 = 15

0000 = 0 (minimum)
1111 = 15 (maximum)
## 5.2. Signed and Unsigned Numbers

**1. Unsigned numbers**
: by default, numbers in binary is set to be positive (unsigned)

**2. Signed numbers**

: for a number to have the option to be negative or positive, the leftmost bit "**sign bit**" determines if the number is positive (0), or negative (1).

e.g. let the leftmost bit be the sign bit
0101 = 5
1101 = -5 (not 13)

: since the leftmost bit is allocated for sign determination, an n-bit string only has (n-1) bit to represent signed numeric values

: thus, an n-bit string can represent a signed value of at most (2^(n-1)) - 1, which is half smaller than representing an unsigned value

e.g.
a 4-bit string can represent a signed value of at most (2^3) - 1 = 7

0111 = 7 (max)
1111 = -7 (min)

### 5.2.1. Importance of Numeric Data Types

: A binary string can either represent an unsigned number or a signed number

e.g.
1011 can both mean 11 or -3

: Declaring the value's data type tells what kind of data a set of bit string represents.

##### A. `int` data type

: this is C's most common data type for integers
: it represents **signed numbers**
: allocates a **32-bit** space, with a **sign bit**. It can represent of numbers of at most (2^(32-1)) = 2,147,483,648.

##### B. `unsigned int` data type

: this is C's most common data type for integers
: it represents **signed numbers**
: allocates a **32-bit** space, completely for value representation. It can represent of numbers of at most (2^(32)) = 4,294,967,295.

## 5.3. Numeric Overflow

: we know that a numeric data type has a maximum number depending on the bit-length it can allocate.

: Numeric overflow is the scenario where a value exceeds the max value of a data type, in which it can only allocate the rightmost bits with respect to the data type's bit length.

e.g. let there be a data type that allocates 3-bits
assigning a value 8 will cause numeric overflow such that:
8 (digital) = 1000 (binary) = 1 (000 only recorded) -> 0 (digital) by overflow

### 5.3.1 Numeric Overflow in Calculations

: consider the values 7 and 2 which can fit to a 3-bit data type (i.e. 111 for 7, and 010 for 2)

: adding 7 and 2 will yield 9, which will cause overflowing and will result to 1 (since in 1001, only 001 can be allocated to the data type )

## 5.4. Decimal Numbers in Binary

: suppose the binary digits are 0-indexed

: in whole numbers, recall that it can be represented as binary in which its value is the summation of **(n_i) * (2^i)** where **i** is the index of a binary digit from **left to right** and **n_i** is the value of the ith binary digit.

: in the decimal places (right of the decimal point), its value is represented as the summation of **(n_j) / (2^j)** where **j** is the index of a binary digit from **right to left**  and **n_j** is the value of the jth binary digit.

: the decimal value is scene as a fraction. (e.g. 0.5 = 1/2 = 0000.1000(binary))

to visualize:

(... + (n_1 * (2^1)) + (n_0 * (2^0))) . ((n_0 / (2^0)) + (n_1 * (2^1)) + ...)

e.g. 
14.75 = 14.0 + (3/4) = 1110.1100 

### 5.4.1. Decimal Accuracy

: the longer the bit length a data type can allocate, the more accurate its decimal value will be

e.g. in converting 1/3 or 0.333... in binary, having more bits to represent the decimal value will approach to a more accurate value.

## 5.5. Numeric Data Types in C

#### 5.5.1. Motivation
: in C, and almost all programming languages, numbers are mostly present in every program.
: in assigning a numeric variable in our program, we must consider:

1. What kind of number is it?
2. How big of a number is it?

: in C, there are data type keywords that will let us declare an integer, positive integer, or a decimal number, and whether the number needs a long bit-length or a short one.

: by not just relying on a universal numeric data type, we can flexibly conserve RAM space by allocating a short space for short numbers (e.g. age), or specify that the number is big (e.g. world population)

### 5.5.2. C Numeric Data Type Keywords

**1. Keywords based on number type**

| keyword               | Description    |
| --------------------- | -------------- |
| `int` or `signed int` | signed integer |
| `signed int`          | signed integer |
| `float`               | decimal number |

**2. Keywords based on number size*

| keyword | Description   |
| ------- | ------------- |
| `short` | small numbers |
| `long`  | large numbers |

: the number size and number type can be mentioned in the data type simultaneously.

e.g.
```c
short int age = 19;
short float shares = 0.5;
long int population = 8296864572;
long float shares = 
```
