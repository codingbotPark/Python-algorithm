# https://velog.io/@daybreak/Python%EC%97%90%EC%84%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A4%91%EB%B3%B5%EC%A0%9C%EA%B1%B0

# 파이썬에서 중복을 제거하는 방법에는 set함수를 사용하여 제거하는 방법이 있다
# set은 집합 자료형이다
a = []
for i in range(10):
    a.append(int(input()))
    a[i] = a[i] % 42
print(len(set(a)))