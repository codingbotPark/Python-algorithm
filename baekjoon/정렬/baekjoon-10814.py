import sys
case = int(sys.stdin.readline())
array = [[0] * 2 for i in range(case)]
for i in range(case):
    array[i][0],array[i][1] = (sys.stdin.readline()).split()
    array[i][0] = int(array[i][0])
array.sort(key=lambda x : x[0])
for i in array:
    print(*i)
