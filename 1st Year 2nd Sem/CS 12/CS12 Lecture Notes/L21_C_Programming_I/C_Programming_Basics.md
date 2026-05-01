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
### 1) Compiling
`gcc filename.c -o hello`

### 2) Running
`./hello`

: NOTE : You must  recompile then run the code for any revision

## 3. C Initial Points
: these are the usuals, consists of terms, syntax, and the usual template of a C program
### 1) Preprocessor Directive
`#include <stdio.h>`
: like import lines in Python
: loads standard I/O library
#### Preprocessor `#`
: lines starting with `#` is processed even before compilation

### 2) Variables
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

### 3) Functions
```
<return_type> <func_name>(<arg_type> <arg_name>, ...) {
<body>
}
```
: compared to Python, 
	- return type is mentioned first, 
	- the parameters are type-value pairs, and 
	- the body (consists of statements) is enclosed with { }
### 4) Statements
: Statements (except for the last line of a function) end with a semicolon
### 5) Entry Point
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

### 1) Arithmetic Operators
`+, -, *, /, %`

### 2) Comparison Operators
`==, !=, <, >, <=, >=`

### 3) Logical Operators
`&& || !`

### 4) Bitwise Operators
`& | ^ ~ << >>`

### 5) Compound Assignments
: increments, ...
`+= -= *= /=`

### 6) Post Compound Assignments
: increment by 1, ...

NOTE: C has no boolean, only use 0 and 1

## 4) Control Structures
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

## 5) printf and Functions

### 1) printf
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
### 2) Functions
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
: in C, params and functions can only be used if it alread