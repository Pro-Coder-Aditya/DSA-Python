def Merge(arr,start,mid,end):
    temp = []
    a1 = arr[start:mid+1] # 0:2 
    a2 = arr[mid+1:] # 2:n-1
    i = 0
    j = 0
    len1 = len(a1)
    len2 = len(a2)
    while i<len1 and j<len2:
        if a1[i] < a2[j]:
            temp.append(a1[i])
            i+=1
        elif a1[i] == a2[j]:
            temp.append(a1[i])
            temp.append(a2[j])
            i+=1
            j+=1
        elif a1[i] > a2[j]:
            temp.append(a2[j])
            j+=1
    while i<len1:
        temp.append(a1[i])
        i+=1
    while j<len2:
        temp.append(a2[j])
        j+=1
    
    for idx in range(len(temp)):
        arr[start+idx] = temp[idx]
    

def MergeSort(arr,start,end):
    if start < end:
        mid = int((start+end)/2)
        MergeSort(arr,start,mid)
        MergeSort(arr,mid+1,end)
        Merge(arr,start,mid,end)
    

arr = [2,4,1,10,12,3]
MergeSort(arr,0, len(arr)-1)
print(arr)