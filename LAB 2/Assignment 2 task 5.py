N,K=map(int,input().split())
arr=list(map(int,input().split()))
maxlen=0
cur=0
i=0
j=0
while j < len(arr):
    cur += arr[j]
    while cur > K and i <= j:
        cur -= arr[i]
        i += 1   
    maxlen = max(maxlen, j - i + 1)
    j += 1
print(maxlen)