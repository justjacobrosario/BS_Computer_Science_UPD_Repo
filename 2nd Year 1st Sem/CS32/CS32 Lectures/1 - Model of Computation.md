
## 1.1. Random Access Machine (RAM)

: RAM is a part of every computer that usually stores temporary information (memory) from a running program.

: Suppose that the time of executing all basic memory operations is exactly `θ(1)` (e.g. getting a the index of any element regardless of the location in the RAM always takes `θ(1)`)

## 1.1.1. RAM Recall : As an Array of memory

: Consider RAM as a list of information, where every byte (8-bit string) of information has a specific address index, such that **contiguous** (adjacent/ neighboring) information has consecutive address.

>	e.g. suppose the character 'A' is in address 10000, given that another character 'B' is next to 'A', then its  address is 10001.

### 1.1.2. Pointer Recall
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
## 1.2. Dynamic Arrays

: Dynamic array has
1. the array itself (set as the pointer of its 0th element)
2. current number of elements (size)
3. total possible number of elements (cap) 
### 1.2.1. Dynamic Arrays in C

```c
typedef struct DynamicArray {
	int size; // current number of filled slots
	int cap; // total slots
	int *a; // basis pointer of 0th element, (a is the array, can do a[index])
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

#### A. Appending to the head
1. **Dynamic Array**
: 
2. **Linked List**



