# Recursive Python program for level
# order traversal of Binary Tree

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def dfs_findpath(root, val, path, found):
    if root:
        if found[0]:
            return path
        
        path.append(root.val)

        if root.val == val:
            found[0] = True
            return path

        dfs_findpath(root.left, val, path, found)
        dfs_findpath(root.right, val, path, found)

        if not found[0]:
            path.remove(root.val)
    
    return path
   
def find_path(root, val):
    path = dfs_findpath(root, val, [], [False])
    return path

def find_lca(root, node1, node2):
    path_node1 = dfs_findpath(root, node1, [], [False])
    path_node2 = dfs_findpath(root, node2, [], [False])

    for i in range(len(path_node1)):
        if path_node1[i] != path_node2[i]:
            return path_node1[i-1]
        
    return None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(9)

    print(find_lca(root, 4, 5))