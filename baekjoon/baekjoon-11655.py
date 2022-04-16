# 들어오는 문자를 아스키코드로 바꾼 후
# 계산해서 문자로 다시 리턴
def encryption(value):
    value = ord(value)
    if value > 64 and value < 91:
        value += 13
        if value > 90:
            value -= 26
    elif value > 96 and value < 123:
        value += 13
        if value > 122:
            value -=26
    return chr(value)

print("".join(list(map(lambda x:encryption(x),list(input())))))
