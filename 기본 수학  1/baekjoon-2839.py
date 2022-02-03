# 5를 한 번 쓰는 방법, 2번쓰는 방법 등등을 하나하나 다 해본
# 경우들의 값을 배열에 저장, 마지막에 비교 후 출력

results = []
sugar = int(input())
for i in range((sugar // 5)+1):
    for j in range((sugar // 3)+1):
        copySugar = sugar
        copySugar -= ((i * 5) + (j * 3))
        if copySugar == 0:
            results.append(i + j)
if results == []:
    print(-1)
else:
    print(min(results))

# 시행착오
# 그냥 비교해서 풀었을 때랑 한 숫자로만 나눠서 나온 수를 비교해서
# 작은 수를 출력
# allSugar = int(input())
# pack3 = allSugar
# pack5 = allSugar
# packMix = allSugar
# if allSugar % 5 == 0:
#     pack5 = allSugar // 5
# elif allSugar % 3 == 0:
#     pack3 = allSugar // 3
#
# while 1: # 그냥 한 번 돌리기
#     if (allSugar - 5) > 6:
#         allSugar -= 5
#         packMix += 1
#     elif (allSugar - 3) >= 0:
#         allSugar -= 3
#         packMix += 1
#     if allSugar <= 0:
#         break
# if allSugar < 0:
#     print(-1)
# else:
#     print(min([pack3,pack5,packMix]))
#
#
#
# # five와 three가 서로 반비례하는 것이 아닌
# # five가 하나인 경우 ~~ 해서 해야한다
# results = []
# sugar = int(input())
# three = (sugar // 3)
# five = 0
# while 1:
#     if three < 0 or five < 0:
#         break
#     copySugar = sugar
#     copySugar -= (3 * three)
#     copySugar -= (5 * five)
#     if copySugar == 0:
#         print("들어옴")
#         results.append(three + five)
#     five += 1
#     three -= 1
# print(results)

# # 백준아이디 cieske 님 코드
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    # 극한으로 적은 설탕가방이 나오는 상황은 5의 배수, 5로만 나누어지는 수 일 것이다
# 5만 나오는 상황의 무게 5 짜리 가방의 개수에서 부터
# 5짜리 가방의 개수를 하나씩 줄이며 3으로 나누어 떨어지는 수가 있는지
# while문으로 확인, 있다면 무게 3짜리 가방이 c 에 저장되고 while문이 끝난다
    if b%3 == 0:
        c = b//3
        
        break
    a -= 1
    b += 5
        
# while문이 끝나면 break로 끝났을 때, 즉 무게 5짜리 가방을 제외한 무게가 3의 배수일 때 와 a가 음수가 되었을 때, 즉 답이 안 나오고 끝났을 때를 분류
if b%3 == 0:
    print(a+c)
else:
    print(-1)


