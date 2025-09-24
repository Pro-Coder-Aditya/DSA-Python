def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        isSwap = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                isSwap = True
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]

        if isSwap == False:
            return arr
        
    return arr
 
arr = [3, 1, 4, 6, 2, 10, 5]
newarr = BubbleSort(arr)
print(newarr)