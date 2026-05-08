---
field: programming
---

## 1. Pointers and Memory

### a) Memory
: memory is an array of bytes
: completely contains all the data whenever a program runs

: it consists of an Address (index), and a Value (byte)
e.g.
`int x = 1`

| Address  | Value |
| -------- | ----- |
| `0x1000` | `1`   |
| `0x1004` |       |
| `0x100F` |       |
| ...      |       |
this is a memory of x

### b) Bytes as Values
#### 1] char
: recall that `char` is a one-byte integer in the range -128 to 127 (8-bit)
: a byte can be mapped to a value in `char`

e.g. `0x41` -> `65` in ascii -> `A` in char

### c) Pointers

#### 1] Pointer Value
: Memory address or index of a certain value

#### 2] Pointer
: the variable that contains a pointer value (i.e. doesnt have the house, just the address of it)

#### 3] `*`
: the pointer symbol does things differently depending on where you will use it

#### 4] `&var`
: returns the address of the value of `var`

### d) Using Pointers
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

| code              | Address  | Value                    |
| ----------------- | -------- | ------------------------ |
| `int x= 4`        | `0x1000` | 4                        |
| `int *pX = &xint` | `0x1004` | `0x1000` (address of  x) |
|                   | `0x100F` |                          |

#### 2] Dereferencing a Pointer
: whenever we call `*pX` again, instead of returning the address of x, it returns the value of x (hence referring to the value in the address)

e.g.
```c
int x = 4;
int *pX = &x;

printf("%d", *pX); // prints 4 instead of 0x1000
```
memory will look like this:

| code              | Address  | Value                     |
| ----------------- | -------- | ------------------------- |
| `int x= 4`        | `0x1000` | 4                         |
| `int *pX = &xint` | `0x1004` | `0x1000` (address of  x)  |
| `*pX`             | `0x100F` | 4 (pointed to value of x) |
