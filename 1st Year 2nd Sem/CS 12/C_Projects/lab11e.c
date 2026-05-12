#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//

#include "alphanumsorter.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define ALPHANUMSORTER_H


void sort_alphanum(const char *s, char **a, char **d){
    int m = 0;
    int n = 0;
    int i = 0;
    while (s[i] != '\0'){
        if (s[i] >= '0' && s[i] <= '9'){
            n ++;
        }
        else{
            m++;
        }
        i ++;
    }


    char *alphaarr = (char *)malloc((m + 1) * sizeof(char));
    char *numarr = (char *)malloc((n + 1) * sizeof(char));

    int ai = 0;
    int di = 0;
    for (int k = 0; k <= i; k++){
        if (s[k] >= '0' && s[k] <= '9'){
            
            numarr[di++] = s[k];
        }
        else{
            alphaarr[ai++] = s[k];
        }
    }

    alphaarr[ai] = '\0';
    numarr[di] = '\0';

    *a = alphaarr;
    *d = numarr;
}

//

int main(){
	char *s = "DCS251isveryfun";
    char *a;
    char *d;

    sort_alphanum(s, &a, &d);

}