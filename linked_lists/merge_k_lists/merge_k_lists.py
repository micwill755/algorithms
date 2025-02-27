
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

# 
def reverse_k_lists(lists):
    curr = lists
    l_len = len(curr)
    head = None
    currOutput = None
    currQIndex = -1
    queue = []
    start = False

    while queue or not start:
        start = True
        min = 100000000
        for i in range(l_len):
            if curr[i] is not None:
                queue.append(curr[i])
                curr[i] = curr[i].next        
        
        for i in range(len(queue)):
            if queue[i].data < min:
                min = queue[i].data
                currQIndex = i

        if head is None:
            head = Node(min)
            currOutput = head
        else:
            head.next = Node(min)
            head = head.next
        
        if currQIndex < len(queue):
            queue.remove(queue[currQIndex])
            
    return currOutput

if __name__ == "__main__":
    listOne = Node(1)
    listOne.next = Node(4)
    listOne.next.next = Node(5) 
    listTwo = Node(1)
    listTwo.next = Node(3)
    listTwo.next.next = Node(4)
    listThree = Node(2)
    listThree.next = Node(6)

    lists = [listOne, listTwo, listThree]
    res = reverse_k_lists(lists)

    while res:
        print(res.data)
        res = res.next
