
'''

To find the mean of the elements of the array. 

Mean = (Sum of elements of the Array) /
       (Total no of elements in Array)
Examples: 

Input : 1 2 3 4 5
Output : 3

Input : 1 2 3
Output : 2

'''

def sum(n):
    if n <= 1:
        return n
    return n + sum(n - 1)
    
if __name__ == '__main__':
    print(sum(3))