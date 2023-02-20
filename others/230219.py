n = int(input())
votes = list(map(int,input().split()))

result = -1
# 1. 보통 풀거같은 코드?
for i in range(1,n+1):
    # 과반수 이상(votes의 / 2 이상) 일 떄
    if (votes.count(i) > ((len(votes) / 2))):
        result = i
print(result)

# 2. max함수를 사용한 코드
# 어차피 가장 빈도수가 높은 수가 과반수를 안 넘으면
# 나머지도 다 안넘는 점을 이용!
temp = max(votes,key=votes.count)
if (votes.count(temp) > (len(votes) / 2)):
    print(temp)
else:
    print(-1)


