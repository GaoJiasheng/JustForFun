#include <stdio.h>
#include "print.h"

void print_array(int *array, int length, int ptr1, int ptr2) {
    int i = 0;

    printf("----------------->\n");
    for(i=0; i< length; i++) {
        if(i==ptr1) {
            printf("%d(*1)  ", array[i]);
        }
        else if (i == ptr2) {
            printf("%d(*2)  ", array[i]);
        }
        else {
            printf("%d  ", array[i]);
        }
    }
    printf("\n");

}


void rise_sort(int *array, int length) {
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


void down_sort(int *array, int length) {
    int i = 0, j=0, temp = 0;
    int swap = TRUE;

    for(i=0; i < length-1; i++) {
        if (swap == FALSE) {
            break; 
        };

        for (j=0; j < length -1; j ++) {
            if (array[j] < array[j+1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j+1] = temp;
                swap = TRUE;
            };
        };
    };
}
