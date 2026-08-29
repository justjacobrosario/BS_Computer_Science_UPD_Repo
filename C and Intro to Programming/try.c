#include "distinct_arrangements.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define DISTINCT_ARRANGEMENTS_H

int64_t distinct_arrangements(const char *s){
    int64_t n, u_ct, is_u, res, r, ct, c, k;
    n = strlen(s);

    if (n==0) return 1;

    char *u = malloc(sizeof(char)*26);
    u_ct = 0;

    for (int64_t i =0; i < n; i++){
        char l = s[i];
        is_u = 1;

        for (int64_t j = 0; j < u_ct; j++){
            if (l == u[j]){
                is_u = 0;
                break;
            }
        }

        if (is_u == 1){
            u[u_ct] = l;
            u_ct++;
        }
    }

    res = 1;
    r = n;
    for (int i = 0; i < u_ct; i++){
        char cu = u[i];
        ct = 0;
        for (int j = 0 ; j < n ; j++){
            if (cu == s[j]) ct++;
        }

        k = ct;
        if (k > r / 2) k = r-k;
        c = 1;
        for (int64_t i = 1; i <= k; i++){
            c = c * (r - k + i)/ i;
        }

        res *= c;
        r -= ct;
    }
    return res;
}
