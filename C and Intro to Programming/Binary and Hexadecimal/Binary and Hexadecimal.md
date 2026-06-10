

# 1. Reading Binary
## 1.1. Decimal (Base-10)
: let there be an array of number 0-indexed from left to right

: the digit value of the ith digit is n * 10^(i * 10) where n is the value of the ith digit

e.g.
..., z, y, x = (x * 10^(0 * 10)) + (y * 10^(1 * 10)) + (z * 10^(2 * 10)) + ... + n * 10^(i * 10)

2 is 1 * 10^(0 * 10)
12 is (2 * 10^(0 * 10)) + (1 * 10^(1 * 10))

## 1.2. Binary (Base-2)
: let there be an array of number 0-indexed from left to right

: the binary value of the ith place is n * (i^2) where n is the value of the ith digit, and n is either 1 or 0

e.g.
1010 (binary) = 0*(0^2) + 1*(1^2) + 0*(2^2) + 1*(3^2) = 10 (decimal)

2 + 8 = 10

