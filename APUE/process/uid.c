#include "../apue.h"

int main() {
    printf("uid is :%d \n euid is %d\n\n", getuid(), geteuid());
    return 0;
}
