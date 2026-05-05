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

int main(){
    int c2[2] = {100, 10};
    int v2[2] = {1000, 9};
    printf("%d", max_value(10, 2, c2, v2));
}
