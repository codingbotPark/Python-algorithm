# https://aigong.tistory.com/397
# 이분탐색을 하면 답을 구할 수 있다고 한다
k,n = map(int,input().split())
l = sorted([int(input()) for _ in range(k)])

start, end = 1, l[-1]



#  # 아래와 같은 방법이지만,
# # remainArr(랜선으로 사용하고 남은 길이)의 값에 랜선으로 사용할 수 있는 개수를 곱해준다
# # 곱하지 않는다면 n개의 랜선으로 나누고 나머지 하나의 길이만 다르게 계산했을 때의 결과이기 때문에
# import sys
# k,n = map(int,input().split())

# arr = [0] * k
# total = 0

# for i in range(k):
#     arr[i] = int(sys.stdin.readline())
#     total += arr[i]

# avg = total // n

# # 실제 avg로 각 수를 나눴을 때 값
# counter = 0




# 다 나누고 평균을 구한 값이 나왔다
# 이 값을 실제 랜선들에 각각 나누어도 랜선의 개수 이상만큼 차이가 나지 않는다(n으로 나눴기 때문에)


# # 값을 받고, total // avg로 나눈 값이 몇이 부족한지 찾는다,
# # 찾고 부족한 n번째 작은 값을 가져와 그 값에 1 추가되게 한다,
# import sys
# k, n = map(int,input().split())

# arr = [0] * k
# total = 0

# for i in range(k):
#     arr[i] = int(sys.stdin.readline())
#     total += arr[i]

# avg = total // n # 임시 avg

# counter = 0
# remainArr = [0] * k

# for i in range(k):
#     remainArr[i] = arr[i] % avg
#     counter += arr[i] // avg

# remainArr.sort()



# # 당연하지만 시간초과가 떳다
# 
# import sys

# k,n = map(int,input().split())
# arr = [0] * k
# total = 0
# for i in range(k):
#     arr[i] = int(sys.stdin.readline())
#     total += arr[i]

# total = (total // n) + 1
# counter = 0

# while (counter != n):
#     total -= 1
#     counter = 0
#     for i in arr:
#         counter += i // total

# print(total)
    

