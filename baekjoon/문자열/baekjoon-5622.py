# 상근이의 할머니는 전화번호를 각 숫자에 해당하는 문자로 외우기 때문에 각 알파벳에 해당하는 숫자를 구하면 된다
# 이를 알파벳의 아스키코드 값(65~90)의 연산으로 
# (x(미지수) - 59) // 3 로 나타낼 수 있다

alph = list(input())
num = [] # 상근이 할머니의 알파벳을 숫자로 변경해 저장
time = 0 # 숫자를 치는데 걸리는 시간들의 합을 저장
for i in alph:
    if i > 'O': # 4자리 알파벳이 나올 때
        if i < 'T':
            temp = 7
        elif i < 'W':
            temp = 8
        else:
            temp = 9
    else:
        temp = (ord(i) - 59) // 3
    num.append(temp)
for i in num:
    time += 1+i
print(time)
