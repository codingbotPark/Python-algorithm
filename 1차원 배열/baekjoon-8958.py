a = int(input())
temp = 0 # 임시로 점수를 기록할 변수
c = [] # 점수를 기록할 배열
for i in range(a):
    b = list(input()) # o / x 를 입력받기
    plusScore = 1 # 증가될 스코어
    for j in range(len(b)): # 길이만큼 o x 를 비교하기
        if b[j] == 'O': # 맞을 때
            temp += plusScore
            plusScore += 1
        else: # 아닐 때
            plusScore = 1
    c.append(temp)
    temp = 0

for i in range(a): # 점수출력
    print(c[i])