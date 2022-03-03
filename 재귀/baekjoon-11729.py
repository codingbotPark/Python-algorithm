# 1 = 1
# 2 = 3, 처음이 2가 
# 3 = 7, 처음이 1

# n 짜리 탑을 세우려면, n-1짜리 탑을 세워야 한다
# (n짜리 탑을 3에 세우려면 n-1짜리 탑을 2에 세워야 한다)

# 홀수 탑 = (1 3), 짝수 탑 = (1 2)



# 두 수를 입력받고 그에 맞는 배열에서 값을 옮기는 함수
def change(x,y):
    print(x,y)
    if x == 1:
        tmep = one[-1]
        one.pop()
        if y == 2:
            two.append(tmep)
        else:
            three.append(tmep)
    elif x == 2:
        temp = two[-1]
        two.pop()
        if y == 1:
            one.append(temp)
        else:
            three.append(temp)
    else:
        temp = three[-1]
        three.pop()
        if y == 1:
            one.append(temp)
        else:
            two.append(temp)

startPo = True
def buildTower(n):
    if n == 1:
        if startPo:
            change(1,3)
            # 3번자리에 1을 놓음
        else:
            change(1,2)
            # 2번자리에 1을 놓음 
    else:
        startPo = not(startPo)
        buildTower(n-1)
        # 탑쌓는 과정이 더 필요함 ...

one = []
two = []
three = []
num = int(input())
for i in range(num,0,-1):
    one.append(i)



    

# num = int(input())


