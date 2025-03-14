#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

char* convert(char* s, int numRows) {
    if (numRows == 1) {
        return s;
    }

    int len = strlen(s);
    char* res = (char*)malloc(sizeof(char) * (len + 1));
    int index = 0;
    int increment = (numRows - 1) * 2;

    for (int r = 0; r < numRows; r++) {
        for (int j = r; j < len; j += increment) {
            res[index++] = s[j];
            // check in middle row and in bounds
            if (r > 0 && r < numRows - 1 && j + increment - 2 * r < len) {
                res[index++] = s[j + increment - 2 * r];
            }
        }
    }

    res[index] = '\0';
    return res;
}

int main()
{
    char* s = "PAYPALISHIRING";
    int numRows = 4;

    char* res = convert(s, numRows);
    printf("%s\n", res);
    
    return 0;
}