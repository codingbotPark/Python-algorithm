# 91 을 91 + 9 + 1 = 101
# 100 을 100 + 1 + 0 + 0 = 101
# 이렇게 101이란 수를 만들 수 있을 때
# 91과 100을 101의 생성자 라고 한다
# 
# 이런 생성자가 없는 수를 셀프넘버라고 한다
# 
# 즉 생성자자신과 새성자 각각의 수를 더했을 때 특정한 수가 나오면 그 수는 셀프넘버가 아니라는 말이기 때문에
#
# 생성자가 있는지 없는지를 구하기 위해 내가 생각한 방법은
# 각각의 수를 더하는데 각각의 수는 최대가 9일 것이다
# (10은 1 과 0 으로 쳐지기 때문에)
# 그래서 효율적이진 않지만 
# 
# 생성자가 있는 n이라는 수의 생성자는
# n - (n의 길이 * 9) 부터 n 사이에 있을 것이기 때문에
# 반복문으로 돌아가며 찾는다


def isSelfNum(num): # 셀프넘버인지 아닌지 판별
    # n - (n의 길이 * 9) 가 음수일 때 0으로 바꿔주기
    startNum = num - (len(str(num)) * 9)
    if startNum < 0:
        startNum = 0

    for i in range(startNum,num):
        v = i # 배열로 만든 수들의 합을 임시로 저장하는 변수
        i = list(map(int,list(str(i)))) #  정수형 값의 각각 더함
        for j in i:
            v += j
        if v == num: # 배열의 수들 합이 num일 때
            # print("셀프넘버가 아니다")
            return 0 # 셀프넘버가 아닐 때 0을 리턴
    # 반복문을 다 돌았을 때 return 0이 되지 않았다면 셀프넘버
    # print("셀프넘버이다")
    return 1

        
for i in range(1,10000):
    if isSelfNum(i) == 1:
        print(i)



# https://github.com/jongpark1234 코드
num = 0
numlist = []
while True:
    num += 1
    temp = num + sum(list(map(int, str(num))))
    if num > 10000:
        break
    else:
        numlist.append(temp)
# 요기까지 nulist에 셀프넘버가 아닌 수들을 넣는다
for i in range(1, 10001):
    if numlist.count(i) == 0:
        # 셀프넘버들은 배열에 없기 때문에 출력
        print(i)