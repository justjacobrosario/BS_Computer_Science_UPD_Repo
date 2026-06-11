: Programming languages are meant for humans to understand machine language (binary strings).
: This can be done by assigning variable names to a data's address, an instruction, a set of instructions, etc.

# 3.1. Program Recall

: Every program is a sequence of instructions (Program Flow)
: A program is a data in the RAM, where it  starts at a certain address referring to the first instruction, then to the next consecutive instructions until the program ends.

1. CPU (Central Processing Unit) : The CPU keeps track of the programming instructions to execute. It points the address of the current instruction, then redirects to the address of the next consecutive instruction once it proceeds. 

2. Instruction Pointer : the pointer of the CPU pointing/containing to the address of the current instruction. (p.s. pointers don't delete previous instructions, it just shifts the address of the next instruction to be executed)

3. Recursion : Process where we run the previous instructions once more. This is achieved by repointing the address of the previous instruction.

e.g. 
- A : Declare x = 1
- B : Increment x by 1
- C : Print x

First, the instruction pointer points the address of A, then B, then C. `[A -> B -> C]`

To recurse this, we can first point the address of A, then B, then C, and then go back to B and then C. `[A -> B -> C -> B -> C]`


# 3.2. Functions

### 3.2.1. Motivation: Functions as sets of instructions

: A function is a compilation of instructions
: Instead of listing instructions repeatedly, the function containing these can be assigned and called by its **function name**.
: functions input values, which are processed through the set of instructions, and return something.

e.g. without focusing on the technical syntax, consider the following
```c
int incr(int x){ // ignore this first
	x += 1; // 1. increments x by 1
	return x; // 2. returns the new value of x
}

// by calling incr, it willl run instructions 1 and 2

incr(10); // this will return 11
```
### 3.2.2. Parts of a Function

: In this section, we will use C programming to describe a function, but we will not focus on the syntax of C that much for now.

Functions in Python and C:
* * this part is solely for Python users learning C. Proceed to A. Defining Functions.
: In Python, functions can:
	1. have optional return type
	2. be defined anywhere (even inside functions)
	3. do higher-order funcs

: in C, functions:
	1. need return type (except for voids)
	2. can only be defined outside any code blocks / functions
	3. cannot do higher-order functions
	4. are executed in order of function calls, parameters must have value, or at least has a prototype


#### A. Defining Functions

: Recall that a function contains a set of instructions, in which input value/s will be processed through those and will return some value/s

: By defining a function, we first declare:
1. Function name
>	: The function name is what we will be calling to run the function.
>
2. Parameter/s
>	: The input values to be processed.
>	: The values of each parameter is assigned every time the function is called.
>	: Parameters are often enclosed in parenthesis, after the function name.
>
3. Function Body
>	: These are the sets of instructions that will process the parameters.
>	: When a function is intended to return something, the last instruction is the `return` line, which returns the output value
4. Return Value/s
	: The output value/s that will be returned
	: Certain programming languages (like C), declare the data type of the return value at the first part, to indicate that the function will return such type of data.

e.g. going back to the previous sample
```c
// return data type is an integer
// function name is incr
// parameter is x, which is an integer
int incr(int x){ 
	x += 1; 
	return x;
}
```


#### B. Calling Functions

: Calling a function usually contain the function name and the value of the parameter/s

e.g.
```c
incr(10) // this will return 11
```

## 3.3. Learning a Programming Language

: Recall that the purpose of the programming language is to help humans understand, access, and manipulate machine language (binary strings).

: There are several programming language because each is responsible for focusing on some particular aspect (Python for Machine Learning, JavaScript for Web Development, etc.)

### 3.3.1. How to learn a new programming language

1. Know the syntax of the language
>	Understand how variables and functions are assigned and declared, how operators and data types look like, etc.
2. Learn basic functions local in the language. 
>	These are surface-level functions that mostly do tasks that is frequently and basically done.
3. Learn how to use libraries and their functions. 
>	After having a sufficient vocabulary on the basic functions, one can study libraries, their purpose, and the functions provided by the library.