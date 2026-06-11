 

## 1.1. Decimal (Base-10)
: let there be an array of number 0-indexed from left to right

: the digit value of the ith digit is n * 10^(i * 10) where n is the value of the ith digit

e.g.
..., z, y, x = (x * 10^(0 * 10)) + (y * 10^(1 * 10)) + (z * 10^(2 * 10)) + ... + n * 10^(i * 10)

2 is 1 * 10^(0 * 10)
12 is (2 * 10^(0 * 10)) + (1 * 10^(1 * 10))

## 1.2. Binary (Base-2)
### 1.2.1. Binary to Decimal (and vice-versa)

: let there be an array of number 0-indexed from left to right

: the binary value of the ith place is n * (i^2) where n is the value of the ith digit, and n is either 1 or 0

e.g.
1010 (binary) = 0*(0^2) + 1*(1^2) + 0*(2^2) + 1*(3^2) = 2 + 8 = 10 (decimal)

### 1.2.2. Binary Conventions

: binary numbers are conventionally spaced in 4 binary digits to make it more visually readable and easier to convert into hexadecimal

e.g. 
instead of 101101010011, it's 1011 0101 0011.

## 1.3. Hexadecimal (Base-16)

### 1.3.1. Hexadecimal to Binary (and vice-versa)
: hexadecimals are converted from 4 binary digits
: we use hexadecimals to represent every possible values of a 4 binary digit using one character in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}

e.g.
bin : hex : dig
0000 = 0 = 0
0001 = 1 = 1
0010 = 2 = 2
0011 = 3 = 3
0100 = 4 = 4
0101 = 5 = 5
0110 = 6 = 6
0111 = 7 = 7
1000 = 8 = 8
1001 = 9 = 9
1010 = A = 10
1011 = B = 11
1100 = C = 12
1101 = D = 13
1110 = E = 14
1111 = F = 15

### 1.3.2. Hexadecimal to Decimal (and vice-versa)

: the hexadecimal value of the ith place is n * (i^16) where n is the value (converted decimal like A = 10, B = 11, ...) of the ith digit, and n is either 1 or 0

e.g. 
3A (hex) 
= (A* (0^16)) +(3 * (1^16))
= 10 + 3 * 48 
= 58




