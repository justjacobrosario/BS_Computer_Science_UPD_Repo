# 3.1. Program Recall

: Every program is a sequence of instructions (Program Flow)
: A program is a data in the RAM, where it  starts at a certain address referring to the first instruction, then to the next consecutive instructions until the program ends.

1. CPU (Central Processing Unit) : The CPU keeps track of the programming instructions to execute. It points the address of the current instruction, then redirects to the address of the next consecutive instruction once it proceeds. 

2. Instruction Pointer : the pointer of the CPU pointing/containing to the address of the current instruction. (p.s. pointers don't delete previous instruction, it just shifts the address of the instruction to be executed)

3. Recursion : Process where we run the previous instructions again. This is achieved by repointing the address of the previous instruction.

e.g. 
- A : Declare x = 1
- B: Increment x by 1
- C: Print x

First, the instruction pointer points the address of A, then B, then C. `[A -> B -> C]`

To recurse this, we can first point the address of A, then B, then C, and then go back to B and then C. `[A -> B -> C -> B -> C]`


