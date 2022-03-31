
# 2를 나누고 
# 해가 소수라면 해를 두 번 출력
# 
# 소수가 아니라면 수를 올리며 소수일 때 멈춰서
# 소수가 될 때까지 올린 수를 -한 수와 +한 수 두 개를 출력

from math import sqrt

def isPrime(i):
    if i == 1:
        return 0
    for j in range(2,int(sqrt(i))+1):
        if i % j == 0:
            return 0
    return 1

caseNum = int(input())
for i in range(caseNum):
    num = int(input())
    temp = num // 2
    if isPrime(temp):
        print(temp,temp)
    else:
        count = 0
        while not((isPrime(temp))) or not(isPrime(temp-(count*2))):
            # 두 수 모두 소수가 될 때 멈춰준다
            temp+=1
            count+=1
        print(temp-(count*2),temp)


