#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

// a*l-----l*()a
/*
    Big(O) = O(n)
    Aux Space = O(lp + rp + left + right)
*/
bool check_palidrome_with_special(char *str) {
    int len = strlen(str);
    int lp = 0;
    int rp = len - 1;
    int l_len = 0;
    int r_len = 0;
    char *left = (char *)malloc(len * sizeof(char));
    char *right = (char *)malloc(len * sizeof(char));

    while (lp < len || rp >= 0) {
        if (lp < (len) && isalnum(str[lp])) {
            left[l_len++] = str[lp];
        }
        if (rp >= 0 && isalnum(str[rp])) {
            right[r_len++] = str[rp];
        }
        lp++;
        rp--;
    }

    return strcmp(left, right) == 0;
}

int main()
{   
    printf("Is palindrome %d", check_palidrome_with_special("a*l---ul--l*()a"));
    return 0;
}