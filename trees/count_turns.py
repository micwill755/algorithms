'''

Number of turns to reach from one node to other in binary tree
Given a binary tree and two nodes. The task is to count the number of turns needed to reach from one node to another node of the Binary tree.

Examples: 

Input:   Below Binary Tree and two nodes
        5 & 6 
                   1
                /     \
               2        3
             /   \    /   \
            4     5   6     7
           /         / \
          8         9   10
Output: Number of Turns needed to reach 
from 5 to 6:  3
        
Input: For above tree if two nodes are 1 & 4
Output: Straight line : 0 turn 

'''

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def count_turns(root, node1, node2):
    path1 = get_path_from_root(root, node1, '', [False])
    path2 = get_path_from_root(root, node2, '', [False])

    # if we have no result from either node return
    if len(path1) == 0 and len(path2) == 0: 
        return -1
    
    # we reverse the first string because we are traveling back to the root from the first node
    path1 = path1[::-1] + path2
    turns = 0
    
    # count how many direction changes occur between adjacent nodes
    for i in range(len(path1) - 1): 
        if path1[i] != path1[i + 1]:
            turns += 1

    return turns

def get_path_from_root(root, val, path, found_path):
    if root is None:
        return
    
    if root.val == val:
        found_path[0] = path
        return found_path[0]

    get_path_from_root(root.left, val, path + 'l', found_path)
    get_path_from_root(root.right, val, path + 'r', found_path)

    return found_path[0]

if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.left.left.left = Node(8) 
    root.right.left.left = Node(9) 
    root.right.left.right = Node(10) 

    print(count_turns(root, 8, 7))

    #print(find_lca(root, 4, 5))