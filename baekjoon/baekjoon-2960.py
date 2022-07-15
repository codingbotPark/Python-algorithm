n,k = map(int,input().split())

# 0번째와 1번째는 기본값으로 True를 넣어준다
arr = [False for i in range(n+2)]
arr[0] = True
arr[1] = True

p = 2 # 기본은 2

while True:
    for i in range(p,n+1,p):
        if not(arr[i]):
            k -= 1
            if(k == 0):
                print(i)
                quit() # 프로그램 종료
            arr[i] = True

    try:
        p = arr.index(False)
    except:
        break