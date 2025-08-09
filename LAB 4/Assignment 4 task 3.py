n=int(input())
matrix=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tem=list(map(int,input().split()))
    for j in range(1,len(tem)):
        matrix[i][tem[j]]=1
for i in matrix:
    for j in i:
        print(j,end=" ")
    print("")