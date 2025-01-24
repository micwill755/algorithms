
'''

Longest Increasing Subsequence (LIS)
Last Updated : 22 Aug, 2024
Given an array arr[] of size N, the task is to find the length of the Longest Increasing Subsequence (LIS) i.e., the longest possible subsequence in which the elements of the subsequence are sorted in increasing order.

Examples:            

Input: arr[] = {3, 10, 2, 1, 20}
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = {50, 3, 10, 7, 40, 80}
Output: 4
Explanation: The longest increasing subsequence is {3, 7, 40, 80}

Input: arr[] = {30, 20, 10}
Output:1
Explanation: The longest increasing subsequences are {30}, {20} and (10)

Input: arr[] = {10, 20, 35, 80}
Output: 4
Explanation: The whole array is sorted

'''
inputs = [
    [3, 10, 2, 1, 20],

]
'''[50, 3, 10, 7, 40, 80],
    [30, 20, 10],
    [10, 20, 35, 80]'''
##### bruteforce

def longest_common_subsequence_bruteforce(arr):
    max = 0 
    length = len(arr)
    
    for i in range(length):
        if i > max:
            break
        
        temp = i
        count = 1
        
        for j in range(i + 1, length):
            if arr[j] > arr[temp]:
                count += 1
                temp = j

        if count > max:
            max = count
    
    return max

##### bruteforce

##### recursion left to right

def left_to_right(arr, i, j, m):
    print (arr)
    if m == 0:
        return 1
    else:
        if arr[j] > arr[i]:
            return 1 + left_to_right(arr, i+1, j+1, m-1)
        return left_to_right(arr, i+1, j+1, m-1)
    
def longest_common_subsequence_recursion_left_to_right(arr, i, n, mx):
    if n == 0:
        return 0
    else:
        mex = max(mx, left_to_right(arr, 0, 1, n-1))
    longest_common_subsequence_recursion_left_to_right(arr[1:], i+1, n-1, 1)
    return mex

##### recursion left to right

def lis_end_at_i(arr, i):
    # Base case
    if i == 0:
        return 1

    # Consider all elements on the left of i,
    # recursively compute LISs ending with 
    # them and consider the largest
    mx = 1
    for prev in range(i):
        if arr[prev] < arr[i]:
            mx = max(mx, lis_end_at_i(arr, prev) + 1)
    return mx

def lis(arr):
    n = len(arr)
    res = 1
    for i in range(1, n):
        res = max(res, lis_end_at_i(arr, i))
    return res

def run_examples():
    count = 1
    for arr in inputs:
        #print ('example {} - LIS {}'.format(count, longest_common_subsequence_bruteforce(arr)))
        #print ('example {} - LIS {}'.format(count, longest_common_subsequence_recursion_left_to_right(arr, 0, len (arr), 1)))
        print ('example {} - LIS {}'.format(count, lis(arr)))
        count += 1

if __name__ == '__main__':
    run_examples()