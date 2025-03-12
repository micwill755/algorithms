#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

int strStr(char* haystack, char* needle) {
    for (int i = 0; haystack[i] != '\0'; i++) {
        // if we find first char
        if (haystack[i] == needle[0]) {
            int j = 0;

            while (needle[j] != '\0') {
                if (haystack[i + j] != needle[j]) {
                    break;
                }
                j++;
            }

            if (needle[j] == '\0')
                return i;
        }
    }

    return -1;
}

// Example usage
int main() {
    strStr("sadbutsad", "sad");
}