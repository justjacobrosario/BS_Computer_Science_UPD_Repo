#include <stdio.h>
#include <stdint.h>



typedef struct node Node;
struct node {
    int64_t value;
    Node *next;
};

int64_t linked_list_sum(Node *head, int i, int j){
	int64_t tot = 0;

	int x = 0;
	Node *curr = head;
	while (x < i){
		curr = curr->next;
		x ++;
	}

	tot = curr.value;

	while (x < j){
		tot += curr->value;
		curr = curr->next;
		x++;
	}
	return tot;
}

int main(){
	struct Node n0;
	struct Node n1;
	struct Node n2;

	n0.value = 1;
	n0->next = n1;

	n1.value = 3;
	n1->next = n2;

	n2.value = 9;
	n2->next = NULL;

	Node arr[3] = {n0, n1, n2};

	printf("%d\n", linked_list_sum(arr, 0, 2));
}