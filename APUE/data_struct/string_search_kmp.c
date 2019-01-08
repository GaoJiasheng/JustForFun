#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int * get_new(char * model) {
    int len, i;
    int *new;
    len = strlen(model);
    new = malloc(sizeof(int) * len);
    
    for(i=0; i < len; i++) {
        if(i == 0 || i == 1)  {
            new[i] = i - 1;
        } else {
            if(model[i-1] == model[new[i-1]]) {
                new[i] = new[i-1] + 1;
            } else {
                new[i] = 0;
            }
        }
    }
    return new;
}

int kmp_search(char *orin, char *model) {
    int i=0, j=0;
    int *new;
    new = get_new(model);
    while(i <= strlen(orin) && j <= strlen(model)) {
        if(j == strlen(model)) {
            return i-j;
        }
        if(i == strlen(orin))  {
            return -1;
        }

        if(orin[i] == model[j]) {
            i++;
            j++;
        } else {
            if(j == 0) {
                i++;
            } else {
                j = new[j];
                if(j == -1) {
                    j = 0; 
                }
            }
        }
    }
    return -1;
}

int main(void) {
    char *b= "abcsdfkcabcasdfkgjlab";
    char *c= "sdfkg";
    int * new;
    int i;
    i = kmp_search(b, c);

    printf("result: %d\n", i);
}
