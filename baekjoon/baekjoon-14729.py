# https://code-code.tistory.com/10
# format을 사용하여 소수점 n번째 자리까지 0으로 채울 수 있다
# 그냥 하위 7명만을 출력하면 된다

# zfill을 4로해서 수까지 딱 나오게 헸다
import sys
arr = [0] * 100001
for i in range(int(input())):
    arr[int(float(sys.stdin.readline().strip()) * 1000)]+=1
counter = 0
for i in range(len(arr)):
    for j in range(0,arr[i]):
        temp = list(str(i).zfill(4))
        temp.insert(-3,".")
        print("".join(temp))
        counter += 1
        if counter == 7:
            exit()
    


# 왜 틀렸는지 모르겠다
# import sys
# arr = [0] * 100001 # 100점까지
# num = int(input())
# for i in range(num):
#     arr[int(float(sys.stdin.readline().strip()) * 1000)]+=1
# counter = 0
# for i in range(len(arr)):
#     for j in range(0,arr[i]):
#         temp = list(str(i).zfill(5))
#         temp.insert(-3,".")
#         print("".join(temp))
#         counter += 1
#         if counter == 7:
#             exit()
        

# 메모리 초과가 났기 때문에 100000짜리 배열을만들어 ++해준다
# 문제 이해를 잘못함
# import sys
# arr = [0] * 100001 # 100점까지
# num = int(input())
# for i in range(num):
#     arr[int(float(sys.stdin.readline().strip()) * 1000)]+=1
# for i in range(len(arr)):
#     for j in range(0,arr[i]):
#         temp = list(str(i).zfill(5))
#         temp.insert(-3,".")
#         print("".join(temp))

# 메모리 초과, 그냥 배열에 append하지 않는다
# import sys
# arr=[]
# for i in range(int(input())):
#     arr.append(sys.stdin.readline())
# arr.sort()
# for i in arr:
#     print(i,end="")

# import sys
# num = int(input())
# arr = [0] * num
# for i in range(num):
#     arr[i] = float(sys.stdin.readline())
#     # arr[i] = input()
# arr.sort()
# for i in arr:
#     # print(format(i,"f"))
#     print("{:.3f}".format(i))