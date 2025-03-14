#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

void reverse(char* s, int start, int end) {
    while (start < end) {
        char tmp = s[start];
        s[start] = s[end];
        s[end] = tmp;
        start++;
        end--;
    }
}

void removeSpaces(char* s) {
    int i, j;
    for (i = 0, j = 0; s[i]; ++i)
        // if not a space or (if a space and previous is not a space)
        if (s[i] != ' ' || (i > 0 && s[i - 1] != ' ')) 
            s[j++] = s[i];


    // check last char is not a space
    if (j > 0 && s[j - 1] == ' ') 
        j--;

    s[j] = '\0';
}

char* reverseWords(char* s) {
    // first remove starting, trailing spaces and > 1 space between words
    removeSpaces(s);
    int n = strlen(s);
    // step 2 reverse the string
    reverse(s, 0, n - 1);

    // step 3 - 2 pointers to loop through string and reverse each word 
    // when rp lands on a space
    int lp = 0;
    for (int rp = 0; rp < n; rp++) {
        if (s[rp] == ' ') {
            reverse(s, lp, rp - 1);
            lp = rp + 1;
        }
    }

    reverse(s, lp, n - 1);
    return s;
}

int main()
{
    char s[] = "  hello world  ";
    char* result = reverseWords(s);
    printf("%s\n", result);
    
    return 0;
}