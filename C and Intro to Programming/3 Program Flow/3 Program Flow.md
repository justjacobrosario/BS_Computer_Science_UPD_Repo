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
- B: Increment x by 1
- C: Print x

First, the instruction pointer points the address of A, then B, then C. `[A -> B -> C]`

To recurse this, we can first point the address of A, then B, then C, and then go back to B and then C. `[A -> B -> C -> B -> C]`


# 3.2. Functions

### 3.2.1. Functions as sets of instructions

: compilation of instructions
: instead of listing instructions repeatedly, the function containing these can be assigned and called by its **function name**.
: functions input values, processed those through the instructions, and return something

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

#### A. Function Definition

: By defining a function, we first declare:
1. Function name
2. Parameter/s
3. Function Body
4. Return Value/s