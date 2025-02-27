#include <stdlib.h>
#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void dfs(struct TreeNode* root) {
    if (root == NULL)
        return;
    dfs(root->left);
    printf("%d\n", root->val);
    dfs(root->right);
}

struct TreeNode* sortedListToBST(int* nums, int numsSize) {
    if (numsSize == 0)
        return NULL;
    int mid = numsSize / 2;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = nums[mid];
    root->left = sortedListToBST(nums, mid);
    root->right = sortedListToBST(nums + mid + 1, numsSize - mid - 1);
    return root;
}

int main() {
    int nums[] = {-10,-3,0,5,9};
    int size = sizeof(nums) / sizeof(nums[0]);
    struct TreeNode* root = sortedListToBST(nums, size);
    dfs(root);
    return 0;
}
