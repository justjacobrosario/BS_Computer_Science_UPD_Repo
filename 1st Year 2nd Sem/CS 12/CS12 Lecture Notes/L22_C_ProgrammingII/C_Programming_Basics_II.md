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
|                         | `0x1013`     | `lis[1]` or 6 | ...                                                       |
|                         | `0x1017`     | `lis[2]` or 7 | ...                                                       |

### b) Pointers

#### 1] Pointer Value
: Memory address or index of a certain value

#### 2] Pointer
: the variable that contains a pointer value 
(i.e. doesnt have the house, just the address of it)

#### 3] `*`
: the pointer symbol does things differently depending on where you will use it

#### 4] `&var`
: returns the address of the value of `var`

### c) Using Pointers
#### 1] Initializing a Pointer
`data_type *pVar = &var`

e.g.
```c
int x = 4;
int *pX = &x; // pX contains the address of x
```

: i.e. `pVar` is the pointer that contains the address of `var`, where the value of `var` is a type of `data_type` (like an int, char, etc.)

: whenever we use `*` in the middle of declaring a datatype to a variable, we assign that variable `(pVar)` as the pointer to the address value (pVar points to &x)

memory will look like this:

| code           | Address  | Value                    |
| -------------- | -------- | ------------------------ |
| `int x= 4`     | `0x1000` | 4                        |
| `int *pX = &x` | `0x1008` | `0x1000` (address of  x) |
|                | `0x100F` |                          |

#### 2] Dereferencing a Pointer (return value of var addressed to p)
: whenever we call `*pX` again, instead of returning the address of x, it returns the value of x (hence referring to the value in the address)
: mutating the value of `*pX` also mutates the value of `x`

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
#### 4] Return Values as Pointers
`any_data_type *func_name() {}`

: when a function returns a pointer value (address)
e.g.
```c
int *create_num_67(){
	int *p = malloc(sizeof(int)); // allocates memory for an int
	
	// sizeof(int) tells that we need 4 bytes to allocate 67
	// malloc() requests for a free block of memory fo size 4 bytes where we will place the value of *p there
	// malloc(sizeof(int)) gives the address of the free memory to be used
	
	*p = 67;
	return p // returns the address
}

int main() {
	int *num = create67();
	printf("%d\n", *num); // 67
	}
```
### d) Pointers in arrays
: NOTE: You cannot assign a pointer to the address of the whole list at once
: You can only assign a pointer to the address of a single element w index n
#### Initializing pointer via indexing or arithmethic method
```c

int main(){
    char lis[] = {'a', 'b', 'c'};
    // I. Indexing method
    char *pfirst = &lis[0]; // &lis[n]
    // II. Arithmetic Method
    // see lis as the point of the array (no need for *)
    char *pfirst2 = lis + 0; // lis + n
    
    // lis[i] <-> *(lis + i)

    printf("%c\n", *pfirst); // a
    printf("%c\n", *pfirst2); // a
}

```

### e) Parameterizing arrays in functions using pointers

: basically the parameter for an array is a pointer
: in the function body, refer to the array using its pointer parameter
: but when called, its argument is an array

like this template:
```c
void f(int *pArray, int n) {
    for (int i = 0; i < n; i ++){
        pArray[i] ...; // uses each element of the array
    }
}

int main(){
    int arr[] = {...};
    f(arr, n_val);
    
    // for printing purposes
    for (int k = 0; k < n_val; k++){
        printf("%d\n", lis[k]);
    }
}
```

e.g.
```c
void increm_each(int *pArray, int n) {
    for (int i = 0; i < n; i ++){
        pArray[i]++;
    }
}

int main(){
    int arr[] = {1, 2, 3};
    increm_each(arr, 3);
    
    for (int k = 0; k < 3; k++){
        printf("%d\n", lis[k]);
    }
}
/*
2
3
4
*/
```

### f) NEVER return a pointer value or address `&var` of a local variable to a function
e.g.
```c
int *f() {
	a = 67;
	return &a;
}

/*
when a function is called, all local variables in it will be allocated a memory

but when the function is done, that memory will be cleared out. so returning the address to a specific part of the memory will return unpredictable values
*/
```

## 2. scanf
`scanf(<format_specifier_string>, <ptr1>, <ptr2>, ...)
: input version of printf, but it takes pointers instead
: since the parameter  is a pointer, the value must be an address of a n existing variable
: the inputted value of the user will then be set as the value of the variables addressed in the parameters
e.g.
```c
int a;
scanf("%d", &a);
// user inputs 1
// scanf sets the pointer *(&a) = 1
// by mutation, a = 1
```

:similar to python's input() where it asks for the user's input

e.g.
```c
int main(){
    int a, b;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Enter another number: ");
    scanf("%d", &b);

    printf("%d + %d = %d\n", a, b,a+b); }
/*
Enter a number: 3
Enter another number: 3
3 +3 = 6
*/
```

: ADVICE: whenever you need to input the length of an array, ask for it first before declaring that array

e.g.
```c

int main(){

    // declare variable to make a pointer later
    int n;

    // NOTICE: ask the length of array
    printf("%s", "How many elements: ");
    scanf("%d", &n);

    // NOTICE: then declare the array itself
    int arr[n] = {};

    // asks the value of element from 0th-index onwards
    for (int i = 0; i < n; i++){
        printf("%dth-element (ints onlyy muna): " , i);
        scanf("%d", &arr[i]);
    }

    // printing purposes
    for (int k = 0; k < n; k++){
        printf("%d", arr[k]);
    }
}

/*
How many elements: 5
0th-element (ints onlyy muna): 1
1th-element (ints onlyy muna): 2
2th-element (ints onlyy muna): 3
3th-element (ints onlyy muna): 4
4th-element (ints onlyy muna): 5
12345
*/
```

e.g.
```c

int main(){

    // declare variable to make a pointer later
    int n;

    // NOTICE: ask FIRST the length of array
    printf("%s", "How many elements: ");
    scanf("%d", &n);

    // NOTICE: then declare the array itself
    int arr[n] = {};

    // just counts from 0 to n-1 as elements
    for (int i = 0; i < n; i++){
        arr[i] = i;
    }

    // printing purposes
    for (int k = 0; k < n; k++){
        printf("%d\n", arr[k]);
    }
}

/*
How many elements: 5
0
1
2
3
4
*/
```

## 3. Null Pointers
### a) returning a pointer value where null pointers are necessary
: whenever we return a pointer value/address, there are times that there is no address to be returned
: what we return in these cases are null pointer `NULL`

e.g.
```c
```