
def fibo(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

num = int(input())
print(fibo(num))


# 시행착오▼
# 재귀가 없을 때의 피보나치 수열 코드 
# num = int(input())
# if num == 0:
#     print(0)
# else:
#     temp1 = 0
#     temp2 = 1
#     temp3 = 0
#     for i in range(num-1):
#         temp3 = temp1 + temp2
#         temp1 = temp2
#         temp2 = temp3
#     print(temp3)
