

# arr = [[-1] * 15 for _ in range(5)]
arr = [0] * 5
for i in range(5):
    temp = list(input())
    for j in range(15 - len(temp)):
        temp.append(-1)
    arr[i] = temp
for i in range(15):
    for j in range(5):
        if arr[j][i] == -1:
            continue
        print(arr[j][i],end="")