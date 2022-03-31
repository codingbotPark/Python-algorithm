

# 시행착오▼
n = int(input())
turn = len(str(n)) * 9
for i in range(turn):
    tempN = n -turn + i
    if tempN < 1:
        continue
    sumTempN = sum(list(map(int,list(str(tempN)))))
    if tempN + sumTempN == n:
        print(tempN)
        exit()
print(0)