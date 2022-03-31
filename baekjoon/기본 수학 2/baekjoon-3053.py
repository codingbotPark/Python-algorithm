# 출처 : https://www.delftstack.com/ko/howto/python/pi-in-python/
# 파이썬에서 파이 사용
# math.pi() 함수를 사용해 pi값을 가져온다

# 출처 : https://itholic.github.io/kata-taxicab-circle/
# 택시 기하학에서 원

from math import sqrt
import math
pi = math.pi

r = int(input())
print("{:.6f}".format((r ** 2) * pi))

print("{:.6f}".format((r**2)*2))
