# 만약 한자리 수 일때는 n = n + (n * 10)

# 정수형 값을 문자열 배열로, 문자열 배열을 정수형 배열로
# a = int(input())
# b = list(str(a))
# print(b)
# print(list(map(int,b)))


# a = int(input())
# b = a
# v = 0
# while (True):
#     v += 1
#     if (b < 10): # b가 10이하일 때
#         b = b + (b * 10)
#     c = list(map(int,list(str(b)))) # c는 b의 숫자배열
#     for i in range(len(c)):
#         b += c[i] # b에 값c의 각각의 수를 더한다
#         if i == (len(c) - 1): # 가장 오른쪽의 수와 붙인다

#             b += ((len(c) * 10) * c[i])
#     # 다시 처음 수로 돌아왔는지 검사
#     if a == b:
#         break
# print(v)






# a = int(input()) 
# b = a
# v = 0
# while(1):
#     v += 1
#     if (b < 10):
#         b = b + (b * 10)

#     c = list(map(int,list(str(b))))
#     b = 0
#     for i in range(len(c)):
#         b += c[i]
#         if (i == (len(c) - 1)):
#             # b를 b의 마지막 값으로 만든다
#             b = list(map(int,list(str(b))))
#             b = b[len(b) - 1]
#             print(b)
#             # c의 마지막 값과 b의 마지막 값을 붙인다
#             b += (10 * c[i])
#     if (a == b):
#         break
#     break
# print(v)


# a = int(input())
# b = a
# v = 0

# while(1):
#     v += 1
#     if (b < 10):
#         b = b + (b * 10)
#     else:
#         c = list(map(int,list(str(b))))
#         b = 0
#         for i in range(len(c)):
#             b += c[i]
#             if (i == len(c) - 1):
#                 b = list(map(int,list(str(b))))
#                 b = (c[i] * 10) + b[len(b) - 1]
#     if b == a:
#         break
# print(v)            

# b 가 10 이하일 때의 처리를 생각하지 못하고 else문을 추가하지 않아서 두 번 작업된게 문제였다