# https://wook-2124.tistory.com/247
# 테스트 케이스의 파일의 끝(End Of File)을 문제에서 지정해주기 때문에 이EOF를 try와 except문으로 처리하면 된다
# try:
#   ...
# except [발생 오류 as [오류 메시지 변수]]:
#   ...

while(1):
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break
