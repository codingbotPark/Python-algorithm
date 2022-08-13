lineNum = int(input())
words = [] # 입력받는 단어들
groupWordNum = 0 # 그룹 단어의 개수

for i in range(lineNum): # 회수만큼 반복
    already = '' # 이미 나온 알파벳
    temp = 0
    words.append(input())
    for j in words[i]:
        if already.find(j) < 0:
            already += j
        elif not(temp == j):
            groupWordNum -= 1
            break
        temp = j
    groupWordNum += 1
print(groupWordNum)
        

# a = input()
# print(a[-1])

# j = "a"
# a = "a"
# print(a + j)