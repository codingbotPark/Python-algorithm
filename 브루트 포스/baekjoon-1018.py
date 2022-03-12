# 8 X 8 크기의 체스판을 잘라서 사용
# 그냥 각 칸을 기준으로 8 X 8 을 전체 돌려서 값들을 저장한다

def firstB(y): # 몇번 째 배열인지 전달받음
    counter = 0
    for i in range(8):
        if i % 2 == 0 and copyArray[y][i] == 'W':
            counter += 1
        elif i % 2 == 1 and copyArray[y][i] == 'B':
            counter += 1
    return counter
# 첫 번째가 W라고 생각하는 함수
def firstW(y):
    counter = 0
    for i in range(8):
        if i % 2 == 0 and copyArray[y][i] == 'B':
            counter += 1
        elif i % 2 == 1 and copyArray[y][i] == 'W':
            counter += 1
    return counter

y,x = map(int,input().split())
array = []
for i in range(y):
    array.append(input())

results = []

for i in range(y - 7):
    for j in range(x - 7):
        copyArray = [[0]*8 for i in range(8)]
        # 임의의 8 X 8 체스판을 만든다
        for c in range(8):
            for k in range(8):
                
                copyArray[c][k] = array[c+i][k+j]

        # 배열의 0,0이 W이냐 / B이냐에 따른 
        # 두 가지 경우를 저장
        result = [0]*2

        # 0,0이 W이라 생각할 때
        for m in range(4):
            result[0] += (firstB(m*2)) 
            result[0] += (firstW((m*2)+1))
        for m in range(4):
            result[1] += (firstW(m*2))
            result[1] += (firstB((m*2)+1))

        results.append(min(result))

print(min(results),end="")          



# # 시행착오 ▼
# # 문제 이해를 잘못함
# # 첫 번째가 B라고 생각하는 함수
# def firstB(y): # 몇번 째 배열인지 전달받음
#     counter = 0
#     for i in range(x):
#         if i % 2 == 0 and array[y][i] == 'W':
#             counter += 1
#         elif i % 2 == 1 and array[y][i] == 'B':
#             counter += 1
#     return counter
# # 첫 번째가 W라고 생각하는 함수
# def firstW(y):
#     counter = 0
#     for i in range(x):
#         if i % 2 == 0 and array[y][i] == 'B':
#             counter += 1
#         elif i % 2 == 1 and array[y][i] == 'W':
#             counter += 1
#     return counter

# y,x = map(int,input().split())
# array = []
# for i in range(y):
#     array.append(input())

# firstTemp = 0
# secondTemp = 0

# # [0][0]번째를 B라고 생각했을 때
# for i in range(y):
#     if i % 2 == 0:
#         firstTemp += firstB(i)
#     else:
#         firstTemp += firstW(i)
# for i in range(y):
#     if i % 2 == 0:
#         secondTemp += firstW(i)
#     else:
#         secondTemp += firstB(i)

# print(firstTemp)
# print(secondTemp)

# if firstTemp > secondTemp: print(secondTemp)
# else: print(firstTemp)


# https://github.com/jongpark1234 코드
# 8 X 8 짜리 체스판을 미리 만들어 놓고 다른 것의 개수를 구함
import sys
board1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
board2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
n, m = map(int, sys.stdin.readline().split())
field = [[] for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().strip()
    for j in range(m):
        field[i].append(line[j])
result = 64
for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0
        count2 = 0
        for r in range(8):
            for c in range(8):
                if field[i + r][j + c] != board1[r][c]:
                    count1 += 1
                if field[i + r][j + c] != board2[r][c]: 
                    count2 += 1
        result = min(result, count1, count2)
print(result)
