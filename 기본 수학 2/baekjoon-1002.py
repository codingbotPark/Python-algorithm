# 상황을 나열하면
# 1. 조규현과 백승환의 위치, 류재명과 각각의 거리가 모두 같을 때 = 무한
# 2. 같은 위치에 있고 류재명과 거리가 다를 떄 = 0
# 3. 합이 조규현 백승환 과의 거리보다 짧을 때 = 0
# 4. 합이 조규현 백승환 과의 거리일 때 = 1
# 5. 합이 조규현 백승환 과의 거리보다 클 때 = 2 (+a)

from math import sqrt

caseNum = int(input())
for i in range(caseNum):
    temp2 = list(map(int,input().split()))
    temp1 = temp2[0:3]
    temp2 = temp2[3:6]
    length = sqrt(((temp1[0] - temp2[0])** 2) + ((temp1[1] - temp2[1]) ** 2))

    if (temp1[0] == temp2[0]) and (temp1[1] == temp2[1]): 
        # 두 점이 같은 점에 있을 때
        if temp1[2] == temp2[2]: 
            print(-1)
        else:
            print(0)
    else:
        length = sqrt(((temp1[0] - temp2[0])**2) + ((temp1[1] - temp2[1])**2))# 조규현과 백승환의 거리
        sum = temp1[2] + temp2[2]
        if sum < length: # 3번 상황
            print(0)
        elif sum == length: # 4번 상황
            print(1)
        elif sum > length: # 5번 상황
            minus = abs(temp1[2] - temp2[2])
            if minus == length:
                print(1)
            elif minus > length:
                print(0)
            else:
                print(2)
    
    
# 출처 : https://ponyozzang.tistory.com/260
# 파이썬에서 자르고 싶은 문자열의 앞부분의 인덱스부터 뒷부분까지 지정을 해서 자를 수 있다

# 출처 : https://blockdmask.tistory.com/380
# 파이썬에서 abs함수를 사용해 절댓값을 얻을 수 있다