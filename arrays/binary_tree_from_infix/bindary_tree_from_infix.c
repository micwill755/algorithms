#include <stdio.h>
#include <stdlib.h>

// Definition of a node in the expression tree
typedef struct TreeNode {
    char data;             // Operator or operand
    struct TreeNode* left;  // Pointer to the left child
    struct TreeNode* right; // Pointer to the right child
} TreeNode;

// Function to create a new node
TreeNode* createNode(char data) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    if (newNode != NULL) { // Check if memory allocation was successful
        newNode->data = data;
        newNode->left = NULL;
        newNode->right = NULL;
    } else {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE); // Exit the program if memory allocation fails
    }
    return newNode;
}

// Function to build an expression tree (example for a simple expression "a+b")
TreeNode* buildExpressionTree() {
    TreeNode* root = createNode('+');
    root->left = createNode('a');
    root->right = createNode('b');
    return root;
}

// Function to evaluate the expression tree (for the example above)
int evaluateExpressionTree(TreeNode* root) {
    if (root == NULL) return 0;

    // If the node is a leaf (operand), return its value (assuming 'a' is 1 and 'b' is 2 for simplicity)
    if (root->left == NULL && root->right == NULL) {
        if (root->data == 'a') return 1;
        if (root->data == 'b') return 2;
        return 0; // Default case, should not happen with the current tree
    }

    // Recursively evaluate the subtrees
    int leftValue = evaluateExpressionTree(root->left);
    int rightValue = evaluateExpressionTree(root->right);

    // Apply the operator
    switch (root->data) {
        case '+': return leftValue + rightValue;
        case '-': return leftValue - rightValue;
        case '*': return leftValue * rightValue;
        case '/': return leftValue / rightValue;
        default: return 0; // Default case, should not happen with the current tree
    }
}

// Function to free the memory used by the expression tree
void freeExpressionTree(TreeNode* root) {
    if (root != NULL) {
        freeExpressionTree(root->left);
        freeExpressionTree(root->right);
        free(root);
    }
}

int main() {
    TreeNode* expTree = buildExpressionTree();
    int result = evaluateExpressionTree(expTree);
    printf("Result of the expression: %d\n", result);
    freeExpressionTree(expTree); // Free the allocated memory
    return 0;
}