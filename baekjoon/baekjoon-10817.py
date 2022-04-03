# a,b,c가 모두 다를 때
# a가 중간수라면
# a - b 가 양수 or 음수
# a - c 가 양수였다면 음수, 음수였다면 양수
# 즉 이 둘을 곱하면 -가 나오면 중간 수이다
#
# a, b, c중 같은 수가 있을 때를 대비해
# 0 * n = 0이기 때문에 
# if (a - b) * (a - c) <= 0:

a,b,c = map(int,input().split())
if (a - b) * (a - c) <= 0:
    print(a)
elif (b - a) * (b - c) < 0:
    print(b)
else:
    print(c)