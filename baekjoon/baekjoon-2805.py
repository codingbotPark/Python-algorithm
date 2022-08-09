# 배열을 정렬하고
# 배열에 전의 수보다 큰 n을 넣는다
# 그 넣은 배열을 뒤에서부터 더해가며 계산
#
# 값은 제대로 나오지만 시간초과,
# 무지성 while문이 있어서 예상은 조금 했다


n, m = map(int,input().split())
arr = list(map(int,input().split()))
gapArr = [0] * n

arr.sort()

gapArr[-1] = arr[0]
for i in range(1,len(arr)):
    gapArr[-i-1] = arr[i] - arr[i-1]
# 값 포멧 완성
# reverse를 하지 않기 위해 배열에 반대로 넣어준다

for i in range(len(gapArr)):
    m -= gapArr[i] * (i+1) # m 에 -를 해준다(i개의 통나무가 이미 포함되어서 곱해준다)
    if m <= 0: # 0이거나 0보다 작을 때
        # 값이 그 두수 중 사이에 있다

        # 꼼수를 쓰지 않고 이분탐색
        s = arr[-i-1]
        e = arr[-i-2]
        

        # 조금 꼼수이지만 * -i 안에 답이 있다
        counter = 0
        while(True):
            if (m == 0):
                print(arr[-i-2] + counter) # 2칸 뒤에서 +
                exit()
            m += i+1
            counter+=1


# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# gapArr = [0] * n

# arr.sort()

# gapArr[-1] = arr[0]
# for i in range(1,len(arr)):
#     gapArr[-i-1] = arr[i] - arr[i-1]
# # 값 포멧 완성
# # reverse를 하지 않기 위해 배열에 반대로 넣어준다

# for i in range(len(gapArr)):
#     m -= gapArr[i] * (i+1) # m 에 -를 해준다(i개의 통나무가 이미 포함되어서 곱해준다)
#     if m <= 0: # 0이거나 0보다 작을 때
#         # 값이 그 두수 중 사이에 있다

#         # 조금 꼼수이지만 * -i 안에 답이 있다
#         counter = 0
#         while(True):
#             if (m == 0):
#                 print(arr[-i-2] + counter)
#                 exit()
#             m += i+1
#             counter+=1



# https://claude-u.tistory.com/446
# 그냥 이분탐색이다
# 하지만 pypy3로 했을 때 성공이라는 것은
# 다른 좋은 방법이 있다는 뜻이다
# 위의 내가 예전에 했던 코드에서 마지막 부분에
# 이분탐색을 추가한다
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
