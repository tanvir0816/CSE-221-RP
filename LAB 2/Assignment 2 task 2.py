N,M,K=map(int,(input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))
L=0
R=M-1
diff= float('inf')
idx=[0,0]
while L<N and R>=0:
    summ= a[L]+b[R]
    x=abs(K-summ)
    if x<diff:
        diff=x
        idx[0],idx[1]=L+1,R+1
    if summ<K:
        L+=1
    elif summ>=K:
        R-=1
    
print (f"{idx[0]} {idx[1]}")