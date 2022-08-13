# 한 두줄 입력받은 것이 아닌, 반복문으로 여러줄을 입력받아야 할 땐 input으로 받는다면 시간 초과가 날 수 있다 그래서 sys.stdin.readline()을 사용한다
# 출처 : https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

import sys#sys를 import해주고 사용
# a = input() #test case는 input을 사용해도 무관
a = int(sys.stdin.readline().strip())
for i in range(a):
    a,b = map(int,sys.stdin.readline().split())
    print(a + b)
