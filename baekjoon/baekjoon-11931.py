import sys

num = int(input())
arr = []
for i in range(num):
    arr.append(int(sys.stdin.readline()))
arr.sort()
arr.reverse()
for i in arr:
    print(i)