# https://code-code.tistory.com/10
# format을 사용하여 소수점 n번째 자리까지 0으로 채울 수 있다

import sys

num = int(input())
arr = [0] * num
for i in range(num):
    arr[i] = float(sys.stdin.readline())
    # arr[i] = input()
arr.sort()
for i in arr:
    # print(format(i,"f"))
    print("{:.3f}".format(i))