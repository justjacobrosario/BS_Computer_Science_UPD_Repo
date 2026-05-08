---
field: programming
---

## 1. Pointers and Memory

### a) Memory

#### 1] bit vs bytes
: a byte has 8 bits
: thus n-bit values covers n/8 byte of memory

| datatype  | bit          | byte         |
| --------- | ------------ | ------------ |
| char      | 8-bit        | 1 bytes      |
| short     | 16-bit       | 2 bytes      |
| int       | 32-bit       | 4 bytes      |
| long      | 32 or 64-bit | 4 or 8 bytes |
| long long | 64-bit       | 8 bytes      |
| float     | 32-bit       | 4 bytes      |
| double    | 64-bit       | 8 bytes      |
| void      | 0-bit        | 0 bytes      |

#### 2] Parts of Memory

: it consists of an Address (index), and a Value (byte)
e.g.
`int x = 1`

| Address  | Value |
| -------- | ----- |
| `0x1000` | `1`   |
| `0x1004` |       |
| `0x100F` |       |
| ...      |       |
1 is the value of x and the address is 0x1000

#### 3] Memory as an Array of bytes
: see memory as an array of bytes of values where the index is their address
: a value that is n bytes long is set to the address (previous address + n)

| code                    | address      | value         | remarks                                                   |
| ----------------------- | ------------ | ------------- | --------------------------------------------------------- |
| ...                     | `0x1000`     | ...           | lets set the previous address for the sake of an example  |
| `int a = 1`             | `0x1004`     | 1             | it covers the next 4 bytes since an `int` is 4 bytes long |
| char b = 'a'            | `0x1005`     | 'a'           | it covers the next 1 byte since `char` is 1 byte long     |
| `int lis[] = {5, 6, 7}` | `0x1009`     | `lis[0]` or 5 | elements of arrays have separate addresses (same rule)    |
|                         | `0x1013`<br> | `lis[1]` or 6 | ...                                                       |
|                         | `0x1017`<br> | `lis[2]` or 7 | ...                                                       |

### b) Pointers

#### 1] Pointer Value
: Memory address or index of a certain value

#### 2] Pointer
: the variable that contains a pointer value (i.e. doesnt have the house, just the address of it)

#### 3] `*`
: the pointer symbol does things differently depending on where you will use it

#### 4] `&var`
: returns the address of the value of `var`

### c) Using Pointers
#### 1] Initializing a Pointer
`data_type *pVar = &var`
: i.e. `pVar` is the pointer that is set to the address of `var`, where the value of `var` is a type of `data_type`

: whenever we use `*` in the middle of declaring a datatype to a variable, we assign that variable as the pointer to the address value

e.g.
```c
int x = 4;
int *pX = &x; // pX contains the address of x
```
memory will look like this:

| code           | Address  | Value                    |
| -------------- | -------- | ------------------------ |
| `int x= 4`     | `0x1000` | 4                        |
| `int *pX = &x` | `0x1008` | `0x1000` (address of  x) |
|                | `0x100F` |                          |

#### 2] Dereferencing a Pointer
: whenever we call `*pX` again, instead of returning the address of x, it returns the value of x (hence referring to the value in the address)

e.g.
```c
int x = 4;
int *pX = &x;

printf("%d", *pX); // prints 4 instead of 0x1000
```
memory will look like this:

| code           | Address  | Value                     |
| -------------- | -------- | ------------------------- |
| `int x= 4`     | `0x1000` | 4                         |
| `int *pX = &x` | `0x1004` | `0x1000` (address of  x)  |
| `*pX`          | `0x100F` | 4 (pointed to value of x) |

### d) Pointers in arrays
#### 1] Initializing pointer to an 
