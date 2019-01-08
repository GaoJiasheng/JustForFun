#include <stdio.h>
#include <unistd.h>

int main(void) {
    FILE * file;
    char buf[256];
    int n, i;
    file = popen("ls -al /home", "w");
    n = read(file, &buf, 256);
    for(i=0; i< n-1; i++) {
	printf(buf[i]); 
    }
    pclose(file);
    printf("--");
}
