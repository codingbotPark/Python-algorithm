# https://ddmanager.tistory.com/40
# 정수의 오버플로를 활용해서 x == -x 를 성립할 수 있다
# signed int(4byte)에서-2147483648는 최소값, 2147483647은 최대값이다
# 최소값에서 -부호를 붙이면 2147483648이 되는데, 이는 범위를 벗어나고 다시 -2147483648가 된다

int -2147483648