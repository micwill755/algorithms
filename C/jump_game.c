#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

bool canJump(int* nums, int numsSize) {
    int goal = numsSize - 1;
    for (int i = numsSize - 1; i >= 0; i--) {
        if (i + nums[i] >= goal) {
            goal = i;
        }
    }
    return goal == 0;
}

int main()
{   
    printf("%d", canJump((int[]){2,3,1,0,4}, 5));
    return 0;
}