b = []
for i in range(9):
    b.append(int(input()))
print(max(b))
print(b.index(max(b))+1)

# https://pydole.tistory.com/entry/Python-index-%ED%95%A8%EC%88%98-%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C-%EC%9B%90%ED%95%98%EB%8A%94-%EA%B0%92%EC%9D%98-%EC%9C%84%EC%B9%98-%EC%B0%BE%EA%B8%B0

# 파이썬에서 배열안에 특정 값의 인덱스를 찾은 함수로 index함수가 있다
# 함수명.index(특정값) 의 형태로 사용할 수 있다