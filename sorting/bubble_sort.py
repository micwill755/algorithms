
'''



'''

# O(N^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        # if swapped stay false we are sorted
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return (arr)
 
# Driver Code
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(bubble_sort(arr))