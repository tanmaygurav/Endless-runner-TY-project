def  part(arr,lo,hi):
    i=(lo-1)
    pivot=arr[hi]
    for j in range(lo,hi):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return(i+1)
def qkst(arr,lo,hi):
    if lo<hi:
        pi=part(arr,lo,hi)
        qkst(arr,lo,pi-1)
        qkst(arr,pi+1,hi)

#arr=["adf","btyu","myu","aaa","bbb"]
arr=[1,5,81,1,51,77,61,4,5]
n=len(arr)
qkst(arr,0,n-1)
print("sorted array is:")
for i in range(n):
    print(arr[i])
