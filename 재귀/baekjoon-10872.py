# 출처 : https://dojang.io/mod/page/view.php?id=585

def facto(num):
    if num == 0:
        return 1
    return num * facto(num-1)
        
num = int(input())
print(facto(num))

