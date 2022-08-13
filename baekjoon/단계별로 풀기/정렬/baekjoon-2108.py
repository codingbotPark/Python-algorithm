import math
import sys
from collections import Counter

def rounding(avg):
    if avg < 0:
        if avg % 1 > 0.5:
            return math.ceil(avg)
        else:
            return math.floor(avg)
    else:
        if avg % 1 > 0.5:
            return math.ceil(avg)
        else:
            return math.floor(avg)


case = int(sys.stdin.readline())
array = []
for i in range(case):
    array.append(int(sys.stdin.readline()))
# 산술평균
print(rounding(sum(array)/len(array)))
# 중앙값
array.sort()
print(array[len(array)//2])
# 최빈값
if case > 1:
    cnt = Counter(array)
    cntMost = cnt.most_common(2)
    if (cntMost[0][1] == cntMost[1][1]):
        print(cntMost[1][0])
    else:
        print(cntMost[0][0])
else:
    print(array[0])
print(array[-1] - array[0])

# 산술평균, 중앙값, 최빈값, 범위를 제대로 구해도 틀려서
# 잘못된 부분을 찾기위해 구해야하는 값 하나하나 검색했다
# 산술평균 : https://www.delftstack.com/ko/howto/python/calculate-python-mean/
# 중앙값 : https://blog.naver.com/PostView.naver?blogId=happynut&logNo=222492811906&categoryNo=194&parentCategoryNo=108&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
# 최빈값 : https://codepractice.tistory.com/71
# 범위 : https://mindscale.kr/course/basic-stat-python/4/



# https://puleugo.tistory.com/43
# 파이썬에서 반올림은 오사오입 이라는 방식을 사용하는데,
# 5의앞 자리가 홀수 = 올림, 짝수 = 내림
#
# >>> round(0.5)
# 0
# >>> round(1.5)
# 2
# >>> round(2.5)
# 2
# >>> round(3.5)
# 4
# >>> round(4.5)
# 4
# >>> round(5.5)
# 5
#
# 그래서 위와같은 결과가 나오게 된다
# 그래서 그냥 소수값을 %1 하여 비교해서 +1 혹은 그대로 놔둔 후,
# 소수를 없애는 방법을 사용

# # 시행착오▼
# import sys
# array = [0] * 8001
# num = int(sys.stdin.readline())
# sum = 0
# for i in range(num):
#     temp = sys.stdin.readline()


# import sys
# array1 = [] # 들어온 값을 그냥 추가
# array2 = [0] * 8001 # 들어온 값의 인덱스에 +1
# num =int(sys.stdin.readline())
# sum = 0
# for i in range(num):
#     array1.append(int(sys.stdin.readline()))
#     array2[array1[i]+4000]+=1
#     sum += array1[i]
# avg = (sum / num)

# if avg > 0:
#     if avg%1 >= 0.5:
#         avg = int(avg) + 1
#     else: avg = int(avg)
# else:
#     if avg %1 <= 0.5:
#         avg = int(avg) - 1
#     else:
#         avg = int(avg)

# # 산술평균
# print(avg)

# # 중앙값
# array1.sort()
# print(array1[(num//2)])

# # 최빈값
# freNum = max(array2)
# freValue = 0
# counter = 0
# for i in range(8001):
#     if freNum == array2[i]:
#         counter += 1
#         freValue = i - 4000
#         if counter == 2:
#             print(i - 4000)
#             break
# if counter == 1:
#     print(freValue)

# # 범위
# print(array1[-1] - array1[0])

# # 시행착오▼
# # 중앙값, 산술평균 부분을 다시 해봤지만 맞는 망법을 찾지 못했다 
# import sys
# array1 = [] # 들어온 값을 그냥 추가
# array2 = [0] * 8010 # 들어온 값의 인덱스에 +1
# num =int(sys.stdin.readline())
# sum = 0
# for i in range(num):
#     array1.append(int(sys.stdin.readline()))
#     array2[array1[i]+4000]+=1
#     sum += array1[i]
# avg = (sum / num)

# firstNum = int((avg) * 10)
# if firstNum < 0:
#     firstNum %= 10
#     if firstNum > 5:
#         int(avg) - 1
#     else:
#         int(avg)
# else:
#     firstNum %= 10
#     if firstNum > 5:
#         int(avg) + 1
#     else:
#         int(avg)

# # if avg > 0:
# #     if avg%1 >= 0.5:
# #         avg = int(avg) + 1
# #     else: 
# #         avg = int(avg)
# # else:
# #     if avg %1 >= 0.5:
# #         avg = int(avg)
# #     else:
# #         avg = int(avg) - 1

# # 산술평균
# print(avg)

# # 중앙값
# array1.sort()
# print(array1[(num//2)])

# # array1.sort()
# # print(array1[round(num/2)])

# # array1.sort()
# # center = num //2+1
# # if num == 1: center -= 1
# # print(array1[center])

# # 최빈값
# freNum = max(array2)
# freValue = 0
# counter = 0
# for i in range(8001):
#     if freNum == array2[i]:
#         counter += 1
#         freValue = i - 4000
#         if counter == 2:
#             print(i - 4000)
#             break
# if counter == 1:
#     print(freValue)

# # 범위
# print(array1[-1] - array1[0])


# # # 시행착오▼
# # # 왜인진 모르겠지만 틀린다고 뜬다
# import sys
# num = int(sys.stdin.readline())
# array1 = [0]*8001 # + 하며 추가 
# array2 = []
# sum = 0
# for i in range(num):
#     array2.append(int(sys.stdin.readline()))
#     array1[array2[i]+4000]+=1
#     sum += array2[i]
# print(round(sum/num))
# array2.sort()
# if ((num/2) % 1) > 0.4:
#     num = ((num / 2) % 1)+1
# else:
#     num = ((num/2)%1)-1
# print(array2[round(num)])
# freNumber = max(array1) #가장 큰 수
# counter = 0
# for i in range(len(array1)):
#     if array1[i] == freNumber:
#         counter += 1
#         value = i
#         if counter == 2:
#             value = i
#             break
# print(value - 4000)
# print(array2[-1] - array2[0])


# # 시행착오▼
# # 최빈값 조건 중 '여러 개 있을 때는 최빈값 중 두 번째로 작은 값을 출력한다'를 구현하지 못함
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