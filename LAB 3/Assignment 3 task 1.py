def merge(a, b):
    temp=[]
    i,j=0,0
    inv=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            temp.append(a[i])
            i+=1
        else:
            temp.append(b[j])
            j+=1
            inv+=len(a)-i
    while i<len(a):
        temp.append(a[i])
        i+=1
    while j<len(b):
        temp.append(b[j])
        j+=1
    return temp,inv
def mergeSort(arr):
    if len(arr) <= 1:
        return arr,0
    else:
        mid = len(arr)//2
        a1,inv1 = mergeSort(arr[:mid])
        a2,inv2 = mergeSort(arr[mid:]) 
        out,inv3= merge(a1, a2)
        ii=inv1+inv2+inv3
    return out,ii
N=int(input())
arr=list(map(int, input().split()))
sorted, inversion= mergeSort(arr)

print(inversion)
print(" ".join(map(str, sorted)))