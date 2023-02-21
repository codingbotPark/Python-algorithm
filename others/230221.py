score = [70,80,90,19,23]
temp = sorted(score)
temp.reverse()
answer = []
for i in score:
    answer.append((temp.index(i)) + 1)

print(answer) 

