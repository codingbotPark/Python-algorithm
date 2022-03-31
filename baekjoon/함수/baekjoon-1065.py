a = int(input())
v = 0#등차수열인 개수를 저장
for i in range(1,a+1):
    # 기본세팅
    temp = list(map(int,list(str(i))))
    if len(temp) > 1: #아닐 땐 gap을 추출, 배열을 한 번 세팅
        gap = temp[0] - temp[1]
        temp.pop(0)
        while(len(temp) - 1): 
        # temp배열 안 값이 있는 동안 반복
            if not((temp[0] - temp[1]) == gap):
                # gap과 차이가 다를 땐 비정상적이게 반복을 끝낸다
                # 요기서 비정상적인 말이란 배열이 안없어짐을 말한다
                break
            temp.pop(0)

    if not(len(temp)-1): # 배열 끝까지 돌았을 때
        v += 1

print(v)

# pop함수를 사용하여 배열의 인자로 들어온 인덱스를 배열에서 삭제할 수 있다
# 출처 : https://devpouch.tistory.com/69

