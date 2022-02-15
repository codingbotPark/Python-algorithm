hour, minute = map(int,input().split())
spend = int(input())
temp = minute + spend
hour += (temp // 60)
temp %= 60
print((hour % 24),temp)