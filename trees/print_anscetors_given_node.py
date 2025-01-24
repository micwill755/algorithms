# Recursive Python program for level
# order traversal of Binary Tree

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def get_anscetors(node, k, ans, found):
    if node is None:
        return

    if found[0]:
        return ans
    
    if node.val == k:
        found[0] = True

    ans.append(node.val)

    get_anscetors(node.left, k, ans, found)
    get_anscetors(node.right, k, ans, found)

    if not found[0]:
        ans.pop()
    
    return ans


def print_anscetors(node, k, ans):
    if node is None:
        return

    if node.val == k:
        return True

    if (print_anscetors(node.left, k, ans) or print_anscetors(node.right, k, ans)):
        #ans.append(node.val)
        ans.insert(0, node.val)
        return ans

    return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)

    print(get_anscetors(root, 7, [], [False]))
    print(print_anscetors(root, 7, []))