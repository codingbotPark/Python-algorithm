# x,y 좌표의 최대값은 100000이기 때문에
# 람다를 사용해 y좌표에 1000000을 곱한 값과 x좌표의 합으로 정렬

import sys
case = int(sys.stdin.readline())
array =  [[0] * 2 for i in range(case)]
for i in range(case):
    array[i][0], array[i][1] = map(int,sys.stdin.readline().split())
# print(sorted(array,key=lambda x : (x[1] * 1000000) + x[0]))
array.sort(key=lambda x : (x[1] * 1000000) + x[0])
for i in range(case):
    print(array[i][0],array[i][1])

# 람다를 사용해 정렬기준을 만들었다
# https://ooyoung.tistory.com/59MIRICANVAS_ITEM_COPY_KEY