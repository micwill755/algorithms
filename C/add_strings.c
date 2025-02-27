#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* addStrings(char* num1, char* num2) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int maxLen = (len1 > len2) ? len1 : len2;
    char* result = (char*)malloc(sizeof(char) * (maxLen + 2));

    result[maxLen + 1] = '\0'; 

    int carry = 0;
    int i = len1 - 1;
    int j = len2 - 1;
    int k = maxLen;

    while (i >= 0 || j >= 0 || carry) {
        int digit1 = (i >= 0) ? num1[i] - '0' : 0;
        int digit2 = (j >= 0) ? num2[j] - '0' : 0;
        int sum = digit1 + digit2 + carry;
        
        result[k] = (sum % 10) + '0';
        carry = sum / 10;

        i--;
        j--;
        k--;
    }

    return result + k + 1;
}

int main() {
    char num1[] = "123";
    char num2[] = "1456";

    char* result = addStrings(num1, num2);

    printf("%s", result);
    free(result);

    return 0;
}
