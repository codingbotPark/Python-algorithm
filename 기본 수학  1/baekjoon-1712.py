a,b,c = map(int,input().split())
one = c - b
if one <= 0:
    print(-1)
else:
    print((a // one) + 1)

# 시행착오
# 그냥 반복
# a,b,c = map(int,input().split())
# v = 1
# if b > c:
#     print(-1)
# else:
#     while(1):
#         if a + (v * b) < v * c:
#             print(v)
#             break
#         v += 1