## 6.1. `char` Data Type

: data type for each character of a string of text
: a char occupies **1 byte (8 bits)**
: a char value is enclosed by **single parentheses** `''`
e.g. 
```c
char letter = 'a'
```

### 6.1.2. ASCII Table

: a table mapping an 8-bit value to a character
: NOTICE: ASCII is just one of the ways characters is being represented in binary
#### A. Capital Letters

: capital letters begin at **010** (3 rightmost bits)
: the remaining 5 bits are dedicated for each capital letter alphabetically, starting at **00001**

e.g. 
`'A'` = 0100 0001
`'B'` = 0100 0010
...
`'Z'` = 0101 1010

#### B. Lowercase Letters

: lowercase letters begin are **011**
: the remaining 5 bits are dedicated for each lowercase letter alphabetically, starting at **00001**

e.g. 
`'a'` = 0110 0001
`'b'` = 0110 0010
...
`'z'` = 0111 1010

#### C. Char Numbers

: Numbers enclosed by single parentheses, numbers inside a string, and numbers we output in the keyboard are char numbers by default (not int)

: char numbers begin are **0011**
: the remaining 4 bits are dedicated for each digital number, starting at **0000**

e.g. 
`'0'` = 0011 0000
`'1'` = 0011 0001
...
`'9'` = 0011 1001

: notice that an `int 9` = 1001, but a `char 9` = 0011 1001, thus they are different values.
