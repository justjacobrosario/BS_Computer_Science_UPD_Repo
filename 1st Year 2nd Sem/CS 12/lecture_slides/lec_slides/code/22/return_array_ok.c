#include <stdio.h>
 
// `out` is a parameter that will contain result;
// actual return value is unused (void)
void range(int *out, int n) {
    for (int i = 0; i < n; i++) {
        out[i] = i;
    }
}
 
int main() {
    int n = 10, sum = 0;  // `nums` is allocated
    int nums[10] = {};    // in `main`
 
    range(nums, n);       // `range` modifies
                          // `nums` directly
    for (int i = 0; i < n; i++) {
        sum += nums[i];
    }
 
    printf("%d\n", sum);
}