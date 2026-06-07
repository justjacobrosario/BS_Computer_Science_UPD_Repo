#include <stdio.h>
 
int main() {
    int n = 5, i = 1, sum1 = 0, sum2 = 0;
 
    for (int k = 1; k <= n; k++) {
        sum1 += k;
    }
 
    while (i <= n) {
        i++;
    }
 
    if (sum1 == sum2) {
        printf("Both are equal\n");
    } else if (sum1 < sum2) {
        printf("sum1 < sum2\n");
    } else {
        printf("sum1 > sum2\n");
    }
}