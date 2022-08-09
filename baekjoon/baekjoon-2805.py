# 배열을 정렬하고
# 배열에 전의 수보다 큰 n을 넣는다
# 그 넣은 배열을 뒤에서부터 더해가며 계산

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

        # 조금 꼼수이지만 * -i 안에 답이 있다
        counter = 0
        while(True):
            if (m == 0):
                print(arr[-i-2] + counter)
                exit()
            m += i+1
            counter+=1
