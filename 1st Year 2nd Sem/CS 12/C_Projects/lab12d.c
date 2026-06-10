#include <stdio.h>
#include <stdint.h>


typedef struct skates Skates;
struct skates {
    char brand[5+1];
    int64_t price;
};

typedef struct skates_pair SkatesPair;
struct skates_pair {
    Skates skates1;
    Skates skates2;
};


#include "cheap_skates.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define CHEAP_SKATES_H

SkatesPair cheap_skates_pair(int n, Skates *shop_items){
    Skates s1, s2;

    if (shop_items[0].price < shop_items[1].price){
    	s1 = shop_items[0];
    	s2 = shop_items[1];
    }

    else {
    	s1 = shop_items[1];
    	s2 = shop_items[0];
    }

    for (int i = 2; i < n; i++){
    	if (shop_items[i].price < s1.price){
    		s2 = s1;
    		s1 = shop_items[i];
    	}
    	else if (shop_items[i].price < s2.price){
    		s2 = shop_items[i];
    	}
    }

    SkatesPair pair;
    pair.skates1 = s1;
    pair.skates2 = s2;
    return pair;
    
}

int main() {
    Skates items[] = {
    {"Nike", 1000},
    {"Nice", 30},
    {"Yike", 20},
    {"Nyek", 40},
    };

    printf("%d\n",cheap_skates_pair(4, items).skates1.price);
    printf("%d\n",cheap_skates_pair(4, items).skates2.price);
}
