
from math import sqrt


def isPrime(i):
    if i == 1:
        return 0
    for j in range(2,int(sqrt(i))+1):
        if i % j == 0:
            return 0
    return 1

m,n = map(int,input().split())
for i in range(m,n+1):
    if isPrime(i):
        print(i)