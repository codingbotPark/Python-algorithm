# import sys

# array = []
# for i in range(int(sys.stdin.readline())):
#     array.append(int(sys.stdin.readline()))
# array.sort()
# print(*array,sep="\n")


# 이건 고민한다고 해결되지 않을 것 같아서 검색했다
# https://yoonsang-it.tistory.com/49
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)
# 최대로 입력될 수 있는 수가 10000이기 때문에 그냥 10000개의 배열을 만들어,
# 그 수에 혜당하는 인덱스의 값을 + 1 해서 그 수만큼 출력한다
# 천만개의 수를 입력받아 배열에 저장하는 것 보다, 10000개의 배열을 만들 때가 더 효율적이다