## 1.1. Intro to Computers

: Computers are fast such that it can execute a finite sequences of instructions (**instruction set**)

: Computers are also dumb, such that it can only do simple primitive operations. However, it has claimed that utilizing these operations can sufficiently implement any imaginable algorithm (**Turing completeness**).

: Computers implement operations using machine "**low-level** (only computers can understand)" language (binaries). In order for humans to communicate, "**high-level** (humans can understand)" languages are made such as **compilers**.

: A high-level language that has a set of syntax ran in a program is a **programming language**. Like C and Python, humans can be able to instruct computers to do primitive operations to make an algorithm.

## 1.1. Random Access Machine (RAM)

: RAM is a part of every computer that usually stores temporary information (memory of  values of variables, strings, etc.) from a running program. Consider it as a *scratch paper* for executing programs. **Registers** are chunks of working data in the RAM

: Computers can execiute basic memory operations in equal time intervals. Suppose that the time of executing all basic memory operations is exactly `θ(1)` (e.g. getting a the index of any element regardless of the location in the RAM always takes `θ(1)`)

### 1.1.1. Bytes, and RAM as an Array of memory

: A byte is a chunk of 8-bit memory. That means if a byte represents an int, it can represent 2^8 = 256 distinct ints.

: The byte is a common unit of memory that measures memory allocation and execution. A **word** is a length of memory (in bytes) where a computer can do single operation in it.

>	e.g. A 64-bit (8 byte) computer has a word of length 8 bytes. The larger the word,the faster a computer is since it  can make operate in larger data.

: Aside from being a scratch paper for temporary data, see RAM as a *list* of memory that can be indexed from  0 to n-1 in bytes (where n is the size of the RAM, like 6 GB or 32 GB).

: Consider RAM as a list of information, where every byte of information has a specific address index, such that **contiguous** (adjacent/ neighboring) information has consecutive address.

>	e.g. suppose the character 'A' is in address 10000, given that another character 'B' is next to 'A' and characters only occupy one byte, then its address is 10001 (just one byte added).

### 1.1.2. Operating Systems

: A running computer needs chunks of RAM to be able to run. Thus a RAM is partially used by the computer.

: Operating systems lets humans to interactively utilize memory in such a way that it does not interfere with other programs' memory usage.

: It does this by humans requesting a certain chunk of contiguous memory (**memory allocation**). In C, `malloc(n)` is an operation where `n` bytes of memory is being allocated to you, and returns the address of the first byte of that memory. (you cannot control where OS allocates memory to you)

### 1.1.3. Common C Operations

: C is a high-level language where it lets people make algorithms and interact with memory. These are the operations that can be done in C:

1. **Memory allocation**

: `malloc` allocates memory, `free` frees up allocated memory

2. **Using Variables**

: A variable represents a value of a certain **data type**. A data type has a fixed memory length (e.g. `char` has length of 1 byte, `int` has length of 4 bytes)

: Variables are stored in the RAM, where its memory is contiguous. Variables can be referred by basically calling its *variable name* or its *address* using **pointers**

4. **Memory access and mutation**
5. **Basic Operations (arithmetic, comparison, logical operations)**
6. **Conditionals (if, else statements)**
7. **Loops (for, while loops)**
8. **Function Calls (e.g. recursion)**

### 1.1.4. Pointer Recall
#### A. Pointer declaration and calling
: Let `int x = 1;`, `int *px = &x` is a pointer of x
: calling `*px` basically returns the value in that address (which is 1)

#### B. Pointer in Arrays

1. **Common way of making an array**
: we usually make array like this
```c
// let
int lis[3] = {1, 2, 3};

printf("%d", lis[0]); // 1
printf("%d", lis[1]); // 2
```

