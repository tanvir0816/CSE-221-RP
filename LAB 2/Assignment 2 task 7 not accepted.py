n,q=map(int,input().split())
arr=list(map(int,input().split()))
outp=[]
for i in range(q):
    x,y=map(int,input().split())
    l=0
    r=len(arr)-1
    while l<=r and arr[l]<x:
        l+=1
    while l<=r and arr[r]>y:
        r-=1
    outp.append(r-l+1)
for i in outp:
    print(i)