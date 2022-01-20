# https://dev-note-97.tistory.com/13
# 파이썬에서 역순으로 정렬할 때 배열명.sort(reverse=True)를 하면 내림차순(역순) 으로 정렬이 된다

overNums = []
caseNum = int(input())
for i in range(caseNum):
    overNum = 0 # 평균보다 높은 값의 개수를 임시로 저장
    data = list(map(int,input().split()))
    avg = (sum(data) - data[0]) / data[0]
    for i in range(1,len(data)):
        if data[i] > avg:
            overNum+=1
    overNums.append((overNum / data[0]) * 100)
for i in range(caseNum):
    print(f'{overNums[i]:.3f}%')


# 런타임 에러가 떠서
# 기존에 배열을 뒤집어 평균보다 작은 값이 나올 때 break를 해 for문의 i 값을 평균보다 높은 값의 개수를 구했었는데
# 그냥 정렬하지 않고 요소 하나하나를 모두 비교하여 개수를 구하는 방식으로 바꿈
# ▽▽

# c = [] # 평균들을 저장할 배열
# a = int(input())
# for i in range(a):
#     b = list(map(int,input().split()))
#     avg = (sum(b) - b[0]) / b[0]
#     b.sort(reverse=True) # b를 정렬해서 값 추출에 시간을 줄인다
#     for i in range(len(b)-1):
#         if b[i] <= avg:
#             # print(i)
#             c.append((i / b[-1]) * 100) # 전체 수 중 평균보다 높은 사람의 수
#             break
# for i in range(a):
#     print(f'{c[i]:.3f}%')

# 런타임 에러


# https://animoto1.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%86%8C%EC%88%98%EC%A0%90-%EC%9E%90%EB%A6%AC-%EC%A0%9C%ED%95%9C%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95

# 파이썬에서 출력할 소수점 자리를 제한하는 방법은
# round - round(값,반올림할 자리수)
# 등이있다