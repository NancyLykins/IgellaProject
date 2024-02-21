#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *args[]){
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
