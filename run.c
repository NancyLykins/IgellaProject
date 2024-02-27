#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *args[]){
    char *point = args[1];
    char conf[1];
    if(strcmp(args[1], "git") == 0){
        system("git branch");
        printf("Confirmar branch y/n: ");
        scanf("%s", &conf);
        if(strcmp(conf, "y") == 0){
            system("git add .");
            char commit[] = "git commit -m '";
            strcat(commit, args[2]);
            strcat(commit, "'");
            system(commit);
        }
        return 0;
    }
    printf("%s '%s'\n", args[1], args[2]);
    for(int i = 1; i < argc; i++){
        char *parm = args[i];
        if(strcmp(parm, "api") == 0){
            printf("Starting API");
            system("(cd api && npm run dev)");
        } else if(strcmp(parm, "bot") == 0){
            printf("Starting discord client");
            system("(cd bot && python client.py)");
        } else if(strcmp(parm, "web") == 0){
            printf("Starting web server");
            system("(cd web && php -S localhost:5000)");
        } else{
            printf("The parmn %c is not valid", *parm);
        }
    }
}
