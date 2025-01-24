'''
Given a Binary Tree, find the maximum sum path from a leaf to root.
For example, in the following tree, there are three leaf to root paths 8->-2->10, -4->-2->10 and 7->10. The sums of these three paths are 16, 4 and 17 respectively. The maximum of them is 17 and the path for maximum is 7->10.

                  10
               /      \
             -2        7
           /   \     
          8     -4    
'''

INT_MIN = -2**32

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def calcMax(root, curr, max):
    if root is None:
        return 0
    
    # if root is leaf node we can return root.data
    if root.left is None and root.right is None:
        if (curr + root.data) > max[0]:
            max[0] = curr + root.data
    
    calcMax(root.left, curr + root.data, max)
    calcMax(root.right, curr + root.data, max)

    return max

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
 
    # Constructing tree given in the above figure 
    '''root = Node(10)
    root.left = Node(-2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(-4)'''

    print(calcMax(root, 0, [INT_MIN]))
    '''
    or simply
    
    res= [INT_MIN]
    calcMax(root, res)
    print(res[0])

    '''