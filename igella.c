#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define CONF_FILE ".igella.conf" //Config file name 
#define LOCAL_IP "192.168.0.9:8080"

int edit_file(char *file_path, char *key, char *value){
    char env_line[1000];
    char *lf = "\n";
    long position;
    FILE *dot_env;
    dot_env = fopen(file_path, "r+");
    if (dot_env == NULL) {
        printf("Error opening file %s\n", file_path);
        return 1;
    }
    while(fgets(env_line, 100, dot_env) != NULL){
        if(strncmp(env_line, key, strlen(key)) == 0){
            char *new_conf = (char *) malloc(sizeof(char) * (strlen(key) + strlen(value) + 4));
            int line_length = strlen(env_line);
            int diference = 0;
            sprintf(new_conf, "%s = %s", key, value);
            int new_line_length = strlen(new_conf);
            position = ftell(dot_env);
            fseek(dot_env, -strlen(env_line), SEEK_CUR);
            diference = line_length - new_line_length - 1;
            int i = 0;
            new_conf = (char *) realloc(new_conf, new_line_length + diference);
            while(i < diference){
                strcat(new_conf, " ");
                i++;
            }
            fputs(new_conf, dot_env);
            fputs(lf, dot_env);
            fseek(dot_env, position, SEEK_SET);
            free(new_conf);
        }
    }
    fclose(dot_env);
    return 0;
}

int conf_igella(){
    char line[1000];
    char *api_env_path = NULL;
    char *web_env_path = NULL;
    char *bot_env_path = NULL;

    FILE *config_file;
    config_file = fopen(CONF_FILE, "r");

    if(config_file == NULL){
        printf("Arquivo %s não encontrado\n", CONF_FILE);
        return 404;
    }

    while(fgets(line, sizeof(line), config_file) != NULL){
        if(line[0] != '#' && line[0] != '\n'){
            char *key = strtok(line, " = ");
            char *value = strtok(NULL, " = ");
            char *nl = strchr(value, '\n');
            if(nl != NULL) *nl = '\0';
            if(strcmp(key, "api_env_path") == 0){
                api_env_path = (char *) realloc(api_env_path, strlen(value) + 1);
                strcpy(api_env_path, value);
            } else if(strcmp(key, "bot_env_path") == 0){
                bot_env_path = (char *) realloc(bot_env_path, strlen(value) + 1);
                strcpy(bot_env_path, value);
            } else if(strcmp(key, "web_env_path") == 0){
                web_env_path = (char *) realloc(web_env_path, strlen(value) + 1);
                strcpy(web_env_path, value);
            }

            if(strcmp(key, "API_URL") == 0){
                edit_file(api_env_path, key, value);
                edit_file(bot_env_path, key, value);
            } else if(strcmp(key, "WEB_URL") == 0){
                edit_file(api_env_path, key, value);
            } else if(strcmp(key, "PORT") == 0){
                edit_file(api_env_path, key, value);
            } else if(strcmp(key, "BOT_TOKEN") == 0){
                edit_file(bot_env_path, key, value);
            }
        }
    }
    printf("\n");
    fclose(config_file);
    return 0;
}

int main(int argc, char *args[]){
    if(strcmp(args[1], "git") == 0){
        system("git add .");
        char *commit = (char *) malloc(strlen(args[2]) + 20);
        sprintf(commit, "git commit -m '%s'", args[2]);
        system(commit);
        system("git push origin master");
        return 0;
    }

    for(int i = 1; i < argc; i++){
        char *parm = args[i];
        if(strcmp(parm, "api") == 0){
            system("(cd api && npm run dev)");
        } else if(strcmp(parm, "bot") == 0){
            system("(cd bot && python client.py)");

        } else if(strcmp(parm, "web") == 0){
            char *start_web_command = (char *) malloc(sizeof(char) * 50);
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
        } else if(strcmp(parm, "conf") == 0){
            conf_igella();
        } else{
            printf("The parmn %s is not valid\n", parm);
        }
    }
    return 0;
}
