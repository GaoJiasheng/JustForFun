#include "apue.h"
#include <errno.h>      /*for definition of errno */
#include <stdarg.h>     /*ISO C variable aruments */

static void err_doit(int,int, const char *, va_list);

/*
 * Nonfatal error related to a system call.
 * Print a message and return.
 */

void err_ret(const char * fmt, ...)
{
    va_list     ap;
    va_start(ap,fmt);
    err_doit(1,errno,fmt,ap);
    va_end(ap);
}

/*
 * Faltal error related to a system call.
 * Print a message and terminate.
 */
void err_sys(const char * fmt, ...)
{
    va_list     ap;
    va_start(ap,fmt);
    err_doit(1,errno,fmt,ap);
    va_end(ap);
    exit(1);
}

/*
 * Faltal error unrelated to a system call.
 * Error code passed as explict parameter.
 * Print a message and terminate.
 */
void err_exit(int error, const char * fmt, ...)
{
    va_list     ap;
    va_start(ap,fmt);
    err_doit(1,error,fmt,ap);
    va_end(ap);
    exit(1);
}

/*
 * Faltal error related to a system call.
 * Print a message, dump core, and terminate.
 */
void err_dump(const char * fmt, ...)
{
    va_list     ap;
    va_start(ap,fmt);
    err_doit(1,errno,fmt,ap);
    va_end(ap);
    abort();
    exit(1);
}

/*
 * Nonfatal error unrelated to a system call.
 * Print a message and return.
 */
void err_msg(const char *fmt, ...)
{
    va_list     ap;
    va_start(ap,fmt);
    err_doit(0,0,fmt,ap);
    va_end(ap);
}

/*
 * Faltal error unrelated to a system call.
 * Print a message and terminate.
 */
void err_quit(const char * fmt, ...)
{
    va_list ap;
    va_start(ap,fmt);
    err_doit(0,0,fmt,ap);
    va_end(ap);
    exit(1);
}

/*
 * Print a message and return to caller.
 * Caller specifies "errnoflag".
 */

static void err_doit(int errnoflag,int error, const char * fmt,va_list ap)
{
    char buf[MAXLINE];
    vsnprintf(buf, MAXLINE, fmt,ap);
    if(errnoflag)
        snprintf(buf+strlen(buf), MAXLINE-strlen(buf),": %s",strerror(error));
    strcat(buf,"\n");
    fflush(stdout);
    fputs(buf,stderr);
    fflush(NULL);
}
