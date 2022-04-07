num = int(input())
array = [0,1]
for i in range(2,num+1):
    array.append(array[i-1]+array[i-2])
print(array[num])


# def fibo(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return fibo(num -1) + fibo(num - 2)

# num = int(input())
# print(fibo(num+1))