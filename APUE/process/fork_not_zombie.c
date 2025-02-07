#include <sys/wait.h>
#include "../apue.h"

int main(void) {
    pid_t pid;

    if ((pid = fork()) < 0) {
        err_sys("fork error"); 
    } else if (pid == 0) {
        if ((pid = fork()) < 0) 
            err_sys("fork2 error");
        else if (pid > 0)
            exit(0);

        sleep(2);
        printf("second child, parent pid = %d\n", getppid());
    }

    if (waitpid(pid, NULL, 0) != pid)
        err_sys("waitpid error");

    exit(0);
}
