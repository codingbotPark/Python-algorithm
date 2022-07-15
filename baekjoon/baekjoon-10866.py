# https://leonkong.cc/posts/python-deque.html
# 파이썬에는 deque가 있다
# deque는 양방향 큐라서 양 끝 엘리먼트의 append와 pop이
# 압도적으로 빠르다고 한다

from collections import deque
import sys

arr = deque()

for i in range(int(input())):
    command = sys.stdin.readline()
    if command.startswith("push_front"):
        arr.appendleft((command.split())[1])
    elif command.startswith("push_back"):
        arr.append((command.split())[1])
    elif command.startswith("pop_front"):
        try:
            print(arr.popleft())
        except:
            print(-1)
    elif command.startswith("pop_back"):
        try:
            print(arr.pop())
        except:
            print(-1)
    elif command.startswith("size"):
        print(len(arr))
    elif command.startswith("empty"):
        try:
            if arr[0]:
                print(0)
        except:
            print(1)
    elif command.startswith("front"):
        try:
            print(arr[0])
        except:
            print(-1)
    elif command.startswith("back"):
        try:
            print(arr[-1])
        except:
            print(-1)
