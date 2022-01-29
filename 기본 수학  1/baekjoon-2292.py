n = int(input())
n -= 1 # 7까지 2이기 때문에 6으로 맞춰준다
i = 0
while 1:
    n -= (i * 6)
    if n <= 0:
        print(i + 1)
        break
    i += 1