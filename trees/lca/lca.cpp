#include <iostream>
using namespace std;

class Node {
    public:
    int data;
    Node *left, *right;
    Node(int data) {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* lca (Node* root, int v1, int v2) {
    if (root == NULL) 
        return NULL;
    if (root->data == v1 || root->data == v2) 
        return root;

    Node* left = lca(root->left, v1, v2);
    Node* right = lca(root->right, v1, v2);

    if (left && right) 
        return root;
    
    return left ? left : right;
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    Node* ans = lca(root, 4, 5);
    if(ans == nullptr){
        cout<<"No common ancestor found";
    }
    else{
        cout<<"The ancestor found is "<<ans->data;
    }
    return 0;
}