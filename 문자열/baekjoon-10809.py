from operator import index


a = list(input())
for i in range(97,123):
    if (a.count(chr(i)) == 0):
        print(-1,end=" ")
    else:
        print(a.index(chr(i)),end=' ')

# index함수는 중복된 값이 있으면 가장 최소의 위치를 리턴한다
# 출처 : https://pydole.tistory.com/entry/Python-index-%ED%95%A8%EC%88%98-%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C-%EC%9B%90%ED%95%98%EB%8A%94-%EA%B0%92%EC%9D%98-%EC%9C%84%EC%B9%98-%EC%B0%BE%EA%B8%B0

# count함수는 배열에서 값의 유무를 확인한다
# +시간이 오래걸리는 함수이다
# 출처 : https://blockdmask.tistory.com/410
