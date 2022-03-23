# 계속 시간초과가 나서 결국 구글링을 했다..https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wook2124&logNo=222177426333
# 나와 차이점을 각각 살펴보면
#
# 나는 x,y값을 각각 받고 x+y를 저장하는 배열을 만들어,
# 이 합이 저장된 배열을 sort한 뒤,
# 각각의 값을 비교하며 순서대로 출력
#
# 코드에서는 x,y값을 각각 받고 바로 sorted()함수를 사용해
# x,y값이 저장된 배열을 정렬하고
# 순서대로 출력했다

import sys
case = int(sys.stdin.readline())
array = [[0] * 2 for i in range(case)]
for i in range(case):
    array[i][0],array[i][1] = map(int,sys.stdin.readline().split())
# SArray = sorted(array)
array.sort()
for i in range(case):
    print(array[i][0],array[i][1])

# # 시행착오▼
# # 시간초과
# import sys
# case = int(sys.stdin.readline())
# array = [[0] * 2 for i in range(case)]
# values = [0] * case
# for i in range(case):
#     array[i][0], array[i][1] = map(int,sys.stdin.readline().split())
#     values[i] = array[i][0] + array[i][1]
# values.sort()
# for i in range(case):
#     for j in array:
#         if values[i] == j[0] + j[1]:
#             print(j[0],j[1])

# # 시행착오▼
# # 시간초과
# import sys5
# case = int(sys.stdin.readline())
# nums = [[0] * 2 for i in range(case)]
# for i in range(case):
#     nums[i][0],nums[i][1] = map(int,sys.stdin.readline().split())

# for i in range(case-1):
#     for j in range(case -i -1):
#         if nums[j][0]+nums[j][1] > nums[j+1][0]+nums[j+1][1]:
#             temp1 = nums[j][0]
#             temp2 = nums[j][1]
#             nums[j][0] = nums[j+1][0]
#             nums[j][1] = nums[j+1][1]
#             nums[j+1][0] = temp1
#             nums[j+1][1] = temp2

# for i in range(case):
#     print(*nums[i])

# # 시행착오▼
# # 시간초과
# case = int(input())
# value = []
# nums = [[0] * 2 for i in range(case)]
# for i in range(case):
#     nums[i][0],nums[i][1] = map(int,input().split())
#     value.append(nums[i][0]+nums[i][1])
# value.sort()
# for i in range(case):
#     for j in range(case):
#         if value[i]  == nums[j][0] + nums[j][1]:
#             print(nums[j][0],nums[j][1])
#             # del nums[j]
#             break

