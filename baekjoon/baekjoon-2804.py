# https://www.delftstack.com/ko/howto/python/python-exit-program/#exit-%EB%A9%94%EC%84%9C%EB%93%9C%EB%A1%9C-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EC%A2%85%EB%A3%8C
# 함수에서 exit() 를 해서 없앨 수 있다


def printResult(x,y):
    for i in range(len(arr2)):
        # 맞을 땐 그냥 arr1을 출력
        if i == y:
            for j in arr1:
                print(j,end="")
        else:
            for j in range(len(arr1)):
                if j == x:
                    print(arr2[i],end="")
                else:
                    print(".",end="")
                
        print()
    exit()

arr1, arr2 = input().split()
arr1 = list(arr1)
arr2 = list(arr2)
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            printResult(i,j)

            