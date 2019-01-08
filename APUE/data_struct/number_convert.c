#include <stdio.h>

//newbase is new base
//value is value in decimal
void ConvertDecToOther(int newbase, int value) {
    //level is stack's top sign
    //stack is stack self
    int level;
    int stack[100];

    //init stack top
    level = 0;

    while(value != 0) {
        stack[level++] = value % newbase;
        value = value / newbase;
    }

    for(; level>0; level--) {
        printf("%d", stack[level-1]);
        if ((level-1) % 4 == 0) {
            printf(" ");
        }
    }
    printf("\n");
}

int main(void) {
    ConvertDecToOther(8, 1178);
}
