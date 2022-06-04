# https://ddmanager.tistory.com/40
# x와 -x가 같은 경우를 찾아야 하는데, 답이 없을 것이다 라 생각하기 쉽다
# 프로그래밍에서는 정수의 오버플로가 발생하는 경우에 같아질 수 있다

num = 2147483648
print(num == -num)