#include <stdio.h>
#include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *first, *second, *prev;

void inorder(struct TreeNode *root) {
    if (root == NULL)
        return;
    
    inorder(root->left);
    
    if (prev != NULL && root->val < prev->val) {
        if (first == NULL) {
            first = prev;
        } 
        second = root;
    }
    
    prev = root;
    inorder(root->right);
}

void recoverTree(struct TreeNode* root) {
    first = second = prev = NULL;
    inorder(root);
    
    if (first && second) {
        int temp = first->val;
        first->val = second->val;
        second->val = temp;
    }
}

// Helper function to create a new node
struct TreeNode* newNode(int data) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = data;
    node->left = node->right = NULL;
    return node;
}

// Helper function to print inorder traversal (for testing)
void printInorder(struct TreeNode* node) {
    if (node == NULL)
        return;
    printInorder(node->left);
    printf("%d ", node->val);
    printInorder(node->right);
}

// Example usage
int main() {
    // Create a BST with two swapped nodes
    struct TreeNode* root = newNode(3);
    root->left = newNode(1);
    root->right = newNode(4);
    root->right->left = newNode(2);

    printf("Inorder traversal before recovery: ");
    printInorder(root);
    printf("\n");

    recoverTree(root);

    printf("Inorder traversal after recovery: ");
    printInorder(root);
    printf("\n");

    return 0;
}