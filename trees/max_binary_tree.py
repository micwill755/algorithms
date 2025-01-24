# Python3 program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
def construct_max_binary_tree(nums):
    if not nums:
        return None

    max_index = nums.index(max(nums))  # Find index of maximum value
    root = Node(nums[max_index])  # Create root node
    root.left = construct_max_binary_tree(nums[:max_index]) # Build left subtree
    root.right = construct_max_binary_tree(nums[max_index+1:]) # Build right subtree

    return root

def construct_output_dfs(node, output):
    # Base Case
    if node is None:
        #output.append(None)
        return None
    else:
        output.append(node.val)
        construct_output_dfs(node.left, output)
        construct_output_dfs(node.right, output)
        
def construct_output_bfs(node, output):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        if current_node:
            output.append(current_node.val)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            output.append(None)

head = construct_max_binary_tree([3,2,1,6,0,5])
output = []
construct_output_bfs(head, output)
print(output)
