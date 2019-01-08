#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0
typedef int bool;

typedef struct stack {
    int len;
    int top;
    char *body;
} Stack;

Stack CreateStack(int len) {
    Stack ret;
    ret.len = len;
    ret.top = 0;
    ret.body = malloc(sizeof(char) * len);
    return ret;
}

char Pop(Stack * stack) {
    if(stack -> top <= 0) {
        return '\0';
    } else {
        char ret;
        ret = (stack -> body)[(stack -> top) - 1];
        (stack -> body)[--stack -> top] = '\0';
        return ret;
    }
}

char Push(Stack * stack, char a) {
    if(stack -> top >= stack -> len - 1) {
        return '\0';
    } else {
        (stack -> body)[stack -> top++] = a;
        return a;
    }
}

bool _is_left_bracket(char c) {
    if(c == '(' || c == '[' || c == '{') {
        return TRUE;
    } else {
        return FALSE;
    }
}

bool _is_right_bracket(char c) {
    if(c == ')' || c == ']' || c == '}') {
        return TRUE;
    } else {
        return FALSE;
    }
}

bool _can_matched(char a, char b) {
    if (a == '(' && b == ')') {
        return TRUE;
    }

    if (a == '[' && b == ']') {
        return TRUE;
    }

    if (a == '{' && b == '}') {
        return TRUE;
    }
    return FALSE;
}


int main(void) {
    Stack stack;
    char c; //just can input (){}[], 0 to end
    stack = CreateStack(10);
    while (1) {
        fflush(stdin);
        c = getchar();
        if(_is_left_bracket(c)) {
            c = Push(&stack, c);
            if (c == '\0') {
                printf("Error!!Stack FULL!!\n");
                break;
            }
        } else if (_is_right_bracket(c)) {
            char temp;
            temp = Pop(&stack);
            if(temp == '\0') {
                printf("Success!!Stack is Empty!\n");
                break;
            }
            if(_can_matched(temp, c)) {
                goto PRINT;
            } else {
                printf("Your input is wrong, cannot match(%c, %c)!!\n", temp, c);
                break;
            }
        } else {
            if(c == 10) {
                continue;
            } else {
                printf("Their are some charactor cannot match'%d'!!\n", c);
                break;
            }
        }
PRINT:
        if (stack.top != 0) {
            printf("c:%c\tbody:%s\ttop:%d\n", c, stack.body, stack.top);
        } else {
            printf("Success!!Stack is Empty!\n");
            break;
        }
    }

    return 0;
}
