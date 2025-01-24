'''
Subarray with 0 sum
Given an array of positive and negative numbers, the task is to find if there is a subarray (of size at least one) with 0 sum.

Examples: 

Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true
Explanation: The third element is zero. A single element is also a sub-array.

Input: {-3, 2, 3, 1, 6}
Output: false 
'''

def sub_array_with_sum_0(arr):
    for i in range (len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == 0:
                return True
    return False


def sub_array_with_sum_0_using_prefix(arr):
    prefix = set()
    n_sum = 0
    for i in range (len(arr)):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in prefix:
            return True
        prefix.add(n_sum)
    return False
            
print(sub_array_with_sum_0_using_prefix([4, 2, -3, 1, 6]))
print(sub_array_with_sum_0_using_prefix([4, 2, 0, 1, 6]))
print(sub_array_with_sum_0_using_prefix([-3, 2, 3, 1, 6]))