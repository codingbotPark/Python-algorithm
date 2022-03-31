# 가장 먼 거리를 가는 것은 아래와 같은 형태
# 1 = 1
# 1 1 = 1증가 = 2
# 1 2 1 = 2증가 = 4
# 1 2 2 1 = 2증가 = 6
# 1 2 3 2 1 = 3증가 = 9
# 1 2 3 3 2 1 = 3증가 = 12
# 1 2 3 4 3 2 1 = 4증가 = 16
# 1 2 3 4 4 3 2 1 = 4증가 = 20

caseNum = int(input())
for i in range(caseNum):
    start,end = map(int,input().split())
    length = end - start
    if length < 4:
        print(length)
    else:
        plus = 2
        comNum = 4
        value = 3
        changePlusNum = False
        while 1:
            if length <= comNum:
                print(value)
                break
            else:
                if changePlusNum:
                    changePlusNum = False
                    plus+=1
                    comNum += plus
                else:
                    changePlusNum = True
                    comNum += plus
            value+=1

# 시행착오
# 주어진 수를 2(1+1), 4(2+2), 6(3+3) 2의 배수로 마이너스 하여 값의 범위를 나누어 계산
# caseNum = int(input())
# for i in range(caseNum):
#     start, end = map(int,input().split())
#     length = end - start
#     minus = 1
#     moveNum = 1
#     while 1:
#         length -= minus
#         if length <= 0: 
#             break
#         if moveNum == 1:
#             minus += 1
#         else:
#             minus += 2
#         moveNum += 1
#     print(moveNum)
#
#
# changePlusNum을 다시 False화 시켜주지 않았었다
# caseNum = int(input())
# for i in range(caseNum):
#     start,end = map(int,input().split())
#     length = end - start
#     if length < 4:
#         print(length)
#     else:
#         plus = 2
#         comNum = 4
#         value = 3
#         changePlusNum = False
#         while 1:
#             if length <= comNum:
#                 print(value)
#                 break
#             else:
#                 if changePlusNum:
#                     plus+=1
#                     comNum += plus
#                 else:
#                     changePlusNum = True
#                     comNum += plus
#             value+=1

# https://github.com/jongpark1234 코드
# 나의 코드와 같은 역할인데
# 4이하의 수를 예외처리 하지 않았고
# 1증가,유지,1증가,유지 하는 증가하는 수를 짝수일때와 아닐 때를 구분하여 함
for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    count = 0; length = 1; totalength = 0
    while totalength < distance:
        count += 1
        totalength += length
        if count % 2 == 0:
            length += 1
    print(count)