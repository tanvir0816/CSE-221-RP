N=int(input())
arr = list(map(int, input().split()))
for j in range(N):
    for i in range(N-1):
        if (arr[i]>arr[i+1]):
            if arr[i]%2==0 and arr[i+1]%2==0:
                arr[i],arr[i+1]=arr[i+1],arr[i]
            elif arr[i]%2==1 and arr[i+1]%2==1:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            pass
for i in arr:
    print(i,end=" ")