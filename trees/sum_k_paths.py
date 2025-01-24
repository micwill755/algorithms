'''
Count all K Sum Paths in Binary Tree
Given a binary tree and an integer k, the task is to count the number of paths in the tree such that the sum of the nodes in each path equals k. A path can start from any node and end at any node and must be downward only.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def countNodePath(root, k, sum, paths, s):
    if root is None:
        return
    
    sum += root.val

    if sum == k or sum in s:
        paths[0] += 1

    countNodePath(root.left, k, sum, paths, s)
    countNodePath(root.right, k, sum, paths, s)

def countAllPaths (root, k, paths, s):
    if root is None:
        return

    countNodePath (root, k, 0, paths, s)
    countAllPaths(root.left, k, paths, s)
    countAllPaths(root.right, k, paths, s)

def countAllPathsUsingPrefix(map, root, k, paths, sum):
    if root:
        sum += root.val
        if sum == k or sum - k in map:
            paths[0] += 1
        map[sum] = map.get(sum, 0) + 1
        countAllPathsUsingPrefix(map, root.left, k, paths, sum)
        countAllPathsUsingPrefix(map, root.right, k, paths, sum)
        map[sum] -= 1

root = Node(8)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(2)
root.left.right.right = Node(1)
root.right.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)

k = 7 
pathCount = [0] 
s = set()
#countAllPaths(root, k, pathCount, s)
countAllPathsUsingPrefix({}, root, k, pathCount, 0)

print(pathCount[0])