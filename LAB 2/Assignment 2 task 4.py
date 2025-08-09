N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(map(int, input().split()))
new=[]
i=0
j=0
while i<N and j<M:
    if a[i]<=b[j]:
        new.append(a[i])
        i+=1
    else:
        new.append(b[j])
        j+=1
while i<N:
    new.append(a[i])
    i+=1
while j<M:
    new.append(b[j])
    j+=1
for i in new:
    print(i,end=" ")
