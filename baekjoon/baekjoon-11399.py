# 앞 사람의 업무를 뒤 사람이 기다려야 하기 때문에,
# 시간이 적게 걸리는 사람의 업무가 먼저 실행되어야 한다

num = int(input())
arr = list(map(int,input().split()))
arr.sort()

counter = 0
for i in range(num,0,-1):
    counter += arr[-i] * i

print(counter)