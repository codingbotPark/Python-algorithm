# 주어진 수를 2(1+1), 4(2+2), 6(3+3) 2의 배수로 마이너스 하여 값의 범위를 나누어 계산

caseNum = int(input())
for i in range(caseNum):
    start, end = map(int,input().split())
    length = end - start
    minus = 1
    moveNum = 1
    while 1:
        length -= minus
        if length <= 0: 
            break
        if moveNum == 1:
            minus += 1
        else:
            minus += 2
        moveNum += 1
    print(moveNum)