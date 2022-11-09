def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R= arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i < len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j < len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print ("Sorted array is")
for i in range(len(arr)):
    print (arr[i])
