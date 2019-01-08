#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
typedef int bool;

typedef struct node{
    int coefficient;
    int index;
    struct node * next;
} Node;

typedef struct polynmial{
    Node * start;
} Polynmial;

//create an empty polynmial
Polynmial CreatePolyn() {
    Polynmial *ret;
    ret = malloc(sizeof(Polynmial));
    ret -> start = NULL;
    return *ret;
}

//judge a polynmial if empty
bool IsPolynEmpty(Polynmial poly) {
    if(poly.start == NULL) {
        return TRUE;
    } else {
        return FALSE;
    }
}

//destory polynmial
void DestroyPolyn(Polynmial poly) {
    Node *round_ptr, *temp;

    round_ptr = poly.start;
    poly.start = NULL;

    while(round_ptr != NULL) {
        temp = round_ptr;
        round_ptr = round_ptr->next;
        free(temp);
    }
}

//print polynmial
void PrintPolyn(Polynmial poly, bool is_debug) {
    Node *round_ptr;
    round_ptr = poly.start;

    while (round_ptr != NULL) {
        if(is_debug != TRUE) {
            printf("%d*x^%d --> ", round_ptr -> coefficient, round_ptr -> index);
        } else {
            printf("(%d, %d) --> ", round_ptr -> coefficient, round_ptr -> index);
        }
        round_ptr = round_ptr -> next;
    }
    printf("NULL\n");
}

//return length of polynmial
int LengthOfPolyn(Polynmial poly) {
    Node * round_ptr;
    int count = 0;

    round_ptr = poly.start;

    while (round_ptr != NULL) {
        count++;
        round_ptr = round_ptr -> next;
    }
    return count;

}

//add node to polynomial
bool AddNode(Polynmial *poly, int coefficient, int index) {
    Node * ptr, *pre_ptr;
    ptr = poly -> start;

    while(ptr != NULL) {
        if(index == ptr -> index) {
            break;
        }
        pre_ptr = ptr;
        ptr = ptr -> next;
    }

    if(ptr == NULL) {
        //说明多项式中没有同阶的项
        ptr = malloc(sizeof(Polynmial));
        if (ptr != NULL) {
            ptr -> coefficient = coefficient;
            ptr -> index = index;
            ptr -> next = poly -> start;
            poly-> start = ptr;
            return TRUE;
        } else {
            return FALSE;
        }
    } else {
        //多项式中有同阶的项,ptr指向
        ptr -> coefficient += coefficient;
        if (0 == ptr -> coefficient) {
            pre_ptr -> next = ptr -> next;
            free(ptr);
        }
        return TRUE;
    }
}

//multiply node to polynomial
Polynmial MultiplyNode(Polynmial poly1, int coefficient, int index){
    Polynmial result;
    Node *ptr;
    int coe,ind;

    result = CreatePolyn();
    ptr = poly1.start;

    while(ptr != NULL) {
        coe = ptr -> coefficient * coefficient;
        ind = ptr -> index + index;
        AddNode(&result, coe, ind);
        ptr = ptr -> next;
    }
    return result;
}

//将两个多项式相加
Polynmial AddPolyn(Polynmial poly1, Polynmial poly2) {
    Polynmial result;
    Node *ptr1, *ptr2;

    result = CreatePolyn();

    ptr1 = poly1.start, ptr2 = poly2.start;

    while(ptr1 != NULL) {
        AddNode(&result, ptr1 -> coefficient, ptr1 -> index);
        ptr1 = ptr1 -> next;
    }

    while(ptr2 != NULL) {
        AddNode(&result, ptr2 -> coefficient, ptr2 -> index);
        ptr2 = ptr2 -> next;
    }

    //PrintPolyn(result, TRUE);
    return result;
}

//将两个多项式相减
Polynmial SubtractPolyn(Polynmial *poly1, Polynmial *poly2) {
    Polynmial result;
    Node *ptr1, *ptr2;

    result = CreatePolyn();

    ptr1 = poly1 -> start, ptr2 = poly2 -> start;

    while(ptr1 != NULL) {
        AddNode(&result, ptr1 -> coefficient, ptr1 -> index);
        ptr1 = ptr1 -> next;
    }

    while(ptr2 != NULL) {
        AddNode(&result, -(ptr2 -> coefficient), ptr2 -> index);
        ptr2 = ptr2 -> next;
    }

    //PrintPolyn(result, TRUE);
    return result;
}

//将两个多项式相乘
Polynmial MultiplyPolyn(Polynmial poly1, Polynmial poly2) {
    Node *ptr1;
    Polynmial temp, temp2, result;

    ptr1 = poly1.start;

    result = CreatePolyn();

    while(ptr1 != NULL) {
        temp = MultiplyNode(poly2, ptr1 -> coefficient, ptr1 -> index);
        temp2 = result;
        result = AddPolyn(result, temp);
        DestroyPolyn(temp);
        DestroyPolyn(temp2);
        ptr1 = ptr1 -> next;
    }

    return result;
}


int main(void) {
    //printf("Hello data structure !!\n\n");
    Polynmial x, y, z;
    x=CreatePolyn();
    y=CreatePolyn();
    AddNode(&x, 1, 1);
    AddNode(&x, 2, 2);
    AddNode(&y, 1, 1);
    AddNode(&y, 2, 2);
    printf("x:\n");
    PrintPolyn(x, TRUE);
    printf("y:\n");
    PrintPolyn(y, TRUE);
    z = MultiplyPolyn(x, y);
    printf("x * y:\n");
    PrintPolyn(z, TRUE);
}
