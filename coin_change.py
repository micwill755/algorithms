
'''

Given an integer array of coins[ ] of size N representing different types of denominations and an integer sum, the task is to count all combinations of coins to make a given value sum.  

Note: Assume that you have an infinite supply of each type of coin. 

Examples: 

Input: sum = 4, coins[] = {1,2,3}
Output: 4
Explanation: there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2} and {1, 3}

Input: sum = 10, coins[] = {2, 5, 3, 6}
Output: 5
Explanation: There are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}

Input: sum = 10, coins[] = {10}
Output: 1
Explanation: The only is to pick 1 coin of value 10.

Input: sum = 5, coins[] = {4}
Output: 0
Explanation: We cannot make sum 5 with the given coins

'''

def count_sum(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return count_sum(n - m, m) + count_sum(n, m - 1)
    
if __name__ == '__main__':
    print(count_sum(5, {1, 2, 3}))