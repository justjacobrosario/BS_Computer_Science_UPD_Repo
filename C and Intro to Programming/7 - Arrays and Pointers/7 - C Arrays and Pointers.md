[[6 - C Other Data Types]]

some assumptions to be considered (not totally true, but assume such for now to make things simple):
- let all text chars as ascii chars
- let `unsigned short int` data type allocate 2 bytes in size
## 7.1. C Arrays

## 7.1.1. Initializing Arrays in C

: arrays in C are fixed-size
: no len(), size is explicitly or implicitly fixed upon declaration
: we can get the length of arrays using `sizeof` (basically returns the size of a data type or variable)

e.g. suppose `arr` is an array
```c
int length = sizeof(arr) / sizeof(arr[0])
```

### A. Python lists vs C Arrays

: in python, we do lists like this
```python
lis = [1, 2, 3, 4]

lis[1] = 10
lis.append(67)

print("len: " + str(len(lis))) # len: 5

for n in lis:
	print(n)
	
'''
1
10
3
4
67
'''
```

: in C, we do arrays as `<data_type> <arr_name>[];`
: arrays can be an array of int `e.g. int arr[];`, an array of char, and so on.

```c
#include <stdio.h>
#include <stdint.h>

// lis, lis2, lis3, lis4, lis5 are diff ways to initialize an array  (more ways using pointers laterr)

int main(){
    int lis[] = {1, 2, 3, 4}; // implicit length
    int lis2[4] = {2, 4, 6, 8}; // explicit length
    
    int lis3[10] = {}; // {0,0,0,0,0,0,0,0,0,0}
    int lis4[10] = {1}; // {1,0,0,0,0,0,0,0,0,0}
    int lis5[10]; // garbage e.g. {0429, 39120, -32190, ...}
    
    lis[1] = 10; // mutable but no append method
	
	// u cant print most arrays once (need to loop)
    for (int i = 0; i<4;i++){
        printf("%d\n", lis[i]);
    }
}
// 1
// 10
// 3
// 4
```

## 7.2. C-style Strings and ASCII

: **String** is a type of `char` array

**A. Strings are Null Terminated**
: a C string is an array ends with a `'\0'` null char
: we use `'\0'` to prompt that only the bytes before it are the elements of array (i.e. prevents the program to )

e.g. in the binary representation of "123"
- we know that every element in a string is a char. Thus "123" consists of char numbers (not ints!). And a char is 1 byte
- refer to [[6 - C Other Data Types]] to recall how char numbers  are represented as binary

: if we are to represent "123" 

00110001001001100011001100000000

(just added spaces and colons to separate chars):

0011 0001 : 0011 0010 : 0011 0011 : 0000 0000

this is like `{'1', '2', '3', '\0'}` in arrays

: thus in an n-char string, it is n+1 bytes long (+1 bc of the null char)

```c
char arr[4] = {'a', 'b', 'c', '\0'}
```

**B. Strings is a Special Char Array**

: strings is so special, instead of manually looping its elements, we can simply print it once using its own format specifier `%s`

: we can do that because we know until when should `printf` stop printing via the null char.

e.g. suppose `arr` is a string
```c
printf("%s", arr) // only for null terminating strings
```

**Note: char arrays without `'\0'` are not strings**
### 7.2.1. Declaring Strings

: since we know when to stop using the null char, we don't need to explicitly declare the array length for strings

```c
#include <stdio.h>

// str1, str2, and str3 are diff ways to make strings

int main(){
	// like a pythonstr
    char str1[] = "Hello x";
    // list of chars
    //NOTE: "" for str, '' for chars
    char str2[] = {'H', 'e', 'l', 'l', 'o', ' ', 'x', '\0'};
    // list of ascii nums
    char str3[] = {72,101,108,108,111,32,88,0};

    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);

}
```

*: aside from directly giving values to the char array, we can input string and then assign it to a char array later using `scanf`*


## 7.3. Arrays in RAM
: an array is a collection of elements with the same data type.

: recall that in RAM, elements are represented in bytes.
: in memory, elements of an array are **contiguous**, or their byte representation are adjacent to each other.

e.g. in an array of `unsigned short int` {1, 2, 3}

