# insert를 사용하여 가장 앞에 넣으면 느려서 deque의 popleft를 사용하여 빼준다
from collections import deque



arr = deque([])

import sys

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        # arr.insert(0,command[1])
        arr.appendleft(command[1])
    elif command[0] == "front":
        if len(arr):
            print(arr[len(arr) - 1])
        else:
            print(-1)
    elif command[0] == "back":
        if len(arr):
            print(arr[0])
        else:
            print(-1)
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "pop":
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif command[0] == "empty":
        if len(arr):
            print(0)
        else:
            print(1)