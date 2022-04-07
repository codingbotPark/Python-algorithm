# https://blockdmask.tistory.com/531
# 파이썬 map사용
# https://lsjsj92.tistory.com/201
# 파이썬 아스키코드 변환



# 시행착오▼
# 최대가 36진수이고, 36진수에서 최대 수는 Z이기 때문에
# 영어를 숫자로 변경
# def toNum(num):
#     if ord(num) > 64:
#         return (ord(num) - 64) + 10
#     else:
#         return num

# num,n = input().split()
# # num=list(num)
# num = list(map(toNum,num))

# sum = num[0]
# for i in range(1,len(num)):
#     sum *= num[i]
# print(sum-1)