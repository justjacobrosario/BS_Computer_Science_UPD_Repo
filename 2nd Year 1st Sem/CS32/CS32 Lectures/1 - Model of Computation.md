
## 1.1. Random Access Machine (RAM)

: RAM is a part of every computer that usually stores temporary information (memory) from a running program.

: Suppose that the time of executing all basic memory operations is exactly `θ(1)` (e.g. getting a the index of any element regardless of the location in the RAM always takes `θ(1)`)

## 1.1.1. RAM Recall : As an Array of memory

: Consider RAM as a list of information, where every byte (8-bit string) of information has a specific address index, such that **contiguous** (adjacent/ neighboring) information has consecutive address.

>	e.g. suppose the character 'A' is in address 10000, given that another character 'B' is next to 'A', then its  address is 10001.


## 1.2. Dynamic Arrays

: Dynamic array is a list with a given current size, allocated size cap, and pointer pointing to the address of the 0th element.
### 1.2.1. Dynamic Arrays in C

: let `struct list` be a dynamic array

```c
struct list {
	int size; // current number of filled slots
	int cap; // total slots
	int *a; // basis pointer of 0th element
}
```

### 1.2.2. Contiguity of Elements

: Elements of dynamic arrays are **contiguous** in a sense where their address are consecutive

>	i.e. let the pointer to the 0th element of the array be `p0th`. getting the next element is basically getting its pointer, which is conveniently `p0th + 1`.
>	


