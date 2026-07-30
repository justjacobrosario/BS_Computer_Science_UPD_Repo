#include <stdio.h>
#include <stdint.h>



#include "global_warning.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define GLOBAL_WARNING_H

int64_t *trigger_warning(int n, int64_t *d, int64_t x){
	int64_t pref = 0;

	for (int i = 0; i < n; i++){
		pref += d[i];

		if (pref > x){
			return &d[i];
		}
	}
	return NULL;
}

int main(){
	int64_t *result = trigger_warning(9, (int64_t[]){3, -1, 4, 1, -5, -9, 2, 6, 5}, 6);
    
    if (result != NULL) {
        printf("%lld", *result);
    }

    return 0;
}