from traceback import print_tb


a,b = map(int,input().split())
if (b - 45 < 0):#시간을 바꾸어야함
    if (a - 1 < 0):#시간을 바꾸어야함2
        print((a+23)-(45 // 60),(b+60)-45)
    else:
        print(a-1,(b+60)-45)
else:
    print(a,b-45)