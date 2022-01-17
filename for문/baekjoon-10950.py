a = int(input())
A = []
for i in range(a):
    b,c = map(int,input().split())
    A.append(b+c)
for i in range(a):
    print(A[i])