
## 1.1. Random Access Machine (RAM)

: RAM is a part of every computer that usually stores temporary information (memory) from a running program.

: Suppose that the time of executing all basic memory operations is exactly `θ(1)` (e.g. getting a the index of any element regardless of the location in the RAM always takes `θ(1)`)

## 1.1.1. RAM Recall : As an Array of memory

: Consider RAM as a list of information, where every byte (8-bit string) of information has a specific address index, such that **contiguous** (adjacent/ neighboring) information has consecutive address.

>	e.g. suppose the character 'A' is in address 10000, given that another character 'B' is next to 'A', then its  address is 10001.


## 1.2. Dynamic Arrays

: Dynamic array is a list with a given current size, allocated size cap, and pointer pointing to the address of the 0th element.
### 1.2.1. Dynamic Arrays in C

```c
typedef struct DynamicArray {
	int size; // current number of filled slots
	int cap; // total slots
	int *a; // basis pointer of 0th element
} DynamicArray; 
```

### 1.2.2. Why Dynamic Array: Contiguity of Elements

: Elements of dynamic arrays are **contiguous** in a sense where their address are consecutive

>	i.e. let the pointer to the 0th element of the array be `p0th`. getting the ith element is basically getting its pointer, which is conveniently `p0th + i` since they are indexed next to each other.
>	

## 1.3. Linked Lists

: Linked lists consist of a set of nodes which contains a value and the pointer of the next node.

: Nodes of a linked list is **not necessarily contiguous**, nodes are addressed in random free spaces of the RAM (thus arithmetical indexing is not possible)

### 1.3.1. Linked Lists in C

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


### 1.3.2. Why Linked Lists: Independent Pointer Connections

: Basically, a node is connected to the next node, which are. independent to the other nodes in the linked list.

>	i.e. If we remove the 3rd node, we will just connect the 2nd node to the 4th node. 

## 1.4. Dynamic Arrays vs Linked Lists

: They both have their own pros and cons


