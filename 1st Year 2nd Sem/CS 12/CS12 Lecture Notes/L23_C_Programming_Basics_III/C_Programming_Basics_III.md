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

consider this
```c
typedef struct student Student;
    struct student {
        int baon;
        char name[123];
        char univ[123];
    };

    struct student maria = {
        76,
        "Maria Clara",
        "UST"
    };
```

#### 1] per attribute
```c

void increm_baon1(int *baon){
    *baon = *baon + 1;
}

    printf("%d\n", maria.baon); // 76
    increm_baon(&maria.baon);
	printf("%d\n", maria.baon); // 77
}
```

#### 2] getting whole struct obj, and 
```c

void increm_baon2(Student *p){
    int *q = &((*p).baon); // get address of attribute
    *q = (*p).baon + 1;
}

    printf("%d\n", maria.baon); // 76
    increm_baon2(&maria);
	printf("%d\n", maria.baon); // 77
}
```

#### 3] getting whole struct obj, and 
```c

void increm_baon3(Student *p){
    int *q = &p->baon; // get address of attribute
    *q = p->baon + 1;
}

    printf("%d\n", maria.baon); // 76
    increm_baon3(&maria);
	printf("%d\n", maria.baon); // 77
}
```

## 2. Dynamic Memory Allocation

### a) `malloc(sizeof(...))`
: returns a pointer, pointing the address of free memory
: `NULL` when failed

```c


int *make_range(int n){
	int *lis = malloc(sizeof(int) * n);
	// array of random values {32091, 22, 54463, 7, ...}
	
	for (int i = 0; i < n; i++){
		lis[i] = i;
	}

	return lis;
}

int main(){
	int n = 11;
	int *p = make_range(n);

	for (int i = 0; i < n; i++){
		printf("%d ", *(p + i));
	}

}

\\ 0 1 2 3 4 5 6 7 8 9 10 
```

### b) `calloc(elem_num, size)`
```c

int *make_range(int n){
	int *lis = calloc(n, sizeof(int) * n);
	// array of zero values {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	
	for (int i = 0; i < n; i++){
		lis[i] = i;
	}

	return lis;
}

int main(){
	int n = 11;
	int *p = make_range(n);

	for (int i = 0; i < n; i++){
		printf("%d ", *(p + i));
	}

}

\\ 0 1 2 3 4 5 6 7 8 9 10 


```