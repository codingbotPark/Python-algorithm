# 레이저와 막대기를 나누고,
# (를 만날 때 stick +1
# )를 만날 때 stick +1 , count -1을 해준다

string = input().replace("()","|")

stick = 0 # 현재 레이저의 범위 막대기의 개수
count = 0 # 나눠진 막대기의 개수

for i in string:
    if i == "(":
        stick+=1
    elif i == ")":
        stick-=1
        count+=1
    else: # 레이저
        count += stick

print(count)