#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
  pid_t pid = fork();

  if(pid == 0){
  printf("child PID : %d\n", getpid());
//   execlp("date", "date", NULL);
  }
  else{
    wait(NULL);
    printf("parent ID : %d\n", getpid());
  }
}