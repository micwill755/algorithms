#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

*/


// Definition for a binary tree node.
struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

/*bool helper(struct TreeNode* node, long min, long max) {
    if (node == NULL) 
        return true; // Base case: empty tree is valid
    if (node->val <= min || node->val >= max) 
        return false; // Check constraints
    
    // Recursively check left and right subtrees
    return helper(node->left, min, node->val) && helper(node->right, node->val, max);
}
bool isValidBST(struct TreeNode* root) {
    return helper(root, -10000000000, 10000000000);
}*/

bool isValidBST(struct TreeNode* root) {
    struct TreeNode* curr = root;
    struct TreeNode* pre;
    int prevValue = INT_MIN; 

    while (curr != NULL) {
        if (curr->left == NULL) {
          
            // Process curr node
            if (curr->data <= prevValue) {
              
                // Not in ascending order
                return 0; 
            }
            prevValue = curr->data;
            curr = curr->right;
        } else {
          
            // Find the inorder predecessor of curr
            pre = curr->left;
            while (pre->right != NULL && pre->right != curr) {
                pre = pre->right;
            }

            if (pre->right == NULL) {
              
                // Create a temporary thread to the curr node
                pre->right = curr;
                curr = curr->left;
            } else {
              
                // Remove the temporary thread
                pre->right = NULL;

                // Process the curr node
                if (curr->data <= prevValue) {
                  
                    // Not in ascending order
                    return 0; 
                }
                prevValue = curr->data;
                curr = curr->right;
            }
        }
    }

    return 1; 
}

// Example usage
int main() {
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->data = 2;
    root->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->left->data = 1;
    root->left->left = NULL;
    root->left->right = NULL;
    root->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->right->data = 3;
    root->right->left = NULL;
    root->right->right = NULL;

    if (isValidBST(root)) {
        printf("The binary tree is a valid BST.\n");
    } else {
        printf("The binary tree is not a valid BST.\n");
    }
    // Free allocated memory
    free(root->left);
    free(root->right);
    free(root);
}