#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define conf ".igella.conf" //Config file name 

int edit_file(char *file_path, char *key, char *value){
    char env_line[1000];
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
            diference = line_length - strlen(new_conf);
            int i = 0;
            new_conf = (char *) realloc(new_conf, strlen(new_conf) + diference);
            while(i < diference){
                strcat(new_conf, " ");
                i++;
            }
            strcat(new_conf, "\n");
            fputs(new_conf, dot_env);
            fseek(dot_env, position, SEEK_SET);
        }
    }
    fclose(dot_env);
    return 0;
}


int main(){
    char line[1000];
    
    char *api_env_path = NULL;
    char *web_env_path = NULL;
    char *bot_env_path = NULL;
    

    FILE *config_file;
    
    config_file = fopen(conf, "r");

    if(config_file == NULL){
        printf("Arquivo %s não encontrado\n", conf);
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
            } else if(strcmp(key, "API_URL") == 0){
                edit_file(api_env_path, key, value);
            } else if(strcmp(key, "WEB_URL") == 0){
                edit_file(api_env_path, key, value);
            }
        }
    }
    printf("\n");
    fclose(config_file);
    free(api_env_path);
    free(web_env_path);
    free(bot_env_path);
    return 0;
}