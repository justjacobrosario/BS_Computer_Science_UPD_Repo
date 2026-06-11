## 4.1. Intro Background
1. Inspired the design of Python and Javascript
2. Low-level Prog. Lang.

## 4.2. Compiling and Running C Program
: considering that gcc is installed in the terminal
	check  by `gcc --version`
: workflow:
```
filename.c (1. make file) -> 
`gcc filename.c -o hello` (2. compile file) -> 
`./hello` -> (4. runs the executable)
```
### a) Compiling
`gcc filename.c -o hello`

### b) Running
`./hello`

: NOTE : You must recompile then run the code for any revision

## 4.3. C Initial Points

: these are the usuals, consists of terms, syntax, and the usual template of a C program
### 4.3.1. Preprocessor Directive

`#include <...>`
: this is how one can access libraries
: like import lines in Python
: the basic `#include <stio.h>`loads the standard I/O library
#### Preprocessor `#`

: lines starting with `#` is processed even before compilation
### 4.3.2. Entry Point

`int main() {}`
: basically the `main` function that is always called 
: every global variable declaration and function calls to be executed must be within here.
: returns 0 (can be remove ONLY for `main`)

: this is a basic C program
```c
#include <stdio.h>

int main() {
    printf("Hello, worldz!\n");
	return 0
}
```

### 4.3.3. Variables
#### A. Declaration
: before giving a value, variables must first be defined with its data type
: snake_case like Python
: when we only declare variables, useless random memory called "garbage" is there, which gives certain bytes of memory the moment variables are declared (even if theres no value yet!)

#### B. Assignment
: basically assigning values to variables
: can be done separately or simultaneously with declaration

#### C. Constantiating
`const <var_type> <var_name> = <value>`
: ONLY if variable value is meant to be constant
: making variables constant is kept constant by the compiler
: usually uppercase

e.g.
```c
// separated
int a; // value of a is garbage (unpredictable value)
a = 1; // a is now set to have a value 1

// declared and assigned 
int b = 2;

// can declare and assign multiple variables w same type
int c = 3, d = 4;

// can make variables constant
const int ABSOLUTE_ZERO = 0
```

### 4.3.4. Statements
: Statements (a variable assignment, function call, return statement, etc.) must end with a semicolon `;`
: There are **exceptions**. 
1. Preprocessor directives e.g. `#include <stdio.h>`
2. Braced lines of a function `{}`
e.g.
```c
int main(){ // braced
	printf("This printf line is a statement");
} // braced
```


### 4.3.5. Functions
```
<return_type> <func_name>(<arg_type1> <arg_name1>, ...) {
<body>
}
```
: compared to Python, 
	- return type is mentioned first, 
	- the parameters are type-value pairs, and 
	- the body (consists of statements) is enclosed with { }

#### A. Defining Functions
: for functions  that has a return value, simply type the return type on the first line of the func

```c
#include <stdio.h>

int return_square(int n){
    return n * n;
}
int main() {
    
printf("%d\n",return_square(2));
// i addded \n to just make a new line for aesthetics

}
```

: for functions that doesnt return anything (like when it only prints things), make the first keyword be `void`

```c
#include <stdio.h>

void print_square(int n){
    printf("%d\n", n*n); // n*n is seen as a single int, thats why only one %d
    // i addded \n to just make a new line for aesthetics
}

int main() {
    print_square(2);
}

```
#### B. Calling Functions

: To call a function to process its parameters with their respective values:

`func_name(param1_val, param2_val, ...)`

#### C. Function Prototyping

: If the function body is not yet available, one can simply declare:

`<return type> <func_name>(<param1 type>, ...)`

e.g. 
standard func declaration (no prototyping):
```c
void show_sum(int a, int b) {
    printf("%d + %d = %d\n", a, b, a+b);
}

int main() {
    show_sum(1, 2); // func is defined above
}
```

with prototype:
```c
// Prototype: return type + name + arg types
void show_sum(int, int);

int main() {
    show_sum(1, 2); // func prototype above
}

void show_sum(int a, int b) {
    printf("%d + %d = %d\n", a, b, a+b);
}
```


## 4.4. Operators and Control Structures

**1.  Arithmetic Operators**
`+, -, *, /, %`

**2.  Comparison Operators**
`==, !=, <, >, <=, >=`

**3. Logical Operators**
`&& || !`

**4. Bitwise Operators**
`& | ^ ~ << >>`

**5. Compound Assignments**
: increments, ...
`+= -= *= /=`

**6. Post Compound Assignments**
: increment by 1, ...
`++, --`

NOTE: C has no boolean, only use 0 and 1

## 4.5. Control Structures (If statements)
```c
if (x > 0) {
    printf("positive\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}

// ternary
char verdict = x > 0 ? "positive" : "negative";

// while
while (x > 0) {
    x--;
}

// for (condition in parens!)
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

when compared to Python:
```python
# if-elif-else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# while
while x > 0:
    x -= 1

# for range
for i in range(5):
    print(i)
