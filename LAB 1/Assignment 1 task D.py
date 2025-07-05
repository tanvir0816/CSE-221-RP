T=int(input())
y=[]
for i in range(T):
    N=int(input())
    a=input().split()
    x=0

    while x<N-1:
        if int(a[x])<=int(a[x+1]):    
            x+=1
        else:
            break
    
    if x==N-1:
        y.append("YES")
    else:
        y.append("NO")
for i in y:
    print(i)