: however, we need to already decide the fixed size of the array (where it can't be modified again, which is *not dynamic*)

2. **Making arrays using pointers**
: we basically declare a pointer, then allocate memory depending on the size of our array. The pointer name is also the array name 

```c
	int size = 3;
    int *orig_arr = malloc(size * sizeof(int));

    orig_arr[0] = 1;
    orig_arr[1] = 2;
    orig_arr[2] = 3;
    
    printf("%d", orig_arr[0]); // 1
    // we can also refer elements based on pointers (*orig_arr refers to the 0th element)
    printf("%d", *orig_arr); // 1
    // we can arithmetically index using pointers (this returns the 1th element)
    printf("%d", *orig_arr + 1); // 2
```

: (but this time, we can freely manipulate the array size, which is *dynamic*)

: how? since pointers are mutable, 
>	1. we can make a temporary pointer with the updated size, making our `temp_arr`.
>	2. we can preserve the values of the `orig_arr` by assigning them to the `temp_arr`.
>	3. if we increased the size, we can also set the values of the new element/s
>	4. once the `temp_arr`'s element is settled, we free up the memory of the `orig_arr`
>	5. we assign the `orig_arr = temp_arr`
>	6. we free up the memory of `temp_arr`
: our `orig_arr` was dynamically changed in terms of its size
```c

	// lets make our orig_arr
	int size = 3;
    int *orig_arr = malloc(size * sizeof(int));

    orig_arr[0] = 1;
    orig_arr[1] = 2;
    orig_arr[2] = 3;

    // lets try to change the size and copying the values of each element

    // 1.
    size = 10;
    int *temp_arr = malloc(size * sizeof(int));

    // 2.
    temp_arr[0] = orig_arr[0];
    temp_arr[1] = orig_arr[1];
    temp_arr[2] = orig_arr[2];

    // 3.
    temp_arr[9] = 67;

    // 4.
    free(orig_arr);

    // 5.
    orig_arr = temp_arr;

    // 6.
    free(temp_arr);
```


## Data Types, Abstact Data Types, Data Structures

#### A. Data Types
: **Data types**, as mentioned recently, is an established type of value that has a fixed memory length.. (e.g. `int`, `char`, `float`, `bool`)

#### B. Abstract Data Types
: **Abstract Data Types (ADT)** , is a *description* (focus on the word description) of a unique data type. 

: It does not have an official memory length, nor it has a specific implementation in code.

>	e.g.
>	A **list** is an ADT such that the following describes a list:
>	- contains a fixed finite size n referring to the number of values (elements)
>	- has the following methods:
>	- list.size() -> n
>	- list.get(i) -> ith value
>	- list.set(i, val) -> sets val to the ith-index
>	- list.append(val) -> ...
>	- list.pop(val) -> ...

#### C. Data Structures
: **Data Structures** are attempts, implementation in code of a data type

>	The **list** ADT can be implemented as **Dynamic Arrays** and **Linked Lists**
## 1.3. Dynamic Arrays

: Dynamic array has
1. the array itself (set as the pointer of its 0th element)
2. current number of elements (size)
3. total possible number of elements (cap) 
### 1.3.1. Dynamic Arrays in C

```c
typedef struct DynamicArray {
	int size; // current number of filled slots
	int cap; // total slots
	int *a; // basis pointer of 0th element, (a is the array, can do a[index])
} DynamicArray; 
```

### 1.3.2. Why Dynamic Array: Contiguity of Elements

: Elements of dynamic arrays are **contiguous** in a sense where their address are consecutive

>	i.e. let the pointer to the 0th element of the array be `p0th`. getting the ith element is basically getting its pointer, which is conveniently `p0th + i` since they are indexed next to each other.
>	

## 1.4. Linked Lists

: Linked lists consist of a set of nodes which contains a value and the pointer of the next node.

: Nodes of a linked list is **not necessarily contiguous**, nodes are addressed in random free spaces of the RAM (thus arithmetical indexing is not possible)

### 1.4.1. Linked Lists in C

```c
typedef struct Node {
	int value; // value of the current Node
	struct Node* next; // not `Node* next;` bc the typedef is still not yet declared
} Node; // this Node is the typedef declaration

typedef struct LinkedList {
	Node* head;
	Node* tail;
	int size;
} LinkedList;
```


### 1.4.2. Why Linked Lists: Independent Pointer Connections

: Basically, a node is connected to the next node, which are. independent to the other nodes in the linked list.

>	i.e. If we remove the 3rd node, we will just connect the 2nd node to the 4th node. 

## 1.5. Dynamic Arrays vs Linked Lists

: They both have their own pros and cons

#### A. Appending from the tail
1. **Dynamic Array** (slower if cap needs to be resized)

: As long as the cap is larger than its current size `n`, one can basically just assign value to the `n`th element 

*(if cap=size and is needed to realloc the array for a larger block of free memory, recommended to double the cap instead of just incrementing it so that future appends wont need to increase the cap)

2. **Linked List** 

: Basically just makes a new node, set its pointer as the next node of the current tail, and set that new node as the new tail of the list

#### B. Popping from Tail

1. **Dynamic Array**
: Can just decrement the size counter to not count the last element

2. **Linked List** (slower, needs manual traversing of nodes)
: Needs to traverse to the node before the tail, and then disconnect it to the tail to virtually pop the last element

#### C. Random Lookup 

1. **Dynamic Array**

: can just refer to the address by arithmetically indexing it (since it is contiguous) to return the value of the demanded ith element

2. **Linked List** (slower, still needs to manually traverse to the ith node)

: needs to traverse the addresses from the head to the ith element from node to node

#### D. Arbitrary Deletion and Insertion from an index

1. **Dynamic Array**

: By adding or removing the ith element, the (i+1)th to the (n-1)th elements will be shifted to their memory addresses

2. **Linked List** 

: Can just remove or  add a node to the ith link, and then connect it to the two (or one if its the last node) adjacent node/s. 

