# https://ponyozzang.tistory.com/587
# clear함수로 배열을 비울 수 있다
# https://wikidocs.net/64
# 람다로 배열을 만들 수 있다

import sys

arr = [False] * 20

def check(x):
    # x가 있을 때 true
    return arr[x-1]

def remove(x):
    # 있을 때 삭제
    if check(x):
        arr[x-1] = False

def add(x):
    if not(check(x)):
        arr[x-1] = True

def toggle(x):
    if check(x):
        remove(x)
    else:
        add(x)

def all():
    for i in range(20):
        arr[i] = True

def empty():
    for i in range(20):
        arr[i] = False

for i in range(int(input())):
    inputV = list(sys.stdin.readline().split())
    # print(inputV)
    if inputV[0] == "add":
        add(int(inputV[1]))
    elif inputV[0] == "remove":
        remove(int(inputV[1]))
    elif inputV[0] == "check":
        if check(int(inputV[1])):
            print(1)
        else:
            print(0)
    elif inputV[0] == "toggle":
        toggle(int(inputV[1]))
    elif inputV[0] == "all":
        all()
    elif inputV[0] == "empty":
        empty()

# import sys

# arr = []

# def check(x):
#     if x in arr:
#         return 1
#     else:
#         return 0

# def add(x):
#     if not(check(x)):
#         arr.append(x)

# def remove(x):
#     if check(x):
#         arr.remove(x)

# def toggle(x):
#     if check(x):
#         remove(x)
#     else:
#         add(x)

# def empty():
#     arr.clear()

# def all():
#     empty()
#     (lambda x:add(str(x)))(range(1,21))

# for i in range(int(input())):
#     value = list(sys.stdin.readline().split())
#     cal = value[0]
#     if cal == "add":
#         add(value[1])
#     elif cal == "remove":
#         remove(value[1])
#     elif cal == "toggle":
#         toggle(value[1])
#     elif cal == "check":
#         print(check(value[1]))
#     elif cal == "empty":
#         empty()
#     elif cal == "all":
#         all()


# 입력받은 문자를 바로 함수로 사용하기 위해 딕셔너리를 사용
# 딕셔너리의 함수에 인자를 어케전달하는지 몰라서 포기
# arr = []

# def check(x):
#     if x in arr:
#         return 1
#     else:
#         return 0

# def add(x):
#     if not(check(x)):
#         arr.append(x)

# def remove(x):
#     if not(check(x)):
#         arr.remove(x)

# def toggle(x):
#     if check(x):
#         remove(x)
#     else:
#         add(x)

# def empty():
#     for i in range(len(arr)):
#         arr.pop()

# def all():
#     empty()
#     for i in range(1,21):
#         arr.append(i)

# Cal = {
#     'add' : add(),
#     'remove' : remove(),
#     'check' : print(check()),
#     'toggle' : toggle(),
#     'all' : all(),
#     'empty' : empty()
# }

# for i in range(int(input())):
#     value = list(input().split())
#     Cal[value[0]]


# 이렇게 하는건 당연히 비효율적인거같다
# def check(arr,x):
#     if x in arr:
#         return 1
#     else:
#         return 0

# arr = []

# for i in range(int(input())):
#     # cal,x = input().split()
#     value = list(input().split())
#     if value[0] == "add":
#         if not(check(arr,value[1])):
#             arr.append(value[1])
#     elif value[0] == "remove":
#         if not(check(arr,value[1])):
#             arr.remove(value[1])
#     elif value[0] == "check":
#         print(check(arr,value[1]))
#     elif value[0] == "toggle":
#         if check(arr,value[1]):
#             arr.


