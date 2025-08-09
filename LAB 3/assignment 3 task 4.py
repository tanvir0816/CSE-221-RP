modulo = 10**9 + 7
def multiplicate(mat1, mat2):
    a1=(mat1[0][0]*mat2[0][0] + mat1[0][1]*mat2[1][0]) % modulo
    a2=(mat1[0][0]*mat2[0][1] + mat1[0][1]*mat2[1][1]) % modulo
    b1=(mat1[1][0]*mat2[0][0] + mat1[1][1]*mat2[1][0]) % modulo
    b2=(mat1[1][0]*mat2[0][1] + mat1[1][1]*mat2[1][1]) % modulo
    return [[a1,a2],[b1,b2]]
def mat_pow(matrix, power):
    result = [[1, 0], [0, 1]]
    while power>0:
        if power % 2==1:
            result = multiplicate(result, matrix)
        matrix = multiplicate(matrix, matrix)
        power //= 2
    return result
T = int(input())
arr=[]
for _ in range(T):
    a11, a12, a21, a22 = map(int, input().split())
    X = int(input())
    mat1 = [[a11, a12], [a21, a22]]
    result = mat_pow(mat1, X)
    arr.append(result)
for i in arr:
    print(i[0][0], i[0][1])
    print(i[1][0], i[1][1])
