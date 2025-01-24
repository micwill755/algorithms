#include <iostream>
using namespace std;

class Node {
    public:
    int data;
    Node* left;
    Node* right;
    Node(int data){
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

int sum(Node *node) {
    if(node == NULL) return 0;
    return sum(node->left) + node->data + sum(node->right);
}

/*bool sumTree(Node *node) {
    int ls, rs = 0;
    if (node == NULL) return true;

    ls = sum(node->left);
    rs = sum(node->right);

    if (node->data == ls + rs && sumTree(node->left) && sumTree(node->right))
        return true;

    return false;
}*/

bool sumTree(Node *node) {
    int ls, rs = 0;
    if (node == NULL || (node->left == NULL && node->right == NULL)) return true;

    ls = sum(node->left);
    rs = sum(node->right);

    if (node->data == ls + rs && sumTree(node->left) && sumTree(node->right))
        return true;

    return false;
}

int main() {
    Node *root = new Node(26);
    root->left = new Node(10);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(6);
    root->right->right = new Node(3);

    if (sumTree(root))
        cout << "The given tree is a SumTree ";
    else
        cout << "The given tree is not a SumTree ";

    return 0;
}