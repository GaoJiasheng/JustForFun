#include "../apue.h"
#include <fcntl.h>

/* just a function
 * use to add attribution or del attribution from fd
 */

void set_fl(int fd, int flags) {
    int val;

    if ((val = fcntl(fd, F_GETFL, 0)) < 0) {
	err_sys("fcntl F_GETFL error");
    }

    val |= flags ; /* Add Attr*/
    val ~= flags ; /* Del Attr*/

    if (fcntl(fd, F_SETFL, val) < 0) {
	err_sys("fcntl F_SETFLL error");
    }

    exit(0);
}
