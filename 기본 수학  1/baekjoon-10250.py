
import math
values = []
testNum = int(input())
for i in range(testNum):
    height,width,Num = map(int,input().split())
    roomNum = math.ceil(Num / height) # 호
    floorNum = Num % height # 층
    print(f"{floorNum}{str(roomNum).zfill(2)}")
#     values.append(str(floorNum)+str(roomNum).zfill(2))
# for i in values:
#     print(i)


# 출처 : https://brownbears.tistory.com/483
# 문자열의 길이를 지정하고 문자열 앞에 남는 길이만큼 앞에 0 을 채우는 방법은
# zfill(개수) 를 사용하여 [현재 스트링의 길이 - 개수] 만큼 0 을 채울 수 있다
