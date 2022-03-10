# 첫 번째가 B라고 생각하는 함수
def firstB(y): # 몇번 째 배열인지 전달받음
    counter = 0
    for i in range(x):
        if i % 2 == 0 and array[y][i] == 'W':
            counter += 1
        elif array[y][i] == 'B':
            counter += 1
    return counter
# 첫 번째가 W라고 생각하는 함수
def firstW(y):
    counter = 0
    for i in range(x):
        if i % 2 == 0 and array[y][i] == 'B':
            counter += 1
        elif array[y][i] == 'W':
            counter += 1
    return counter

y,x = map(int,input().split())
array = []
for i in range(y):
    array.append(input())

firstTemp = 0
secondTemp = 0

# [0][0]번째를 B라고 생각했을 때
for i in range(y):
    if i % 2 == 0:
        firstTemp += firstB(i)
    else:
        firstTemp += firstW(i)
for i in range(y):
    if i % 2 == 0:
        secondTemp += firstW(i)
    else:
        secondTemp += firstB(i)

if firstTemp > secondTemp: print(secondTemp)
else: print(firstTemp)