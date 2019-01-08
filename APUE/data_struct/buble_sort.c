#include <stdio.h>
#include "common/print.h"


void buble_sort(int *, int);

int main(void) {
    int array[10] = {6,3,15,5,8,2,4,9,123,1};
    print_array(array, 10, 5, -1);
    buble_sort(array, 10);
    print_array(array, 10, -1, -1);
    return 0;
}

void buble_sort(int *array, int length) {
    int i = 0, j=0, temp = 0;
    int swap = TRUE;

    for(i=0; i < length-1; i++) {
        if (swap == FALSE) {
            break; 
        };

        for (j=0; j < length -1; j ++) {
            if (array[j] > array[j+1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j+1] = temp;
                swap = TRUE;
            };
        };
    };
}
