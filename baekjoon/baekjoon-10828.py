import sys
arr = []
for i in range(int(input())):
    case = list(sys.stdin.readline().split())
    if case[0] == "push":
        arr.append(case[1])
    elif case[0] == "pop":
        try:
            print(arr.pop())
        except:
            print(-1)
    elif case[0] == "size":
        print(len(arr))
    elif case[0] == "empty":
        try:
            arr[0]
            print(0)
        except:
            print(1)
    elif case[0] == "top":
        try:
            print(arr[-1])
        except:
            print(-1)
