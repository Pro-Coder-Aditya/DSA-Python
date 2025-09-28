def part(arr,s,e):
    pivot = arr[e]
    i = s-1
    for j in range(s,e):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    i+=1  
    arr[i], arr[e] = arr[e], arr[i]
    return i     


def quickSort(arr,s,e):
    if(s<e):
        pId = part(arr,s,e)
        quickSort(arr,s,pId-1) #LHS
        quickSort(arr,pId+1,e) #RHS
    
arr = [5,2,1,4,6,3]
quickSort(arr,0,len(arr)-1)
print(arr)