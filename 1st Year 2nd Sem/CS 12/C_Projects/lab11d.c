#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//

#include "maxnasumlaude.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAXNASUMLAUDE_H


int64_t max_subarray_sum(int n, int *a, int **l, int **r){
    int64_t max = 0;
    int64_t curr_max = 0;

    int s = 0;
    int e = 0;
    int curr_s = 0;

    for (int i = 0; i <n ; i++){
        curr_max += a[i];

        if (curr_max > max){
            max = curr_max;
            s = curr_s;
            e = i + 1;
        }

        if (curr_max < 0){
            curr_max =0;
            curr_s = i +1;
        }

    }

    *l = a + s;
    *r = a + e;

    return max;

}

//

int main(){
	int a[4] = {2, -1, 3, -100};
    int *l, *r;

    printf("%lld\n", max_subarray_sum(4, a, &l, &r));
}