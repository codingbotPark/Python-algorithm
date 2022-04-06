num = int(input())
if num > 1:
    print(" " * (num - 1),end="")
    print("*")
for i in range(1,num-1):
    print(" " * (num - 1 - i),end="")
    # 2일 때는 출력하면 안됨
    print("*",end="")
    print(" " * ((i * 2) - 1),end="")
    print("*")
print("*" * ((num * 2) - 1))


# num = int(input())
# for i in range(1,num):
#     print(" " * (num - i),end="")
#     print("*",end="")
#     print(" " * (i - 2),end="")
#     print("*")
# print("*" * ((i * 2) - 1))
