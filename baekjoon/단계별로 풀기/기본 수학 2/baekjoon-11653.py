num = int(input())
i = 2   
while i <= num:
    if num % i == 0:
        num //= i
        print(i)
        i-=1
    i+=1
        