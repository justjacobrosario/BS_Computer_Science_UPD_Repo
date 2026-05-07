---
field: programming
---
## 1. Intro Background
1. Inspired the design of Python and Javascript
2. Low-level Prog. Lang.

## 2. Compiling and Running C Program
: considering that gcc is installed in the terminal
	check  by `gcc --version`
: workflow:
```
filename.c -> (1. make file) -> 
`gcc filename.c -o hello` -> (2. compile file) -> 
hello -> (3. makes a binary executable)
`./hello` -> (4. runs the executable)

```
### a) Compiling
`gcc filename.c -o hello`

### b) Running
`./hello`

: NOTE : You must  recompile then run the code for any revision

## 3. C Initial Points
: these are the usuals, consists of terms, syntax, and the usual template of a C program
### a) Preprocessor Directive
`#include <stdio.h>`
: like import lines in Python
: loads standard I/O library
#### Preprocessor `#`
: lines starting with `#` is processed even before compilation

### b) Variables
#### 1] Declaration
: before giving a value, variables must first be defined with its data type
: snake_case like Python
: when we only declare variables, useless random memory called "garbage" is there, which gives certain bytes of memory the moment variables are declared (even if theres no value yet!)

#### 2] Assignment
: basically assigning values to variables
: can be done separately or simultaneously with declaration

#### 3] Constantiating
`const <var_type> <var_name> = <value>`
: ONLY if variable value is meant to be constant
: making variables constant is kept constant by the compiler
: usually uppercase

```c
// separated
int a;
a = 1;

// declared and assigned 
int b = 2;

// can declare and assign multiple variables w same type
int c = 3, d = 4;

// can make variables constant
const int ABSOLUTE_ZERO = 0
```


#### 2] Assignment

### a) Functions
```
<return_type> <func_name>(<arg_type> <arg_name>, ...) {
<body>
}
```
: compared to Python, 
	- return type is mentioned first, 
	- the parameters are type-value pairs, and 
	- the body (consists of statements) is enclosed with { }
### b) Statements
: Statements (except for the last line of a function) end with a semicolon
### c) Entry Point
`int main() {}`
: basically the `main` function that is always called 
: returns 0 (can be remove ONLY for `main`)

: this is a basic C program
```c
#include <stdio.h>

int main() {
    printf("Hello, wordsald!\n");
	return 0
}
```


## 3. Operators and Control Structures

### a) Arithmetic Operators
`+, -, *, /, %`

### b) Comparison Operators
`==, !=, <, >, <=, >=`

### c) Logical Operators
`&& || !`

### d) Bitwise Operators
`& | ^ ~ << >>`

### e) Compound Assignments
: increments, ...
`+= -= *= /=`

### f) Post Compound Assignments
: increment by 1, ...

NOTE: C has no boolean, only use 0 and 1

## 4. Control Structures
```c
if (x > 0) {
    printf("positive\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}

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

## 5. printf and Functions

### a) printf
: similar to Python's `print(f" ... ")`
in Python:
```python
print(f"{x} + {y} = {x+y}")
```

: it is type-variable pair
in C:
```c
printf("%d + %d = %d\n", x, y, x+y);
//     string to print,  vars, expression
// order of vars must be the same to the type hints
```

| data type                                                                               | type hint                               |
| --------------------------------------------------------------------------------------- | --------------------------------------- |
| Signed Int                                                                              | %d                                      |
| Unsigned Int                                                                            | %u                                      |
| Single ASCII char                                                                       | %c                                      |
| String (char array)                                                                     | %s                                      |
| Float/double                                                                            | %f                                      |
| long/long long                                                                          | %ld / %lld                              |
| Hex                                                                                     | %x                                      |
| Special elements<br>(these are added in the type part)<br>e.g.<br>`printf("%d\n", n*2)` | newline: \n<br>tab: \t<br>null char: \0 |
### b) Functions
: In python functions can:
	1. optional return type
	2. can be defined anywhere (even inside functions)
	3. can do higher-order funcs

: in C, functions:
	1. need return type (except for voids)
	2. defined outside any code blocks / funcs
	3. no higher-order funcs
	4. order is vital, parameters must have value, or at least has a prototype

#### 1] Defining Functions
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

#### 3] function prototype
: in C, params and functions can only be used if it already has been defined

: however, calling functions before defining it can be valid via prototypes

: prototypes basically defines the return type and parameter of the function (without the body yet)

e.g.

```c
void show_sum(int a, int b) {
    printf("%d + %d = %d\n", a, b, a+b);
}

int main() {
    show_sum(1, 2); // func is defined above
}
```

via prototype:

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

## 4.