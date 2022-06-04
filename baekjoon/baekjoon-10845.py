# 파이썬 배열에서 가장 앞 요소를 추가하는 방법은
# insert이다, insert(넣을 인덱스, 넣을 값)

arr = []

import sys

for i in range(int(input())):
    command = (sys.stdin.readline()).split()
    if command[0] == "push":
        arr.insert(0,int(command[1]))
    elif command[0] == "pop":
        if (len(arr)):
            print(arr.pop())
        else: # 배열이 비었을 때
            print(-1)
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        # arr가 비었을 때 len(arr) == 0 은 true, int 형으로 바꿔준다
        print(int(len(arr) == 0))
    elif command[0] == "front":
        if (len(arr)):
            print(arr[len(arr) - 1])
        else:
            print(-1)
    elif command[0] =="back":
        if (len(arr)):
            print(arr[0])
        else:
            print(-1)