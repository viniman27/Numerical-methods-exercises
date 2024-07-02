#include "interface.h"
#include <stdio.h>
#include <string.h>

Dictionary* dictionary;

void init_dictionary(Dictionary* dict) {
    dict->numEntries = 0;
}

int add_word(Dictionary* dict, char* word) {
    int i;
    for (i = 0; i < dict->numEntries; i++) {
        if (strcmp(dict->entries[i].word, word) == 0) {
            dict->entries[i].count++;
            return 0;
        }
    }
    if (dict->numEntries < 100) {
        strcpy(dict->entries[dict->numEntries].word, word);
        dict->entries[dict->numEntries].count = 1;
        dict->numEntries++;
        return 0;
    }
    return -1; // Dicionário cheio
}

void print_dictionary(Dictionary* dict) {
    int i;
    for (i = 0; i < dict->numEntries; i++) {
        printf("%s: %d\n", dict->entries[i].word, dict->entries[i].count);
    }
}

void* print_dictionary_1_svc(void* argp, struct svc_req* rqstp) {
    return dictionary;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Uso: %s <porta>\n", argv[0]);
        return 1;
    }

    dictionary = (Dictionary*)malloc(sizeof(Dictionary));
    if (dictionary == NULL) {
        printf("Erro ao alocar memória para o dicionário.\n");
        return 1;
    }

    init_dictionary(dictionary);

    svc_run();

    return 0;
}