# 좌표평면 위 직사각형의 좌표들은 모두 x좌표,y좌표 각각 맞는 점이 하나씩은 있기 때문에


x = []
y = []
for i in range(3):
    tempX,tempY = map(int,input().split())
    x.append(tempX)
    y.append(tempY)

if x.count(tempX)==2:
    for i in range(2):
        x.remove(tempX)
    print(*x,end=" ")
else:
    print(tempX,end=" ")

if y.count(tempY)==2:
    for i in range(2):
        y.remove(tempY)
    print(*y,end="")
else:
    print(tempY,end=" ")