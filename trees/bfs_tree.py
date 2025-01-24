# Recursive Python program for level
# order traversal of Binary Tree

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def calcHeight(root):
    if root is None:
        return -1
    lHeight = calcHeight(root.left)
    rHeight = calcHeight(root.right)
    return max(lHeight, rHeight) + 1

def printLevelOrder(root):
    h = calcHeight(root)
    for level in range(0, h+1):
        printLevel(root, level)

def printLevel(root, level):
    if root is None:
        return
    elif level == 0:
        print(root.data)
    else:
        printLevel(root.left, level - 1)
        printLevel(root.right, level - 1)

def printLevelOrderUsingQueue(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while (len(queue) > 0):
        print(queue[0].data, end=' ')
        first = queue.pop(0)
        if first.left is not None:
            queue.append(first.left)
        if first.right is not None:
            queue.append(first.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #printLevelOrder(root)
    printLevelOrderUsingQueue(root)