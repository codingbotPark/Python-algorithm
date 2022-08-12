import sys

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

arr.sort(reverse=True)
# 정렬

tri = [0,0,0] 
for i in range(len(arr)):
    if tri[0] < tri[1] + tri[2]:
        print(sum(tri))
        exit()
    try:
        tri[0] = arr[i]
        tri[1] = arr[i+1]
        tri[2] = arr[i+2]
    except:
        print(-1)
        exit()
