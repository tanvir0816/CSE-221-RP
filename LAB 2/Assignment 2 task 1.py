n=list(map(int, input().split()))
a=list(map(int, input().split()))
i=0
j=n[0]-1
while i<j:
    if a[i]+a[j]==n[1]:
        print(i+1,j+1)
        break
    elif (a[i]+a[j])<n[1]:
        i+=1
    elif a[i]+a[j]>n[1]:
        j-=1
if i>=j:
    print(-1)