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

remove_dupes(Node *head):

	// suppose that only small letter (26 chars)
	// 0th index is 'a', then 'b', 'c', ...
	char char_counts[26] = {}
	
	Node dummy
	dummy.next = head
	
	Node *tail = &dummy
	
	WHILE (*tail->next != NULL):
	
		// if the value of the next node in array
		// is > 0, skip it
		IF (char_counts[tail->next->value - 'a'] > 0):
			tail->next = tail->next->next
		
		// else, record next node	
		ELSE:
			char_counts[(tail->next->value - 'a')]++;
			tail = tail->next;
			
	RETURN dummy.next
	
```


## C implementation

```c
#include <stdio.h>

typedef struct Node {
	char value;
	struct Node *next;
} Node;

Node *remove_dupes(Node *head){

	char char_counts[26] = {};

	Node dummy;
	dummy.next = head;

	Node *tail = &dummy;

	while (tail->next != NULL){

		// if value of next node in array is >0, skip
		if (char_counts[(tail->next->value - 'a')] > 0){

			tail->next = tail->next->next;
		}
		else{

			char_counts[(tail->next->value - 'a')]++;
			tail = tail->next;
		}
	}

	return dummy.next;

}


int main(){
	Node a = {'a', 0};
	Node b = {'c', 0};
	Node c = {'c', 0};
	Node d = {'d', 0};
	Node e = {'e', 0};
	a.next = &b;
	b.next = &c;
	c.next = &d;
	d.next = &e;
	e.next = NULL;
	
	Node *res = remove_dupes(&a);

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
e
*/
```
