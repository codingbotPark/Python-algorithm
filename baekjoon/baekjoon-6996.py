# 파이썬에서 index를 사용해 배열에서 원하는 값의 위치를
# 찾으려 할 때 없으면 ValueError를 보내는데
# try, except로 사용할 수 있는지 확인 == 사용할 수 있다
# a = [1,2]
# try:
#     print(a.index(3))
# except:
#     print("이게되네?")

num = int(input())
for i in range(num):
    a,b = input().split()
    print(a,"&",b,end=" ")
    if not(len(a) == len(b)):
        print("are NOT anagrams.")
        continue
    
    a = list(a)
    b = list(b)
    for i in a:
        try:
            b.pop(b.index(i))
        except:
            break
    if len(b):
        print("are NOT anagrams.")
    else:
        print("are anagrams.")
        

# # ▼ 시행착오
# # 문자열을 배열로, 배열을 문자열로 하는 과정에서
# # 문제가 생김
# num = int(input())
# for i in range(num):
#     a,b = input().split()
#     print(f"{a} & {b}",end=" ")
#     # ▲ 입력
#     for j in a:
#         # a를 하나하나 돌며 b와 비교해 찾음
#         result = b.find(j)
#         if result > -1:
#             b = list(b)
#             b.pop(result-1)
#             b = str(b)
#         else:
#             break
#     print(b)
#     if len(b):
#         print("are NOT anagrams.")
#     else:
#         print("are anagrams.")

