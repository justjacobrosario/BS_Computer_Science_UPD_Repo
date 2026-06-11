#include <stdio.h>
#include <math.h>

int main() {
    int bin;

    printf("Enter Binary: ");
    scanf("%d\n", &bin);

    int copy = bin;

    int i = 0;

    int curr;

    int res = 0;

    while (copy > 0){
        curr = copy % 10; //leftmost val
        res += (curr * pow(2, i));

        i += 1;
        copy = floor(copy / 10);
    }


    printf("Digital Output: %d", res);


}