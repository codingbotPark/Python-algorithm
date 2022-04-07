num = int(input())
arr = ["*"] * num
for i in range(num):
    if i % 2 == 1:
        print(" ",end="")
    print(*arr)