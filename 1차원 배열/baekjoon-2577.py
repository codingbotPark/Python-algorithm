from itertools import count


a = int(input())
b = int(input())
c = int(input())
v = a * b * c
v = list(map(int,list(str(v))))
for i in range(10):
    print(v.count(i))
