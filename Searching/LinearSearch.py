def LinearSearch(arr, target):
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1
    
arr = [3, 5, 7, 20, 12, 6, 4]
target = 5
result = LinearSearch(arr, target)

if (result != -1):
    print("Element found at index", result)
else:
    print("Element not found")