in binary (where a byte is virtually divided in colons):
`0000 0000 0000 0001 : 0000 0000 0000 0010
{              `1`             ,               `2`             } 

e.g. in a string "a1" is {`'a'`, '`1`', '`\0`'}
- we know that lowercases starts with `0110`
- we know that number chars starts with `0011`

in binary (where a byte is virtually divided in colons):
`0110 0001 : 0011 0001 : 0000 0000`
{   `'a'`      ,    `'1'`       ,    `'\0'`    } 


## 7.4. Memory

: lets first focus on the memory and its terms

#### A. bit vs bytes
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

#### B. Parts of Memory (Address and Value)

: it consists of an **Address (index)**, and the **Value (in bytes of binary)**
: Addresses are also made of binary integers. For 64-bit computers, **Addresses are 8 bytes long**
: when printed, its format specifier is `%p`
: for simplicity, instead of showing address as 8 bytes long (which it is realistically), we will show addresses to be `0x<4 bits>`
e.g.
`{'a', 'b', 'c'}`

| Address  | Value       |
| -------- | ----------- |
| `0x1000` | `0110 0001` |
| `0x1001` | `0110 0010` |
| `0x1002` | `0110 0011` |
| ...      | ...         |


#### C. Memory as an Array of bytes
: see memory as an array of bytes of values where the index is their address
: a value that is n bytes long is set to the address (previous address + n)

: see memory as an array like this
{... , 0000 0000, 0000 0000, 0000 0000, 0000 0001... }
      `0x1001`    `0x1002`   `0x1003`    `0x1004` ...  addresses

#### D. Importance of data type specification

: **data types** specifies the memory length of data. It can be more than 1 byte, where it covers multiple addresses. (e.g. an int covers 4 bytes long, so it also covers 4 contiguous addresses, such that it is referenced to the first address)

| code                    | address  | value         | remarks                                                  |
| ----------------------- | -------- | ------------- | -------------------------------------------------------- |
| ...                     | `0x1000` | ...           | lets set the previous address for the sake of an example |
| `int a = 1`             | `0x1001` | 1             | an `int` is 4 bytes long, so it uses the net 4 address   |
| char b = 'a'            | `0x1005` | 'a'           | `char` is 1 byte long, so it covers the next 1 byte      |
| `int lis[] = {5, 6, 7}` | `0x1006` | `lis[0]` or 5 | elements of arrays have separate addresses (same rule)   |
|                         | `0x1009` | `lis[1]` or 6 | ...                                                      |
|                         | `0x1013` | `lis[2]` or 7 | ...                                                      |

## 7.5. Pointers

: we know that each byte is found to a certain address in RAM
: a value can be referenced to the address of its first byte

#### 1] Pointer Value
: Memory address or index of a certain value

#### 2] Pointer
: the variable that contains a memory address
(i.e. a variable that points to the address of a value)
(i.e. a pointer doesn't have the house, just the address of it)

#### 3] `*`
: the pointer symbol does things differently depending on where you will use it (more on it later)

#### 4] `&var`
: returns the address of the value of `var`

### A. Using Pointers
: the `*` has diff purpose for the 1st and 2nd usage
: the 1st `*` initializes a var to be a pointer, the 2nd `*` dereferences the pointer to the value of the address that its pointing.
#### 1] Initializing a Pointer
`data_type *pVar = &var`

: *we need to explicitly mention the **data type** to know how long the data is and until what address the data cover (recall 7.4.D. Importance of data type specification)*

e.g.
```c
int x = 4;
int *pX = &x; // pX contains the address of x

// or

int x = 4;
int *pX; // * declares pX as a pointer
pX = &x; // no need to add *, bc it has already been declared
```

: i.e. `pX` is the pointer that contains the address of `x`, where the value of `x` is a type of `int`

: whenever we use `*` in the middle of declaring a datatype to a variable, we assign that variable `pX` as the pointer to the address value (pX points to &x)

memory will look like this:

| code           | Address  | Value                    |
| -------------- | -------- | ------------------------ |
| `int x= 4`     | `0x1000` | 4                        |
| `int *pX = &x` | `0x1008` | `0x1000` (address of  x) |
|                | `0x100F` |                          |

#### 2] Dereferencing a Pointer (return value of var addressed to p)

: whenever we call `*pX` again, instead of returning the address (calling `pX` returns the address of x), it returns the value of x (hence referring to the value in the address)
: mutating the value of `*pX` also mutates the value of `x`

e.g.
```c
int x = 4;
int *pX = &x;

printf("%p", pX); // prints 0x1000 (notice that addresses has a format specifier %p)
printf("%d", *pX); // Dereferencing: prints 4 instead of 0x1000
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
	
	// 1) sizeof(int) tells that we need 4 bytes to allocate 67
	// 2) malloc() requests for a free block of memory fo size 4 bytes where we will place the value of *p there
	// 3) malloc(sizeof(int)) gives the address of the free memory to be used
	
	*p = 67;
	return p // returns the address
}

int main() {
	int *num = create67();
	printf("%d\n", *num); // 67
	}
