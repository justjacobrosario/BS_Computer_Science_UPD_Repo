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
(1. make file) -> ( 2. compile file) -> (3)
filename.c -> `gcc filename.c -o hello` -> hello -> `./hello`
```
### 1) Compiling
`gcc filename.c -o hello`

### 2) Running
`./hello`

: NOTE : You must  recompile then run the code for any revision

## 3. C Initial Points
### 1) `#include <stdio.h>`
: like import lines in Python
### 2) `int main() {}`
: `main` function is always called 
: returns  0

```c
#include <stdio.h>

int main() {
    printf("Hello, wordsald!\n");
	return 0
}
```

### 3) Variables
#### 1] Declaration
: before giving a value, variables must first be defined with its data type
: snake_case like Python

```c
int a:
int b, c:
```

#### 2] Assignment

### 4) Functions
```
<return_type> <func_name>(<arg_type> <arg_name>, ...) {
<body>
}
```
: compared to Python, return type is mentioned first, the parameters are type-value pairs, and the body (consists of statements) is enclosed with { }
### 5) Statements
: Statements (except for the last line of a function) end with a semicolon