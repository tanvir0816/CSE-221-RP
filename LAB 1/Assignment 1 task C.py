N=int(input())
y=[]
for i in range(N):
    k=int(input())
    sum = (k*(k+1))/2   
    y.append(int(sum))
for i in y:
    print(i)