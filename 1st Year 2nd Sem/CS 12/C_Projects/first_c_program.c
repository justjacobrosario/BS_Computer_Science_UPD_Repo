#include <stdio.h>




int max_value(int w, int n, const int *c, const int *v) {
    int res = w;

    for (int i = 0; i < n; i++) {
        if (c[i] <= w) {
            new = w - c[i] + v[i];
            if (new > res) {
                res = new;
            }
        }
    }
    return res;
}

int main(){
    int c[3] = {10, 100, 5};
    int v[3] = {1, 1000, 7};
    max_value(10, 3, c, v);
}
