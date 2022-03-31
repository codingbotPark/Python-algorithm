# 하루동안 증가하는 량 = 낮 - 밤
# 근데 낮에서 끝날 수 있기 때문에
# 전체 길이 v에서 낮인 up을 빼고,하루를 추가한다
# 그 후 남은 v에서 하루동안 증가하는 량인 낮(up) - 밤(down)을 나누고
# 나눈 값을 올림함으로써 오직 '도달하는' 데 걸리는 날을 출력

import math
up,down,v = map(int,input().split())
print( math.ceil((v - up) / (up - down)) + 1)

# 출처 : https://devpouch.tistory.com/155
# 올림은 math모듈의 ceil함수를 사용한다