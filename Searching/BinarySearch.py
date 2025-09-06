def BinarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = int((start + end) / 2)
        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            end = mid - 1
        elif (arr[mid] < target):
            start = mid + 1
        
    return -1

arr = [10, 20, 30, 40, 50, 60, 80]
target = 80

print(BinarySearch(arr, target))