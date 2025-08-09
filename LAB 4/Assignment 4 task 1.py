N,M=map(int,input().split())
matrix=[[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    u,v,w=map(int,input().split())

    matrix[u-1][v-1]=w
for i in matrix:
    for j in i:
        print(j,end=" ")
    print("")