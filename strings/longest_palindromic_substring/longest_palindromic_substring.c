#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/* brute force */

void substring(char *dest, const char *src, int start, int end) {
    int len = end - start + 1;
    strncpy(dest, src + start, len);
    dest[len] = '\0'; // Null-terminate the substring
}

bool check_palindromic_string(const char *s) {
    for (int i = 0; i < strlen(s) / 2; i++){
        if (s[i] != s[strlen(s) - i - 1]) {
            return false;
        }
    }
    return true;
}
    
// time complexity is O(n^3)
// auxiliary space O(1)
// space complexity O(n + 1)

const char* get_longest_palindromic_string(const char *str){
    char *longest = "";
    for (int i = 0; i < strlen(str); i++) {
        for (int j = i; j < strlen(str); j++) {
            char sub[(j+1)- i];
            substring(sub, str, i, j);
            if (check_palindromic_string(sub)) {
                if (strlen(sub) > strlen(longest)) {
                    //longest = sub;
                }
            }
        }
    }
    return longest;
}

int main() {
    char *str = "babad";
    printf("%s\n", get_longest_palindromic_string(str));

    return 0;
}

/* brute force */
