
'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1

Input: head = [1,2,3,4,5], k = 2

1-2  3-4  5
2-1  4-3  5

Output: [2,1,4,3,5]


Input: head = [1,2,3,4,5], k = 3

1-2-3 4-5
3-2-1

Output: [3,2,1,4,5]

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse K groups
def reverseKGroup(head, k):
    if head is None:
        return head

    curr = head
    newHead = None
    tail = None

    while curr is not None:
        groupHead = curr
        prev = None
        nextNode = None
        count = 0

        # Reverse the nodes in the current group
        while curr is not None and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count += 1

        # If newHead is null, set it to the
        # last node of the first group
        if newHead is None:
            newHead = prev

        # Connect the previous group to the
        # current reversed group
        if tail is not None:
            tail.next = prev

        # Move tail to the end of 
        # the reversed group
        tail = groupHead

    return newHead

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Creating a sample singly linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseKGroup(head, 2)
    printList(head)
        
        

'''
    Time complexity O(n)
'''

'''def reverse_group(input, k):
    groups = len(input) // k
    output = []

    for i in range(groups):
        group = input[i * k: (i + 1) * k]
        output += group[::-1]
        print(output)

    if len(input) % k != 0:
        output += input[groups * k:]
    return output

if __name__ == '__main__':
    res = reverse_group([1, 2, 3, 4, 5], 2)
    print(res)'''