def findPrime(i):
    if i == 1:
        return 0
    for j in range(2,(i//2) + 1):
        if i % j == 0:
            return 0
    return 1

m = int(input())
n = int(input())
primeSum = 0
minPrime = 0
for i in range(m,n+1):
    if findPrime(i):
        if primeSum == 0:
            minPrime = i
        primeSum += i

if not(minPrime):
    print(-1)
else:
    print(primeSum)
    print(minPrime)
