num = int(input())
for i in range(num):
    for b in range(i):
        print(" ",end="")
    for s in range(((num - i) * 2) - 1):
        print("*",end="")
    print()
for i in range(0,num-1):
    for b in range(num - i - 2):
        print(" ",end="")
    for s in range((i * 2) + 3):
        print("*",end="")
    print()