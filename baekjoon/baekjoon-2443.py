num = int(input())
for i in range(num):
    print(" " * (i) + "*" * (((num - i) * 2) - 1))