#include <stdio.h>
 
int *range_wrong(int n) {
    int ret[n];
 
    for (int i = 0; i < n; i++) {
        ret[i] = i;
    }
 
    return ret;  // Never return a pointer
}                // to own local variable!
 
int main() {
    int n = 10, sum = 0;
    int *nums = range_wrong(n);
 
    for (int i = 0; i < n; i++) {
        sum += nums[i];
    }
 
    printf("%d\n", sum);
}