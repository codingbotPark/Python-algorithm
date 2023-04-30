from collections import deque

def printMaps(maps):
    for i in maps:
        print(i)

def solution(maps):
    q = deque([[[0,0],1,maps]]) # [y,x] , cost
    
    mapXSize = len(maps[0]) -1
    mapYSize = len(maps) -1
    
    answer = -1
    
    while q:
        position, cost,maps = q.popleft()

        y = position[0]
        x = position[1]
        
        maps[y][x] = 0

        if y== mapYSize and x == mapXSize:
            if answer == -1 or answer > cost:
                answer = cost
        
        # 오른쪽 부터 간다
        if x+1 <= mapXSize and maps[y][x+1] == 1:
            q.append([[y,x+1],cost+1,maps])
            
        # 아래
        if y+1 <= mapYSize and maps[y+1][x] == 1:
            q.append([[y+1,x],cost+1,maps])
        
        # 왼쪽
        if x-1 > -1 and maps[y][x-1] == 1:
            q.append([[y,x-1],cost+1,maps])
        
        # 위쪽
        if y - 1 > -1 and maps[y-1][x] == 1:
            q.append([[y-1,x],cost+1,maps])
        
    return answer


def solution(maps):
    x,y = 0,0
    x_length, y_length = len(maps[0]), len(maps)
    bfs = deque([])
    distance = 1

    while x != x_length - 1 or y != y_length - 1:
        if x != x_length -1 and maps[y][x+1] == 1:
            bfs.append((x+1,y,distance + 1))

        if x != 0 and maps[y][x-1] == 1:
            bfs.append((x-1, y, distance + 1))   

        if y != y_length -1 and maps[y+1][x] == 1:
            bfs.append((x,y+1,distance + 1))

        if y != 0 and maps[y-1][x] == 1:
            bfs.append((x, y-1, distance + 1))

        maps[y][x] = 0
        if bfs:
            x, y, distance = bfs.popleft()
        else:
            return -1 

    return distance

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))