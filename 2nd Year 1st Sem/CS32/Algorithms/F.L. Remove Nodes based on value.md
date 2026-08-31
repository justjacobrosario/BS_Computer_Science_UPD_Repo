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

remove_char(Node *head, char target):
	Node dummy // this will contain the new head node
	
	dummy.next = head
	Node *tail = &dummy
	
	// init iteration on tail->next, which is the head
	WHILE (tail->next != NULL):
		
		// if next node has target char, skip
		IF (tail->next->value == target):
			tail->next == tail->next->next
		
		// else, keep the next node
		ELSE:
			tail = tail->next
			
	return dummy.next
```


## C implementation

```c
#include <stdio.h>

typedef struct Node {
	char value;
	struct Node *next;
} Node;

Node *remove_char(Node *head, char target){
	Node dummy;
	dummy.next = head;

	Node *tail = &dummy;

	while (tail->next != NULL){

		if (tail->next->value == target){

			tail->next = tail->next->next;
		}
		else{
			tail = tail->next;
		}
	}

	return dummy.next;

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
	
	Node *res = remove_char(&a, 'b');

	while (res != NULL){
		printf("%c\n", res->value);
		res = res->next;


	}


	return 0;
}

/*
a
c
d
*/

```
