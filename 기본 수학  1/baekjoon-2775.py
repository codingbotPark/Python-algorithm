# 그냥 2차원 배열에 값 다 계산하자~
# 14 X 14짜리 2차원 배열에 각각 값들을 계산해서 넣음


valueArray = [[0] * 15 for i in range(15)]

for i in range(1,15): # 0층 세팅
    valueArray[0][i] = i

for i in range(1,15):
    for j in range(1,15): # 호를 돌린다
        for n in range(1,j+1): # 호 만큼 현재층-1 층의 사람 수를 센다
            valueArray[i][j] += valueArray[i-1][n]

# for i in range(15):
#     for j in range(1,15):
#         print(valueArray[i][j],end=' ')
#     print()

caseNum = int(input())
for i in range(caseNum):
    print(valueArray[int(input())][int(input())])



# 시행착오
# 각 층마다 전체 수를 주어진 호가 다르다 생각하고 했을 때를 적어봤는데...
# 입력값 : 2 2
# 호 001 002
# 명  1   2   3
# 호 101 102      1증가
# 호  1   3   4     0증가
# 명 201 202      1증가
# 명  1   4   5
#
# 입력값 : 3 3
# 호 001 002 003
# 명  1   2   3   6
# 호 101 102 103      4증가
# 명  1   3   6   10    1증가
# 호 201 202 203      5증가 0증가
# 명  1   4   10  15    1증가
# 호 301 302 303      6증가 
# 명  1   5   15  21    
#
# 입력값 : 4 4
# 호 001 002 003 004
# 명  1   2   3   4   10
# 호 101 102 103 104      10증가
# 명  1   3   6   10  20      5증가
# 호 201 202 203 204      15증가    1증가
# 명  1   4   10  20  35      6증가     0증가
# 호 301 302 303 304      21증가    1증가
# 명  1   5   15  35  56      7증가
# 호 401 402 403 404      28증가
# 명  1   6   21  56  84
#
# 입력값 : 5 5
# 호 001 002 003 004 005
# 명  1   2   3   4   5   15
# 호 101 102 103 104 105      20증가
# 명  1   3   6   10  15  35      15증가
# 호 201 202 203 204 205      35증가  6증가
# 명  1   4   10  20  35  70      21증가  3증가
# 호 301 302 303 304 305      56증가  9증가   4증가?
# 명  1   5   15  35  70  126     30증가  7증가
# 호 401 402 403 404 405      86증가  16증가
# 명  1   6   21  56  126 212     46증가
# 호 501 502 503 504 505      120증가
# 명  1   7   28  84  212 332