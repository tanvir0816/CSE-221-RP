n,q=map(int,input().split())
z=list(map(int,input().split()))
oup=[]
for i in range(q):
    x,y=map(int,input().split())
    left = 0
    right = len(z)
    while left < right:
        mid = (left + right) // 2
        if z[mid] >= x:
            right = mid
        else:
            left = mid + 1
    lower = left  
    left = 0
    right = len(z)
    while left < right:
        mid = (left + right) // 2
        if z[mid] > y:
            right = mid
        else:
            left = mid + 1
    upper = left 
    oup.append(left-right)
for i in oup:
    print(i)