#include <stdio.h>
#include <stdint.h>

#include "range_sum_query.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define RANGE_SUM_QUERY_H

int64_t linked_list_sum(Node *head, int i, int j){
	int64_t tot = 0;

	int x = 0;
	Node *curr = head;
	while (x < i && curr != NULL){
		curr = curr->next;
		x ++;
	}

	while (x < j && curr != NULL){
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