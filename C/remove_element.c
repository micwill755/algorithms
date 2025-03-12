#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

int removeElement(int* nums, int numsSize, int val) {
    int k = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[k++] = nums[i];
        }
    }
    return k;
}

int main()
{   
    int nums[] = {0,1,2,2,3,0,4,2};
    int val = 2;
    int size = sizeof(nums) / sizeof(nums[0]);
    int k = removeElement(nums, size, val);
    printf("k = %d\n", k);
    return 0;
}