```

### B. Pointers in arrays

let there be `char lis[] = {'a', 'b', 'c'}`

: every element has their own pointer value (address)
: there is no single pointer to every elements of the whole array

: **the array name `lis` is the pointer** for the address of the first element (which also virtually points to the whole array)

: so `*lis => lis[0]`, `*(lis + 1) => lis[1]`
: thus `*(lis + i) = lis[i]` for any i < array_length


#### Indexing Arrays via Pointers
: 1. we know that array elements are contiguous
`(arr[0], arr[1], ... )`

: 2. we know the pointer `*arr` dereferences the first element ( which is same for `arr[0]`)

: 3. Thus, `*(arr + i)` is equivalent to `arr[i]` for some index 0 <= i <= array length.


```c
int main(){
    char arr[] = {'a', 'b', 'c'};
    
    // I. Indexing method
    printf("%c", arr[1]); // b
    
    // II. Arithmetic Method
    printf("%c", *(arr + 1)); //b
    
    // lis[i] <-> *(lis + i)
}
```

### e) Parameterizing arrays in functions using pointers

: if a parameter is an array, parameterize the array as a pointer
`e.g. void f(int *arr){...}`
: when called, it dereferences, its argument is an array

like this template:
```c
void f(int *arr, int n) {
    for (int i = 0; i < n; i ++){
        arr[i] ...; // uses each element of the array
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

int *g() {
	int lis[3] = {1, 2, 3} // makes this in sets of addresses
	return &lis // returns the address of first element
}

/*
1. when a function is called, all local variables in it will be made and will be allocated a memory

2. but when the function is done running, that memory will be cleared out. 

3. so returning the address to a specific part of the memory will return unpredictable values (HEISENBUGS)
*/
```

Heisenbugs: when the address of a cleared out variable is being used by other unrelated variables
	
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

: scanf stops every space, tabs and \n if format specifier is %d / %f / %s

: scanf DONT skip space, tabs and \n if %c / %[^\n]
## 3. Null Pointers
### a) Sentinel Value
: a value that we usually return as the final result if there is no more return values to be returned relative to the function

: e.g. in python, we use `None` when we can't find a negative number in a function `find_negative([1, 2, 3])`

: in C, since the return type is infered at the start, the sentinel value must adhere to that

#### `NULL` Pointer
: sentinel value that points to an address where there is no value

e.g.
```c
int *first_negative(int *p, int n){
	for (int i = 0; i < n; i++){
		if (*(p + i) < 0) {
			return (p+i);
		}
	}
	return NULL; // sentinel value, when there is no negative number
}
```

### b. Segmentation Fault (segfault)
: when we try to access a memory address from using pointers, but certain programs in our computer uses it and our c program is not allowed to access it.

: e.g. we get a block of memory address where google chrome currently uses

: commonly encountered from using `NULL`

## 4. Input Buffer
: in scanf, every input (char, int, \n, space, tabs) will be listed in an input buffer

: depending on the datatype in the scanf, certain inputted elements are consumed or left in the input buffer

e.g. we inputted `1a\n` or we typed 1 then a then enter
`scanf("%d", &some_var)` consumes `1`, leaving `a` and `\n` in the input buffer


lets have an id msg input program
e.g.
```c
int main() {
	int id;
	char msg[67];

	while (1) {
		printf("Input id: ");
		scanf("%d", &id);

		printf("Input message: ");
		scanf("%s", msg);

		printf("ID: %d, MSG: %s\n", id, msg);
	}
}

// E.G.
/*
Input id: 0
Input message: Hello
ID: 0, MSG: Hello

however:

Input id: 1
Input message: Hello world
ID: 1, MSG: Hello
Input id: Input message: ID: 1, MSG: world
*/
```

: lets consider the input, and the input buffer
1. in the first attempt 
- we typed `0\n`, where theres \n since we click enter. 
- INPUT BUFFER: {0, \n}
- `scanf("%d", &id);` only gets digits, leaves non-digits, lile \n
- INPUT BUFFER: {\n}
- we typed `Hello\n` 
- INPUT BUFFER:  {\n, H, e, l, l, o, \n}
- `scanf("%s", msg);` only gets chars, stops and leaves non-chars
- INPUT BUFFER:  {\n, \n}
- the program ends so we didnt have any complication with the remaining \n

2. in the second attempt
- we typed `1\n`,
- INPUT BUFFER: {1, \n}
- `scanf("%d", &id);` only gets digits, leaves non-digits, lile \n
- INPUT BUFFER: {\n}
- we typed `Hello World\n` 
- INPUT BUFFER:  {\n, H, e, l, l, o, ' ', W, o, r, l, d, \n}
- `scanf("%s", msg);` only gets chars, stops and leaves non-chars
- INPUT BUFFER:  {\n, ' ', W, o, r, l, d, \n}
- there are still remaining chars that will be received by the next scanf lines
- to fix that we use fgets
## 5. fgets
`fgets(pointer, size, stdin)`

: from the word get s (get string)
: replaces  `scanf("%s", %some_var)` to store phrases rather than just the first word

: it reads both chars and spaces (which `scanf("%s", msg);` leaves )
: it stops reading when
1. \n encountered
2. exceeds (n-1) chars
3. EOF encountered
: returns the same pointer with the values
: if failed, returns NULL

## 6. fgetc(stdin)
`fgetc(stdin)`

: gets a single character 
: is practically used in times where there is a remaining `\n` in the input buffer that we need to remove before using fgets

to fix the previous program
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int length;

    printf("Enter string length: ");
    scanf("%d", &length);

    // Consume the leftover newline character left by scanf
    fgetc(stdin);

    // Dynamically allocate memory (+1 for the '\0' null terminator)
    char *str = malloc((length + 1) * sizeof(char));

    if (str == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the string: ");
    
    // fgets reads up to (length + 1) characters, including '\0'
    fgets(str, length + 1, stdin);

    // Trim the trailing newline if fgets captured it
    str[strcspn(str, "\n")] = '\0';

    printf("\nYou entered: %s\n", str);

    // Free dynamically allocated memory
    free(str);
    return 0;
}
```