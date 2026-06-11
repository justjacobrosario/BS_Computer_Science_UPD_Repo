[[1 - Binary and Hexadecimal]]

: These features are mostly present to all programming languages
# 2.1. Include Statements
: includes libraries (compilation of program files) to your current file
e.g.
: C's `include <...>`
: Python's `import ...`

# 2.2. Data Types
 : identify the type of data by declaring data types
 : this is to make sure one data is being operated and processed according to its type

e.g. 
```c
int num_int = 11
char num_str = "11"

// they have the same set of symbols, but diferent types

// num_int can be processed arithmetically while num_str can't
```

# 2.3. Basics regarding RAM (Memory)


: data in RAM exists while a program is running. Once the program has ended, the data in the RAM will be erased (unlike data in hard disks).
: data in RAM are temporary

## 2.3.1. Address

: Every byte (8 bits) has an address indexed from 0 onwards.
: Data in RAM  can only be accessed and use by referring to its address. However, manually recording and typing one's address (which can go up to several digits) is tedious and impractical.
: Programming languages keep track of memory addresses for data to automatically be used.

e.g.
consider that we have 4GB RAM (4 billion bytes), and a byte has one unique address

| RAM ADdress   | value   |
| ------------- | ------- |
| 0             |         |
| 1             |         |
| ...           | ...     |
| 3,806,321,213 | "hello" |
| ...           | ...     |
| 4,000,000,000 |         |


: Programming languages can conveniently assign an address to a certain variable a human can refer. 
: In C, pointers are variables that points to the address of another variable

| RAM ADdress   | value |
| ------------- | ----- |
| 0             |       |
| 1             |       |
| ...           | ...   |
| 1075837252    | 19    |
| ...           | ...   |
| 4,000,000,000 |       |
 
```c
#include <stdio.h>

int main() {
    int age = 19;
    int *p_age = &age; 
    // &age is the address of age variable
    // calling the pointer *p_age will return the value addressed to &age
	
	// some programming language can automatically return the value by calling the variable itself
    printf("%d\n", age); // returns 19

	// some can also return the value by calling the pointer of its address
    printf("%d\n", *p_age); // still 19
    
    // calling the address return the indexed address of the variable in the RAM
	    printf("%d\n", &age); // like 1075837252
	    
}
```

 
# 2.3.2. Program Flow in RAM

: Aside from variables, programs are also data in the RAM

: A program contains sets of instructions called *program flow* in which each instruction is a set of binary data in the RAM

: Once the program flow completes, the data allocated to it will be freed, so that its address can be assigned to other data.