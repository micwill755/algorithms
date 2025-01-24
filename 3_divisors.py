# Python3 program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
# using loops
'''def count_divisors(N):
    arr = []
    for i in range(1, N + 1):
        if N % i == 0:
            arr.append(i)
    return arr'''

# using recursion to replace loops
'''def count_divisors(arr, i, n):
    if i == n:
        return arr
    else:
        if n % i == 0:
            arr.append(i)
        return count_divisors(arr, i + 1, n)'''

# using n-1 approach
def count_divisors(n, m):
    if m == 0:
        return 0
    else:
        return (n % m == 0) + count_divisors(n, m - 1)

print(count_divisors(6, 6))