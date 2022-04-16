endDay = [31,28,31,30,31,30,31,31,30,31,30,31]
dayArr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

a,sum = map(int,input().split())
for i in range(a-1):
    sum += endDay[i]
print(dayArr[sum % 7])
