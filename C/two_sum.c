#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int compare(const void *a, const void *b) {
    int arg1 = *(const int *)a;
    int arg2 = *(const int *)b;

    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    qsort(nums, numsSize, sizeof(int), compare);

    int left = 0, right = numsSize - 1;

    while(left < right) {
        int sum = nums[left] + nums[right];
        if(sum == target) {
            *returnSize = 2;
            int* result = (int*)malloc(*returnSize * sizeof(int));
            result[0] = left;
            result[1] = right;
            return result;
        } else if(sum < target) {
            left++;
        } else {
            right--;
        }
    }
    *returnSize = 0;
    return NULL;
}

int main()
{   
    int nums[] = {3, 2, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 6;
    int returnSize = 0;
    twoSum(nums, numsSize, target, &returnSize);
    for (int i = 0; i < returnSize; i++){
        printf("%d\n", nums[i]);    
    }
    return 0;
}