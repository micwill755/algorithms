
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

'''def mean (arr, sum, count):
    if len (arr) == 0:
        return sum / count
    sum += arr[0]
    return mean(arr[1:], sum, count + 1)'''

def mean(arr, n):
    if n == 1:
        return arr[0]
    else:
        return ((mean (arr, n - 1) * (n - 1)) + arr[n - 1]) / n
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(len(arr))
    print(mean (arr, len(arr)))