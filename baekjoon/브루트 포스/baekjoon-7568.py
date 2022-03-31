num = int(input())
height = []
weight = []
grade = []
for i in range(num):
    a,b = map(int,input().split())
    weight.append(a)
    height.append(b)
for i in range(num):
    gradeIs = 1
    for j in range(num):
        if i == j:
            continue
        if weight[i] < weight[j]:
            if height[i] < height[j]:
                gradeIs+=1
    grade.append(gradeIs)
print(*grade)
