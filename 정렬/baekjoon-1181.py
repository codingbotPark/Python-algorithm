import sys
case = int(sys.stdin.readline())
array = []
for i in range(case):
    array.append(sys.stdin.readline().strip())
# print("Start")
array = list(set(array))
array.sort()
array.sort(key=lambda x : len(x))
for i in array:
    print(i)

# sys.stdin.readline으로 입력을 받을 때 계행문자 처리는
# .strip() 를 해서 할 수 있다
# https://hwisaek.tistory.com/entry/Python-sysstdinreadline-%EA%B0%9C%ED%96%89-%EB%AC%B8%EC%9E%90-%EC%B2%98%EB%A6%AC