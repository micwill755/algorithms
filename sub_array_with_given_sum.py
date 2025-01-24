'''
Subarray with Given Sum 
Given an unsorted array of integers, find a subarray that adds to a given number. If there is more than one subarray with the sum of the given number, print any of them.

Examples:  

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33


Input: arr[] = {2, 12, -2, -20, 10}, sum = -10
Output: Sum found between indexes 1 to 3
Explanation: Sum of elements between indices 0 and 3 is 12 – 2 – 20 = -10


Input: arr[] = {-10, 0, 2, -2, -20, 10}, sum = 20
Output: No subarray with given sum exists
Explanation: There is no subarray with the given sum

https://www.youtube.com/watch?v=fFVZt-6sgyo
'''

def sub_array_with_sum_k(arr, k):
    for i in range (len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                return True
    return False

def sub_array_with_sum_k_using_prefix(arr, k):
    prefix = {}
    n_sum = 0
    count = 0
    for i in range (len(arr)):
        n_sum += arr[i]
        if n_sum == 0 or (n_sum - k) in prefix:
            count += 1
        prefix[n_sum] = i

    return count
            
print(sub_array_with_sum_k_using_prefix([1, 4, 20, 3, 10, 5], 33))
print(sub_array_with_sum_k_using_prefix([2, 12, -2, -20, 10], 10))
print(sub_array_with_sum_k_using_prefix([-10, 0, 2, -2, -20, 10], 20))