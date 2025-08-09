T=int(input())
arr=[]
for i in range(T):
    k,x=map(int,input().split())
    res=(k+(k-1)//(x-1))
    arr.append(res)
for i in arr:
    print(i)