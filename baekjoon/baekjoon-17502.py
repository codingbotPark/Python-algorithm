num = int(input())
arr = list(input())
for i in range(len(arr)//2+1):
    if arr[i] == "?":
        if not(arr[-i-1] == "?"):
            arr[i] = arr[-i-1]
        else:
            arr[i] = "a"
            arr[-i-1] = "a"
    else:
        if arr[-i-1] == "?":
            arr[-i-1] = arr[i]
print("".join(arr))