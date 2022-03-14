# 일부로 c언어스럽게 풀어봤다

# num = int(input())
# array = []
# for i in range(num):
#     array.append(int(input()))
# for i in range(num):
#     for j in range(num - i - 1):
#         if array[j] > array[j + 1]:
#             temp = array[j]
#             array[j] = array[j + 1]
#             array[j + 1] = temp
# for i in range(num):
#     print(array[i])


# 많은 수를 받기 때문에 sys를 사용
import sys

num = int(sys.stdin.readline())
array = []
for i in range(num):
    array.append(int(sys.stdin.readline()))
array.sort()
for i in range(num):
    print(array[i])