def sumsearch(a,n):
    i=0
    j=len(a)-1
    while i<j:
        if a[i][0]+a[j][0]==n:
            return (a[i][1], a[j][1])
        elif (a[i][0]+a[j][0])<n:
            i+=1
        elif a[i][0]+a[j][0]>n:
            j-=1
    if i>=j:
        return -1
n,x=map(int, input().split())
a=list(map(int, input().split()))
tem = [(val, idx + 1) for idx, val in enumerate(a)] 
tem.sort()
flag=False
for i in range(n):
    val,firidx=tem[i]
    target=x-val
    arr2=tem[:i]+tem[i+1:]
    res=sumsearch(arr2,target)
    if res!=-1:
        secidx,thiridx=res
        print(f"{firidx} {secidx} {thiridx}")
        flag=True
        break
if not flag:
    print(-1)