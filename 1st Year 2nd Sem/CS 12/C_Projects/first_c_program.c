#include <stdio.h>




int max_value(int w, int n, const int *c, const int *v) {
    int res = w;

    for (int i = 0; i < n; i++) {
        if (c[i] <= w) {
            int new = w - c[i] + v[i];
            if (new > res) {
                res = new;
            }
        }
    }
    return res;
}
#include "birthday.h"

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VERIFY(b) do {\
    bool _b = (b);\
    fprintf(stderr, "verifying: " #b "\n");\
    if (!_b) {\
        fprintf(stderr, "verification failed!\n");\
        exit(1);\
    }\
} while (0)

void test1() {
    int c[3] = {10, 100, 5};
    int v[3] = {1, 1000, 7};

    VERIFY(max_value(10, 3, c, v) == 12);
}

void test2() {
    int c2[2] = {100, 10};
    int v2[2] = {1000, 9};

    VERIFY(max_value(10, 2, c2, v2) == 10);
}

int main() {
    test1();
    test2();
    // TODO: add more test cases
}