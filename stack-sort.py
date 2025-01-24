
'''

How to Sort a Stack using Recursion
Last Updated : 13 Mar, 2023
Given a stack, the task is to sort it using recursion.

Example: 

Input: elements present in stack from top to bottom -3 14 18 -5 30
Output: 30 18 14 -3 -5
Explanation: The given stack is sorted know 30 > 18 > 14 > -3 > -5

Input: elements present in stack from top to bottom 1 2 3
Output: 3 2 1
Explanation: The given stack is sorted know 3 > 2 > 1

'''

# first solution
def stack (stk, numbers):
    if len(stk) == 0:
        for n in numbers:
            stk.append(n)
        print (stk)
        return
    else:
        last = stk[0]
        if len(numbers) == 0:
            numbers.append(last)
        # if negative number check to last element
        if last < 0:
            if last < numbers[len(numbers) - 1]:
                numbers.append(last)
        # if positive number check to first element
        elif last > 0:
            if last > numbers[0]:
                numbers.insert(0, last)
        stack(stk[1:], numbers)

#stack([-3, 14, 18, -5, 30], [])

# Python program to sort a stack using recursion
 
# Recursive method to insert element in sorted way
 
def sortedInsert(s, element):
 
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
 
        # Remove the top item and recur
        temp = s.pop()
        sortedInsert(s, element)
 
        # Put back the top item removed earlier
        s.append(temp)
 
# Method to sort stack
 
 
def sortStack(s):
 
    # If stack is not empty
    if len(s) != 0:
 
        # Remove the top item
        temp = s.pop()
 
        # Sort remaining stack
        sortStack(s)
 
        # Push the top item back in sorted stack
        sortedInsert(s, temp)
 
# Printing contents of stack
 
 
def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
 
    print("Stack elements before sorting: ")
    printStack(s)
 
    sortStack(s)
 
    print("\nStack elements after sorting: ")
    printStack(s)