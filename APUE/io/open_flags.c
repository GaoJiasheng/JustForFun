#include "apue.h"
#include <fcntl.h>

int main(void) {
    printf("O_RDONLY:%d\n", O_RDONLY);
    printf("O_WRONLY:%d\n", O_WRONLY);
    printf("O_RDWR:%d\n", O_RDWR);
    printf("O_NONBLOCK:%d\n", O_NONBLOCK);
    printf("O_APPEND:%d\n", O_APPEND);
    printf("O_CREAT:%d\n", O_CREAT);
    printf("O_EXCL:%d\n", O_EXCL);
    printf("O_TRUNC:%d\n", O_TRUNC);
    printf("O_NOCTTY:%d\n", O_NOCTTY);
}
