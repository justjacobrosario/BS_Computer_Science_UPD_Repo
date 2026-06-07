#include <stdio.h>      // Intention: Should
#include <stdint.h>     // return rounded-down
#include <inttypes.h>   // average
 
uint32_t middle_int(uint32_t x, uint32_t y) {
    return (x + y) / 2;
}
 
int main() {
    uint32_t x = 2000000000;  // 2 billion
    uint32_t y = 3000000000;  // 3 billion
    uint32_t z = middle_int(x, y);
 
    printf("%" PRIu32 "\n", z);  // uint32_t
}