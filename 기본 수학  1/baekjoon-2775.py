# 0 층에 사는 사람은 0층의 i호에는 i명 만큼 살기 때문에
# 각 층의 1 호는 한 명씩 살고
# 102호 = 3명 202호 = 4명 302호 = 5명
# 103호 = 6명 203호 = 10명 303호 = 15명
# 104호 = 10명 204호 = 20명 304호  = 35명

# num = int(input())
# v = 0
# for i in range(num):
#     k = int(input()) # 층
#     n = int(input()) # 호
#     for i in range(k):

valueArray = [[0] * 14 for i in range(14)]
for i in range(0,14):
    valueArray[0][i] = i + 1
    print(valueArray[0][i])
