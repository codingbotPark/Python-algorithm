a = int(input())
b = []
for i in range(a):
    b.append(list(input().split()))
    b[i][1] = list(b[i][1])
for i in range(a): # 줄의 개수만큼 입력
    for j in range(len(b[i][1])): #영어의 개수만큼
        for z in range(int(b[i][0])): # 반복될 개수만큼
            print(b[i][1][j],end='')
    print()

# # https://github.com/jongpark1234 코드
# # 한번 입력, 출력 해도 테스트 케이스를 통과한다
# for _ in range(int(input())):
#     temp = ''
#     r, s = input().split() 
#     for i in s: # 문자열을 for문에서 배열과 같이 돌릴 수 있다
#         temp += i * int(r) # r만큼 반복해서 i(문자열각각의 문자) 를 곱해서 출력
#     print(temp)