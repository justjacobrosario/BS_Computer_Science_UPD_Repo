---
field: algorithms
problem type: function problem
data structure: linked lists
---

## pseudocode:

```text

Structure Node
	char value
	Node *next

reverse(Node *head):
	Node *prev, *curr, *next
	
	// initialize vars
	// goal: head becomes tail, head.next is NULL
	
	prev = NULL
	curr = head
	
	WHILE (curr != NULL):
		next = curr->next
		curr->next = prev  // makes tail->next NULL
		prev = curr
		curr = next
		


```





## C implementation

```c
#include <stdio.h>

typedef struct Node {
	char val;
	struct Node *next;
} Node;

Node *reverse(Node * head){
	Node *prev = NULL;
	Node *curr = head;
	Node *next;

	while (curr != NULL){
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return prev;


}


int main(){
	Node a = {'a', 0};
	Node b = {'b', 0};
	Node c = {'c', 0};
	Node d = {'d', 0};
	a.next = &b;
	b.next = &c;
	c.next = &d;
	d.next = NULL;
	
	Node *res = reverse(&a);

	while (res != NULL){
		printf("%c\n", res->val);
		res = res->next;


	}


	return 0;
}

/*
c
d
b
a
*/
```