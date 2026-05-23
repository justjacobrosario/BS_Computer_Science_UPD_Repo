---
field: programming
---

## 1. Structs

: primitive version of python classes (without methods)
: a datatype that contains a group of values with fixed names (can have diff data types)

### a) Initializing a struct
e.g. 
```c
struct student {
	int baon;
	char name[123];
	char univ[123];
}
```
### b) Initializing a struct (and its attributes)

e.g.
```c
struct student juan;

juan.name = "Juan Dela Cruz";
juan.baon = 67;
juan.univ = "UP Diliman"
```

or

```c
struct student maria = {
	.name = "Maria Clara",
	.baon = 76,
	.univ = "UST"}
```
### c) parameterizing structs in functions
