# 수에 6이 적어도 3개 이상 연속으로 들어가야 한다
num = int(input())
# 1부터 시작해도 똑같다
value = 665
while num > 0:
    value += 1
    if str(value).count("666"):
        num-=1
    int(value)
print(value)

