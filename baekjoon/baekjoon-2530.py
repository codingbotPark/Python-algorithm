h, m, s = map(int,input().split())
d = int(input())
s += d

m += (s//60)
s %= 60

h += (m//60)
m %= 60

h %= 24
print(h,m,s)
