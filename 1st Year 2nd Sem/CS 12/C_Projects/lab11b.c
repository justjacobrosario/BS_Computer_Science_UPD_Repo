#include <stdio.h>

typedef struct ShulkerBox ShulkerBox;

struct ShulkerBox {
    ShulkerBox *inner_box;
    int weight;
};

//
/*
#include "shulker.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define SHULKER_H
*/

int measure_weight(const ShulkerBox *s){

	int tot = 0;
	const ShulkerBox *curr = s;


	while (curr != NULL){
		tot = tot + (curr->weight);
		curr = curr->inner_box;
		
	}

	return tot;
}

//

int main(){
	ShulkerBox b = {NULL, 5};
    ShulkerBox a = {&b, 67};
    ShulkerBox c = {&a, 74};

	printf("%d\n", measure_weight(&c));
}