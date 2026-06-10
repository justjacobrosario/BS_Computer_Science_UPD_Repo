#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//

#include "boundbox.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define BOUNDBOX_H


int64_t *bounding_box_area(int n, const Point *p) {

    int64_t *a = malloc((n + 1) * sizeof(int64_t));

    a[0] = 0;

    if (n == 0) {
    	return a;
    }

    int min_x = p[0].x;
    int max_x = p[0].x;
    int min_y = p[0].y;
    int max_y = p[0].y;

    a[1] = 0;

    for (int i = 1; i < n; i++) {

        if (p[i].x < min_x){ 
        	min_x = p[i].x;
        }
        if (p[i].x > max_x) {
        	max_x = p[i].x;
        }
        if (p[i].y < min_y) {
        	min_y = p[i].y;
        }
        if (p[i].y > max_y) {
        	max_y = p[i].y;
        }

        a[i + 1] =
            (int64_t)(max_x - min_x) *
            (max_y - min_y);
    }

    return a;
}

//

int main(){
	Point p[4] = {
        {.x = 0, .y = 0},
        {.x = 2, .y = 2},
        {.x = 1, .y = 1},
        {.x = -1, .y = 1},
    };

	int64_t *a = bounding_box_area(4, p);

    for (int i = 0; i <= 4; i++) {
        printf("%lld\n", a[i]);
    }

    free(a);

}