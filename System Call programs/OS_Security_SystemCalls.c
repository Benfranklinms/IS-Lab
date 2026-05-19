// Experiment No.: 6 - OS SECURITY USING SYSTEM CALLS
// Aim: To demonstrate OS security using Linux system calls
// (fork, exec, getpid, exit, wait, close, stat, opendir, readdir)

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();
  if (pid == 0) {
    printf("Child PID: %d\n", getpid());
    struct stat file_info;
    stat("sample.txt", &file_info);
    printf("sample.txt size: %ld bytes\n", file_info.st_size);
    DIR *dir = opendir(".");
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
      printf("Found: %s\n", entry->d_name);
    }
    close(dirfd(dir));
    execlp("date", "date", NULL);
    exit(EXIT_FAILURE);
  } else {
    printf("Parent PID: %d\n", getpid());
    wait(NULL);
    exit(EXIT_SUCCESS);
  }
}
