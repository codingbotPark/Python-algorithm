# 더 효과적으로 딕셔너리를 사용해야한다

# 박종현과의 통화
# 사전이란 객체와 같은 느낌,
# 키 값과, 값이 있듯
# 
# 딕셔너리를 만드는 방법에는 
# A = [1,2,3]
# B = [5,6,7]
# A = B
# A[0] = 1
# 를 하면 1,6,7이 나오는데 이는 얕은복사라고 하고
# 이를 없애려면 A = B[:] (슬라이싱)를 해야한다
# 


case = int(input())
array = []
Dict = {}
# array = map(int,list(input())) # 2 4 -10 4 -9
array = list(map(int,input().split()))
tempArray = list(set(array))
tempArray.sort()

for i in range(len(tempArray)):
    # 딕셔너리에 key값으로 tempArray의 값이 들어가고
    # 값으로는 i가 들어온다
    Dict[tempArray[i]] = i
for i in array:
    print(Dict[i], end=" ")


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