# 더 효과적으로 딕셔너리를 사용해야한다
import sys
case = int(sys.stdin.readline())
array = []
array = list(sys.stdin.readline().split())
dictionary = {i:array[i] for i in range(len(array))}
print(dictionary)


# 딕셔너리를 써서 아래처럼 각각 매칭되게 해야한다
# 1 1 3 3 2 2 6 6 5 5
# 0 0 2

# 0 0 2 2 1 1 4 4 3 3

# 1 2 3 5 6
# {
#     1:0
#     2:1
#     3:2
#     5:3
#     6:4
# }


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