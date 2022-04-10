# https://wikidocs.net/22803

while True:
    array = []
    string = input()
    if string == "#":
        break
    string = set(list(string))
    for i in string:
        if ord(i) > 64 and ord(i) < 91:
            array.append(ord(i) + 32)
        elif ord(i) > 96 and ord(i) < 123:
            array.append(ord(i))
    array = set(array)
    print(len(array))
    
# 시행착오▼
# 음 안된다
# while True:
#     array = []
#     string = input()
#     if string == "#":
#         break
#     # 한 번 중복을 제거한다
#     string = set(list(string))
#     for i in string:
#         if ord(i) > 64 and ord(i) < 91:
#             value = ord(i) + 32
#         else:
#             value = ord(i)
#         if value > 96 and value < 123:
#             array.append(value)
#     print(len(array)-1)

# 시행착오▼
# 대문자, 소문자로 넘어가면서를 생각 못했다
# # 알파벳일 때만 true를 반환 
# def filterAlph(value):
#     if ord(value) > 96 and ord(value) < 123:
#         return True
#     return False
# while(1):
#     alph = []
#     string = input()
#     if string == "#":
#         break
#     set(string)
#     for i in string:
#         # 알파벳일 때 수를 넣는다
#         if ord(i) > 64 and ord(i) < 91:
#             i = ord(i) + 32
#         if filterAlph(i):
#             alph.append(i)
#     print(set(alph))