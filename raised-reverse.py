
'''

Find the value of a number raised to its reverse
Last Updated : 09 May, 2023
Given a number N and its reverse R. The task is to find the number obtained when the number is raised to the power of its own reverse. The answer can be very large, return the result modulo 109+7.

Examples:
 Input : N = 2, R = 2
Output: 4
Explanation: Number 2 raised to the power of its reverse 2 gives 4 which gives 4 as a result after performing modulo 109+7

Input : N = 57, R = 75
Output: 262042770
Explanation: 5775 modulo 109+7 gives us the result as 262042770

'''

def power (n, r):
    if n == 0:
        return 0
    elif r == 0:
        return 1
    elif r == 1:
        return n
    
    '''(pow(10, 9) + 7)'''
    return n * power(n, r - 1) % 1000000007 
    
print(power(4, 4))