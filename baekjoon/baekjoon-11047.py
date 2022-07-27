import sys
num,k = map(int,input().split())

arr = [0] * num

for i in range(1,num+1):
    arr[-i] = int(sys.stdin.readline())

counter = 0

i = 0
while(k != 0):
    result = k // arr[i]
    if result > 0:
        counter += result
        k %= arr[i]
    i += 1

print(counter)



# 시간초과가 떳다
# 아마도 이중 while문이 느린 것 같다
# 그냥 나누기를 하고, 나누고 남은 값을 k에 저장한다
# 
# import sys

# num, k = map(int,input().split())
# arr = [0] * num
# for i in range(1,num+1):
#     arr[-i] = int(sys.stdin.readline())

# # 내림차순으로 arr에 들어감

# counter = 0

# i = 0
# while (k != 0):
#     # 0이 아니고, -했을 때 양수일 때 까지
#     while (k !=0 and k - arr[i] >= 0):
#         k -= arr[i]
#         counter+=1
#     i+=1
# print(counter)