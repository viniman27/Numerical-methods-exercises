#ifndef DICTIONARY_INTERFACE_H
#define DICTIONARY_INTERFACE_H

typedef struct {
    char word[100];
    int count;
} WordEntry;

typedef struct {
    int numEntries;
    WordEntry entries[100];
} Dictionary;

void init_dictionary(Dictionary* dict);
int add_word(Dictionary* dict, char* word);
void print_dictionary(Dictionary* dict);

#endif