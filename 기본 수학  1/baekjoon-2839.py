allSugar = int(input())
Pack = 0
if allSugar %3 == 0:
    print(allSugar // 3)
elif allSugar %5 == 0:
    print(allSugar // 5)
else:
    while 1:
        if (allSugar - 5) >= 3:
            print("5팩")
            allSugar -= 5
            Pack+=1
        elif (allSugar - 3) >= 0:
            print("3팩")
            allSugar -= 3
            Pack+=1
        else:
            print(-1)
            exit()
        if allSugar <= 0:
            break
    if allSugar == 0:
        print(Pack)
    else:
        print(-1)