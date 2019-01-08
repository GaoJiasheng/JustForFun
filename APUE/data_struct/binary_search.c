#include <stdio.h>
#include "common/print.h"

#define TRUE 1
#define FALSE 0

typedef  int bool;

int binary_search(int *, int, int);

int main(void) {
    int array[20];
    int i = 0,result = -1;
    for(i = 0;i < 20; i++) {
        array[i] = i * 4;
    }
    result = binary_search(array, 20, 16);
    printf("\n\nThe result is : %d\n", result);
}

//只考虑升序情况
int binary_search(int * array, int len, int key) {
    int i = 0;
    int start = 0, end = len-1, mid = 0;
    int index = -1;

    while(start < end) {
        print_array(array, 20, start, end);
        if(array[start] == key) {
            index =  start;
            break;
        } else if(array[end] == key) {
            index = end;
            break;
        } else {
            mid = (start + end)/2;
            if(array[mid] == key) {
                index = mid;
                break;
            } else if(array[mid] > key) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
    }

    return index;
}
