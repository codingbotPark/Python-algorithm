# 일부로 c언어스럽게 풀어봤다

num = int(input())
array = []
for i in range(num):
    array.append(input())
for i in range(num - 1):
    for j in range(num - i - 1):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j+ 1]
            array[j+1] = temp
for i in range(num):
    print(array[i])