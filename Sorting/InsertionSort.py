def InsertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1
        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous -= 1
        arr[previous + 1] = current
    
    return arr

arr = [2, 4, 1, 10, 12, 3]
print(InsertionSort(arr))