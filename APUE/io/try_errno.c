#include "apue.h"
#include <errno.h>

int main(void) {
    fprintf(stderr, "EACES: %s\n", strerror(EACCES));
    errno = ENOENT;
    perror(argv[0]);
    exit(0);
}
