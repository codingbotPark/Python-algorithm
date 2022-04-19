# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# 파이썬에서 진수 변환은 int, bin() = 2, oct() = 8, hex() = 16
# 에서 진수 앞 진법표시를 없애려면 [2:] 를 하면 된다
# 아래와 같이 n진수에서 n진수로 변경시킬 수 있다
# solution(int('c',16),4) (16진수인 c를 4진수로 변경)

# 회문인지 확인
def isCircular(temp):
    for i in range(len(temp)//2):
        if not(temp[i] == temp[-i-1]):
            return 0
    return 1

# 10진법 -> n진법의 수로 바꾸는 함수
# 링크의 글을 보고 만들었고, 10진수의 수와 바꿀 진수를 인자로 받는다
def changeValue(v,q):
    result = ''
    
    while v > 0:
        v, mod = divmod(v,q)
        result += str(mod)

    return result[::-1]

def impleNumbers(number):
    for i in range(2,63):
        # 몇진법이든지 회문이기만 하면되기 때문에 return 1을 해준다
        if isCircular(list(map(int,list(changeValue(number,i))))):
            return 1
    return 0
            

num = int(input())
for i in range(num):
    inValue = int(input())
    if impleNumbers(inValue): # 회문일 떄 1
        print(1)
    else:
        print(0)




# 시행착오▼
# 문제를 잘못읽어서 B진법 (2 ~ 64) 중 모두를 확인해야한다
# num = int(input())
# arr = [0] * num
# for i in range(num):
#     temp = list(map(int,list(input())))
#     # -1을 해줘서 반복문을 돈 다음 if문에서
#     # 수 하나가 들어왔어도 1이 출력될 수 있게 맞춰줌
#     j = -1
#     # 반만 돌아도 수가 홀 수 일 때 중간수가 남기 때문에 된다
#     for j in range(0,len(temp)//2):
#         if not(temp[j] == temp[-j-1]):
#             j += 1
#             break
#     if j == (len(temp) // 2) -1:
#         print(1)
#     else:
#         print(0)

