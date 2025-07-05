N=int(input())
y=[]
for i in range(N):
    k=input()
    T=k.split()
    if T[2]=="+":
        a=round((int(T[1])+int(T[3])),6)
    elif T[2]=="-":
        a=round((int(T[1])-int(T[3])),6)
    elif T[2]=="*":
        a=round((int(T[1])*int(T[3])),6)
    else:
        a=round((int(T[1])/int(T[3])),6)
    y.append(a)
for i in y:
    print(i)