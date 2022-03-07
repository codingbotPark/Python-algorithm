cardNum,dealerNum = map(int,input().split())
cards = list(map(int,input().split()))
closeNum = 0
for x in cards:
    for y in cards:
        if y == x:
            continue
        for z in cards:
            if x == z or y == z:
                continue
            temp = x+y+z
            if closeNum < temp and temp <= dealerNum:
                closeNum = temp
print(closeNum)