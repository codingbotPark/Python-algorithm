num = int(input())
for i in range(num * 2):
    for j in range(num):
        if (i + j)%2 == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    print()    
    