# https://velog.io/@ayoung0073/algorithm-baekjoon-1463
# https://pgh268400.tistory.com/461
num = int(input())

# x + 1크기의 배열 생성
arr = [0] * (num + 1)

# https://data-make.tistory.com/384
# bottom up = 반복문
# top down = 재귀(파이썬에서는 시간복잡도 문제)
# 다이나믹프로그래밍 bottom up 이라고 한다

# 배열에 그 수가 되기 위해 몇 번 연산이 필요한지 수를 넣는다
for i in range(2, num + 1):
    # 2부터 1로 초기화 (1 은 0번 연산)
    arr[i] = arr[i - 1] + 1

    # 3으로 나누었을 때가 더 연산수가 적다(우선시됨)
    # min의 두 개의 인자는 작은 수를 리턴
    # if i % 3 == 0:
    #     arr[i] = min(arr[i], arr[i // 3] + 1) # 이전 2의 배수에 * 2이기 때문에
    # elif i % 2 == 0:
    #     arr[i] = min(arr[i], arr[i//2] + 1)

    # 위는 틀리다

    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1) # 연산 수 비교
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)

print(arr[num])



# 2 또는 3이기 때문에 
# 3으로 나누었을 때 1이 남으면 3으로 나누기,
# 2로 나누었을 때 1이 남으면 2로 나누기
# num = int(input())
# if num % 3 == 1:
#     print((num // 3))
# else:
#     print((num // 2))


# 1번이 3으로 나누기
# 2번이 2로 나누기
# 3번이 1을 빼기
#
# 만약 -1을 했을 때 3의 배수라면 -1을 하고, 아니면 2로 나눈다
#
# num = int(input())
# counter = 0
# while(num != 1):
#     counter += 1
#     if num % 3 == 0:
#         num /= 3
#     else:
#         if (num -1) % 3 == 0:
#             num -= 1
#         elif num % 2 == 0:
#             num /= 2
#         else:
#             num -= 1
# print(counter)



