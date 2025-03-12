#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    /*if (strsSize == 0) return ""; 
    for (int i = 0; strs[0][i] != '\0'; i++) {
        char currentChar = strs[0][i];
        for (int j = 1; j < strsSize; j++) {
            if (strs[j][i] != currentChar || strs[j][i] == '\0') {
                strs[0][i] = '\0'; 
                return strs[0];
            }
        }
    }
    return strs[0];*/

    char* prefix = (char*)malloc(sizeof(char) * 200);
    int curr = 0;

    for (int i = 0; strs[0][i] != '\0'; i++) {
        char currentChar = strs[0][i];
        for (int j = 1; j < strsSize; j++) {
            if (strs[j][i] != currentChar || strs[j][i] == '\0') {
                prefix[i] = '\0'; 
                return prefix;
            }
        }
        prefix[curr++] = strs[0][i];
    }
    
    prefix[curr] = '\0'; 
    return prefix;
}

int main()
{   
    printf("%s", longestCommonPrefix((char*[]){"a"}, 1));
    return 0;
}