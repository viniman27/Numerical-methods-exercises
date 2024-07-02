#include "interface.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <rpc/rpc.h>

int main(int argc, char* argv[]) {
    CLIENT* client;
    Dictionary* dict;
    char* server;
    char* filename;
    FILE* file;
    char word[100];
    int mode;

    if (argc < 4) {
        printf("Uso: %s <server> <mode> <filename>\n", argv[0]);
        return 1;
    }

    server = argv[1];
    mode = atoi(argv[2]);
    filename = argv[3];
    dict = (Dictionary*)malloc(sizeof(Dictionary));

    if (dict == NULL) {
        printf("Erro ao alocar memória para o dicionário.\n");
        return 1;
    }

    init_dictionary(dict);

    if (mode == 0) { // Modo inclusão
        file = fopen(filename, "r");
        if (file == NULL) {
            printf("Erro ao abrir o arquivo.\n");
            return 1;
        }

        while (fscanf(file, "%s", word) != EOF) {
            if (add_word(dict, word) < 0) {
                printf("Dicionário cheio.\n");
                break;
            }
        }

        fclose(file);
    } else if (mode == 1) { // Modo consulta
        if (add_word(dict, "IMPRIMIR") < 0) {
            printf("Dicionário cheio.\n");
            return 1;
        }
    } else {
        printf("Modo inválido.\n");
        return 1;
    }

    if (mode == 0) {
        printf("Modo inclusão:\n");
        print_dictionary(dict);
    } else if (mode == 1) {
        printf("Modo consulta:\n");

        dict = print_dictionary_1(NULL, client);
        if (dict == NULL) {
            clnt_perror(client, server);
            return 1;
        }

        print_dictionary(dict);
    }

    clnt_destroy(client);
    free(dict);

    return 0;
}