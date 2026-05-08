#include <stdio.h>
#include <stdint.h>

int main(){
    char ch = 'A'; // character
    int nums[] = {10, 20, 30}; // array of 32-bit integers
    int64_t x = -1; // 64-bit integer
    int y; // 32-bit integer

    printf("%d %d %d %d\n", &ch, nums, &x, &y);
    scanf("%d %d %d %d\n", &ch, nums, &x, &y);
}
