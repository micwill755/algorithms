'''
Find the maximum path sum between two leaves of a binary tree
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another. 

The maximum sum path may or may not go through the root. For example, in the following binary tree, the maximum sum is 27(3 + 6 + 9 + 0 – 1 + 10). Expected time complexity is O(n). If one side of the root is empty, then the function should return minus infinite (INT_MIN in case of C/C++)

'''

INT_MIN = -2**32

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def calcMax(root, res):
    if root is None:
        return 0
    
    # if root is leaf node we can return root.data
    if not root.left and not root.right:
        return root.data
    
    ls = calcMax(root.left, res)
    rs = calcMax(root.right, res)

    # if our root contains left and right nodes
    if root.left and root.right:
        res[0] = max(res[0], ls + rs + root.data)
        return max(ls, rs) + root.data

    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data

def calcMaxRoot(root):
    res= [INT_MIN]
    if root is None:
        return 0
    if root.left and root.right:
        calcMax(root, res)
    return res[0]

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)

    print(calcMaxRoot(root))
    '''
    or simply
    
    res= [INT_MIN]
    calcMax(root, res)
    print(res[0])

    '''