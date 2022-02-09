# 에라토스테네스의 체는 많은 량의 소수를 구할 때 좋은 알고리즘이다
# 1 부터 n까지의 배열을 만들어 주고 
#
# 1. 2부터 n // 2 까지의 수까지 
# 2. 각 수를 제외한 그 수의 배수들을 지워준다
# 3. 지워진 수는 건너 뛴다
# 
# 출처 : https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4#%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4%EB%A5%BC_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4%EB%A1%9C_%EA%B5%AC%ED%98%84
# 출처 : https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
# 출처 : https://www.youtube.com/watch?v=5ypkoEgFdH8&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=25


# 1부터 num * 2 만큼의 배열을 에라토스테네스의 체를 사용해 소수만 남도록 하고
# (num + 1) ~ (num * 2) 까지의 범위 중 소수의 개수(True)를 구한다
while 1:
    num = int(input())
    if num == 0:
        break
    # 2차원 배열을 만들어준다
    # True = 있는 수 False = 없는 수
    # array = [True] * ((num * 2) + 1)# n-1 인덱스
    array = [True] * ((num * 2))# n-1 인덱스
    for i in range(2,(len(array) // 2) + 1): # 배열을 False로 만듬
        if i == True: # True일 때
            j = i * 2
            while j < len(array):
                array[j] = False
                j += i
    primeNum = 0
    for i in range(num,len(array)):
        if array[i]:
            primeNum += 1
    print(primeNum)

# 시행착오
# 시간초과
# from math import sqrt

# def isPrime(i):
#     if i == 1:
#         return 0
#     for j in range(2,int(sqrt(i))+1):
#         if i % j == 0:
#             return 0
#     return 1

# while 1:
#     num = int(input())
#     if num == 0:
#         break
#     primeNum = 0
#     for i in range(num+1,2*num+1):
#         primeNum += isPrime(i)
#     print(primeNum)


