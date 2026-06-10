#include <stdio.h>
#include <math.h>


int length_getter(int n){
    int digit_num = 0;

    if (n == 0){
        return 1;
    }

    while (n > 0) {
        digit_num += 1;
        n = floor(n / 10);

    }

    return digit_num;


}

int binary_conv(){
    int bin;
    int res = 0;


    printf("Binary: ");
    scanf("%d", &bin);

    int len = length_getter(bin);

    for (int i = 0; i < len ; i += 1){
        int ten = 10;
        int exp = i + 1;

        int mod1st = pow(ten, exp);
        int mod2nd = pow(ten, exp - 1);
        int val = (bin % mod1st) - (bin % mod2nd);


        // 1010 i = 2, 1010 % 10^2 - 1010 % 10^1
        printf("%d\n%d \n\n", (bin), (bin % mod2nd));

        res += val;

    }

    return res;
    

    
}

int main(){
    printf("%d", binary_conv());
}