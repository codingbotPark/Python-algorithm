# 각 자리수들을 n의 제곱으로 쳐서 곱한 후 더해야 한다
def toNum(num):
    if ord(num) > 64:
        return int((ord(num) - 65) + 10)
    else:
        return int(num)

string,number = input().split()
string = list(string)
number = int(number)
sum = 0
for i in range(1,len(string)+1):
    sum += toNum(string[-i]) * (number ** (i-1))
print(sum)
    # print(string[-i])


# for i in range(len(string)-1,-1,-1):
#     print(string[i],end="")


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
# print(sum-1)f