# # 값을 받고, total // avg로 나눈 값이 몇이 부족한지 찾는다,
# # 찾고 부족한 n번째 작은 값을 가져와 그 값에 1 추가되게 한다,
# import sys
# k, n = map(int,input().split())

# arr = [0] * k
# total = 0

# for i in range(k):
#     arr[i] = int(sys.stdin.readline())
#     total += arr[i]

# avg = total // n # 임시 avg

# counter = 0
# remainArr = [0] * k

# for i in range(k):
#     remainArr[i] = arr[i] % avg
#     counter += arr[i] // avg

# remainArr.sort()



# # 당연하지만 시간초과가 떳다
# 
# import sys

# k,n = map(int,input().split())
# arr = [0] * k
# total = 0
# for i in range(k):
#     arr[i] = int(sys.stdin.readline())
#     total += arr[i]

# total = (total // n) + 1
# counter = 0

# while (counter != n):
#     total -= 1
#     counter = 0
#     for i in arr:
#         counter += i // total

# print(total)
    

