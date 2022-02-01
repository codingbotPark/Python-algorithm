# 출처 : https://blockdmask.tistory.com/468
# join함수를 사용하여 배열의 값들을 붙여서 출력할 수 있다

# join함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐 하나의 문자열로 바꾸어 변환하는 함수이다
# 기준으로 출력할 문자.join(문자열리스트) 의 형태이고,
# 문자열리스트여야만 한다

a,b = input().split()
a = list(map(int,a))
b = list(map(int,b))
a = a[::-1]
b = b[::-1]
if a > b:
    print("".join(map(str,a)))
else:
    print("".join(map(str,b)))

# 출처 : https://includestdio.tistory.com/32
# 리스트에 reverse를 사용하면 배열을 뒤집는다
# 
# reverse는 리턴값이 없는 함수여서 바로 print 할 순 없다
# 
# reversed 함수는 배열이 리턴이 된다
#
# 이 문제에서는 reverse함수를 사용하지 않고
# 배열을 [::-1] 돌려줘서 -1(거꾸로) 배열을 돌아서 뒤집어 줬다

# # https://github.com/jongpark1234 코드
# # 그냥 split으로 나누고 리스트로 만들어 max값을 바로 출력
# print(max(input()[::-1].split()))