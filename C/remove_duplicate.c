#include "stdlib.h"
#include "stdio.h"

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) 
        return 0;

    int k = 1;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[k - 1]) {
            nums[k++] = nums[i];
        }
    }
    return k;
}

int main() {
    int nums[] = {1,1,2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int k = removeDuplicates(nums, numsSize);
    printf("k: %d\n", k);
    for (int i = 0; i < k; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;
}