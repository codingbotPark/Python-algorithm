from collections import deque

def solution(numbers, target):
    # 들어갈 숫자
    queue = deque([[0,'',0]])
    # answer = ''
    answer = 0

    while queue:
        c,string,idx = queue.popleft()

        if c == target and idx == len(numbers):
            answer += 1
            # answer += (string + " = " + str(target) + "\n")
            # print(answer)
        
        if idx < len(numbers):
            # 마이너스를 먼저 추가해준다
            queue.append([c - numbers[idx],string+"-"+str(numbers[idx]), idx+1])
            queue.append([c + numbers[idx],string+"+"+str(numbers[idx]), idx+1])

    return answer

# print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))


# BFS 
'''
from collections import deque
x=int(input())
Q=deque([x])
visited=[0]*(x+1)
while Q:
    c=Q.popleft()
    if c==1:
        break
    if c%3==0 and visited[c//3]==0:
        Q.append(c//3)
        visited[c//3]=visited[c]+1
    if c%2==0 and visited[c//2]==0:
        Q.append(c//2)
        visited[c//2]=visited[c]+1
    if visited[c-1]==0:
        Q.append(c-1)
        visited[c-1]=visited[c]+1
print(visited[1])
'''