#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
char note[0x100]="/bin/sh\x00";
int main(int argc, char *argv[0x20]){
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    char name[0x100];
    int rah=0;
    for(int i=0;i<0x200;i++){
        name[i]=argv[1][i];
    }
    system("echo False>admincheck.txt");
    if(argc!=3){
        printf("Only two arguments are needed\n");
    }
    else if(strcmp(argv[1], "admin")==0 && strcmp(argv[2], "whale")==0){
        printf("Login success");
        rah=1;
    }
    if(rah!=0){
        system("echo True>admincheck.txt");
    }
    return 0;
}
