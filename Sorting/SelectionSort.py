def SelectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # swap
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr

arr = [2, 4, 1, 10, 12, 3]
print(SelectionSort(arr))