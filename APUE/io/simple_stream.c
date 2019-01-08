#include "apue.h"

int main(void) {
    if (lseek(STDIN_FILENO, 0, SEEK_CUR) == -1)
        printf("cannot seek\n");
    else
        printf("SEEK OK\n");

    exit(0);
}

/*
 * method to use :
 * ./a.out < /etc/passwd
 * cat /etc/passwd | a.out
 * ./a.ut < /var/spool/cron/FIFO
 */
