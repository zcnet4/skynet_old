#pragma once
#include <stdio.h>
#include <fcntl.h>
#include <assert.h>
#include <pthread.h>

#define random rand
#define srandom srand
#define snprintf _snprintf
typedef int ssize_t;

#ifdef _MSC_VER
# define inline __inline
#include "atomic_lock.h"
#endif

#ifndef __inline
	#define __inline __inline
#endif

//typedef long pid_t;
pid_t getpid();
int kill(pid_t pid, int exit_code);

// defined in WinSock2.h
__declspec(dllimport) int __stdcall gethostname(char *buffer, int len);
void usleep(size_t us);
void sleep(size_t ms);

//typedef struct timespec {
//	int tv_sec;
//	int tv_nsec;
//} timespec;

enum { CLOCK_THREAD_CPUTIME_ID, CLOCK_REALTIME, CLOCK_MONOTONIC };
int clock_gettime(int what, struct timespec *ti);

enum { LOCK_EX, LOCK_NB };
int flock(int fd, int flag);


struct sigaction {
	void (*sa_handler)(int);
};
enum { SIGPIPE };
void sigaction(int flag, struct sigaction *action, int param);

int pipe(int fd[2]);
int daemon(int a, int b);

char *strsep(char **stringp, const char *delim);

int write(int fd, const void *ptr, size_t sz);
int read(int fd, void *buffer, size_t sz);
int close(int fd);

void debug_log(char* log);
void debug_box(char* msg);


