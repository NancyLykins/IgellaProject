#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define LOCAL_IP "192.168.0.9:8080"

int main(int argc, char *args[]){
    char *point = args[1];
    char conf[1];

    if(strcmp(args[1], "git") == 0){
        system("git add .");
        char *commit;
        sprintf(commit, "git commit -m '%s'", args[2]);
        system(commit);
        return 0;
    }

    for(int i = 1; i < argc; i++){
        char *parm = args[i];
        if(strcmp(parm, "api") == 0){
            system("(cd api && npm run dev)");
        
        } else if(strcmp(parm, "bot") == 0){
            system("(cd bot && python client.py)");
        
        } else if(strcmp(parm, "web") == 0){
            char *start_web_command;
            sprintf(start_web_command, "(cd web && php -S %s)", LOCAL_IP);
            system(start_web_command);
            
        } else if(strcmp(parm, "init") == 0){
            printf("Confign all");
            system("(cd api && npm install)");
            char option[3] = "no";
            do{
                printf("Your OS is based in debian? (y|yes / n|no)");
                scanf("%s", option);
                if(option[0] == 'y'){                   
                    printf("\n\nUncomment ;extension=curl to it works correctly"); 
                    system("sudo apt install php-curl");
                    return 0;
                } else if(option[0] == 'n'){
                    printf("Then fuck yourself");
                    return 400;
                }
            } while(option[0] != 'y');

        
        } else{
            printf("The parmn %s is not valid", parm);
        }
    }
    return 0;
}