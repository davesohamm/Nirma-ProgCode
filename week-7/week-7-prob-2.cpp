// 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-2 "Tree: Height of a Binary Tree"
#include <iostream>
#include <algorithm>
#include <cstddef>

class Node {
public:
    int data;
    Node *left;
    Node *right;
    Node(int d) {
        data = d;
        left = NULL;
        right = NULL;
    }
};

class Solution {
public:
    Node* insert(Node* root, int data) {
        if(root == NULL) {
            return new Node(data);
        } else {
            Node* cur;
            if(data <= root->data) {
                cur = insert(root->left, data);
                root->left = cur;
            } else {
                cur = insert(root->right, data);
                root->right = cur;
            }
            return root;
        }
    }

    int getHeight(Node* root) {
        if (root == NULL) {
            return -1;
        } else {
            return 1 + std::max(getHeight(root->left), getHeight(root->right));
        }
    }
};

int main() {
    Solution myTree;
    Node* root = NULL;
    int n;
    std::cin >> n;
    int data;

    if (n > 0) {
        for(int i = 0; i < n; i++) {
            std::cin >> data;
            root = myTree.insert(root, data);
        }
    }
    
    int height = myTree.getHeight(root);
    std::cout << height;
    
    return 0;
}
