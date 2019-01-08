#include "../apue.h"

int main(void) {
    pid_t pid;
    pid = fork();
    if(pid == 0) {
	printf("Now pid is in child: %d . \n", getpid());
	printf("Now ppid is in child: %d . \n", getppid());
    } else {
	printf("Now pid is parent : %d . \n", getpid());
	printf("Now ppid is in parent: %d . \n", getppid());
	sleep(2);
    }
}
