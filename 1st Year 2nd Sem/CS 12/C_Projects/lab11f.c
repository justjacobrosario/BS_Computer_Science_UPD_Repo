#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//

#include "middlesquare.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define MIDDLESQUARE_H


int *gen_msq_seq(int d, int x, int k) {
    int *res = (int *)malloc(k * sizeof(int));
    
    if (k > 0) {
        res[0] = x;
    }

    int64_t r = 1;
    for (int i = 0; i < d / 2; i++) {
        r *= 10;
    }

    int64_t m = 1;
    for (int i = 0; i < d; i++) {
        m *= 10;
    }

    for (int i = 1; i < k; i++) {
        int64_t prev = res[i - 1];
        int64_t y = prev * prev;
        res[i] = (int)((y / r) % m);
    }

    return res;
}

//

int main(){
	int n = 3;
    int **m = (int**)malloc(n * sizeof(int*));

    for (int i = 0; i < n; ++i) {
        m[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            m[i][j] = 1 + 3 * i + j;
        }
    }

    int ans[3][3] = {
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9},
    };

    transpose(n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%s\n", );
        }
    }
}

}