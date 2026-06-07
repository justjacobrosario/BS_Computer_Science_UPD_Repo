#include <stdio.h>
 
int main() {
    // `nums` always contains five integers;
    // remaining are initialized to 0
    int nums[5] = {10, 20};
 
    // `count` dictates which indices are "empty"
    int count = 2;
 
    // Loop is bounded by `count`
    for (int i = 0; i < count; i++) {
        printf("nums[%d]: %d\n", i, nums[i]);
    }
 
    for (int i = count; i < 5; i++) {
        nums[i] = 12;
        count++;
    }
 
    for (int i = 0; i < count; i++) {
        printf("nums[%d]: %d\n", i, nums[i]);
    }
}
