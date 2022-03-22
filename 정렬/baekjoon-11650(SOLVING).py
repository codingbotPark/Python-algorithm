# # 시간초과
# import sys
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

