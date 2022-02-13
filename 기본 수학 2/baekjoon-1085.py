x,y,width,height = map(int,input().split())
values = []
values.append(width - x)
values.append(height - y)
values.append(x)
values.append(y)
print(min(values))
