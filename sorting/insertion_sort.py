
'''



'''

# O(N^2) - but we are not allowed to del elements
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                del arr[i]
                arr.insert(j, temp)
                break
    return arr
 
# O(N^2) - moving elements without deleting from the array 
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Driver Code
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(insertionSort(arr))