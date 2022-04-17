import sys
arr = []
num = int(input())
for i in range(num):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in arr:
    print(i)