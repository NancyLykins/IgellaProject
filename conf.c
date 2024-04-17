#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define conf ".igella.conf" //Config file name 

int main(){
    char line[1000];
    char env_line[1000];
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
                FILE *dot_env;
                dot_env = fopen(api_env_path, "r");
                if (dot_env == NULL) {
                    printf("Error opening file %s\n", api_env_path);
                    return 1;
                }
                while(fgets(env_line, 100, dot_env) != NULL){
                    char *nl = strchr(env_line, '\n');
                    if(nl != NULL) *nl = '\0';
                    printf("%s\n", env_line);
                    if(strncmp(env_line, key, sizeof(key))){
                        printf("Access");
                        fprintf(dot_env, "%s", key);
                    }
                }
                fclose(dot_env);
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