
# 시행착오▼
# 최빈값 조건 중 '여러 개 있을 때는 최빈값 중 두 번째로 작은 값을 출력한다'를 구현하지 못함
# import sys
# num = int(sys.stdin.readline())
# array = []
# array2 = [0] * 8000
# sum = 0
# for i in range(num):
#     array.append(int(sys.stdin.readline()))
#     array2[array[i]] += 1
#     sum += array[i]
# print(sum/num)
# array.sort()
# print(array[num/2])
# print(max(array2))
# print(array2[-1] - array2[0])

# 시행착오▼
# 중앙값을 구하는데는 이런 방법이 좋지 않을 것 같아서
# import sys
# num = sys.stdin.readline()
# array = [] * 8000
# sum = 0
# for i in range(num):
#     input = sys.stdin.readline()
#     sum += input
#     array[input] += 1
# print(sum/num)