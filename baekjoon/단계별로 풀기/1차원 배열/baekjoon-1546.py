a = int(input())
b = list(map(int,input().split()))
maxScore = max(b)
sumScore = 0
for i in range(a):
    b[i] = (b[i] / maxScore) * 100
    sumScore += b[i]
print(sumScore / a)