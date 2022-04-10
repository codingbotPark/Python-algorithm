mush = [0] * 10
for i in range(len(mush)):
    mush[i] = int(input())
sum1 = 0
for i in range(len(mush) -1):
    sum1 += mush[i]
    # 10개를 다 돌기 전 100을 넘을 때
    if sum1 + mush[i+1]>100:
        break 
sum2 = mush[i+1] + sum1
if 100 - sum1 < sum2 - 100:
    print(sum1)
else:
    print(sum2)