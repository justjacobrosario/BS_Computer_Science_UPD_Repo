: we will be covering about number values in C

### 5.1. Numbers in Binary

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

: A binary string can either represent 