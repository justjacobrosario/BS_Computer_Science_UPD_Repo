#include <stdio.h>
#include <math.h>

int main() {

    int bin = 0;
    int deci = 0;
    
    printf("Enter Binary: ");
    scanf("%d", &bin);

    int temp = bin;
    int ctr = 0;
    while (temp != 0) {
        deci = deci + (temp % 10 * pow(2, ctr));
        temp /= 10;
        ctr += 1;
    }


    printf("\nBinary: %d", bin);
    printf("\nDecimal: %d", deci);

    return 0;
}

// 11
// 1
// 0
