num = int(input())
for i in range(5 * num):
    if (i // num) % 2 == 0:
        print("@" * num,end="")
        print("   " * num,end="")
        print("@" * num)
    else:
        print("@" * 5 * num)