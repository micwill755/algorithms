# Recursive Python program for level
# order traversal of Binary Tree

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def diff_sums(root):
    sum_even = 0
    sum_odd = 0
    queue = [(root, 1)]

    while (len(queue) > 0):
        last = queue.pop()
        if last[1] % 2 == 0:
            sum_even += last[0].val
        else:
            sum_odd += last[0].val

        if last[0].left:
            queue.append((last[0].left, last[1] + 1))

        if last[0].right:
            queue.append((last[0].right, last[1] + 1))

    return sum_even - sum_odd
 
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(9)

    print(diff_sums(root))