```

## 4.6. printf function

: similar to Python's `print(f" ... ")`
in Python:
```python
print(f"{x} + {y} = {x+y}")
```

: it is type-variable pair
in C:
`printf(<string to print>, <var1>, <var2>, ...)`
: the first format specifier refers to var1, ...
: the listed variable can be an expression (1+2 is a single variable)
: the nth format specifier must be the same type as the nth variable.

```c
printf("%d + %d = %d\n", 1, 2, 1+2); // 1 + 2 = 3
//     string to print,  vars or expression
// order of vars must be the same to the format specifier
```

: the first `%d` refers to the first variable 1, and so on.

##### - `printf` format specifiers

| data type                                                                                 | type hint                               |
| ----------------------------------------------------------------------------------------- | --------------------------------------- |
| Signed Int                                                                                | %d                                      |
| Unsigned Int                                                                              | %u                                      |
| Single ASCII char                                                                         | %c                                      |
| String (char array)                                                                       | %s                                      |
| Float/double                                                                              | %f                                      |
| long/long long                                                                            | %ld / %lld                              |
| Hex                                                                                       | %x                                      |
| Special elements<br>(these are added in the string part)<br>e.g.<br>`printf("%d\n", n*2)` | newline: \n<br>tab: \t<br>null char: \0 |

## 3. Top Level and Scoping Rules
### a) Top level codes
: codes outside any blocks { }
: only declarations of variables and functions, and preprocessor directives are allowed here

#### 1] Preprocessor Macro
: defining a variable to a value before compilation
: immutable

#### 2] Global Variables
: basically declared variables in top level
: like preprocessor macro but is executed after compilation, both preprocessors and globals are accessible anywhere
: mutable

```c
#include <stdio.h>

#define N 100
int eyy = 10;

int main(){
    //N--; errorr
    eyy--;
    printf("%d", eyy); // 9
}
```
### b) Scope Rules
#### 1] Global Variables and Preprocessors are accessible anywhere

#### 2] local variables (variables declared in a block is only accessible within that block)


## 4. Integer Data Types and Limits


| Bits | Signed Type        | Range             | Unsigned Type                | Range       |
| ---- | ------------------ | ----------------- | ---------------------------- | ----------- |
| 8    | char, int8_t       | −128 to 127       | unsigned char, uint8_t       | 0 to 255    |
| 16   | short, int16_t     | −32,768 to 32,767 | unsigned short, uint16_t     | 0 to 65,535 |
| 32   | int, int32_t       | ≈ −2.1B to 2.1B   | unsigned int, uint32_t       | 0 to ≈4.3B  |
| 64   | long long, int64_t | −2⁶³, 2⁶³−1       | unsigned long long, uint64_t | (0, 2⁶⁴−1)  |

: include `stdint.h` to use fixed-width types like the types ending with `_t`
: include `stdbool.h` to use bools `true`, `false`

### a) Type Casting
: Safe: short width to long width
: Unsafe: long width to short width

```c
#include <stdio.h>
#include <stdint.h>

int16_t x_16_bit = 123456789;
int32_t y_32_bit = 123456789;

int main(){
    int32_t widen_x = x_16_bit;
    int16_t narrowed_y = y_32_bit;
    printf("x: %d\n", widen_x); 
    printf("y: %d", narrowed_y);  // error heree
}
```

### b) Type Limits
: type limit errors occur when a variable is mutated into a value beyond the bounds of its data type

## 4. Arrays in C

: arrays in c are fixed-size
: no len(), size is explicitly or implicitly fixed upon declaration

in python, we do lists like this
```python
lis = [1, 2, 3, 4]

lis[1] = 10
lis.append(67)

print("len: " + str(len(lis))) # len: 5

for n in lis:
	print(n)
	
'''
1
10
3
4
67
'''
```

in c:
```c
// no len()
#include <stdio.h>
#include <stdint.h>


int main(){
    int lis[] = {1, 2, 3, 4}; // implicit length
    int lis2[4] = {2, 4, 6, 8}; // explicit length
    
    int lis3[10] = {}; // {0,0,0,0,0,0,0,0,0,0}
    int lis4[10] = {1}; // {1,0,0,0,0,0,0,0,0,0}
    int lis5[10]; // garbage e.g. {0429, 39120, -32190, ...}
	
	// indexing out of bounds will error
    for (int i = 0; i<4;i++){
        lis[1] = 10; // mutable but no append method
        printf("%d\n", lis[i]);
    }
}
// 1
// 10
// 3
// 4
```

## C-style Strings and ASCII

: python has a string type, c doesnt
: a c string is an array f char values ending with a `\0` null char

### a. declaring a string variable

```c
#include <stdio.h>

int main(){
	// like a pythonstr
    char str1[] = "Hello x";
    // list of chars
    //NOTE: "" for str, '' for chars
    char str2[] = {'H', 'e', 'l', 'l', 'o', ' ', 'x', '\0'};
    // list of ascii nums
    char str3[] = {72,101,108,108,111,32,88,0};

    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);

}
```

