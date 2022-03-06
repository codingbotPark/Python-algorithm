




# https://namu.wiki/w/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98%20%ED%83%91
# 사실 이동 회수를 구하지 못해서 검색했다
# 이동 회수는 2n - 1이다
# 1 = 1
# 2 = 3, 처음이 2
# 3 = 7, 처음이 1
# 4 = 15, 처음이 2
# 5 = 31, 처음이 1

# n 짜리 탑을 세우려면, n-1짜리 탑을 세워야 한다
# (n짜리 탑을 3에 세우려면 n-1짜리 탑을 2에 세워야 한다)

# 홀수 탑 = (1 3), 짝수 탑 = (1 2)



# # 시행착오▼
# # 재귀로 풀기
# # 두 수를 입력받고 그에 맞는 배열에서 값을 옮기는 함수
# def change(x,y):
#     print(x,y)
#     if x == 1:
#         tmep = one[-1]
#         one.pop()
#         if y == 2:
#             two.append(tmep)
#         else:
#             three.append(tmep)
#     elif x == 2:
#         temp = two[-1]
#         two.pop()
#         if y == 1:
#             one.append(temp)
#         else:
#             three.append(temp)
#     else:
#         temp = three[-1]
#         three.pop()
#         if y == 1:
#             one.append(temp)
#         else:
#             two.append(temp)

# startPo = True
# def buildTower(n):
#     if n == 1:
#         if startPo:
#             change(1,3)
#             # true일 때 3번자리에 1을 놓음
#         else:
#             change(1,2)
#             # false일 때 2번자리에 1을 놓음 
#     else:
#         startPo = not(startPo)
#         buildTower(n-1)
#         # 탑쌓는 과정이 더 필요함 ...

# one = []
# two = []
# three = []
# num = int(input())
# for i in range(num,0,-1):
#     one.append(i)
# buildTower(num)

