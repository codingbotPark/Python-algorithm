# 시행착오▼
# 시간초과
# import sys
# case = sys.stdin.readline()
# array = list(sys.stdin.readline().split())
# array = list(map(int,array))
# for i in array:
#     temp = []
#     for j in array:
#         if i > j:
#             if not(j in temp):
#                 temp.append(j)
#     print(len(temp),end=' ')

# 시행착오▼
# 문제를 제대로 알지못함
# import sys
# case = int(sys.stdin.readline())
# array = list(sys.stdin.readline().split())
# value = [0] * case
# for i in range(case):
#     for j in range(case):
#         if array[i] > array[j]:
#             value[i] += 1
# print(*value)