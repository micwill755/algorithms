'''
Print Root-to-Leaf Paths in a Binary Tree Using Recursion
Last Updated : 07 Oct, 2024
Given a Binary Tree of nodes, the task is to find all the possible paths from the root node to all the leaf nodes of the binary tree.
'''

INT_MIN = -2**32

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def collectPaths(root, path, paths):
    if root:
        path.append(root.data)
        # if leaf
        if root.left is None and root.right is None:
            paths.append(path.copy())
        else:
            collectPaths(root.left, path, paths)
            collectPaths(root.right, path, paths)
        path.pop()
        return paths

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    
    print(collectPaths(root, [], []))