def findPrime(i):
    for j in range(2,(i//2) + 1):
        if i % j == 0:
            return 0
    if i == 1:
        return 0
    return 1


alphNum = int(input())
cases= map(int,input().split())
primes = 0
for i in cases:
    if findPrime(i):
        primes += 1
print(primes)