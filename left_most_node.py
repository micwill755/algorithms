'''
Left View of a Binary Tree
Given a Binary Tree, the task is to print the left view of the Binary Tree. 
The left view of a Binary Tree is a set of leftmost nodes for every level.
Another way to look at it is to print the first node for every level.
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLeftView(root, level, max_level):
    if root is None:
        return
    
    if max_level < level:
        print(root.data, end=' ')
        max_level = level
        print(max_level)

    printLeftView(root.left, level + 1, max_level)
    printLeftView(root.right, level + 1, max_level)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)

    printLeftView(root, 1, [0])