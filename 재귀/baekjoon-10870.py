num = 0
def fibo(n):
    if n == 2:
        return 1
    return 1 + fibo(n-1)
n = int(input())
if n == 0:
    print(0)
elif n==1:
    print(1)
else:
    print(fibo(n))